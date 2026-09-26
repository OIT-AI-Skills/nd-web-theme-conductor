# Interactive Components — ND Web Theme v4

Accordions, FAQs, tabs, dialogs, timelines and other behavior-backed patterns. Theme CSS/JS on Conductor pages powers these — no custom JS needed.

**Contents:** Accordion, FAQ,  Editor-safe hand-built FAQ (accordion + anchor ToC), Tabs, Dialog, Timeline, Pagination, Social Share, Navigation (Anchor)

## Accordion

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


## FAQ

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


### Editor-safe hand-built FAQ (accordion + anchor ToC)

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


## Tabs

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


## Dialog

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


## Timeline

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


## Pagination

Numbered pagination nav. Usually generated by Conductor listings.

**Default**

```html
<div role="navigation" aria-label="Pagination" class="pagination" separator=" "><span class="previous_page disabled" aria-label="Previous page">Previous</span> <span class="current">1</span> <a aria-label="Page 2" href="#">2</a> <a aria-label="Page 3" href="#">3</a> <a aria-label="Page 4" href="#">4</a> <a aria-label="Page 5" href="#">5</a> <span class="gap">…</span> <a aria-label="Page 38" href="#">38</a> <a class="next_page" aria-label="Next page" rel="next" href="#">Next</a></div>
```


## Social Share

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


## Navigation (Anchor)

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

