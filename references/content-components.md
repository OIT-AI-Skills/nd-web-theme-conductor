# Text & Content Components — ND Web Theme v4

Everyday content formatting: headings, lists, buttons, quotes, notices, tables, icons. Markup extracted from the official NDT4 Storybook.

**Contents:** Headings, Page Title, Lists, Buttons, Quotes, Notice, Table, Footnote, Byline, Media Mention, Icons & Stickers

## Headings

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


## Page Title

The `h1.page-title` is rendered by the theme from the Conductor page title — don't add another h1 in content. Size auto-adjusts via `data-length`; size modifiers exist (`.page-title--sm` etc.) for special cases.

**Default**

```html
<h1 class="page-title">Page Title</h1>
```


## Lists

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


## Buttons

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


## Quotes

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


## Notice

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


## Table

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


## Footnote

Superscript references linking to a footnotes list.

**Default**

```html
<ol class="list--footnote"><li>University of Notre Dame, “About Notre Dame,” last modified July 15, 2024, <a href="https://www.nd.edu/about/">https://www.nd.edu/about/</a>.</li><li>Notre Dame Archives, “A Brief History of the University of Notre Dame,” updated March 11, 2023, <a href="https://archives.nd.edu/history.htm">https://archives.nd.edu/history.htm</a>.</li><li>Hesburgh Libraries, University of Notre Dame, “Services and Resources,” accessed February 18, 2026, <a href="https://library.nd.edu/services/">https://library.nd.edu/services/</a>.</li><li>Notre Dame Athletics, “Fighting Irish Football: History and Traditions,” updated August 20, 2025, <a href="https://fightingirish.com/history/">https://fightingirish.com/history/</a>.</li></ol>
```


## Byline

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


## Media Mention

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


## Icons & Stickers

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

