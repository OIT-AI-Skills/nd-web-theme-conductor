# Banners, Sections & Full-Width Layouts — ND Web Theme v4

How ND sites build homepage-style storytelling pages: stacked full-width sections with alternating imagery, colors, and CTAs.

**Contents:** Section basics, Banner variants, Banner Group, Page Headers

## Section basics

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


## Banner variants

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


## Banner Group

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


## Page Headers

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

