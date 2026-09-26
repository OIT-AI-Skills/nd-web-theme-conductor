# Notre Dame Web Theme v4 + Conductor — flattened skill

> Single-file version of the `nd-web-theme` Claude skill, for pasting into Gemini, ChatGPT, or any AI tool that doesn't support installable skills. Paste this whole document as context/system instructions, then make your request (e.g. "build a page about X for our Conductor site").
>
> Generated from the official NDT4 Storybook (webtheme.nd.edu) and live Conductor sites.


# Notre Dame Web Theme v4 + Conductor content

You are producing content for a Conductor-managed nd.edu site running NDT4. The theme already supplies the site header, navigation, page title, sidebar, footer, fonts, colors, spacing, responsiveness, and dark mode. Your job is to author only the **content region** — the HTML inside `.page-primary` — using the theme's own components and classes so the result is indistinguishable from pages built by ND's web team.

Why this matters: AI-generated pages typically fail by re-inventing what the theme provides — inline styles, raw hex colors, invented class names (`callout`, `row`, `columns`), duplicate hero titles. Those pages look almost right, then break in dark mode, on mobile, or at the next theme update. Everything you need already exists as a theme component; your task is selection and composition, not invention.

## Live theme documentation (MCP) — optional

The theme's Storybook is served over the Model Context Protocol at **`https://webtheme.nd.edu/mcp`** (read-only, no login). If the tool you're using supports MCP servers, connect it — it exposes three tools that are authoritative for component markup and options, and the reference sections in this document are a snapshot that can lag behind the theme:

- `docs-list` — every component, collection, template, and docs page, with its ID. Call once per task; the response is long.
- `docs-show` (`id`) — a component's description, options table, rendered HTML for its first stories, the IDs of its remaining stories, and its modifier-class / CSS / accessibility notes. Also returns whole docs pages (`foundation-colors--docs`, `foundation-utilities--docs`, `foundation-grid--docs`, `foundation-typography--docs`, `foundation-accessibility--docs`).
- `docs-show-story` (`storyId`) — the HTML for one specific variant, e.g. `components-notice--warning`.

Rules when they're available: never invent an option, modifier, or class that `docs-show` doesn't list; only use IDs the tools returned; and remember Storybook renders whole pages — the site header/footer, page headers, page title, navigation, and `templates-*` entries are produced by Conductor and the theme, so read them for context but never copy them into content HTML. Where MCP output and this document disagree, MCP wins.

Without MCP, everything you need is below.

## Workflow

1. **Understand the content.** What is this page for, who reads it, what should they do next? Get real copy or write it; structure beats decoration.

2. **Review the "Page Anatomy" section below first** — it defines the theme/content boundary and the rules that prevent the classic failures.

3. **Pick components from the reference sections below** (all included in this document): text & content components, cards & media, interactive components, banners & sections, forms, foundation (grid/colors/utilities), and Conductor CMS notes. If the MCP tools above are connected, confirm each component's markup and options with `docs-show` before using it.

4. **Compose the fragment.** Copy component markup from `docs-show` or the references and adapt it. Start headings at `<h2>` (the page title is the theme's `<h1>`). Prefer plain semantic HTML for prose — it's already styled.

5. **Verify against the checklist below.** Fix anything that fails.

6. **Deliver two things:** (a) the content fragment (what gets pasted into Conductor's HTML source view), and (b) a standalone preview: the fragment wrapped in the "Preview page shell" template at the end of this document, so the user can save it as an .html file, open it in a browser, and see the result with the real theme CSS before touching Conductor.

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

- **News, events, people, FAQs:** Conductor generates these listings from structured content. If the user wants a news feed or staff directory, point them to the Conductor content type first (see conductor.md); hand-build the markup only for one-off or custom layouts.
- **FAQ pages:** the theme's numbered FAQ treatment comes from Conductor's FAQ module, which requires setup by the ND Creative team — recommend the site owner work with them (webhelp@nd.edu). Never hand-paste the module's `dl.faq`/`div.faq-item` markup into the editor: it strips the div wrappers on save and the styling silently dies. For hand-built Q&A content, use the editor-safe accordion pattern (with an anchor ToC for 4+ questions) from interactive-components.md.
- **Editor survival:** whatever you generate must survive Conductor's WYSIWYG sanitizer. It preserves ordinary divs, classes, and standard block elements, but rewrites markup that violates strict HTML content models (e.g. divs inside `dl`). Prefer plain-vanilla element nesting, and tell the user: after pasting and saving, re-open the source view — if Conductor restructured your markup, the affected component needs the editor-safe alternative or the ND Creative team.
- **ND Creative team:** advanced styling, custom theme layouts, and special Conductor features (FAQ module, other structured-content modules) are their territory — point site owners to them rather than approximating those features in content HTML.
- **Breathing room:** dense output is the second-most-common tell of off-theme pages (after inline styles). When stacking blocks — benefits, feature blurbs, definition pairs — prefer layouts with built-in spacing: `.grid .grid-md-2/3` of `h3`+`p` divs (2rem gap) or cards. Avoid `dl.list--grid` for anything but genuinely compact term/definition data (it has zero row gap). After composing, reread the fragment asking "where will this feel cramped?" and add `.mb-*`/`.pb-*` utilities or switch patterns.
- **"Make it pop":** reach for theme options — `.bg--*` section backgrounds, featured cards, stats, quotes, stickers — before custom CSS. The theme has more range than it first appears; banners-and-sections.md is the showpiece file.
- **Existing off-theme pages:** when fixing a page (e.g., AI-generated HTML with inline styles), map each visual intention to its theme equivalent rather than translating style-for-style. A "hero banner" duplicating the page title should usually be deleted, not restyled.
- **Other ND sub-brands/sites:** everything here applies to any Conductor site on NDT4, not just one site. Site-specific accent styles belong in that site's stylesheet, not in content.


---

## Page Anatomy — what the theme renders vs. what you author

Understanding this split is the difference between content that "plugs in" and content that fights the theme.

### The full page skeleton (theme + Conductor render all of this)

```
<body id="..." class="... page--full-width? nav-top--true ..." data-theme="light">
  <nav class="skip-links">…</nav>
  <div id="wrapper" class="wrapper">
    <header id="header" class="site-header">   ← site title, marks, primary nav, search
    <main id="content" class="site-content">
      <div class="page-header [page-header--inset|fade|screen|…]">
        <div class="page-title-wrapper">
          [breadcrumbs]
          <h1 class="page-title">…</h1>        ← from the Conductor page title field
        </div>
        [figure.page-image]                     ← featured image from page settings
      </div>
      <div class="page-primary">
        ★ YOUR CONTENT GOES HERE ★
      </div>
      <div class="page-sidebar">…</div>         ← section nav, from Conductor
    </main>
    <footer id="footer" class="site-footer">…</footer>
  </div>
</body>
```

Everything marked with arrows is produced by Conductor and the theme from page settings — the site header, navigation, breadcrumbs, the `h1.page-title`, the featured image treatment, the sidebar, and the footer. **Content you author is the inside of `.page-primary`.**

Practical consequences:

- Never author another `<h1>` — the page title is already the h1. Start your content's heading outline at `<h2>`.
- Never author `.wrapper`, `.site-header`, `.page-header`, `.page-title`, `.page-sidebar`, or `.site-footer` markup — it will duplicate what's already on the page.
- Don't re-state the page title as a hero banner at the top of the content; the page header already does that job. If a page needs a big visual opening, that's the *featured image* / page-header variant in Conductor's page settings, not content HTML.
- The theme is responsive and has a dark mode (`data-theme`). Content built from theme classes inherits both for free; hard-coded colors break dark mode.

### Content-region building blocks

Inside `.page-primary`, plain semantic HTML is already styled: `h2`–`h4`, `p`, `ul`/`ol`, `table`, `blockquote`, `figure`/`img`, `a`. Reach for components (cards, notices, accordions, …) only when the content calls for them.

For richer layouts within the content column:

- `.grid` + `.grid-md-2/3/…` for columns (see foundation.md).
- Components from the reference files (cards-and-media.md, content-components.md, interactive-components.md).

### Full-width pages

Some pages (homepages, landing pages) are set to full width in Conductor (`body.page--full-width`). There the content region can also contain full-bleed sections:

```html
<div class="page-secondary full-width">
  <section class="section bg--brand-blue bg--full-bleed">
    <div class="block-center text-center">
      <h2 class="section-title">…</h2>
      …
    </div>
  </section>
  <section class="section home-news bg--full-bleed bg--warm-white">…</section>
</div>
```

See banners-and-sections.md for the banner patterns that live inside these sections. On a standard (non-full-width) page, stick to the content column — full-bleed sections need the full-width page setting to look right.

### Custom CSS, when the theme truly has no equivalent

Order of preference:

1. A theme class that already does it (check foundation.md utilities first — spacing, alignment, backgrounds cover most "I just need to nudge this" cases).
2. Theme CSS variables in a small scoped style block, so values stay on-token.
3. Only then: custom CSS. Scope it to the page or feature with a single wrapper class, and put it in the site stylesheet (each Conductor site has one, loaded after the theme) or a `<style>` block at the top of the content. Use the theme's reserved cascade layer so you never need `!important`:

```html
<div class="tool-page">…</div>
<style>
  @layer site {
    .tool-page .comparison-callout {
      border-inline-start: 4px solid var(--brand-gold);
      padding: 1rem;
      background: var(--sky-blue-light);
    }
  }
</style>
```

Never: inline `style=""` attributes sprinkled across elements, raw hex colors that shadow brand tokens, custom fonts, or re-implementations of components the theme already ships (buttons, callouts/notices, cards, tabs). Those are exactly how pages drift off-brand and break in dark mode or the next theme update.


---

## Foundation — Colors, Typography, Grid, Utilities (ND Web Theme v4)

The theme's design tokens and layout system. Use these instead of hand-rolled values: every color, spacing step, and breakpoint you need already exists as a class or CSS variable.

**Contents:** Colors, Typography, Grid, Utility classes, Breakpoints, Animations, CSS layers

### Colors

Use CSS variables or `.bg--*` classes — never raw hex values in content.

Brand palette (CSS variable → hex):

| Color | Variable | Hex |
|---|---|---|
| Brand Blue Bright | `--brand-blue-bright` | #1c4f8f |
| Brand Blue Light | `--brand-blue-light` | #143865 |
| Brand Blue | `--brand-blue` | #0c2340 |
| Brand Blue Dark | `--brand-blue-dark` | #081629 |
| Brand Gold Bright | `--brand-gold-bright` | #d39f10 |
| Brand Gold Light | `--brand-gold-light` | #ddc278 |
| Brand Gold | `--brand-gold` | #ae9142 |
| Brand Gold Dark | `--brand-gold-dark` | #8c7535 |
| Brand Green Bright | `--brand-green-bright` | #35b36a |
| Brand Green | `--brand-green` | #0a843d |
| Brand Green Dark | `--brand-green-dark` | #085e2c |
| Sky Blue Light | `--sky-blue-light` | #edf2f9 |
| Sky Blue | `--sky-blue` | #e1e8f2 |
| Sky Blue Dark | `--sky-blue-dark` | #c1cddd |
| Warm White | `--warm-white` | #f8f4ec |
| Warm White Dark | `--warm-white-dark` | #efe9d9 |
| Gray Extra Extra Light | `--gray-extra-extra-light` | #f1f2f4 |
| Gray Extra Light | `--gray-extra-light` | #e9ebee |
| Gray Light | `--gray-light` | #d6dadf |
| Gray | `--gray` | #555555 |
| Gray Dark | `--gray-dark` | #333333 |

Background classes (apply to any element; each sets an appropriate light/dark color scheme for its text): `.bg--white`, `.bg--gray-extra-extra-light`, `.bg--gray-extra-light`, `.bg--gray-light`, `.bg--gray`, `.bg--gray-dark`, `.bg--black`, `.bg--sky-blue-light`, `.bg--sky-blue`, `.bg--sky-blue-dark`, `.bg--warm-white`, `.bg--brand-blue-bright`, `.bg--brand-blue-light`, `.bg--brand-blue`, `.bg--brand-blue-dark`.

Gradients: add `.bg--gradient` to a `.bg--*` element, plus a direction class: `.bg--to-bottom`, `.bg--to-bottom-right`, `.bg--to-bottom-left`, `.bg--to-left`, `.bg--to-top-left`, `.bg--to-top`, `.bg--to-top-right`. Transparent overlay: `.bg--transparent` combined with a `.bg--*` color.

Rules from the brand guidelines:

- Brand Blue and Dark Gray are the only heading colors in body copy; white is allowed on dark backgrounds. Don't override the theme's default font colors.
- Secondary/tertiary colors should be no more than ~25% of color usage on a page.
- Text contrast must meet WCAG AA (4.5:1 normal text, 3:1 large text).

### Typography

Fonts load automatically: Garamond Premier Pro (ornamental headings, page titles, blockquotes) and Galaxie Polaris (default headings and body copy). Font-stack variables: `--font-heading`, plus the default body stack. Never load your own fonts or specify font-family in content.

- Body copy shouldn't exceed ~70 characters per line (theme containers already handle this — another reason not to fight the layout).
- `.h1` … `.h6` classes restyle any element to that heading's look without changing semantics.

### Grid

`.grid` + a breakpoint-column modifier `.grid-<bp>-<n>` (n = 1–6). Children fill cells in order.

| Breakpoint | Min width | Modifier |
|---|---|---|
| Extra small | none | `.grid-xs-*` |
| Small | 480px | `.grid-sm-*` |
| Medium | 768px | `.grid-md-*` |
| Medium large | 960px | `.grid-ml-*` |
| Large | 1280px | `.grid-lg-*` |
| Extra large | 1440px | `.grid-xl-*` |
| Extra-extra large | 1600px | `.grid-xxl-*` |

```html
<div class="grid grid-md-3">
  <div>One of three columns</div>
  <div>Two of three columns</div>
  <div>Three of three columns</div>
</div>
```

Stack modifiers to change column count per breakpoint: `class="grid grid-sm-2 grid-lg-4"`. Span columns with `.span-<bp>-<n>` (e.g. `.span-md-2`); `.full` spans the whole row. Reorder per breakpoint with `.order-<bp>-<n>`. Gap: default 2rem (`--grid-gap`); adjust with `.grid-gap-xs/sm/md/lg/xl` or remove with `.no-gap`.

### Utility classes

- Spacing: margin `m-0`…`m-5`, `m-auto`; padding `p-0`…`p-5`. Block-axis (`mb-`, `pb-`), inline-axis (`mi-`, `pi-`), and start/end variants (`mbs-`, `mbe-`, `pbs-`, `pbe-`, `mis-`, `mie-`, `pis-`, `pie-`). Steps: 1 = 0.5rem, 2 = 1rem, … `mi-gutter` uses the gutter width.
- Text: `.text-start`, `.text-center`, `.text-end`, `.text-pretty`, `.text-balance`.
- Visibility: `.hidden` (display:none), `.invisible`, `.visually-hidden` (screen-reader only), responsive `.visually-hidden-md/ml/lg/xl/xxl`.
- Display: `.d-inline`, `.d-block`, `.d-grid`, `.d-flex`, `.d-none`; `.position-sticky`, `.position-fixed`.
- Flex: `.flex-row`, `.flex-column`, `.flex-wrap`, `.flex-nowrap`, `.flex-grow-1`, `.flex-shrink-0`; alignment `.justify-center`, `.align-center`, `.align-self-end`, `.align-content-between`.
- Object fit: `.object-fit-cover`, `.object-fit-contain`, etc.
- Column-width containers: `.col--sm`, `.col--md`, `.col--lg`, `.col--xl`, `.col--c`, `.col--screen`.
- Misc: `.wrap-link` (force long links to wrap), `.block-center` (centered max-width column).

### Animations

Optional `animate.css` (`https://conductor.nd.edu/stylesheets/themes/ndt/4.0/animate.css`, included after the main stylesheet — many sites don't load it; check before relying on it). Usage: `.animate` plus `.animate--fade-in`, `.animate--fade-in-up`, `.animate--fade-in-left`, `.animate--fade-in-right`, `.animate--move-up/down/left/right`. Keep animations short (<500ms) and purposeful; the theme already respects `prefers-reduced-motion`.

### CSS layers

NDT4 organizes styles in CSS cascade layers and reserves an empty `site` layer for site-specific styles. Custom site CSS added via `@layer site { ... }` will layer correctly above the theme without specificity fights.


---

## Text & Content Components — ND Web Theme v4

Everyday content formatting: headings, lists, buttons, quotes, notices, tables, icons. Markup extracted from the official NDT4 Storybook.

**Contents:** Headings, Page Title, Lists, Buttons, Quotes, Notice, Table, Footnote, Byline, Media Mention, Icons & Stickers

### Headings

Default heading hierarchy is styled automatically. Utility classes `.h1` … `.h6` apply a heading's *style* to any element, useful when the semantic level and visual size differ. Never pick heading levels for looks — keep the outline semantic (one h2 per section, h3 under h2, no skips) and restyle with classes.

**Heading Classes**

```html
<p class="h1">This is a paragraph with class ".h1"</p>
<p class="h2">This is a paragraph with class ".h2"</p>
<p class="h3">This is a paragraph with class ".h3"</p>
<p class="h4">This is a paragraph with class ".h4"</p>
<p class="h5">This is a paragraph with class ".h5"</p>
<p class="h6">This is a paragraph with class ".h6"</p>
```

**Heading With Styled Link**

```html
<h2 class="heading--linked"><a href="#">Heading with a styled link</a></h2>
```


### Page Title

The `h1.page-title` is rendered by the theme from the Conductor page title — don't add another h1 in content. Size auto-adjusts via `data-length`; size modifiers exist (`.page-title--sm` etc.) for special cases.

**Default**

```html
<h1 class="page-title">Page Title</h1>
```


### Lists

Standard `ul`/`ol` are styled. Modifiers: `.no-bullets`, `.list--inline`, `.list--stepped` (numbered process steps; add `.grid .grid-md-3` for columns), description lists are plain `dl` (add `.grid .grid-md-2` etc. for columns). **Caution:** `dl.list--grid` is a compact two-column term/definition layout with zero row gap — it packs entries tightly by design. Don't use it for feature/benefit blocks that need breathing room; use a `.grid .grid-md-2` (or `-3`) of `div`s with `h3` + `p` (default 2rem gap), or `.card--border` cards, instead.

**Unordered List**

```html
<ul>
          <li>First list item with some longer text to demonstrate wrapping</li>
          <li>Second list item</li>
          <li>Third list item</li>
          <li>Fourth list item with <a href="#">a link</a> embedded in it</li>
        </ul>
```

**Stepped List**

```html
<ol class="ol--stepped">
          <li><strong>Step 1</strong><p>Quisque ante adipiscing vestibulum.</p></li>
          <li><strong>Step 2</strong><p>Quisque ante adipiscing vestibulum.</p></li>
          <li><strong>Step 3</strong><p>Quisque ante adipiscing vestibulum.</p></li>
          <li><strong>Step 4</strong><p>Quisque ante adipiscing vestibulum.</p></li>
        </ol>
```

**Stepped List (Grid)**

```html
<ol class="ol--stepped grid grid-md-3">
          <li><strong>Step 1</strong><p>Quisque ante adipiscing vestibulum.</p></li>
          <li><strong>Step 2</strong><p>Quisque ante adipiscing vestibulum.</p></li>
          <li><strong>Step 3</strong><p>Quisque ante adipiscing vestibulum.</p></li>
        </ol>
```

**Inline List**

```html
<ul class="list--inline">
          <li>Item 1</li>
          <li>Item 2</li>
          <li>Item 3</li>
          <li>Item 4</li>
        </ul>
```

**Description List**

```html
<dl>
          <dt>HTML</dt>
          <dd>HyperText Markup Language is the standard markup language for …</dd>
          <dt>CSS</dt>
          <dd>Cascading Style Sheets is a style sheet language used for describing …</dd>
          <dt>JavaScript</dt>
          <dd>A programming language that enables interactive web pages and is an essential part of web applications.</dd>
          <dt>Accessibility</dt>
          <dd>The practice of making websites usable by people with all abilities and disabilities.</dd>
        </dl>
```

**Description List (Grid)**

```html
<dl class="list--grid">
          <dt>HTML</dt>
          <dd>HyperText Markup Language is the standard markup language for …</dd>
          <dt>CSS</dt>
          <dd>Cascading Style Sheets is a style sheet language used for describing …</dd>
          <dt>JavaScript</dt>
          <dd>A programming language that enables interactive web pages and is an essential part of web applications.</dd>
          <dt>Accessibility</dt>
          <dd>The practice of making websites usable by people with all abilities and disabilities.</dd>
        </dl>
```


### Buttons

Link buttons: `a.btn`. Variants: `.btn--cta` (gold call-to-action), `.btn--more` (arrow reveal), combinations `.btn--cta.btn--more`. Sizes via `.btn--sm`/`.btn--lg`. Group related buttons with `.btn-group` or list many with `ul.list--buttons`. Icon buttons place an svg icon inside. Use a real `<button>` only for JS behaviors; navigation should be `<a>`.

**Single Button**

```html
<a href="#" type="button" class="btn">Button</a>
```

**Default Buttons**

```html
<div><a href="#" type="button" class="btn">Button</a>
  <a href="#" type="button" class="btn btn--secondary">Button</a>
  <a href="#" type="button" class="btn btn--tertiary">Button</a>
  <a href="#" type="button" class="btn btn--neutral">Button</a>
  <a href="#" type="button" class="btn noborder">Button</a>
  </div>
```

**CTA Buttons**

```html
<div><a href="#" type="button" class="btn btn--cta">Button</a>
  <a href="#" type="button" class="btn btn--cta btn--secondary">Button</a>
  <a href="#" type="button" class="btn btn--cta btn--tertiary">Button</a>
  <a href="#" type="button" class="btn btn--cta btn--neutral">Button</a>
  </div>
```

**More Buttons**

```html
<div><a href="#" type="button" class="btn btn--more">Button</a>
  <a href="#" type="button" class="btn btn--secondary btn--more">Button</a>
  <a href="#" type="button" class="btn btn--tertiary btn--more">Button</a>
  <a href="#" type="button" class="btn btn--neutral btn--more">Button</a>
  <a href="#" type="button" class="btn noborder btn--more">Button</a>
  </div>
```

**Default**

```html
<ul class="no-bullets btn-group">
      <li><a class="btn" href="#">Button 1</a></li>
      <li><a class="btn" href="#">Button 2</a></li>
      <li><a class="btn" href="#">Button 3</a></li>
      <li><a class="btn" href="#">Button 4</a></li>
    </ul>
```

**Default**

```html
<ul class="no-bullets btn-list ">
      <li><a class="btn" href="#">Button 1</a></li>
      <li><a class="btn" href="#">Button 2</a></li>
      <li><a class="btn" href="#">Button 3</a></li>
    </ul>
```

**Left**

```html
<a href="#" type="button" class="btn btn--icon btn--left"><svg class="icon" data-icon="plus" aria-hidden="true" focusable="false"><use href="#icon-plus"></use></svg></a>
```

**Default**

```html
<a href="#" type="button" class="btn btn--lede">Notre Dame attracts brilliant, energetic thinkers who are motivated to change the world.</a>
```


### Quotes

Three quote patterns: default `blockquote.quote` (large Garamond pull quote), inline quote with photo (`.quote--inline`, optional `.reversed`), stacked/centered (`.quote--stacked`, `.centered`). Attribution goes in `figcaption`/cite patterns as shown.

**Primary**

```html
<blockquote class="blockquote blockquote--md">
    <p>"As a premier Catholic research university, our research and learning …</p>
  <cite class="cite">- Rev. John I. Jenkins, C.S.C., President of the University of Notre Dame</cite></blockquote>
```

**Primary**

```html
<blockquote class="blockquote">
    <div class="flex-md align-start">
      <figure class="avatar avatar--sm avatar--quote mi-auto mbe-3"><img alt="" src="/images/profile-dowd.jpg" width="600" height="600"></figure>
      <p>"As a premier Catholic research university, our research and learning …</p>
    </div>
  <div class="byline">
  
    <div class="byline-body">
      <p class="byline-title person-name">Rev. Robert A. Dowd, C.S.C.</p>
      <p class="person-title">President of the University of Notre Dame</p>
    </div>
</div></blockquote>
```

**Centered**

```html
<blockquote class="blockquote blockquote--centered">
      <p>"As a premier Catholic research university, our research and learning …</p>
  <div class="byline">
  <figure class="avatar avatar--xs byline-image"><img alt="" src="/images/profile-dowd.jpg" width="600" height="600"></figure>
    <div class="byline-body">
      <p class="byline-title person-name">Rev. Robert A. Dowd, C.S.C.</p>
      <p class="person-title">President of the University of Notre Dame</p>
    </div>
</div></blockquote>
```


### Notice

Callout boxes — use these instead of hand-styled "callouts". `.notice` + color variants `.notice--primary`, `.notice--secondary`, `.notice--success`, `.notice--danger`, `.notice--warning`, `.notice--info`; optional leading icon. `role="alert"` only for genuinely urgent messages.

**Default with Icon**

```html
<div class="notice " role="alert">
      <svg class="icon" data-icon="flag" aria-hidden="true" focusable="false"><use href="#icon-flag"></use></svg>
      <div class="notice-content">This is <a href="#"><strong>an example link</strong></a>. Give it a click if you like.</div>
    </div>
```

**Primary**

```html
<div class="notice notice--primary" role="alert">
      <svg class="icon" data-icon="question" aria-hidden="true" focusable="false"><use href="#icon-question"></use></svg>
      <div class="notice-content">This is <a href="#"><strong>an example link</strong></a>. Give it a click if you like.</div>
    </div>
```

**Warning**

```html
<div class="notice notice--warning" role="alert">
      <svg class="icon" data-icon="prohibited" aria-hidden="true" focusable="false"><use href="#icon-prohibited"></use></svg>
      <div class="notice-content">This is <a href="#"><strong>an example link</strong></a>. Give it a click if you like.</div>
    </div>
```

**Info**

```html
<div class="notice notice--info" role="alert">
      <svg class="icon" data-icon="info" aria-hidden="true" focusable="false"><use href="#icon-info"></use></svg>
      <div class="notice-content">This is <a href="#"><strong>an example link</strong></a>. Give it a click if you like.</div>
    </div>
```


### Table

Tables get theme styling automatically; `.table--minimal` for a lighter look. Wrap wide tables in a scroll container if needed.

**Default**

```html
<table class="">
      <thead>
        <tr>
          <th>Header 1</th>
          <th>Header 2</th>
          <th>Header 3</th>
          <th>Header 4</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Row 1 column 1</td>
          <td>Row 1 column 2</td>
          <td>Row 1 column 3</td>
          <td>Row 1 column 4</td>
        </tr>
        <tr>
          <td>Alpha</td>
          <td>Beta</td>
          <td>Gamma</td>
          <td>Delta</td>
        </tr>
        <tr>
          <td>$19.95</td>
          <td><strong>A bolded item</strong></td>
          <td>Example table</td>
          <td><em>An ITALIC item</em></td>
        </tr>
      </tbody>
    </table>
```

**Minimal Table**

```html
<table class="table--minimal">
      <thead>
        <tr>
          <th>Header 1</th>
          <th>Header 2</th>
          <th>Header 3</th>
          <th>Header 4</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Row 1 column 1</td>
          <td>Row 1 column 2</td>
          <td>Row 1 column 3</td>
          <td>Row 1 column 4</td>
        </tr>
        <tr>
          <td>Alpha</td>
          <td>Beta</td>
          <td>Gamma</td>
          <td>Delta</td>
        </tr>
        <tr>
          <td>$19.95</td>
          <td><strong>A bolded item</strong></td>
          <td>Example table</td>
          <td><em>An ITALIC item</em></td>
        </tr>
      </tbody>
    </table>
```


### Footnote

Superscript references linking to a footnotes list.

**Default**

```html
<ol class="list--footnote"><li>University of Notre Dame, “About Notre Dame,” last modified July 15, 2024, <a href="https://www.nd.edu/about/">https://www.nd.edu/about/</a>.</li><li>Notre Dame Archives, “A Brief History of the University of Notre Dame,” updated March 11, 2023, <a href="https://archives.nd.edu/history.htm">https://archives.nd.edu/history.htm</a>.</li><li>Hesburgh Libraries, University of Notre Dame, “Services and Resources,” accessed February 18, 2026, <a href="https://library.nd.edu/services/">https://library.nd.edu/services/</a>.</li><li>Notre Dame Athletics, “Fighting Irish Football: History and Traditions,” updated August 20, 2025, <a href="https://fightingirish.com/history/">https://fightingirish.com/history/</a>.</li></ol>
```


### Byline

Author attribution row with optional avatar.

**Default**

```html
<div class="byline">
  <figure class="avatar avatar--xs byline-image"><img alt="" src="/images/profile-dowd.jpg" width="600" height="600"></figure>
    <div class="byline-body">
      <p class="byline-title person-name"><a class="byline-link" href="#">Rev. Robert A. Dowd, C.S.C.</a></p>
      <p class="person-title">President of the University of Notre Dame</p>
    </div>
</div>
```


### Media Mention

Press quote/mention formatting: `.media-mention` with publication, date, people.

**Default**

```html
<div class="card-container">
    <div class="card card--media-mention npr">
      <div class="card-body">
        
        <div class="publication-logo">
          <img class="publication-logo-img" alt="National Public Radio" src="https://conductor.nd.edu/images/publications/npr.png" width="180" height="60" loading="lazy">
          <p>National Public Radio</p>
        </div>
        <div class="card-content">
          <h2 class="card-title entry-title">
            <a class="card-link" href="https://example.com/notre-dame-energy-research" target="_blank" id="mention-123" rel="noopener">Notre Dame researchers find breakthrough in renewable energy storage</a>
          </h2>
          <div class="card-summary">
            <p class="entry-date">January 13, 2025</p>
            <p>Researchers at the University of Notre Dame have developed a new …</p>
          </div>
        </div>
      </div>
      
      <div class="card-meta">
        <h3 class="card-meta-title">Mentions</h3>
        <div class="byline-group">
          
        <div class="byline">
          <figure class="avatar avatar--xs byline-image"><img alt="" src="/images/profile-weninger.jpg" width="600" height="600"></figure>
          <div class="byline-body">
            <p class="byline-title">
              <a class="byline-link" href="#john-smith">John Smith</a>
            </p>
            <p class="person-title">College of Arts and Letters</p>
          </div>
        </div>
      
        <div class="byline">
          <figure class="avatar avatar--xs byline-image"><img alt="" src="/images/profile-dowd.jpg" width="600" height="600"></figure>
          <div class="byline-body">
            <p class="byline-title">
              <a class="byline-link" href="#jane-doe">John Doe</a>
            </p>
            <p class="person-title">Computer Science and Engineering</p>
          </div>
        </div>
      
        </div>
      </div>
    
    </div>
  </div>
```

**Default**

```html
<div class="card-container">
    <div class="card card--media-mention-quoted nyt">
      <div class="card-body">
        
        <div class="publication-logo">
          <img class="publication-logo-img" alt="New York Times" src="https://conductor.nd.edu/images/publications/the-new-york-times.png" width="180" height="60" loading="lazy">
          <p>New York Times</p>
        </div>
        <div class="card-content">
          <blockquote class="entry-quote">
            <p>“People are legitimately actually pissed off at the health care …</p>
          </blockquote>
          <div class="summary">
            
          </div>
        </div>
        
      <div class="byline-group">
        
        <div class="byline">
          <figure class="avatar avatar--xs byline-image"><img alt="" src="/images/profile-weninger.jpg" width="600" height="600"></figure>
          <div class="byline-body">
            <p class="byline-title">
              <a class="byline-link" href="#">Tim Weninger</a>
            </p>
            <p class="person-title">in New York Times</p>
          </div>
        </div>
      
      </div>
    
      </div>
      <div class="card-meta">
      <a class="card-btn" href="https://example.com/notre-dame-energy-research" target="_blank" id="mention-123" rel="noopener">Read Article</a>
    </div>
  </div></div>
```


### Icons & Stickers

Icons are SVG symbols inlined by the theme on every Conductor page — reference them with `<use>`; never paste raw SVG paths or emoji.

```html
<svg class="icon" data-icon="arrow-right" aria-hidden="true" focusable="false">
  <use href="#icon-arrow-right"></use>
</svg>
```

Sizes: `.icon--sm`, `.icon--md`, `.icon--lg`, `.icon--xl`.

Available icons (46): angle-left, angle-right, arrow-down, arrow-left, arrow-right, arrow-up, bluesky, box-arrow-up, calendar, calendar-add, check, clock, close, download, envelope, exclamation, external-link, facebook, feed, flag, google, history, home, info, instagram, linkedin, lock, map-pin, menu, minus, mode, newsletter, play, plus, prohibited, question, refresh, search, search-menu, snapchat, success, sync, twitter-x, user, vimeo, youtube

Stickers are larger decorative illustrations (line-art style), same usage with `sticker` classes and `#sticker-*` refs. Sizes `.sticker--sm/md/lg/xl`.

```html
<svg class="sticker sticker--lg" aria-hidden="true" focusable="false">
  <use href="#sticker-graduation-cap"></use>
</svg>
```

Available stickers (13): backpack, book, calculator, cap, chalk-board, computer, dna, earth, easel, globe, microscope, translate, trophy



---

## Cards, Images & Media — ND Web Theme v4

Copy-paste-ready markup extracted from the official NDT4 Storybook. Swap placeholder text, URLs and `/images/...` paths for real content (on a Conductor site, image paths look like `/assets/<id>/<w>x/<filename>`).

**Contents:** Card (Default), Card (Featured), Card (News Article), Card (Event), Card (People), Avatar, Image (Single), Image (Multiple), Gallery, Video, Stat

### Card (Default)

The workhorse component for linked content previews. Structure: `.card-container` > `.card` > `figure.card-image` + `.card-body` (with `.card-title` > `a.card-link`, and `.card-summary`). The whole card becomes clickable via the link inside `.card-title`. Modifiers on `.card`: `.horizontal` (image left at all sizes; add `.horizontal-md` etc. to go horizontal only at that breakpoint and up), `.stacked` (image above text), `.image-right`, `.image-small`, hover effects `.hover-bg` and `.hover-grow`, `.hover-more` on `.card-body` reveals a "more" arrow. Put cards in a `.grid .grid-md-3` (or similar) to lay them out in columns; each card sits in its own grid cell.

**Primary**

```html
<div class="card-container">
  <div class="card"><figure class="card-image"><img src="/images/placeholder-campus-1-600x400.jpg" width="600" height="400" alt=""></figure>
    <div class="card-body">
      <h2 class="card-title"><a class="card-link" href="#">Card Title</a></h2>
      <p class="card-summary">Hendrerit in quis venenatis aliquet venenatis scelerisque in ipsum …</p>
    </div>
  </div>
</div>
```

**External Link** — external links get `rel`/icon treatment automatically

```html
<div class="card-container">
  <div class="card"><figure class="card-image"><img src="/images/placeholder-campus-1-600x400.jpg" width="600" height="400" alt=""></figure>
    <div class="card-body">
      <h2 class="card-title"><a class="card-link" href="https://www.nd.edu/">Card Title</a></h2>
      <p class="card-summary">Hendrerit in quis venenatis aliquet venenatis scelerisque in ipsum …</p>
    </div>
  </div>
</div>
```

**No Image**

```html
<div class="card-container">
  <div class="card">
    <div class="card-body">
      <h2 class="card-title"><a class="card-link" href="#">Card Title</a></h2>
      <p class="card-summary">Hendrerit in quis venenatis aliquet venenatis scelerisque in ipsum …</p>
    </div>
  </div>
</div>
```

**Image Right**

```html
<div class="card-container">
  <div class="card card--image-right"><figure class="card-image"><img src="/images/placeholder-campus-1-600x400.jpg" width="600" height="400" alt=""></figure>
    <div class="card-body">
      <h2 class="card-title"><a class="card-link" href="#">Card Title</a></h2>
      <p class="card-summary">Hendrerit in quis venenatis aliquet venenatis scelerisque in ipsum …</p>
    </div>
  </div>
</div>
```

**Horizontal**

```html
<div class="card-container">
  <div class="card card--horizontal"><figure class="card-image"><img src="/images/placeholder-campus-1-600x400.jpg" width="600" height="400" alt=""></figure>
    <div class="card-body">
      <h2 class="card-title"><a class="card-link" href="#">Card Title</a></h2>
      <p class="card-summary">Hendrerit in quis venenatis aliquet venenatis scelerisque in ipsum …</p>
    </div>
  </div>
</div>
```

**Stacked**

```html
<div class="card-container">
  <div class="card card--stacked"><figure class="card-image"><img src="/images/placeholder-campus-1-600x400.jpg" width="600" height="400" alt=""></figure>
    <div class="card-body">
      <h2 class="card-title"><a class="card-link" href="#">Card Title</a></h2>
      <p class="card-summary">Hendrerit in quis venenatis aliquet venenatis scelerisque in ipsum …</p>
    </div>
  </div>
</div>
```

**Background Color** — use `.bg--*` classes on the card

```html
<div class="card-container">
  <div class="card bg--sky-blue-light"><figure class="card-image"><img src="/images/placeholder-campus-1-600x400.jpg" width="600" height="400" alt=""></figure>
    <div class="card-body">
      <h2 class="card-title"><a class="card-link" href="#">Card Title</a></h2>
      <p class="card-summary">Hendrerit in quis venenatis aliquet venenatis scelerisque in ipsum …</p>
    </div>
  </div>
</div>
```


### Card (Featured)

Large emphasis card for one highlighted item; `.card--featured` with optional `.vertical`.

**Default**

```html
<div class="card-container">
  <div class="card card--featured">
    <figure class="card-image"><img src="/images/placeholder-campus-1-600x400.jpg" width="600" height="400" alt=""></figure>
    <div class="card-body">
      <p class="card-label"><span>Card Label</span></p>
      <h2 class="card-title"><a class="card-link" href="#">Card Title</a></h2>
    </div>
  </div>
</div>
```

**Vertical Card**

```html
<div class="card-container">
  <div class="card card--featured">
    <figure class="card-image"><img src="/images/placeholder-people-1-800x1400.jpg" width="600" height="400" alt=""></figure>
    <div class="card-body">
      <p class="card-label"><span>Card Label</span></p>
      <h2 class="card-title"><a class="card-link" href="#">Card Title</a></h2>
    </div>
  </div>
</div>
```


### Card (News Article)

Used for news snippets; `article.card-container.article.snippet` wrapper with `.card--news` and `.article-meta` for the date. On Conductor sites these are usually generated by news listings, but the markup is useful for hand-built news-style layouts.

**Default**

```html
<article class="article snippet card-container" typeof="NewsArticle">
  <div class="card card--news ">
      <figure class="card-image"><img src="/images/placeholder-campus-1-600x400.jpg" width="600" height="400" alt=""></figure>
    
      <div class="card-body">
        <p class="card-label">Research</p>
        <h2 class="article-title card-title" property="headline">
          <a class="card-link" href="#">Notre Dame Research Discovers New Method to Address Climate Change</a>
        </h2>
        <div class="article-meta">
          <link property="publisher" resource="#siteorg">
          <div property="author" typeof="Person"><meta property="name" content="Jane Smith"></div>
          <p class="meta-item publish-info"><time property="datePublished" datetime="2025-04-01T00:00:00.000Z">April 1, 2025</time></p>
        </div>
        
      </div>
    </div>
  </article>
```

**With Excerpt**

```html
<article class="article snippet card-container" typeof="NewsArticle">
  <div class="card card--news ">
      <figure class="card-image"><img src="/images/placeholder-campus-1-600x400.jpg" width="600" height="400" alt=""></figure>
    
      <div class="card-body">
        <p class="card-label">Research</p>
        <h2 class="article-title card-title" property="headline">
          <a class="card-link" href="#">Notre Dame Research Discovers New Method to Address Climate Change</a>
        </h2>
        <div class="article-meta">
          <link property="publisher" resource="#siteorg">
          <div property="author" typeof="Person"><meta property="name" content="Jane Smith"></div>
          <p class="meta-item publish-info"><time property="datePublished" datetime="2025-04-01T00:00:00.000Z">April 1, 2025</time></p>
        </div>
        <div class="card-summary">The power of ND-LEEF lies in its ability to mimic real-world …</div>
      </div>
    </div>
  </article>
```


### Card (Event)

Event snippet with calendar date block. Usually generated by Conductor event listings; hand-write only for custom event-like layouts.

**Default**

```html
<article class="article card-container snippet event" typeof="Event">
  <div class="card card--event">
    <div aria-hidden="true" class="meta-item event-date">
      <span class="event-month">Apr</span>
      <span class="event-day">15</span>
    </div>
    
    <div class="card-body">
      <h2 class="article-title card-title" property="name"><a href="#" class="card-link">Faculty Workshop on Innovative Teaching Methods</a></h2>
      <meta property="description" content="Join us for an interactive workshop exploring innovative teaching methods and strategies for engaging students in the classroom. Faculty from all disciplines are welcome to attend.">
      <div class="article-meta">
        <p class="meta-item event-time" title="Tue, Apr 15, 10:00 AM - 12:00 PM">
          <time property="startDate" datetime="2025-04-15T10:00-05:00"><svg class="icon" data-icon="clock" aria-hidden="true" focusable="false"><use href="#icon-clock"></use></svg>
          <span class="date-string">Tue, Apr 15</span> at 10:00 AM</time>  - 
          <time property="endDate" datetime="2025-04-15T12:00-05:00">12:00 PM</time>
        </p>
        <p class="meta-item event-location" property="location" typeof="Place"><svg class="icon" data-icon="map-pin" aria-hidden="true" focusable="false"><use href="#icon-map-pin"></use></svg> <span property="name address">DeBartolo Hall, Room 101</span></p>
        <link property="image" href="/images/placeholder-campus-1-600x400.jpg">
        <link property="organizer" resource="#siteorg">
      </div>
    </div>
  </div>
</article>
```

**Compact**

```html
<article class="article card-container snippet event" typeof="Event">
  <div class="card card--event card--event-compact">
    <div aria-hidden="true" class="meta-item event-date">
      <span class="event-month">Apr</span>
      <span class="event-day">15</span>
    </div>
    
    <div class="card-body">
      <h2 class="article-title card-title" property="name"><a href="#" class="card-link">Faculty Workshop on Innovative Teaching Methods</a></h2>
      <meta property="description" content="Join us for an interactive workshop exploring innovative teaching methods and strategies for engaging students in the classroom. Faculty from all disciplines are welcome to attend.">
      <div class="article-meta">
        <p class="meta-item event-time" title="Tue, Apr 15, 10:00 AM - 12:00 PM">
          <time property="startDate" datetime="2025-04-15T10:00-05:00"><svg class="icon" data-icon="clock" aria-hidden="true" focusable="false"><use href="#icon-clock"></use></svg>
          <span class="date-string">Tue, Apr 15</span> at 10:00 AM</time>  - 
          <time property="endDate" datetime="2025-04-15T12:00-05:00">12:00 PM</time>
        </p>
        <p class="meta-item event-location" property="location" typeof="Place"><svg class="icon" data-icon="map-pin" aria-hidden="true" focusable="false"><use href="#icon-map-pin"></use></svg> <span property="name address">DeBartolo Hall, Room 101</span></p>
        <link property="image" href="/images/placeholder-campus-1-600x400.jpg">
        <link property="organizer" resource="#siteorg">
      </div>
    </div>
  </div>
</article>
```


### Card (People)

Directory-style cards for people; pair with `.grid` for a people grid.

**Primary**

```html
<div class="card-container">
    <div class="card card--person ">
      <figure class="avatar avatar--lg card-image"><img alt="" src="/images/profile-dowd.jpg" width="600" height="600"></figure>
      <div class="card-body">
        <h2 class="card-title"><a class="card-link" href="#">John Doe</a></h2>
        <p class="person-title">Person title</p>
        <p class="card-summary">Hendrerit in quis venenatis aliquet venenatis scelerisque in ipsum …</p>
        
      </div>
      
    </div>
    </div>
```

**Compact**

```html
<div class="card-container">
    <div class="card card--person card--compact">
      <figure class="avatar avatar--lg card-image"><img alt="" src="/images/profile-dowd.jpg" width="600" height="600"></figure>
      <div class="card-body">
        <h2 class="card-title"><a class="card-link" href="#">John Doe</a></h2>
        <p class="person-title">Person title</p>
        <p class="card-summary">Hendrerit in quis venenatis aliquet venenatis scelerisque in ipsum …</p>
        
      </div>
      
    </div>
    </div>
```

**Horizontal**

```html
<div class="card-container">
    <div class="card card--person card--horizontal">
      <figure class="avatar avatar--lg card-image"><img alt="" src="/images/profile-dowd.jpg" width="600" height="600"></figure>
      <div class="card-body">
        <h2 class="card-title"><a class="card-link" href="#">John Doe</a></h2>
        <p class="person-title">Person title</p>
        <p class="card-summary">Hendrerit in quis venenatis aliquet venenatis scelerisque in ipsum …</p>
        
      </div>
      
    </div>
    </div>
```


### Avatar

Circular person image; `figure.avatar`. Placeholder: `/images/placeholder-avatar.svg` equivalent on your site.

**With image**

```html
<figure class="avatar avatar--md "><img alt="" src="/images/profile-dowd.jpg" width="600" height="600"></figure>
```

**With caption**

```html
<figure class="avatar avatar--md "><img alt="" src="/images/profile-dowd.jpg" width="600" height="600"><figcaption>Rev. Robert A. Dowd, C.S.C. standing in front of a staircase in the …</figcaption></figure>
```


### Image (Single)

Figures with alignment modifiers: `.image-left`, `.image-right` (floats at medium+), `.image-circle`. Include `width`/`height` for layout stability; use `figcaption` for captions.

**Default**

```html
<figure class="image"><img src="/images/placeholder-campus-3-1200x675.jpg" width="1200" height="765" alt="Image"></figure>
```

**Right**

```html
<figure class="image image-right"><img src="/images/placeholder-campus-3-1200x675.jpg" width="1200" height="765" alt="Image"></figure>
```

**Circle**

```html
<figure class="image image-circle"><img src="/images/placeholder-campus-3-1200x675.jpg" width="1200" height="765" alt="Image"></figure>
```


### Image (Multiple)

Multi-image layouts: `.images-mosaic`, `.images-tiled`.

**Default**

```html
<figure class="image image--tiled">
    <img src="/images/placeholder-campus-1-1200x675.jpg" width="1200" height="675" alt="Image 1"><img src="/images/placeholder-campus-2-1200x675.jpg" width="1200" height="675" alt="Image 2"><img src="/images/placeholder-campus-3-1200x675.jpg" width="1200" height="675" alt="Image 3">
  </figure>
```

**Mosaic**

```html
<figure class="image image--mosaic">
    <img src="/images/placeholder-campus-1-1200x675.jpg" width="1200" height="675" alt="Image 1"><img src="/images/placeholder-campus-2-1200x675.jpg" width="1200" height="675" alt="Image 2"><img src="/images/placeholder-campus-3-1200x675.jpg" width="1200" height="675" alt="Image 3">
  </figure>
```

**Tiled**

```html
<figure class="image image--tiled">
    <img src="/images/placeholder-campus-1-1200x675.jpg" width="1200" height="675" alt="Image 1"><img src="/images/placeholder-campus-2-1200x675.jpg" width="1200" height="675" alt="Image 2"><img src="/images/placeholder-campus-3-1200x675.jpg" width="1200" height="675" alt="Image 3">
  </figure>
```


### Gallery

Image gallery with optional tiled or slider display. Requires theme JS (`ndt.js`) on the page, which Conductor sites load automatically.

**Default**

```html
<link rel="stylesheet" href="https://conductor.nd.edu/stylesheets/lb.css">

    <div class="gallery-wrapper">
      <ul id="gallery-15" class="gallery-lb gallery-15" data-count="15">
        
          <li>
            <a href="#" title="" data-title="Image 1">
              <img src="/images/placeholder-campus-1-600x600.jpg" alt="Gallery image 1" width="400" height="400" loading="lazy">
            </a>
          </li>
        
          <li>
            <a href="#" title="" data-title="Image 2">
              <img src="/images/placeholder-campus-1-600x600.jpg" alt="Gallery image 2" width="400" height="400" loading="lazy">
            </a>
          </li>
        
          <li>
            <a href="#" title="" data-title="Image 3">
              <img src="/images/placeholder-campus-1-600x600.jpg" alt="Gallery image 3" width="400" height="400" loading="lazy">
            </a>
          </li>
        
          <li>
            <a href="#" title="" data-title="Image 4">
              <img src="/images/placeholder-campus-1-600x600.jpg" alt="Gallery image 4" width="400" height="400" loading="lazy">
            </a>
          </li>
        
          <li>
            <a href="#" title="" data-title="Image 5">
              <img src="/images/placeholder-campus-1-600x600.jpg" alt="Gallery image 5" width="400" height="400" loading="lazy">
            </a>
          </li>
        
          <li>
            <a href="#" title="" data-title="Image 6">
              <img src="/images/placeholder-campus-1-600x600.jpg" alt="Gallery image 6" width="400" height="400" loading="lazy">
            </a>
          </li>
        
          <li>
            <a href="#" title="" data-title="Image 7">
              <img src="/images/placeholder-campus-1-600x600.jpg" alt="Gallery image 7" width="400" height="400" loading="lazy">
            </a>
          </li>
        
          <li>
            <a href="#" title="" data-title="Image 8">
              <img src="/images/placeholder-campus-1-600x600.jpg" alt="Gallery image 8" width="400" height="400" loading="lazy">
            </a>
          </li>
        
          <li>
            <a href="#" title="" data-title="Image 9">
              <img src="/images/placeholder-campus-1-600x600.jpg" alt="Gallery image 9" width="400" height="400" loading="lazy">
            </a>
          </li>
        
          <li>
            <a href="#" title="" data-title="Image 10">
              <img src="/images/placeholder-campus-1-600x600.jpg" alt="Gallery image 10" width="400" height="400" loading="lazy">
            </a>
          </li>
        
          <li>
            <a href="#" title="" data-title="Image 11">
              <img src="/images/placeholder-campus-1-600x600.jpg" alt="Gallery image 11" width="400" height="400" loading="lazy">
            </a>
          </li>
        
          <li>
            <a href="#" title="" data-title="Image 12">
              <img src="/images/placeholder-campus-1-600x600.jpg" alt="Gallery image 12" width="400" height="400" loading="lazy">
            </a>
          </li>
        
          <li>
            <a href="#" title="" data-title="Image 13">
              <img src="/images/placeholder-campus-1-600x600.jpg" alt="Gallery image 13" width="400" height="400" loading="lazy">
            </a>
          </li>
        
          <li>
            <a href="#" title="" data-title="Image 14">
              <img src="/images/placeholder-campus-1-600x600.jpg" alt="Gallery image 14" width="400" height="400" loading="lazy">
            </a>
          </li>
        
          <li>
            <a href="#" title="" data-title="Image 15">
              <img src="/images/placeholder-campus-1-600x600.jpg" alt="Gallery image 15" width="400" height="400" loading="lazy">
            </a>
          </li>
        
      </ul>
    </div>
    <script>
    document.addEventListener("DOMContentLoaded", function(){var …</script>
```

**Gallery Tiled**

```html
<link rel="stylesheet" href="https://conductor.nd.edu/stylesheets/lb.css">

    <div class="gallery-wrapper gallery--tiled">
      <ul id="gallery-15" class="gallery-lb gallery-15" data-count="15">
        
          <li>
            <a href="#" title="" data-title="Image 1">
              <img src="/images/placeholder-campus-1-600x600.jpg" alt="Gallery image 1" width="400" height="400" loading="lazy">
            </a>
          </li>
        
          <li>
            <a href="#" title="" data-title="Image 2">
              <img src="/images/placeholder-campus-1-600x600.jpg" alt="Gallery image 2" width="400" height="400" loading="lazy">
            </a>
          </li>
        
          <li>
            <a href="#" title="" data-title="Image 3">
              <img src="/images/placeholder-campus-1-600x600.jpg" alt="Gallery image 3" width="400" height="400" loading="lazy">
            </a>
          </li>
        
          <li>
            <a href="#" title="" data-title="Image 4">
              <img src="/images/placeholder-campus-1-600x600.jpg" alt="Gallery image 4" width="400" height="400" loading="lazy">
            </a>
          </li>
        
          <li>
            <a href="#" title="" data-title="Image 5">
              <img src="/images/placeholder-campus-1-600x600.jpg" alt="Gallery image 5" width="400" height="400" loading="lazy">
            </a>
          </li>
        
          <li>
            <a href="#" title="" data-title="Image 6">
              <img src="/images/placeholder-campus-1-600x600.jpg" alt="Gallery image 6" width="400" height="400" loading="lazy">
            </a>
          </li>
        
          <li>
            <a href="#" title="" data-title="Image 7">
              <img src="/images/placeholder-campus-1-600x600.jpg" alt="Gallery image 7" width="400" height="400" loading="lazy">
            </a>
          </li>
        
          <li>
            <a href="#" title="" data-title="Image 8">
              <img src="/images/placeholder-campus-1-600x600.jpg" alt="Gallery image 8" width="400" height="400" loading="lazy">
            </a>
          </li>
        
          <li>
            <a href="#" title="" data-title="Image 9">
              <img src="/images/placeholder-campus-1-600x600.jpg" alt="Gallery image 9" width="400" height="400" loading="lazy">
            </a>
          </li>
        
          <li>
            <a href="#" title="" data-title="Image 10">
              <img src="/images/placeholder-campus-1-600x600.jpg" alt="Gallery image 10" width="400" height="400" loading="lazy">
            </a>
          </li>
        
          <li>
            <a href="#" title="" data-title="Image 11">
              <img src="/images/placeholder-campus-1-600x600.jpg" alt="Gallery image 11" width="400" height="400" loading="lazy">
            </a>
          </li>
        
          <li>
            <a href="#" title="" data-title="Image 12">
              <img src="/images/placeholder-campus-1-600x600.jpg" alt="Gallery image 12" width="400" height="400" loading="lazy">
            </a>
          </li>
        
          <li>
            <a href="#" title="" data-title="Image 13">
              <img src="/images/placeholder-campus-1-600x600.jpg" alt="Gallery image 13" width="400" height="400" loading="lazy">
            </a>
          </li>
        
          <li>
            <a href="#" title="" data-title="Image 14">
              <img src="/images/placeholder-campus-1-600x600.jpg" alt="Gallery image 14" width="400" height="400" loading="lazy">
            </a>
          </li>
        
          <li>
            <a href="#" title="" data-title="Image 15">
              <img src="/images/placeholder-campus-1-600x600.jpg" alt="Gallery image 15" width="400" height="400" loading="lazy">
            </a>
          </li>
        
      </ul>
    </div>
    <script>
    document.addEventListener("DOMContentLoaded", function(){var …</script>
```

**Gallery Slider**

```html
<link rel="stylesheet" href="https://conductor.nd.edu/stylesheets/lb.css">

    <div class="gallery-wrapper gallery--slider">
      <ul id="gallery-21" class="gallery-lb gallery-21" data-count="21">
        
          <li>
            <a href="#" title="" data-title="Image 1">
              <img src="/images/placeholder-campus-1-600x600.jpg" alt="Gallery image 1" width="400" height="400" loading="lazy">
            </a>
          </li>
        
          <li>
            <a href="#" title="" data-title="Image 2">
              <img src="/images/placeholder-campus-1-600x600.jpg" alt="Gallery image 2" width="400" height="400" loading="lazy">
            </a>
          </li>
        
          <li>
            <a href="#" title="" data-title="Image 3">
              <img src="/images/placeholder-campus-1-600x600.jpg" alt="Gallery image 3" width="400" height="400" loading="lazy">
            </a>
          </li>
        
          <li>
            <a href="#" title="" data-title="Image 4">
              <img src="/images/placeholder-campus-1-600x600.jpg" alt="Gallery image 4" width="400" height="400" loading="lazy">
            </a>
          </li>
        
          <li>
            <a href="#" title="" data-title="Image 5">
              <img src="/images/placeholder-campus-1-600x600.jpg" alt="Gallery image 5" width="400" height="400" loading="lazy">
            </a>
          </li>
        
          <li>
            <a href="#" title="" data-title="Image 6">
              <img src="/images/placeholder-campus-1-600x600.jpg" alt="Gallery image 6" width="400" height="400" loading="lazy">
            </a>
          </li>
        
          <li>
            <a href="#" title="" data-title="Image 7">
              <img src="/images/placeholder-campus-1-600x600.jpg" alt="Gallery image 7" width="400" height="400" loading="lazy">
            </a>
          </li>
        
          <li>
            <a href="#" title="" data-title="Image 8">
              <img src="/images/placeholder-campus-1-600x600.jpg" alt="Gallery image 8" width="400" height="400" loading="lazy">
            </a>
          </li>
        
          <li>
            <a href="#" title="" data-title="Image 9">
              <img src="/images/placeholder-campus-1-600x600.jpg" alt="Gallery image 9" width="400" height="400" loading="lazy">
            </a>
          </li>
        
          <li>
            <a href="#" title="" data-title="Image 10">
              <img src="/images/placeholder-campus-1-600x600.jpg" alt="Gallery image 10" width="400" height="400" loading="lazy">
            </a>
          </li>
        
          <li>
            <a href="#" title="" data-title="Image 11">
              <img src="/images/placeholder-campus-1-600x600.jpg" alt="Gallery image 11" width="400" height="400" loading="lazy">
            </a>
          </li>
        
          <li>
            <a href="#" title="" data-title="Image 12">
              <img src="/images/placeholder-campus-1-600x600.jpg" alt="Gallery image 12" width="400" height="400" loading="lazy">
            </a>
          </li>
        
          <li>
            <a href="#" title="" data-title="Image 13">
              <img src="/images/placeholder-campus-1-600x600.jpg" alt="Gallery image 13" width="400" height="400" loading="lazy">
            </a>
          </li>
        
          <li>
            <a href="#" title="" data-title="Image 14">
              <img src="/images/placeholder-campus-1-600x600.jpg" alt="Gallery image 14" width="400" height="400" loading="lazy">
            </a>
          </li>
        
          <li>
            <a href="#" title="" data-title="Image 15">
              <img src="/images/placeholder-campus-1-600x600.jpg" alt="Gallery image 15" width="400" height="400" loading="lazy">
            </a>
          </li>
        
          <li>
            <a href="#" title="" data-title="Image 16">
              <img src="/images/placeholder-campus-1-600x600.jpg" alt="Gallery image 16" width="400" height="400" loading="lazy">
            </a>
          </li>
        
          <li>
            <a href="#" title="" data-title="Image 17">
              <img src="/images/placeholder-campus-1-600x600.jpg" alt="Gallery image 17" width="400" height="400" loading="lazy">
            </a>
          </li>
        
          <li>
            <a href="#" title="" data-title="Image 18">
              <img src="/images/placeholder-campus-1-600x600.jpg" alt="Gallery image 18" width="400" height="400" loading="lazy">
            </a>
          </li>
        
          <li>
            <a href="#" title="" data-title="Image 19">
              <img src="/images/placeholder-campus-1-600x600.jpg" alt="Gallery image 19" width="400" height="400" loading="lazy">
            </a>
          </li>
        
          <li>
            <a href="#" title="" data-title="Image 20">
              <img src="/images/placeholder-campus-1-600x600.jpg" alt="Gallery image 20" width="400" height="400" loading="lazy">
            </a>
          </li>
        
          <li>
            <a href="#" title="" data-title="Image 21">
              <img src="/images/placeholder-campus-1-600x600.jpg" alt="Gallery image 21" width="400" height="400" loading="lazy">
            </a>
          </li>
        
      </ul>
    </div>
```


### Video

Embeds and video placeholders. `.video-wrapper` keeps 16:9. Placeholder patterns show a play button over a poster image and open the video (needs theme JS).

**Embed**

```html
<div class="video--wrapper">
  <iframe width="1280" height="720" style="aspect-ratio: 16/9;" src="https://www.youtube.com/embed/p_vC10eq474" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="allowfullscreen"></iframe>
</div>
```

**Placeholder**

```html
<div class="video--wrapper">
  <a class="video video--default" href="https://www.youtube.com/watch?v=p_vC10eq474">
    <figure><img title="A YouTube Video" src="http://img.youtube.com/vi/p_vC10eq474/maxresdefault.jpg" width="1280" height="720" alt="A YouTube Video"></figure>
    
  </a>
</div>
```


### Stat

Big numbers with labels. `ul.no-bullets.list--stats` + `.stat-item` with `.stat-value`/`.stat-label`. Center with `.stat-item--center`; stickers can decorate stats (`.stat-sticker`). Sizes via `.list--sm`/`.list--lg` on the list.

**Default**

```html
<ul class="no-bullets list--stats grid grid-sm-3">
  <li class="stat-item">
    
    <span class="stat-value">500+</span>
    <span class="stat-label">Student Clubs and Groups</span>
  </li>
  <li class="stat-item">
    
    <span class="stat-value">28</span>
    <span class="stat-label">Campus Eateries</span>
  </li>
  <li class="stat-item">
    
    <span class="stat-value">10%</span>
    <span class="stat-label">Acceptance Rate</span>
  </li>
</ul>
```

**Centered**

```html
<ul class="no-bullets list--stats grid grid-sm-3">
  <li class="stat-item stat-item--center">
    
    <span class="stat-value">500+</span>
    <span class="stat-label">Student Clubs and Groups</span>
  </li>
  <li class="stat-item stat-item--center">
    
    <span class="stat-value">28</span>
    <span class="stat-label">Campus Eateries</span>
  </li>
  <li class="stat-item stat-item--center">
    
    <span class="stat-value">10%</span>
    <span class="stat-label">Acceptance Rate</span>
  </li>
</ul>
```

**With Stickers** — decorative `#sticker-*` symbols

```html
<ul class="no-bullets list--stats grid grid-sm-3">
  <li class="stat-item">
    <svg class="sticker stat-sticker sticker--md" aria-hidden="true" role="presentation" focusable="false">
      <use href="#sticker-cap"></use>
    </svg>
    <span class="stat-value">96%</span>
    <span class="stat-label">graduation rate (top 5 among research universities)</span>
  </li>
  <li class="stat-item">
    <svg class="sticker stat-sticker sticker--md" aria-hidden="true" role="presentation" focusable="false">
      <use href="#sticker-backpack"></use>
    </svg>
    <span class="stat-value">TOP</span>
    <span class="stat-label">producer of Fullbright Program students for 10 consecutive years</span>
  </li>
  <li class="stat-item">
    <svg class="sticker stat-sticker sticker--md" aria-hidden="true" role="presentation" focusable="false">
      <use href="#sticker-globe"></use>
    </svg>
    <span class="stat-value">9:1</span>
    <span class="stat-label">countries where grads conduct on-site research</span>
  </li>
</ul>
```



---

## Interactive Components — ND Web Theme v4

Accordions, FAQs, tabs, dialogs, timelines and other behavior-backed patterns. Theme CSS/JS on Conductor pages powers these — no custom JS needed.

**Contents:** Accordion, FAQ,  Editor-safe hand-built FAQ (accordion + anchor ToC), Tabs, Dialog, Timeline, Pagination, Social Share, Navigation (Anchor)

### Accordion

Native `<details>`/`<summary>` — works without JS. `.accordion-list` wrapper, `.accordion` on each `details`. Variants: `.accordion--highlight`, `.accordion--bg`, sizes `.accordion--sm`/`.accordion--lg`.

**Default Accordion**

```html
<div class="accordion-list">
  <details class="accordion">
    <summary>Summary One</summary>
    <p>Litora volutpat a ad fermentum scelerisque parturient egestas …</p>
  </details>
  <details class="accordion">
    <summary>Summary Two</summary>
    <p>Litora volutpat a ad fermentum scelerisque parturient egestas …</p>
  </details>
  <details class="accordion">
    <summary>Summary Three</summary>
    <p>Litora volutpat a ad fermentum scelerisque parturient egestas …</p>
  </details>
</div>
```

**Highlighted Accordion**

```html
<div class="accordion-list">
  <details class="accordion accordion--highlight">
    <summary>Summary One</summary>
    <p>Litora volutpat a ad fermentum scelerisque parturient egestas …</p>
  </details>
  <details class="accordion accordion--highlight">
    <summary>Summary Two</summary>
    <p>Litora volutpat a ad fermentum scelerisque parturient egestas …</p>
  </details>
  <details class="accordion accordion--highlight">
    <summary>Summary Three</summary>
    <p>Litora volutpat a ad fermentum scelerisque parturient egestas …</p>
  </details>
</div>
```


### FAQ

The theme's numbered FAQ treatment — gold-circled question numbers, anchors table of contents, back-to-top links, schema.org markup — is produced by **Conductor's FAQ module** (structured FAQ entries + a Smart Tag), which renders `ol.faq-anchors` + `dl.faq` with `div.faq-item` wrappers server-side.

**Do not hand-paste that module markup into the page editor.** Conductor's editor enforces the strict `dl` content model on save and strips the `div.faq-item` wrappers, which silently kills the styling (the CSS selectors `.faq-anchors + .faq` and `.faq-item .faq-q` stop matching, leaving plain text). This was confirmed on a live site. The module markup is shown below only so you can recognize it and preview module-driven pages.

For a real FAQ page, the path is:

1. **Conductor FAQ module (preferred):** requires setup by the ND Creative team — direct the site owner to work with them (webhelp@nd.edu) to enable it. The module manages entries, generates anchors and back-to-top automatically, and can't be mangled by the editor.
2. **Hand-built, editor-safe fallback:** use the theme accordion — `.accordion-list` of `details.accordion` (standard elements the editor preserves). For 4+ questions, precede it with a linked ToC (`ol` of anchor links to `id`s on each `details`) so long pages stay navigable. This won't have the gold numbered circles (those belong to the module), but it is fully on-theme and survives the editor.

What the FAQ module outputs (for recognition/preview only — do not paste):

**FAQ module output — anchors ToC, numbered items, back-to-top**

```html
<div>
    <ol class="faq-anchors" id="faq-faqs-example">
      <li><a href="#faq_001">What is the history behind the Golden Dome?</a></li>
      <li><a href="#faq_002">How competitive is admission to Notre Dame?</a></li>
      <li><a href="#faq_003">What are Notre Dame's most popular majors?</a></li>
      <li><a href="#faq_004">What is the significance of "Fighting Irish" and how did it become Notre Dame's nickname?</a></li>
      <li><a href="#faq_005">What are the residential traditions at Notre Dame?</a></li>
    </ol>
    <dl class="faq">
      <div id="faq_001" class="faq-item" property="mainEntity" typeof="Question">
        <dt class="faq-q" property="name">What is the history behind the Golden Dome?</dt>
        <dd class="faq-a" property="acceptedAnswer" typeof="Answer">
          <div class="faq-a-text" property="text"><p>The Golden Dome is the main building at Notre Dame and one of the …</p></div>
          <p class="link-top"><a href="#faq-faqs-example">Back to top</a></p>
        </dd>
      </div><div id="faq_002" class="faq-item" property="mainEntity" typeof="Question">
        <dt class="faq-q" property="name">How competitive is admission to Notre Dame?</dt>
        <dd class="faq-a" property="acceptedAnswer" typeof="Answer">
          <div class="faq-a-text" property="text"><p>Notre Dame is highly selective, with an acceptance rate typically …</p></div>
          <p class="link-top"><a href="#faq-faqs-example">Back to top</a></p>
        </dd>
      </div><div id="faq_003" class="faq-item" property="mainEntity" typeof="Question">
        <dt class="faq-q" property="name">What are Notre Dame's most popular majors?</dt>
        <dd class="faq-a" property="acceptedAnswer" typeof="Answer">
          <div class="faq-a-text" property="text"><p>Some of Notre Dame's most popular undergraduate majors include …</p></div>
          <p class="link-top"><a href="#faq-faqs-example">Back to top</a></p>
        </dd>
      </div><div id="faq_004" class="faq-item" property="mainEntity" typeof="Question">
        <dt class="faq-q" property="name">What is the significance of "Fighting Irish" and how did it become Notre Dame's nickname?</dt>
        <dd class="faq-a" property="acceptedAnswer" typeof="Answer">
          <div class="faq-a-text" property="text"><p>While the exact origin of the "Fighting Irish" nickname is debated, …</p></div>
          <p class="link-top"><a href="#faq-faqs-example">Back to top</a></p>
        </dd>
      </div><div id="faq_005" class="faq-item" property="mainEntity" typeof="Question">
        <dt class="faq-q" property="name">What are the residential traditions at Notre Dame?</dt>
        <dd class="faq-a" property="acceptedAnswer" typeof="Answer">
          <div class="faq-a-text" property="text"><p>Notre Dame has a unique residential life system with approximately …</p></div>
          <p class="link-top"><a href="#faq-faqs-example">Back to top</a></p>
        </dd>
      </div>
    </dl>
  </div>
```


#### Editor-safe hand-built FAQ (accordion + anchor ToC)

```html
<h2 id="faq-top">Frequently Asked Questions</h2>
<ol>
  <li><a href="#q-allowed">Is AI use allowed in my course?</a></li>
  <li><a href="#q-cite">Do I need to cite AI output?</a></li>
</ol>
<!-- For the full numbered FAQ treatment, ask the ND Creative team (webhelp@nd.edu)
     to enable the Conductor FAQ module. Do not hand-paste module markup. -->
<div class="accordion-list">
  <details class="accordion" id="q-allowed">
    <summary>Is AI use allowed in my course?</summary>
    <p>It depends on your instructor's policy…</p>
    <p class="link-top"><a href="#faq-top">Back to top</a></p>
  </details>
  <details class="accordion" id="q-cite">
    <summary>Do I need to cite AI output?</summary>
    <p>Yes…</p>
    <p class="link-top"><a href="#faq-top">Back to top</a></p>
  </details>
</div>
```


### Tabs

Tabbed panels (requires theme JS, present on Conductor pages).

**Default**

```html
<section class="tabs-wrapper"><div class="tabs-wrapper">
  <nav class="nav-tabs " aria-label="Tabs Navigation" role="tablist">
    <ul id="nav-tabs" role="tablist" aria-label="Tabs" aria-orientation="horizontal">
      <li role="presentation"><a href="#tab-0" class="tab active" aria-selected="true">Tab 1</a></li>
      <li role="presentation"><a href="#tab-1" class="tab" aria-selected="false">Tab 2</a></li>
      <li role="presentation"><a href="#tab-2" class="tab" aria-selected="false">Tab 3</a></li>
      <li role="presentation"><a href="#tab-3" class="tab" aria-selected="false">Tab 4</a></li>
    </ul>
  </nav>
  <div class="tab-panels" aria-labelledby="nav-tabs">
    <div class="tab-panel" id="tab-0" role="tabpanel" aria-labelledby="tab-0">
      <h2>Tab 1</h2>
      <p>Porta vestibulum ullamcorper ac hac a himenaeos dui nisl a …</p>
    </div>
    <div class="tab-panel" id="tab-1" role="tabpanel" aria-labelledby="tab-1" hidden="">
      <h2>Tab 2</h2>
      <p>Atque excepturi perspiciatis fugit natus quas. Minima totam ab enim …</p>
    </div>
    <div class="tab-panel" id="tab-2" role="tabpanel" aria-labelledby="tab-2" hidden="">
      <h2>Tab 3</h2>
      <p>Sunt aliquam molestiae facere non nulla et non eum omnis est rerum …</p>
    </div>
    <div class="tab-panel" id="tab-3" role="tabpanel" aria-labelledby="tab-3" hidden="">
      <h2>Tab 4</h2>
      <p>Et impedit ipsum quo. Tempora ex quas et qui consequatur incidunt …</p>
    </div>
  </div>
</div>
<script>
  document.addEventListener('DOMContentLoaded', function() {
    const tabSets = document.querySelectorAll('.nav-tabs');

    tabSets.forEach(wrapper => {
      const tabs = wrapper.querySelectorAll('.tab');
      const panels = wrapper.parentElement.querySelectorAll('.tab-panel');

      tabs.forEach((tab, index) => {
        tab.addEventListener('click', (e) => {
          e.preventDefault();
          tabs.forEach(t => t.classList.remove('active'));
          panels.forEach(p => p.hidden = true);

          tab.classList.add('active');
          …</script></section>
```


### Dialog

Native `<dialog>` modals opened by a button. Variants for notification/alert, image, video, person bio.

**Default**

```html
<div class="dialog-item">
      <button class="btn dialog-link">Open Dialog</button>
      <dialog class="dialog">
        <div class="dialog-header">
          <form method="dialog" class="dialog-close">
            <button type="submit" title="Close">×</button>
          </form>
          <p class="dialog-heading h4">Dialog Title</p>
        </div>
        <div class="dialog-content">
          
          <div><p>This is the default dialog content. Dialogs can contain any type of information that requires user attention.</p></div>
        </div>
        <div class="dialog-footer">This is a default dialog footer. Use this space for supporting text or action buttons</div>
      </dialog>
    </div>
```


### Timeline

Vertical timeline; alignment variants `.timeline--right`, `.timeline--center`; items may include images.

**Default Timeline**

```html
<ul class="timeline">
  <li class="timeline-item">
    <figure class="timeline-image"></figure>
    <div class="timeline-body">
      <p class="timeline-title">Timeline Item</p>
      <p class="timeline-date">November 2, 2023</p>
      <p>Litora volutpat a ad fermentum scelerisque parturient egestas …</p>
    </div>
  </li>
  <li class="timeline-item">
    <figure class="timeline-image"></figure>
    <div class="timeline-body">
      <p class="timeline-title">Timeline Item</p>
      <p class="timeline-date">November 2, 2023</p>
      <p>Litora volutpat a ad fermentum scelerisque parturient egestas …</p>
    </div>
  </li>
  <li class="timeline-item">
    <figure class="timeline-image"></figure>
    <div class="timeline-body">
      <p class="timeline-title">Timeline Item</p>
      <p class="timeline-date">November 2, 2023</p>
      <p>Litora volutpat a ad fermentum scelerisque parturient egestas …</p>
    </div>
  </li>
</ul>
```


### Pagination

Numbered pagination nav. Usually generated by Conductor listings.

**Default**

```html
<div role="navigation" aria-label="Pagination" class="pagination" separator=" "><span class="previous_page disabled" aria-label="Previous page">Previous</span> <span class="current">1</span> <a aria-label="Page 2" href="#">2</a> <a aria-label="Page 3" href="#">3</a> <a aria-label="Page 4" href="#">4</a> <a aria-label="Page 5" href="#">5</a> <span class="gap">…</span> <a aria-label="Page 38" href="#">38</a> <a class="next_page" aria-label="Next page" rel="next" href="#">Next</a></div>
```


### Social Share

Share links row (native share + networks).

**Social Networks Only**

```html
<div class="social-share">
    <ul class="no-bullets ">
      
      
      <li class="share-facebook share-custom">
        <a title="Share on Facebook" class="btn" href="https://www.facebook.com/dialog/share?app_id=135465433914446&amp;display=popup&amp;href=https%3A%2F%2Fnews.nd.edu%2Fnews%2Fthe-commencement-of-the-class-of-2024%2F&amp;title=The%20Commencement%20of%20the%20class%20of%202024" aria-label="Share on Facebook">
          <svg class="icon" data-icon="facebook">
            <use href="#icon-facebook"></use>
          </svg>
        </a>
      </li>
    
      
      <li class="share-linkedin share-custom">
        <a title="Share on LinkedIn" class="btn" href="https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fnews.nd.edu%2Fnews%2Fthe-commencement-of-the-class-of-2024%2F&amp;title=The%20Commencement%20of%20the%20class%20of%202024" aria-label="Share on LinkedIn">
          <svg class="icon" data-icon="linkedin">
            <use href="#icon-linkedin"></use>
          </svg>
        </a>
      </li>
    
      
      <li class="share-x-twitter share-custom">
        <a title="Share on X/Twitter" class="btn" href="https://twitter.com/intent/tweet?url=https%3A%2F%2Fnews.nd.edu%2Fnews%2Fthe-commencement-of-the-class-of-2024%2F&amp;text=The%20Commencement%20of%20the%20class%20of%202024" aria-label="Share on X/Twitter">
          <svg class="icon" data-icon="twitter-x">
            <use href="#icon-twitter-x"></use>
          </svg>
        </a>
      </li>
    
      
    </ul>
  </div>
```


### Navigation (Anchor)

On-page anchor nav ('On this page') for long pages.

**Default**

```html
<nav id="nav-anchor" class="nav-anchor" aria-label="Anchor">
  <ul>
    <li><a href="#">Academics</a></li>
    <li><a href="#">Admissions</a></li>
    <li><a href="#">Research</a></li>
    <li><a href="#">Global</a></li>
    <li><a href="#">Faith</a></li>
    <li><a href="#">Community</a></li>
    <li><a href="#">About</a></li>
  </ul>
</nav>
```



---

## Banners, Sections & Full-Width Layouts — ND Web Theme v4

How ND sites build homepage-style storytelling pages: stacked full-width sections with alternating imagery, colors, and CTAs.

**Contents:** Section basics, Banner variants, Banner Group, Page Headers

### Section basics

Full-width storytelling blocks live in `.page-secondary.full-width` (after the `.page-primary` content, or as the whole page body on full-width pages). Each block is a `section.section`. Add `.bg--full-bleed` plus a `.bg--*` color to stretch the background edge-to-edge; `.bg--dark` switches text to light-on-dark. `.block-center` centers a max-width column; combine with `.text-center`. A `.heading-action` row pairs a section title with a "view all" style link.

The snippets below include the `<div class="wrapper"><div class="page-secondary full-width">` shell so you can see where sections sit in the page. When pasting into Conductor, do NOT include `<div class="wrapper">` (the theme provides it). Author the `.page-secondary.full-width` div plus its `section.section` children in your content region when building a full-width, homepage-style page.

**Banner (Default) — image + content split**

```html
<div class="wrapper"><div class="page-secondary full-width"><section class="section align-center grid grid-md-2">
  <figure class="section-media"><img src="/images/placeholder-campus-1-1200x800.jpg" width="1200" height="800" alt=""></figure>
  <div class="section-content">
    <h2 class="section-title">Banner Title</h2>
    <p>Risus parturient ullamcorper luctus tempor nisl lacus nec sociis cras …</p>
  <p><a href="#" type="button" class="btn btn--more">Explore all programs</a></p></div>
</section></div></div>
```

**Banner with multiple CTAs**

```html
<div class="wrapper"><div class="page-secondary full-width"><section class="section align-center grid grid-md-2">
  <figure class="section-media"><img src="/images/placeholder-campus-1-1200x800.jpg" width="1200" height="800" alt=""></figure>
  <div class="section-content">
    <h2 class="section-title">Banner Title</h2>
    <p>Risus parturient ullamcorper luctus tempor nisl lacus nec sociis cras …</p>
  <ul class="list--unstyled list--inline"><li><a href="#" type="button" class="btn btn--cta btn--more">Button One</a></li><li><a href="#" type="button" class="btn">Button Two</a></li></ul></div>
</section></div></div>
```

**Banner with background color**

```html
<div class="wrapper"><div class="page-secondary full-width"><section class="section align-center grid grid-md-2 bg--brand-blue bg--full-bleed">
  <figure class="section-media"><img src="/images/placeholder-campus-1-1200x800.jpg" width="1200" height="800" alt=""></figure>
  <div class="section-content">
    <h2 class="section-title">Banner Title</h2>
    <p>Risus parturient ullamcorper luctus tempor nisl lacus nec sociis cras …</p>
  <p><a href="#" type="button" class="btn">Learn More</a></p></div>
</section></div></div>
```


### Banner variants

Other banner layouts. All follow the same `.page-secondary.full-width > section.section` shell.

**Banner (Stacked) — content over full-width media**

```html
<section class="wrapper"><div class="page-secondary full-width"><div class="section">
  <div class="section-intro text-left">
    <h2 class="section-title">Banner Title</h2>
    <p>Risus parturient ullamcorper luctus tempor nisl lacus nec sociis cras …</p>
  <p><a href="#" type="button" class="btn btn--more">Explore all programs</a></p></div>
  <img src="/images/placeholder-campus-3-1600x900.jpg" width="1600" height="900" alt="">

</div></div></section>
```

**Banner (Cards) — heading + card row**

```html
<div class="wrapper"><div class="page-secondary full-width"><section class="section">
  <div class="section-intro text-center">
    <h2 class="section-title">Banner Title</h2>
    <p>Risus parturient ullamcorper luctus tempor nisl lacus nec sociis cras …</p>
  </div>
<div class="flex-auto"><div class="card-container">
  <div class="card"><figure class="card-image"><img src="/images/placeholder-campus-1-600x400.jpg" width="600" height="400" alt=""></figure>
    <div class="card-body">
      <h2 class="card-title">Card Title 1</h2>
      <p class="card-summary">This is a summary of the card content. It provides a brief overview …</p>
    </div>
  </div>
</div><div class="card-container">
  <div class="card"><figure class="card-image"><img src="/images/placeholder-campus-1-600x400.jpg" width="600" height="400" alt=""></figure>
    <div class="card-body">
      <h2 class="card-title">Card Title 2</h2>
      <p class="card-summary">This is a summary of the card content. It provides a brief overview …</p>
    </div>
  </div>
</div><div class="card-container">
  <div class="card"><figure class="card-image"><img src="/images/placeholder-campus-1-600x400.jpg" width="600" height="400" alt=""></figure>
    <div class="card-body">
      <h2 class="card-title">Card Title 3</h2>
      <p class="card-summary">This is a summary of the card content. It provides a brief overview …</p>
    </div>
  </div>
</div></div></section></div></div>
```

**Banner (Accordion)**

```html
<div class="wrapper"><div class="page-secondary full-width"><section class="section">
  <div class="section-intro text-center col--sm">
    <h2 class="section-title">Banner Title</h2>
    <p>Risus parturient ullamcorper luctus tempor nisl lacus nec sociis cras …</p>
  </div>
  <div class="details-group grid grid-ml-2">
    <div class="order-ml-1 details-group--aside-list"><figure class="details-group--aside section-media"><img src="/images/placeholder-campus-1-1600x900.jpg" alt="Accordion Image 1" width="600" height="400"></figure><figure class="details-group--aside section-media"><img src="/images/placeholder-campus-2-1600x900.jpg" alt="Accordion Image 2" width="600" height="400"></figure><figure class="details-group--aside section-media"><img src="/images/placeholder-campus-3-1600x900.jpg" alt="Accordion Image 3" width="600" height="400"></figure></div>  
  <div class="accordion-list">
  <details class="accordion">
    <summary>Summary One</summary>
    <p>Litora volutpat a ad fermentum scelerisque parturient egestas …</p>
  </details>
  <details class="accordion">
    <summary>Summary Two</summary>
    <p>Litora volutpat a ad fermentum scelerisque parturient egestas …</p>
  </details>
  <details class="accordion">
    <summary>Summary Three</summary>
    <p>Litora volutpat a ad fermentum scelerisque parturient egestas …</p>
  </details>
</div></div>
</section></div></div>
```

**Banner (Tiled) — two images**

```html
<div class="wrapper"><div class="page-secondary full-width"><section class="section grid grid-md-2 align-center">
  <figure class="section-image image--tiled">
    <img src="/images/placeholder-campus-3-1200x675.jpg" width="1200" height="675" alt="Modern university campus with tall glass buildings surrounded by green lawns and trees under a clear sky, conveying a welcoming and vibrant academic atmosphere"><img src="/images/placeholder-campus-3-1200x675.jpg" width="1200" height="675" alt="Modern university campus with tall glass buildings surrounded by green lawns and trees under a clear sky, conveying a welcoming and vibrant academic atmosphere">
  </figure>
  <div class="section-content">
    <h2 class="section-title section-title--undefined">Banner Title</h2>
    <p>Quis platea neque nisi a parturient mi suspendisse fusce nisl …</p>
  </div>
</section></div></div>
```

**Banner (Mosaic)**

```html
<div class="wrapper"><div class="page-secondary full-width"><section class="section grid grid-md-2 align-center">
  <figure class="section-image image--mosaic">
    <img src="/images/placeholder-campus-3-1200x675.jpg" width="1200" height="675" alt="Modern university campus with tall glass buildings surrounded by green lawns and trees under a clear sky, conveying a welcoming and vibrant academic atmosphere"><img src="/images/placeholder-campus-3-1200x675.jpg" width="1200" height="675" alt="Modern university campus with tall glass buildings surrounded by green lawns and trees under a clear sky, conveying a welcoming and vibrant academic atmosphere">
  </figure>
  <div class="section-content">
    <h2 class="section-title section-title--undefined">Banner Title</h2>
    <p>Quis platea neque nisi a parturient mi suspendisse fusce nisl …</p>
  </div>
</section></div></div>
```

**Banner (Full) — full-bleed image with overlaid text**

```html
<div class="wrapper"><div class="page-secondary full-width"><section class="section section--screen grid grid-md-2 bg--dark">
  <figure class="section-media section-media--bg bg--gradient bg--brand-blue">
    <img src="/images/placeholder-campus-3-1600x900.jpg" alt="" width="1600" height="900">
  </figure>
  <div class="section-body">
    <h2 class="section-title">Banner Title</h2>
    <p>Quis platea neque nisi a parturient mi suspendisse fusce nisl …</p>
  <p><a href="#" type="button" class="btn btn--cta btn--more">Button One</a></p></div>
</section></div></div>
```


### Banner Group

Alternating sequence of banners; `.banner-group` handles zig-zag layout (`.alternate`) and shared backgrounds.

**Default**

```html
<div class="wrapper"><div class="page-secondary full-width"><div class="section section-group">
<section class="section align-center grid grid-md-2">
  <figure class="section-media"><img src="/images/placeholder-campus-1-1200x800.jpg" width="1200" height="800" alt=""></figure>
  <div class="section-content">
    <h2 class="section-title">Spotlight on Faculty Research</h2>
    <p>Discover the groundbreaking work being done by our faculty members across various disciplines.</p>
  </div>
</section><section class="section align-center grid grid-md-2">
  <figure class="section-media"><img src="/images/placeholder-campus-1-1200x800.jpg" width="1200" height="800" alt=""></figure>
  <div class="section-content">
    <h2 class="section-title">Spotlight on Faculty Research</h2>
    <p>Discover the groundbreaking work being done by our faculty members across various disciplines.</p>
  </div>
</section><section class="section align-center grid grid-md-2">
  <figure class="section-media"><img src="/images/placeholder-campus-1-1200x800.jpg" width="1200" height="800" alt=""></figure>
  <div class="section-content">
    <h2 class="section-title">Spotlight on Faculty Research</h2>
    <p>Discover the groundbreaking work being done by our faculty members across various disciplines.</p>
  </div>
</section>
</div></div></div>
```


### Page Headers

The page header (title + hero image area at the top) is normally controlled by Conductor page settings and the theme, *not* by content-region HTML. Variants seen across sites: default, container, fade, inset, mosaic, screen, tiled — they change how the featured image wraps the `h1.page-title`. If you need to know the markup (e.g., for a static mockup), here is the default:

```html
<section class="wrapper" id="wrapper"><header id="header" class="site-header">
  <a class="header-mark-mobile" href="https://www.nd.edu/" title="University of Notre Dame">
    <svg width="512" height="86" aria-hidden="true" alt="University of Notre Dame"><use href="#mobile-mark"></use></svg>
    <span class="visually-hidden">University of Notre Dame</span>
  </a>
  <div class="header-group">
    <div class="header-title">
      <svg class="header-mark" width="250" height="60" aria-hidden="true" alt="University of Notre Dame"><use href="#academic-mark"></use></svg>
      <div class="header-title-name">
        <h1 id="site-title" class="site-title "><a href="/" accesskey="1" title="Homepage shortcut key = 1">Department of Example</a></h1>
      </div>
    </div>
    <div class="header-nav">
      
      
  <div class="header-util">
    <div class="header-nav-toggle">
      <button class="btn--action global-menu-toggle" aria-label="Open global menu and search" aria-controls="global-menu" aria-haspopup="dialog">
        <svg class="icon-search-menu" alt="Toggle Global Menu"><use href="#icon-search-menu"></use></svg>
        <svg class="icon-search" alt="Toggle Search"><use href="#icon-search"></use></svg>
      </button>
    </div>
  </div>
    </div>
  </div>
</header><main id="content" class="site-content"><div class="page-header">
    <figure class="page-image"><img src="/images/placeholder-campus-3-1600x900.jpg" width="1600" height="900" alt=""></figure>
    <div class="page-title-wrapper">
      <h1 class="page-title page-title--sm">Do more than dream about the future. Fight for it.</h1>
    </div>
  </div><div class="page-sidebar">
  <nav class="nav-site nav-site--section" aria-label="Section">
    <div id="nav_sub">
      <ul class="nav-level-1 depth_1">
        <li class="first"><a href="#">Academics</a></li>
        <li><a href="#">Admissions</a></li>
        <li><a href="#">Research</a></li>
        <li><a href="#">Global</a></li>
        <li><a href="#">Faith</a></li>
        <li><a href="#">Community</a></li>
        <li class="last"><a href="#">About</a></li>
      </ul>
    </div>
  </nav>
  </div></main></section>
```



---

## Forms — ND Web Theme v4

Form markup patterns from the official NDT4 Storybook.

**Contents:** Form layouts, Individual controls

### Form layouts

Complete form patterns. Note: Conductor pages can't run custom server-side handlers — forms usually point at Qualtrics, Formstack, Google Forms, or a service endpoint; often it's better to *link out* to the form. Use these patterns when embedding a search/filter UI or building markup for an external handler.

**Basic Search Form**

```html
<div class="form-combinations"><h2 class="form-title">Search</h2><div class="form-field">
    <label for="input-x5m7v0dh">Search</label>
    <input class="field" id="input-x5m7v0dh" type="search" placeholder="Search Site Name">
    
  </div><button class="btn btn-primary mt-4" type="submit">Search</button></div>
```

**Contact Form**

```html
<div class="form-combinations"><h2 class="form-title">Contact Information</h2><div class="form-field">
    <label for="input-wzd403vm">First Name</label>
    <input class="field" id="input-wzd403vm" type="text" placeholder="Enter your first name">
    
  </div><div class="form-field">
    <label for="input-1qzus14m">Last Name</label>
    <input class="field" id="input-1qzus14m" type="text" placeholder="Enter your last name">
    
  </div><div class="form-field">
    <label for="input-ebecvis5">Email</label>
    <input class="field" id="input-ebecvis5" type="email" placeholder="email@nd.edu">
    
  </div><div class="form-field">
    <label for="input-iifnj2cy">Phone</label>
    <input class="field" id="input-iifnj2cy" type="text" placeholder="(574) 631-5000">
    
  </div><div class="form-field">
    <label for="select-erjmvwud">Department</label>
    <select class="field" name="select-erjmvwud" id="select-erjmvwud">
    <option value="admissions">Admissions</option>
      <option value="registrar">Registrar</option>
      <option value="financialaid">Financial Aid</option>
      <option value="studentaffairs">Student Affairs</option>
    </select>
    
  </div><div class="form-field">
    <label for="textarea-o1n9zozj">Message</label>
    <textarea id="textarea-o1n9zozj" rows="4" placeholder="Your message here..."></textarea>
      
  </div><div class="form-field">
    <label for="checkbox-bm9o3w22">Interests</label>
    <ul class="no-bullets field checkbox-list">
    <li><input id="checkbox-0" type="checkbox" name="checkbox-group"><label for="checkbox-0">Campus Tours</label></li>
      <li><input id="checkbox-1" type="checkbox" name="checkbox-group"><label for="checkbox-1">Information Sessions</label></li>
      <li><input id="checkbox-2" type="checkbox" name="checkbox-group"><label for="checkbox-2">Alumni Events</label></li>
    </ul>
    
  </div><div class="form-field">
    <label for="radio-kg8lgobe">Preferred Contact Method</label>
    <ul class="field no-bullets radio-list" id="radio-kg8lgobe">
      <li><input id="radio-0" type="radio" name="radio-group"><label for="radio-0">Email</label></li>
        <li><input id="radio-1" type="radio" name="radio-group"><label for="radio-1">Phone</label></li>
    </ul>
    
  </div><button class="btn btn-primary mt-4" type="submit">Send Message</button></div>
```


### Individual controls

**Default Input**

```html
<div class="form-field">
    
    <input class="field" id="input-1knyxhbz" type="text" placeholder="">
    
  </div>
```

**With Label**

```html
<div class="form-field">
    <label for="select-x4nnqc3x">Choose an option</label>
    <select class="field" name="select-x4nnqc3x" id="select-x4nnqc3x">
    <option value="option1">Option 1</option>
      <option value="option2">Option 2</option>
      <option value="option3">Option 3</option>
    </select>
    
  </div>
```

**Default Checkbox Group**

```html
<div class="form-field">
    
    <ul class="no-bullets field checkbox-list">
    <li><input id="checkbox-0" type="checkbox" name="checkbox-group"><label for="checkbox-0">Checkbox Input 1 (Default)</label></li>
      <li><input id="checkbox-1" type="checkbox" disabled="" name="checkbox-group"><label for="checkbox-1">Checkbox Input 2 (Disabled)</label></li>
      <li><input id="checkbox-2" type="checkbox" checked="" name="checkbox-group"><label for="checkbox-2">Checkbox Input 3 (Checked)</label></li>
    </ul>
    
  </div>
```

**Default Radio Group**

```html
<div class="form-field">
    
    <ul class="field no-bullets radio-list" id="radio-nuf2x8ym">
      <li><input id="radio-0" type="radio" name="radio-group"><label for="radio-0">Radio Input 1</label></li>
        <li><input id="radio-1" type="radio" checked="" name="radio-group"><label for="radio-1">Radio Input 2 (Selected)</label></li>
        <li><input id="radio-2" type="radio" disabled="" name="radio-group"><label for="radio-2">Radio Input 3 (Disabled)</label></li>
    </ul>
    
  </div>
```

**With Note**

```html
<div class="form-field">
    
    <textarea id="help-text-textarea" rows="3" placeholder="Enter text here..."></textarea>
    <p class="form-field-note">This is some help text.</p>  
  </div>
```

**With Label**

```html
<div class="form-field">
    <span class="label">Toggle Me</span>
    <label class="switch field">
      <input type="checkbox">
      <span class="slider"></span>
    </label>
    
  </div>
```



---

## Conductor — Notre Dame's CMS

Conductor is the university's proprietary CMS (conductor.nd.edu), powering 700+ campus sites. Site owners edit pages in a browser-based editor; the ND Web Theme v4 (NDT4) renders the chrome around their content.

### What editors work with

- **Pages** — title, layout/page settings (featured image, full-width, sidebar), and a WYSIWYG content editor with an HTML source view. Content authored with this skill is pasted into the source view.
- **News, Events, People, FAQs, Media Mentions** — structured content types with their own entry forms; Conductor generates themed listings and cards automatically. Prefer these over hand-building news/event/people markup: hand-built copies won't stay in sync.
- **Snippets** — reusable content fragments that can be included across pages. A component you'll reuse on several pages is a good snippet candidate.
- **Uploads** — images and documents. Uploaded images are served at paths like `/assets/<id>/<width>x/<filename>` (the `<width>x` segment requests a resized rendition — e.g. `/assets/607853/300x/logo.png`). Reference uploaded assets rather than hotlinking external images.
- **Site settings** — navigation, redirects, users/roles, password protection.

### Ground rules for generated content

- The WYSIWYG editor rewrites or strips some markup on save. Confirmed behavior: it enforces strict HTML content models — `div` wrappers inside `<dl>` are stripped (which breaks hand-pasted FAQ-module markup); scripts and unknown embeds are also off-limits. Ordinary `div`s, classes, and standard block elements survive. Keep nesting plain-vanilla, and after pasting, save and re-open the source view to verify Conductor kept your structure. If interactivity beyond the theme's components (accordion, tabs, dialog, gallery) is needed, that's a conversation with the Conductor team (webhelp@nd.edu), not something to sneak into content.
- Advanced styling, custom theme layouts, and special Conductor features — the FAQ module, and the other structured-content modules (News, Events, People, Media Mentions, Galleries) — require setup by the ND Creative team. Direct site owners to work with them (webhelp@nd.edu) rather than hand-building imitations of module output.
- `<style>` blocks: prefer the site stylesheet for anything reused; a page-scoped style block is acceptable for one-off features (see page-anatomy.md). If the editor strips a style block on save, move the CSS to the site stylesheet.
- Forms: Conductor pages have no server-side form handling. Link out to (or embed) Qualtrics/Google/Formstack forms.
- Don't paste content copied from Word/Google Docs without cleanup — it carries inline styles and spans that fight the theme. The same applies to AI-generated HTML that wasn't built against this skill: strip inline styles, replace invented classes with theme classes.
- Every image needs meaningful `alt` text (or `alt=""` when purely decorative) plus `width`/`height` attributes.

### Publishing workflow

Pages support drafts, revision history, publish/unpublish, and server-cache clearing. A safe iteration loop for a big page change: preview locally (this skill's preview), paste into a draft, review on the site, publish.

### Getting help

- User guide: https://conductor.nd.edu/user-guide/
- Theme reference (Storybook): https://webtheme.nd.edu/
- Conductor team: webhelp@nd.edu


---

## Preview page shell

To let the user preview a fragment before pasting it into Conductor, replace `{{CONTENT}}` below with the fragment (and the other `{{...}}` placeholders with the page/site titles), and have them save it as an `.html` file and open it in a browser. It loads the production theme stylesheet, so what they see is what Conductor will render. Remind them: paste only the fragment into Conductor — never this whole file.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{{TITLE}} — NDT4 Preview</title>
  <link rel="stylesheet" href="https://conductor.nd.edu/stylesheets/themes/ndt/4.0/ndt.css">
  <style>
    /* Preview-only banner so nobody mistakes this for a live page */
    .ndt-preview-note { background: #ae9142; color: #0c2340; font-size: 0.8rem; padding: 0.25rem 1rem; text-align: center; }
  </style>
</head>
<body id="preview" class="{{PAGE_CLASS}} nav-top--true" data-theme="light" vocab="https://schema.org/">
  <!-- Optional: for icon/sticker rendering in the preview, inline the SVG sprites from https://webtheme.nd.edu/icons-nd-base.svg and https://webtheme.nd.edu/stickers-nd-base.svg here (cross-origin <use> references do not work). Icons will render on the real Conductor site regardless. -->
  <div class="ndt-preview-note">Local preview — Notre Dame Web Theme v4. Paste the content fragment (not this whole file) into Conductor.</div>
  <div id="wrapper" class="wrapper">
    <header id="header" class="site-header">
      <div class="header-group header-group--inline-xl">
        <div class="header-title">
          <div class="header-title-name">
            <div id="site-title" class="site-title"><a href="#">{{SITE_TITLE}}</a></div>
          </div>
        </div>
      </div>
    </header>
    <main id="content" class="site-content">
      <div class="page-header">
        <div class="page-title-wrapper">
          <h1 class="page-title" data-length="{{TITLE_LENGTH}}">{{TITLE}}</h1>
        </div>
      </div>
      <div class="page-primary">
{{CONTENT}}
      </div>
    </main>
  </div>
  <script src="https://conductor.nd.edu/javascripts/themes/ndt/4.0/ndt.js"></script>
</body>
</html>

```
