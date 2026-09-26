# Cards, Images & Media — ND Web Theme v4

Copy-paste-ready markup extracted from the official NDT4 Storybook. Swap placeholder text, URLs and `/images/...` paths for real content (on a Conductor site, image paths look like `/assets/<id>/<w>x/<filename>`).

**Contents:** Card (Default), Card (Featured), Card (News Article), Card (Event), Card (People), Avatar, Image (Single), Image (Multiple), Gallery, Video, Stat

## Card (Default)

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


## Card (Featured)

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


## Card (News Article)

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


## Card (Event)

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


## Card (People)

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


## Avatar

Circular person image; `figure.avatar`. Placeholder: `/images/placeholder-avatar.svg` equivalent on your site.

**With image**

```html
<figure class="avatar avatar--md "><img alt="" src="/images/profile-dowd.jpg" width="600" height="600"></figure>
```

**With caption**

```html
<figure class="avatar avatar--md "><img alt="" src="/images/profile-dowd.jpg" width="600" height="600"><figcaption>Rev. Robert A. Dowd, C.S.C. standing in front of a staircase in the …</figcaption></figure>
```


## Image (Single)

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


## Image (Multiple)

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


## Gallery

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


## Video

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


## Stat

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

