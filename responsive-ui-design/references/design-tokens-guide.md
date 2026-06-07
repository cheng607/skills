# Design Tokens Guide

## CSS Custom Properties Template

See [assets/design-tokens-template.json](../assets/design-tokens-template.json) for a machine-readable token set.

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

## Semantic Token Naming

```
color-bg-primary, color-bg-muted
color-text-primary, color-text-secondary
color-border-default
color-accent, color-accent-hover
color-danger, color-success
```

## Tailwind Config Extension

Copy from [assets/tailwind-theme-template.js](../assets/tailwind-theme-template.js) or extend manually:

```js
theme: {
  extend: {
    spacing: { '18': '4.5rem' },
    maxWidth: { 'content': '72rem' },
    fontSize: {
      'display': ['3rem', { lineHeight: '1.1', fontWeight: '700' }],
    },
  },
},
screens: {
  'xs': '475px',
},
```

## Token Usage Rules

1. Never hardcode hex in components — reference tokens
2. Spacing: use scale names, not arbitrary px
3. Typography: one modular scale across the app
4. Sync CSS variables with Tailwind theme when both exist
