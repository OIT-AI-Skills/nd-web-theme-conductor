# nd-web-theme — Notre Dame Web Theme v4 + Conductor content skill

An AI agent skill that helps site owners create web page content for University of Notre Dame websites managed in [Conductor](https://conductor.nd.edu/) (ND's CMS) and rendered with the [Notre Dame Web Theme v4](https://webtheme.nd.edu/) (NDT4).

Give an AI assistant this skill and a request like *"build a page announcing our spring workshops"* or *"this page doesn't match our theme — fix it,"* and it produces paste-ready HTML for Conductor's source view, built entirely from official theme components — plus a standalone preview file that renders against the real theme stylesheet so you can check the result in a browser before touching the CMS.

## Why this exists

AI-generated page content usually *almost* matches the ND theme: it invents class names, hard-codes brand hex values, adds inline styles, and re-implements components the theme already ships. Those pages drift off-brand and break in dark mode, on mobile, or at the next theme update. This skill fixes that by giving the model the theme's actual vocabulary — component markup extracted from the official NDT4 Storybook, the real color/spacing/grid tokens, and the rules for what survives Conductor's editor.

## What's in this repo

| Path | Purpose |
|---|---|
| `SKILL.md` | The skill entry point: workflow, pre-delivery checklist, judgment calls |
| `references/page-anatomy.md` | What the theme renders vs. what editors author — read this first |
| `references/foundation.md` | Colors, typography, grid, spacing/utility classes |
| `references/content-components.md` | Headings, lists, buttons, quotes, notices, tables, icons & stickers |
| `references/cards-and-media.md` | Cards (default/featured/news/event/people), images, galleries, video, stats |
| `references/interactive-components.md` | Accordions, FAQs, tabs, dialogs, timelines, pagination |
| `references/banners-and-sections.md` | Full-width sections and banners for landing/homepage-style pages |
| `references/forms.md` | Form markup patterns |
| `references/conductor.md` | How Conductor publishing works; known editor behaviors |
| `assets/preview-template.html` | Page shell for local previews (loads production theme CSS) |
| `assets/icons-nd-base.svg`, `assets/stickers-nd-base.svg` | Official NDT4 SVG sprites, inlined into previews |
| `scripts/make_preview.py` | Wraps a content fragment in the preview shell |
| `nd-web-theme-flattened.md` | Single-file version for tools without skill support (see below) |

All component markup was extracted from the official Storybook at webtheme.nd.edu and cross-checked against production Conductor sites — it is the theme's own markup, not a reconstruction.

## Installing

**Tools that support the agent skills standard (e.g., Claude, ChatGPT):** add the skill from this repo — either package it as a `.skill` file (see below) and save it to your profile, or, in Claude Code, copy the skill directory into your project's `.claude/skills/`.

**Other tools (e.g., Gemini):** paste the contents of `nd-web-theme-flattened.md` into the conversation or system context. It's the same skill restructured as one self-contained document, with the preview shell inlined instead of scripted.

## Using it

Ask for what you need in plain language — the skill handles the theme mechanics:

- "Create a page for our new AI workshop series with three cards and a registration call-to-action."
- "Here's the HTML of our tool page — it was AI-generated and doesn't match the theme. Rebuild it."
- "Make an FAQ page about travel reimbursement with eight questions."

You'll get two files back: a `*-content.html` fragment (paste into Conductor's **HTML source view**) and a `*-preview.html` (open in a browser to review first — it loads the production theme CSS, so what you see is what Conductor will render).

After pasting into Conductor and saving, re-open the source view once to confirm the editor kept your structure — see the caveats below.

## Things worth knowing

- **The theme owns the page chrome.** The site header, navigation, page title (`h1`), sidebar, and footer come from Conductor page settings — generated content is the inside of the content region only, and starts its headings at `h2`.
- **Conductor's editor sanitizes pasted markup.** Ordinary divs and classes survive; markup that violates strict HTML content models does not (confirmed: `div` wrappers inside `<dl>` are stripped, which silently breaks hand-pasted FAQ-module markup). The skill generates editor-safe patterns and says so when a feature needs more.
- **Some features belong to the ND Creative team.** The FAQ module, other structured-content modules (News, Events, People, Media Mentions, Galleries), custom theme layouts, and advanced styling require setup by the Creative team — contact [webhelp@nd.edu](mailto:webhelp@nd.edu). The skill directs users there rather than imitating module output in content HTML.

## Building a preview manually

```bash
python3 scripts/make_preview.py my-page-content.html -o my-page-preview.html \
  --title "Page Title" --site "Site Name" [--full-width]
```

## Repackaging after changes

Edit the skill source, then package it with the [skill-creator](https://github.com/anthropics/skills) tooling (or any zip of the `nd-web-theme/` directory with `SKILL.md` at its root renamed to `.skill`). Keep the `name:` in `SKILL.md` unchanged so updates replace the installed skill rather than duplicating it.

## Maintenance notes

The theme reference files are generated from the live Storybook, so they can be refreshed when NDT4 changes: the extraction renders each Storybook story headlessly and captures its markup (the Storybook's `index.json` lists all stories; each renders at `iframe.html?id=<story-id>&viewMode=story`). If a component looks wrong on a real site, trust the live site and Storybook over this repo, and open an issue or PR.

Questions about the skill: AI Enablement, OIT. Questions about Conductor or the theme: [webhelp@nd.edu](mailto:webhelp@nd.edu).
