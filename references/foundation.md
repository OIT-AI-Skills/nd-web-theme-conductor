# Foundation — Colors, Typography, Grid, Utilities (ND Web Theme v4)

The theme's design tokens and layout system. Use these instead of hand-rolled values: every color, spacing step, and breakpoint you need already exists as a class or CSS variable.

**Contents:** Colors, Typography, Grid, Utility classes, Breakpoints, Animations, CSS layers

## Colors

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

## Typography

Fonts load automatically: Garamond Premier Pro (ornamental headings, page titles, blockquotes) and Galaxie Polaris (default headings and body copy). Font-stack variables: `--font-heading`, plus the default body stack. Never load your own fonts or specify font-family in content.

- Body copy shouldn't exceed ~70 characters per line (theme containers already handle this — another reason not to fight the layout).
- `.h1` … `.h6` classes restyle any element to that heading's look without changing semantics.

## Grid

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

## Utility classes

- Spacing: margin `m-0`…`m-5`, `m-auto`; padding `p-0`…`p-5`. Block-axis (`mb-`, `pb-`), inline-axis (`mi-`, `pi-`), and start/end variants (`mbs-`, `mbe-`, `pbs-`, `pbe-`, `mis-`, `mie-`, `pis-`, `pie-`). Steps: 1 = 0.5rem, 2 = 1rem, … `mi-gutter` uses the gutter width.
- Text: `.text-start`, `.text-center`, `.text-end`, `.text-pretty`, `.text-balance`.
- Visibility: `.hidden` (display:none), `.invisible`, `.visually-hidden` (screen-reader only), responsive `.visually-hidden-md/ml/lg/xl/xxl`.
- Display: `.d-inline`, `.d-block`, `.d-grid`, `.d-flex`, `.d-none`; `.position-sticky`, `.position-fixed`.
- Flex: `.flex-row`, `.flex-column`, `.flex-wrap`, `.flex-nowrap`, `.flex-grow-1`, `.flex-shrink-0`; alignment `.justify-center`, `.align-center`, `.align-self-end`, `.align-content-between`.
- Object fit: `.object-fit-cover`, `.object-fit-contain`, etc.
- Column-width containers: `.col--sm`, `.col--md`, `.col--lg`, `.col--xl`, `.col--c`, `.col--screen`.
- Misc: `.wrap-link` (force long links to wrap), `.block-center` (centered max-width column).

## Animations

Optional `animate.css` (`https://conductor.nd.edu/stylesheets/themes/ndt/4.0/animate.css`, included after the main stylesheet — many sites don't load it; check before relying on it). Usage: `.animate` plus `.animate--fade-in`, `.animate--fade-in-up`, `.animate--fade-in-left`, `.animate--fade-in-right`, `.animate--move-up/down/left/right`. Keep animations short (<500ms) and purposeful; the theme already respects `prefers-reduced-motion`.

## CSS layers

NDT4 organizes styles in CSS cascade layers and reserves an empty `site` layer for site-specific styles. Custom site CSS added via `@layer site { ... }` will layer correctly above the theme without specificity fights.
