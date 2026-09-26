---
name: nd-web-theme
description: Create web page content for University of Notre Dame websites built on Conductor (ND's CMS) and the Notre Dame Web Theme v4 (NDT4). Use this whenever the user wants to create, redesign, style, or fix content for an nd.edu site — pages, landing pages, tool/service pages, FAQs, cards, banners, or any HTML destined for Conductor — even if they only say "our website," name an nd.edu URL, or ask why their page "doesn't match the theme." Produces paste-ready content-region HTML using official theme components plus a local browser preview.
---

# Notre Dame Web Theme v4 + Conductor content

You are producing content for a Conductor-managed nd.edu site running NDT4. The theme already supplies the site header, navigation, page title, sidebar, footer, fonts, colors, spacing, responsiveness, and dark mode. Your job is to author only the **content region** — the HTML inside `.page-primary` — using the theme's own components and classes so the result is indistinguishable from pages built by ND's web team.

Why this matters: AI-generated pages typically fail by re-inventing what the theme provides — inline styles, raw hex colors, invented class names (`callout`, `row`, `columns`), duplicate hero titles. Those pages look almost right, then break in dark mode, on mobile, or at the next theme update. Everything you need already exists as a theme component; your task is selection and composition, not invention.

## Live theme documentation (MCP)

The theme's Storybook is served to AI assistants over the Model Context Protocol at **`https://webtheme.nd.edu/mcp`** (read-only, no login). When those tools are connected they are the authoritative source for component markup and options — the bundled `references/` files are a curated snapshot and can lag behind the theme.

The three tool names below may appear prefixed with the server name, depending on the client.

| Tool | Returns |
|---|---|
| `docs-list` | Every component, collection, template, and docs page with its ID. Call **once** per task; the response is long. |
| `docs-show` (`id`) | A component's description, its options table, rendered HTML for its first stories, the IDs of its remaining stories, and its modifier-class / CSS / accessibility notes. Also returns whole docs pages — `foundation-colors--docs`, `foundation-utilities--docs`, `foundation-grid--docs`, `foundation-typography--docs`, `foundation-accessibility--docs`. |
| `docs-show-story` (`storyId`) | The HTML for one specific variant, e.g. `components-notice--warning`. |

How to use them:

- **Never invent an option, modifier, or class.** If it isn't in `docs-show` output for that component, it doesn't exist — tell the user rather than borrowing a plausible-sounding prop from another design system.
- Only use IDs returned by `docs-list` or `docs-show`. Never guess an ID.
- **Storybook renders whole pages; you author a fragment.** `collections-site-header`, `collections-site-footer`, `collections-page-header-*`, `components-page-title`, `components-navigation-*`, and everything under `templates-*` are produced by Conductor and the theme. Read them for context; never copy them into content HTML.
- The references carry what Storybook doesn't: the theme/content boundary, Conductor editor behavior, spacing judgment, and which features belong to the ND Creative team. Use MCP for *what the markup is*, references for *what to author and what survives*.
- If the tools aren't connected, work from `references/` and mention that connecting the endpoint gives live docs (install steps are in the README).

## Workflow

1. **Understand the content.** What is this page for, who reads it, what should they do next? Get real copy or write it; structure beats decoration.

2. **Read `references/page-anatomy.md` first** (short) — it defines the theme/content boundary and the rules that prevent the classic failures.

3. **Pick components, then get their real markup.** If the MCP tools are connected: `docs-list` once, then `docs-show` for each component you intend to use. Either way, read the reference file for the area you're working in — it covers composition and Conductor constraints the Storybook doesn't:
   - `references/content-components.md` — headings, lists, buttons, quotes, notices/callouts, tables, icons & stickers
   - `references/cards-and-media.md` — cards (default/featured/news/event/people), images, galleries, video, stats
   - `references/interactive-components.md` — accordions, FAQs, tabs, dialogs, timelines, pagination
   - `references/banners-and-sections.md` — full-width sections, banners, page headers (landing/homepage-style pages)
   - `references/forms.md` — form markup (link out for actual submission handling)
   - `references/foundation.md` — grid, spacing/utility classes, color tokens, typography rules
   - `references/conductor.md` — how Conductor publishing works, images/uploads, snippets, what the editor may strip

4. **Compose the fragment.** Copy component markup from `docs-show` or the references and adapt it. Start headings at `<h2>` (the page title is the theme's `<h1>`). Prefer plain semantic HTML for prose — it's already styled. Save as `<slug>-content.html`.

5. **Verify against the checklist below.** Fix anything that fails.

6. **Build the preview** so the user can see it with real theme CSS before touching Conductor:
   ```bash
   python3 scripts/make_preview.py <slug>-content.html -o <slug>-preview.html --title "Page Title" --site "Site Name"
   ```
   Add `--full-width` for pages using full-bleed sections. Deliver **both files** and tell the user: open the preview in a browser to check it, then paste the *content* file into Conductor's HTML source view.

## Checklist (run before delivering)

- No `<h1>` in the fragment; heading levels are sequential (h2 → h3 → h4, no skips).
- No `style=""` attributes. No raw hex colors — theme classes or `var(--*)` tokens only.
- Every class name exists in the theme (if you didn't copy it from `docs-show` or a reference, look it up — don't guess; Bootstrap/Foundation-era names like `row`, `columns`, `label`, `callout`, `btn-primary` are not NDT4).
- No `<script>` tags. No custom fonts. No re-implemented components (the theme's `.notice` is the callout; `.btn` is the button; `.card` is the card).
- Images: real `alt` text (or `alt=""` if decorative), `width`/`height` attributes, uploaded-asset paths (`/assets/<id>/<width>x/<file>`) rather than external hotlinks where possible.
- Links: descriptive text (not "click here"); external links are fine as plain `<a>` — the theme decorates them.
- If custom CSS was truly unavoidable: it's minimal, uses theme variables, is scoped under one feature class, and sits in an `@layer site { ... }` block with a note to move it to the site stylesheet (see page-anatomy.md).
- Dark-mode sanity: nothing sets text or background colors outside `.bg--*` classes and tokens.

## Judgment calls

- **When sources disagree:** MCP output wins over `references/`, and a live production nd.edu site wins over both. Mention the drift so the reference file can be refreshed.
- **News, events, people, FAQs:** Conductor generates these listings from structured content. If the user wants a news feed or staff directory, point them to the Conductor content type first (see conductor.md); hand-build the markup only for one-off or custom layouts.
- **FAQ pages:** the theme's numbered FAQ treatment comes from Conductor's FAQ module, which requires setup by the ND Creative team — recommend the site owner work with them (webhelp@nd.edu). Never hand-paste the module's `dl.faq`/`div.faq-item` markup into the editor: it strips the div wrappers on save and the styling silently dies. For hand-built Q&A content, use the editor-safe accordion pattern (with an anchor ToC for 4+ questions) from interactive-components.md.
- **Editor survival:** whatever you generate must survive Conductor's WYSIWYG sanitizer. It preserves ordinary divs, classes, and standard block elements, but rewrites markup that violates strict HTML content models (e.g. divs inside `dl`). Prefer plain-vanilla element nesting, and tell the user: after pasting and saving, re-open the source view — if Conductor restructured your markup, the affected component needs the editor-safe alternative or the ND Creative team.
- **ND Creative team:** advanced styling, custom theme layouts, and special Conductor features (FAQ module, other structured-content modules) are their territory — point site owners to them rather than approximating those features in content HTML.
- **Breathing room:** dense output is the second-most-common tell of off-theme pages (after inline styles). When stacking blocks — benefits, feature blurbs, definition pairs — prefer layouts with built-in spacing: `.grid .grid-md-2/3` of `h3`+`p` divs (2rem gap) or cards. Avoid `dl.list--grid` for anything but genuinely compact term/definition data (it has zero row gap). After composing, reread the fragment asking "where will this feel cramped?" and add `.mb-*`/`.pb-*` utilities or switch patterns.
- **"Make it pop":** reach for theme options — `.bg--*` section backgrounds, featured cards, stats, quotes, stickers — before custom CSS. The theme has more range than it first appears; banners-and-sections.md is the showpiece file.
- **Existing off-theme pages:** when fixing a page (e.g., AI-generated HTML with inline styles), map each visual intention to its theme equivalent rather than translating style-for-style. A "hero banner" duplicating the page title should usually be deleted, not restyled.
- **Other ND sub-brands/sites:** everything here applies to any Conductor site on NDT4, not just one site. Site-specific accent styles belong in that site's stylesheet, not in content.
