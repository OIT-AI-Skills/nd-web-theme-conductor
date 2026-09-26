# Page Anatomy — what the theme renders vs. what you author

Understanding this split is the difference between content that "plugs in" and content that fights the theme.

## The full page skeleton (theme + Conductor render all of this)

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

## Content-region building blocks

Inside `.page-primary`, plain semantic HTML is already styled: `h2`–`h4`, `p`, `ul`/`ol`, `table`, `blockquote`, `figure`/`img`, `a`. Reach for components (cards, notices, accordions, …) only when the content calls for them.

For richer layouts within the content column:

- `.grid` + `.grid-md-2/3/…` for columns (see foundation.md).
- Components from the reference files (cards-and-media.md, content-components.md, interactive-components.md).

## Full-width pages

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

## Custom CSS, when the theme truly has no equivalent

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
