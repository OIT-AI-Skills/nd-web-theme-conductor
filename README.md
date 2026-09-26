# nd-web-theme — Notre Dame Web Theme v4 + Conductor content skill

An AI agent skill that helps site owners create web page content for University of Notre Dame websites managed in [Conductor](https://conductor.nd.edu/) (ND's CMS) and rendered with the [Notre Dame Web Theme v4](https://webtheme.nd.edu/) (NDT4).

Give an AI assistant this skill and a request like *"build a page announcing our spring workshops"* or *"this page doesn't match our theme — fix it,"* and it produces paste-ready HTML for Conductor's source view, built entirely from official theme components — plus a standalone preview file that renders against the real theme stylesheet so you can check the result in a browser before touching the CMS.

## Why this exists

AI-generated page content usually *almost* matches the ND theme: it invents class names, hard-codes brand hex values, adds inline styles, and re-implements components the theme already ships. Those pages drift off-brand and break in dark mode, on mobile, or at the next theme update. This skill fixes that by giving the model the theme's actual vocabulary — component markup extracted from the official NDT4 Storybook, the real color/spacing/grid tokens, and the rules for what survives Conductor's editor. With the Web Theme MCP endpoint connected, it also verifies component markup and options against the live Storybook before writing them.

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

## How to install this skill

A skill is just a directory with `SKILL.md` at its root — the format ChatGPT Codex, GitHub Copilot, and Claude Code all read. Installing it means cloning this repo into the skills directory your client watches.

| Client | Personal (every project) | One project only |
|---|---|---|
| ChatGPT Codex | `~/.agents/skills/nd-web-theme` | `.agents/skills/nd-web-theme` |
| GitHub Copilot | `~/.copilot/skills/nd-web-theme` | `.github/skills/nd-web-theme` |
| Claude Code | `~/.claude/skills/nd-web-theme` | `.claude/skills/nd-web-theme` |

```bash
# swap the destination for the path your client uses
git clone https://github.com/OIT-AI-Skills/nd-web-theme-conductor.git \
  ~/.agents/skills/nd-web-theme
```

Start a new session afterward. You don't invoke the skill by name — it loads on its own when you ask for ND page content. Run `git pull` in that directory to take updates.

Copilot also reads `.agents/skills` and `.claude/skills` inside a project, so if you're standardizing a repo for a mixed team, one project-level `.agents/skills/nd-web-theme` copy covers both Codex and Copilot.

### Claude apps (claude.ai, desktop)

Zip the repo so that `SKILL.md` sits at the root of the archive, then upload it under **Settings → Capabilities → Skills**:

```bash
git clone https://github.com/OIT-AI-Skills/nd-web-theme-conductor.git nd-web-theme
cd nd-web-theme && rm -rf .git
zip -r ../nd-web-theme.skill .
```

### Tools without skill support (e.g., Gemini)

Paste the contents of `nd-web-theme-flattened.md` into the conversation or system context. It's the same skill restructured as one self-contained document, with the preview shell inlined instead of scripted.

### Connect the live theme documentation (recommended)

The Web Theme Storybook is also served over the Model Context Protocol at `https://webtheme.nd.edu/mcp` — read-only, no login. Connecting it lets the assistant look up the real markup and options for any component instead of relying only on the reference files bundled here. The skill uses it automatically when it's available.

**ChatGPT Codex**

```bash
codex mcp add nd-web-theme --url https://webtheme.nd.edu/mcp
```

Or add it to `~/.codex/config.toml` (use `.codex/config.toml` to scope it to one trusted project):

```toml
[mcp_servers.nd-web-theme]
url = "https://webtheme.nd.edu/mcp"
```

**GitHub Copilot in VS Code** — `.vscode/mcp.json` for one workspace, or your user `mcp.json` for all of them:

```json
{
  "servers": {
    "nd-web-theme": { "type": "http", "url": "https://webtheme.nd.edu/mcp" }
  }
}
```

For the Copilot coding agent, a repository admin adds it under **Settings → Copilot → MCP servers** — same URL, but that form nests servers under an `mcpServers` key rather than `servers`.

**Claude Code**

```bash
claude mcp add --transport http nd-web-theme https://webtheme.nd.edu/mcp --scope user
```

Drop `--scope user` to add it for the current project only. In any of the three clients, run `/mcp` to confirm it connected; you should see three tools — `docs-list`, `docs-show`, and `docs-show-story`.

Worth stating plainly: every nd.edu site is expected to meet the University's [website brand requirements](https://webtheme.nd.edu/) — design standards, quality expectations, and hosting — and vibe-coded sites are no exception. That's what this skill and the MCP endpoint exist to make easy.

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
- **The theme docs can be live.** With the MCP endpoint connected, the skill reads component markup and options straight from the Storybook, so it stays correct as NDT4 changes; without it, it falls back to the reference files in this repo.
- **Some features belong to the ND Creative team.** The FAQ module, other structured-content modules (News, Events, People, Media Mentions, Galleries), custom theme layouts, and advanced styling require setup by the Creative team — contact [webhelp@nd.edu](mailto:webhelp@nd.edu). The skill directs users there rather than imitating module output in content HTML.

## Building a preview manually

```bash
python3 scripts/make_preview.py my-page-content.html -o my-page-preview.html \
  --title "Page Title" --site "Site Name" [--full-width]
```

## Repackaging after changes

Most installs are git clones, so edits reach users with a `git pull` — no packaging step. The only path that needs repackaging is the Claude app upload: rezip the directory with `SKILL.md` at the archive root as shown above. Keep the `name:` in `SKILL.md` unchanged so an upload replaces the installed skill rather than duplicating it.

If you change `SKILL.md` or a reference file, update `nd-web-theme-flattened.md` to match so the paste-in version doesn't drift.

## Maintenance notes

The theme reference files are generated from the live Storybook, so they can be refreshed when NDT4 changes: the extraction renders each Storybook story headlessly and captures its markup (the Storybook's `index.json` lists all stories; each renders at `iframe.html?id=<story-id>&viewMode=story`). The MCP endpoint always reflects the current Storybook, which makes the bundled references a convenience layer rather than the only source — the skill is told to prefer MCP output when the two disagree. If a component looks wrong on a real site, trust the live site and Storybook over this repo, and open an issue or PR.

Questions about the skill: AI Enablement, OIT. Questions about Conductor or the theme: [webhelp@nd.edu](mailto:webhelp@nd.edu).
