---
keyflow_id: sys_public_discovery
status: review
type: human-reviewed-needed
---

# Public Discovery

Use when touching SEO, sitemap, robots, metadata, Open Graph previews, short
links, public indexes, search/discovery feeds, share previews, canonical URLs, or
structured data.

Public discovery is a data exposure surface. Treat it with the same care as a
public API response.

## Discovery Surfaces

Common public discovery outputs include:

- sitemap and robots policy
- canonical URLs and localized alternates
- metadata title and description
- Open Graph, social cards, link unfurls, and preview images
- public search indexes and discovery feeds
- share links, short links, and redirects
- structured data and public manifests

## Rules

- Only include resources that are meant to be discoverable by unauthenticated
  readers, crawlers, link preview bots, or public clients.
- Apply status, visibility, permission, tenant, locale, region, feature flag, and
  release-channel rules before generating discovery output.
- Public route does not mean public discovery. Some public routes are login,
  support, account, debug, test, or callback surfaces that should not be indexed.
- Metadata and previews must use sanitized, minimized fields. Do not leak private
  body content, internal identifiers, tokens, private URLs, draft titles, or
  deleted resource existence.
- Canonical URLs, localized alternates, short links, and redirects must agree
  with repo-local routing policy.
- Discovery caches can outlive normal UI state. Use conservative TTLs and
  invalidation when visibility, slug, title, deletion, or locale changes.

## Do Not

- Do not build sitemap or preview data from raw admin/database objects without a
  public DTO or visibility filter.
- Do not include admin, management, debug, test, API, callback, migration, or
  internal utility routes in public discovery outputs.
- Do not use signed, private, one-time, or viewer-specific URLs in indexable
  metadata or previews.
- Do not reveal private resource existence through distinct preview, metadata,
  redirect, or 404 behavior unless the product explicitly allows it.
- Do not treat link preview bots as trusted users.

## Checks

- Who is allowed to discover this resource without logging in?
- Which fields are safe for crawlers, previews, and public search?
- What happens after deletion, unpublish, privacy change, slug change, or locale
  change?
- Are canonical and alternate URLs consistent with routing?
- Are non-content routes excluded from discovery?
- Can cached preview or sitemap output outlive a permission change?

## Verification

Verify public discovery as output data:

- generated sitemap/robots/search output excludes private and internal routes
- metadata/preview output is minimized and sanitized
- deleted, draft, private, permission-denied, and not-found resources do not leak
  existence through different public details
- canonical, locale alternate, short link, and redirect behavior agree with
  repo-local routing policy
