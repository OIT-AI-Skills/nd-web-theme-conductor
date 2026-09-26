# Conductor — Notre Dame's CMS

Conductor is the university's proprietary CMS (conductor.nd.edu), powering 700+ campus sites. Site owners edit pages in a browser-based editor; the ND Web Theme v4 (NDT4) renders the chrome around their content.

## What editors work with

- **Pages** — title, layout/page settings (featured image, full-width, sidebar), and a WYSIWYG content editor with an HTML source view. Content authored with this skill is pasted into the source view.
- **News, Events, People, FAQs, Media Mentions** — structured content types with their own entry forms; Conductor generates themed listings and cards automatically. Prefer these over hand-building news/event/people markup: hand-built copies won't stay in sync.
- **Snippets** — reusable content fragments that can be included across pages. A component you'll reuse on several pages is a good snippet candidate.
- **Uploads** — images and documents. Uploaded images are served at paths like `/assets/<id>/<width>x/<filename>` (the `<width>x` segment requests a resized rendition — e.g. `/assets/607853/300x/logo.png`). Reference uploaded assets rather than hotlinking external images.
- **Site settings** — navigation, redirects, users/roles, password protection.

## Ground rules for generated content

- The WYSIWYG editor rewrites or strips some markup on save. Confirmed behavior: it enforces strict HTML content models — `div` wrappers inside `<dl>` are stripped (which breaks hand-pasted FAQ-module markup); scripts and unknown embeds are also off-limits. Ordinary `div`s, classes, and standard block elements survive. Keep nesting plain-vanilla, and after pasting, save and re-open the source view to verify Conductor kept your structure. If interactivity beyond the theme's components (accordion, tabs, dialog, gallery) is needed, that's a conversation with the Conductor team (webhelp@nd.edu), not something to sneak into content.
- Advanced styling, custom theme layouts, and special Conductor features — the FAQ module, and the other structured-content modules (News, Events, People, Media Mentions, Galleries) — require setup by the ND Creative team. Direct site owners to work with them (webhelp@nd.edu) rather than hand-building imitations of module output.
- `<style>` blocks: prefer the site stylesheet for anything reused; a page-scoped style block is acceptable for one-off features (see page-anatomy.md). If the editor strips a style block on save, move the CSS to the site stylesheet.
- Forms: Conductor pages have no server-side form handling. Link out to (or embed) Qualtrics/Google/Formstack forms.
- Don't paste content copied from Word/Google Docs without cleanup — it carries inline styles and spans that fight the theme. The same applies to AI-generated HTML that wasn't built against this skill: strip inline styles, replace invented classes with theme classes.
- Every image needs meaningful `alt` text (or `alt=""` when purely decorative) plus `width`/`height` attributes.

## Publishing workflow

Pages support drafts, revision history, publish/unpublish, and server-cache clearing. A safe iteration loop for a big page change: preview locally (this skill's preview), paste into a draft, review on the site, publish.

## Getting help

- User guide: https://conductor.nd.edu/user-guide/
- Theme reference (Storybook): https://webtheme.nd.edu/
- Conductor team: webhelp@nd.edu
