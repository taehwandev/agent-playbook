---
keyflow_id: sys_5541ae16ddef
status: review
type: ai-generated
---

# Server Review

Use for API, worker, database, auth, tenancy, migration, and integration review.

## Review

- Check auth, permission, tenant boundary, validation, and rate-limit behavior.
- Check route/resolver, validator, use case, repository, and response/error
  boundaries against `server-api-implementation.md` when API code changed.
- Verify request parsing is separate from product rules.
- Check idempotency for payments, webhooks, retries, and jobs.
- Review migrations for reversibility, backfill risk, locks, and data loss.
- Ensure errors and logs do not leak secrets, tokens, or personal data.

## Tools

- Static: compiler/typecheck, lint, schema validation.
- Unit: services, policies, validators, mappers.
- Integration: database, cache, queue, external client fakes.
- Contract: API request/response, OpenAPI, GraphQL schema, webhook payloads.
- Load/smoke: only for performance-sensitive or release-critical paths.

## UI/API Test Focus

- API returns correct status, body, and error shape.
- Unauthorized, forbidden, cross-tenant, and expired-session paths are tested.
- Background jobs retry safely and do not duplicate side effects.
- Migration and rollback path is verified when data risk exists.
