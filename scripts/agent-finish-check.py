#!/usr/bin/env python3
"""Verify AgentPlaybook gate evidence before final report, commit, or handoff."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ANSI_RE = re.compile(r"\x1b\[[0-?]*[ -/]*[@-~]")


def clean_output(text: str) -> str:
    return ANSI_RE.sub("", text)


def run_command(command: list[str], cwd: Path) -> dict[str, Any]:
    result = subprocess.run(
        command,
        cwd=str(cwd),
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    return {
        "command": command,
        "cwd": str(cwd),
        "returncode": result.returncode,
        "stdout": clean_output(result.stdout),
        "stderr": clean_output(result.stderr),
    }


def parse_overall(output: str) -> dict[str, str]:
    for raw_line in clean_output(output).splitlines():
        line = raw_line.strip()
        if not line.startswith("Overall:"):
            continue
        value = line.split("Overall:", 1)[1].strip()
        if "Ready" in value:
            status = "Ready"
        elif "Needs review" in value:
            status = "Needs review"
        elif "Blocked" in value:
            status = "Blocked"
        else:
            status = value or "unknown"
        return {"status": status, "line": line}
    return {"status": "unknown", "line": ""}


def parse_gate(value: str) -> tuple[str, str]:
    if "=" not in value:
        raise argparse.ArgumentTypeError("gate evidence must use '<gate>=<evidence>'")
    gate, evidence = value.split("=", 1)
    gate = gate.strip()
    evidence = evidence.strip()
    if not gate or not evidence:
        raise argparse.ArgumentTypeError("gate and evidence must both be non-empty")
    return gate, evidence


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    playbook_root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(
        description="Check route gate evidence, validation, diff hygiene, and VibeGuard."
    )
    parser.add_argument("--project", type=Path, default=Path.cwd())
    parser.add_argument("--rules", type=Path, default=playbook_root)
    parser.add_argument("--evidence", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--gate", action="append", default=[], type=parse_gate)
    parser.add_argument(
        "--allow-vibeguard-review",
        help="required reason when final VibeGuard is not Ready",
    )
    args = parser.parse_args()

    project = args.project.resolve()
    rules = args.rules.resolve()
    evidence_path = (
        args.evidence.resolve()
        if args.evidence
        else project / ".agentplaybook" / "preflight.json"
    )
    output_path = (
        args.output.resolve()
        if args.output
        else project / ".agentplaybook" / "finish.json"
    )

    failures: list[str] = []
    if not evidence_path.exists():
        failures.append(f"missing preflight evidence at {evidence_path}")
        preflight: dict[str, Any] = {}
    else:
        try:
            preflight = json.loads(evidence_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as error:
            failures.append(f"preflight evidence is not valid JSON: {error}")
            preflight = {}

    route = preflight.get("route") or {}
    required_gates = route.get("gates") or []
    if not required_gates:
        failures.append("preflight evidence is missing route gates")
    gate_evidence = dict(args.gate)
    missing_gates = [gate for gate in required_gates if not gate_evidence.get(gate)]
    if missing_gates:
        failures.append("missing required gate evidence: " + ", ".join(missing_gates))

    preflight_vibeguard_command = preflight.get("vibeguard") or {}
    preflight_vibeguard = preflight_vibeguard_command.get("overall") or {}
    if not preflight_vibeguard:
        failures.append("preflight evidence is missing VibeGuard result")
    elif preflight_vibeguard_command.get("returncode") != 0:
        failures.append("preflight VibeGuard audit failed")
    elif preflight_vibeguard.get("status") == "unknown":
        failures.append("preflight VibeGuard overall status could not be parsed")

    validate = run_command(
        [sys.executable, str(playbook_root / "scripts" / "workflow.py"), "validate"],
        playbook_root,
    )
    diff_check = run_command(["git", "diff", "--check"], project)
    vibeguard = run_command(
        [
            "npx",
            "--yes",
            "@taehwandev/vibeguard",
            "audit",
            str(project),
            "--rules",
            str(rules),
        ],
        project,
    )
    vibeguard_output = vibeguard["stdout"] + "\n" + vibeguard["stderr"]
    vibeguard["overall"] = parse_overall(vibeguard_output)

    if validate["returncode"] != 0:
        failures.append("workflow validate failed")
    if diff_check["returncode"] != 0:
        failures.append("git diff --check failed")
    if vibeguard["returncode"] != 0:
        failures.append("final VibeGuard audit failed")

    overall = vibeguard["overall"]["status"]
    if overall != "Ready" and not args.allow_vibeguard_review:
        failures.append(
            "final VibeGuard is not Ready; report the state and pass "
            "--allow-vibeguard-review with a reason if the review is acceptable"
        )

    result = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "playbook_root": str(playbook_root),
        "project": str(project),
        "rules": str(rules),
        "preflight_evidence": str(evidence_path),
        "required_gates": required_gates,
        "gate_evidence": gate_evidence,
        "allow_vibeguard_review": args.allow_vibeguard_review,
        "validate": validate,
        "diff_check": diff_check,
        "vibeguard": vibeguard,
        "failures": failures,
    }
    write_json(output_path, result)

    print(f"Finish evidence: {output_path}")
    print(f"Required gates: {required_gates}")
    print(f"VibeGuard overall: {overall}")

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
