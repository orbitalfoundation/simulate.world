# Simulate World — ongoing polish

Updated September 19, 2026. Start here when continuing the project in a new conversation.

## Purpose and editorial intent

A circa-2015 essay about ecology, whole systems, shared models, and civic understanding, presented with clearer typography, navigation, and mobile behavior. The author wants small, careful improvements to the essay he wrote, with its emotional arc and specific images intact.

Preserve the nine chapters, including “Mixed messages” and “Emerging superpowers,” and the 50 part images. Make room for emotional difficulty before introducing capabilities. Avoid labels such as “original thesis,” “restored presentation,” or forensic reconstruction in the reader experience. The separate contemporary riff is retained at `/draft/`; do not silently substitute its language for the main essay.

## Read next

- [README](../README.md): editing and publication.
- [EDITORIAL](../EDITORIAL.md): dating evidence and remaining limits.
- [Applied audit corrections](../devlog/2026-09-18-audit-corrections.md).
- [Source-linked audit](../devlog/2026-09-18-correctness-audit.md): proposal snapshot; the correction record supersedes it.
- [Development log](../devlog/README.md).

## Current implementation

Repository: https://github.com/orbitalfoundation/simulate.world, branch `main`.
Public site: https://simulate.world/. GitHub Pages publishes the repository root; Cloudflare supplies the domain routing and HTTPS/www redirects. Recheck the current configuration before future infrastructure changes.

The main essay is at `/`; the reading list at `/reading.html`; the author biography at `/about/`; `/news/` redirects to the reading list. A contemporary alternate essay remains at `/draft/`, with indexing disabled.

Edit prose in `source/thesis.json`, resources in `source/resources.json` and `reading-data.json`, and generated markup through `build.py`. Run `python3 build.py` on macOS; it uses `sips` for image dimensions. Layout and navigation use `style.css`, `edition.css`, and `edition.js`. This is a static site, without an npm dependency or an application server.

## Decisions to retain

- The working date June 24, 2015 is inferred from reference-entry dates, not a verified publication timestamp. Do not add an unsupported `datePublished`.
- The domain registration record gives April 20, 2015; registration is separate from essay publication.
- Factual audit corrections were approved and applied. Further fact checking should use primary sources and preserve the narrow editorial scope.
- Keep the reading list primarily of its period. The 2016 Smith and Morowitz book, *The Origin and Nature of Life on Earth*, is an explicit author-requested exception.
- Book covers, linked Voices biographies/selected portraits, and the presentation video with its thumbnail have been added.
- A single top byline is welcome. Repeated author promotion is not. Name links go to About; About links to Substack, Medium, and X. The organization handle is **@orbitalfdn**; the author handle is **@anselm**.
- Keep SEO and social metadata accurate, without inflated authorship or unsupported dates.
- Preserve the alternate essay's useful phrases for possible later work rather than overwriting the main text.
- Record meaningful changes in `devlog/`.

## Open work

No new editorial rewrite is queued by the context split. Continue with the author's next specific request. Known unfinished work includes a complete check of historical external links and a comprehensive rights review of inherited images. Narration/podcasts remain an idea, not produced media.

For relevant changes, rebuild, check generated/local links and `git diff --check`, and inspect desktop/mobile behavior when layout or interaction changes. The author previously authorized direct publication to `main`; that does not extend to publishing another project.

## Scope boundary

This task concerns Simulate World. Save the World is a separate project with a separate editorial arc. The earlier mixed conversation remains available as history; it is not a reason to import the other project's prose, data, or publication settings here.
