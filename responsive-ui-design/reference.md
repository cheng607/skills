# Responsive UI Reference

## Design Token Template

```css
:root {
  /* Spacing */
  --space-xs: 0.25rem;
  --space-sm: 0.5rem;
  --space-md: 1rem;
  --space-lg: 1.5rem;
  --space-xl: 2rem;
  --space-2xl: 3rem;

  /* Typography */
  --font-sans: system-ui, -apple-system, sans-serif;
  --text-sm: 0.875rem;
  --text-base: 1rem;
  --text-lg: 1.125rem;
  --text-xl: 1.25rem;
  --text-2xl: 1.5rem;
  --leading-normal: 1.5;
  --leading-tight: 1.25;

  /* Colors */
  --color-bg: #ffffff;
  --color-bg-muted: #f4f4f5;
  --color-text: #18181b;
  --color-text-muted: #71717a;
  --color-border: #e4e4e7;
  --color-accent: #2563eb;
  --color-accent-hover: #1d4ed8;

  /* Radius & shadow */
  --radius-sm: 0.375rem;
  --radius-md: 0.5rem;
  --shadow-sm: 0 1px 2px rgb(0 0 0 / 0.05);
}

@media (prefers-color-scheme: dark) {
  :root {
    --color-bg: #09090b;
    --color-bg-muted: #27272a;
    --color-text: #fafafa;
    --color-text-muted: #a1a1aa;
    --color-border: #3f3f46;
  }
}
```

## Common Layout Snippets

### Centered page with max width

```html
<main class="mx-auto w-full max-w-6xl px-4 py-8 md:px-6 md:py-12">
  ...
</main>
```

### Holy grail (header + sidebar + main + footer)

```html
<div class="grid min-h-dvh grid-rows-[auto_1fr_auto]">
  <header>...</header>
  <div class="grid lg:grid-cols-[240px_1fr]">
    <aside class="hidden lg:block">...</aside>
    <main>...</main>
  </div>
  <footer>...</footer>
</div>
```

### Responsive table → cards on mobile

```html
<!-- Desktop: table -->
<table class="hidden md:table w-full">...</table>

<!-- Mobile: stacked cards -->
<div class="md:hidden space-y-4">
  <article class="rounded-lg border p-4">...</article>
</div>
```

### Sticky header with safe area

```css
.header {
  position: sticky;
  top: 0;
  z-index: 50;
  padding-top: env(safe-area-inset-top);
}
```

## Tailwind Config Extension Example

```js
// tailwind.config.js excerpt
theme: {
  extend: {
    spacing: {
      '18': '4.5rem',
    },
    maxWidth: {
      'content': '72rem',
    },
    fontSize: {
      'display': ['3rem', { lineHeight: '1.1', fontWeight: '700' }],
    },
  },
},
screens: {
  'xs': '475px',
  // defaults: sm, md, lg, xl, 2xl
},
```

## Breakpoint Testing Checklist

| Viewport | Check |
|----------|-------|
| 320×568 | No overflow, readable text, tappable buttons |
| 375×667 | iPhone SE layout |
| 768×1024 | Tablet two-column where intended |
| 1024×768 | Sidebar visible, content not cramped |
| 1440×900 | Max-width container centered, no overly wide lines |

## Accessibility Quick Reference

| Element | Minimum requirement |
|---------|---------------------|
| Body text | 4.5:1 contrast |
| Large text (≥18px bold / 24px) | 3:1 contrast |
| Focus ring | 2px visible outline, 3:1 against adjacent colors |
| Touch target | 44px minimum dimension |
| Motion | Respect `prefers-reduced-motion: reduce` |

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

## Visual Hierarchy Checklist

Squint test — at a glance, can you identify:

1. **Primary action** (one per viewport section)
2. **Page title** vs section headings vs body
3. **Grouped related content** (spacing + borders/background)
4. **Secondary/destructive actions** visually de-emphasized

If everything looks the same weight, increase contrast between levels: size, weight, color, or whitespace.
