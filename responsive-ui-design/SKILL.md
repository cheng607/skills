---
name: responsive-ui-design
description: >-
  Implements responsive page layouts, spacing systems, typography scales, and
  accessible visual hierarchy using CSS, Tailwind, or design tokens. Use when
  building landing pages, dashboards, mobile layouts, design systems, or when
  the user mentions responsive design, breakpoints, layout, Tailwind, CSS Grid,
  响应式, 页面布局, UI 设计, or 设计规范.
---

# Responsive UI Design

## Quick Start

1. **Mobile-first** — base styles for smallest viewport, enhance with `min-width` breakpoints
2. **Define tokens first** — spacing, type scale, colors, radii, shadows
3. **Pick layout model** — Flexbox for 1D, Grid for 2D page structure
4. **Test at key widths** — 320, 768, 1024, 1440 px
5. **Verify contrast and touch targets** before shipping

Align with the project's design system or Tailwind config when present.

## Breakpoints

Default reference (adjust to project tokens):

| Name | Min width | Typical use |
|------|-----------|-------------|
| base | 0 | Mobile portrait |
| sm | 640px | Large phone / small tablet |
| md | 768px | Tablet |
| lg | 1024px | Laptop |
| xl | 1280px | Desktop |
| 2xl | 1536px | Wide screen |

Tailwind: `class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3"`

CSS:

```css
.container {
  width: min(100% - 2rem, 72rem);
  margin-inline: auto;
}
```

## Spacing System

Use a consistent scale (4px or 8px base):

| Token | Value | Use |
|-------|-------|-----|
| xs | 4px | Icon gaps, tight inline |
| sm | 8px | Related elements |
| md | 16px | Section padding mobile |
| lg | 24px | Card padding |
| xl | 32px | Section gaps |
| 2xl | 48px | Page sections |

Rules:

- Related items: smaller gap; unrelated sections: larger gap
- Prefer token names (`gap-md`) over magic numbers
- Vertical rhythm: stack sections with consistent `gap-y-*`

## Typography

Establish a modular scale:

| Role | Mobile | Desktop | Weight |
|------|--------|---------|--------|
| Display | 2rem | 3rem | 700 |
| H1 | 1.75rem | 2.25rem | 700 |
| H2 | 1.5rem | 1.875rem | 600 |
| H3 | 1.25rem | 1.5rem | 600 |
| Body | 1rem | 1rem | 400 |
| Small | 0.875rem | 0.875rem | 400 |
| Caption | 0.75rem | 0.75rem | 400 |

Rules:

- Max line length: 65–75 characters (`max-w-prose` ≈ 65ch)
- Line height: 1.5–1.6 for body, 1.2–1.3 for headings
- Limit font families to 1–2 (sans + optional mono)

## Layout Patterns

### Page shell

```
┌─────────────────────────────┐
│ Header (sticky optional)    │
├──────────┬──────────────────┤
│ Sidebar  │ Main content     │  ← lg+: side-by-side
│ (drawer  │                  │     md: collapsible
│  mobile) │                  │
├──────────┴──────────────────┤
│ Footer                      │
└─────────────────────────────┘
```

Mobile: sidebar → off-canvas drawer; main full width.

### Content grid

```html
<!-- Auto-fit responsive card grid -->
<div class="grid grid-cols-[repeat(auto-fit,minmax(min(100%,280px),1fr))] gap-6">
```

### Stack → Row pattern

```html
<div class="flex flex-col md:flex-row md:items-center gap-4">
  <div class="flex-1">...</div>
  <div class="shrink-0">...</div>
</div>
```

## Color & Contrast

- Text on background: minimum **4.5:1** (WCAG AA body), **3:1** for large text
- Interactive elements: distinguish default / hover / active / disabled
- Never rely on color alone — add icon, underline, or label for state

Semantic token naming:

```
color-bg-primary, color-bg-muted
color-text-primary, color-text-secondary
color-border-default
color-accent, color-accent-hover
color-danger, color-success
```

## Touch & Interaction

- Minimum touch target: **44×44 px** (Apple HIG) or **48×48 dp** (Material)
- Adequate spacing between tappable elements (≥ 8px)
- Hover styles only where pointer exists; don't hide critical actions behind hover-only UI on mobile

## Images & Media

```html
<img src="..." alt="Descriptive text" loading="lazy"
     class="w-full h-auto object-cover" />
```

- Use `aspect-ratio` or fixed aspect containers to prevent layout shift
- `srcset` / `<picture>` for art direction at breakpoints
- Decorative images: `alt=""`

## Tailwind Conventions

When using Tailwind:

1. Read `tailwind.config` for project tokens before inventing classes
2. Order: layout → spacing → sizing → typography → color → effects
3. Extract repeated patterns to `@apply` or components, not 40-class strings everywhere
4. Use `container` + `mx-auto px-4` for page width

```tsx
// Repeated pattern → component
function PageSection({ title, children }) {
  return (
    <section className="py-12 md:py-16">
      <div className="mx-auto max-w-6xl px-4 md:px-6">
        <h2 className="text-2xl font-semibold md:text-3xl">{title}</h2>
        <div className="mt-6">{children}</div>
      </div>
    </section>
  );
}
```

## CSS Module / Vanilla CSS

Prefer logical properties:

```css
.card {
  padding-inline: var(--space-md);
  margin-block-end: var(--space-lg);
}
```

Use `@media (min-width: 768px)` for enhancements, not desktop-first overrides.

## Container Queries

When component width matters more than viewport:

```css
.card-grid {
  container-type: inline-size;
}
@container (min-width: 400px) {
  .card { flex-direction: row; }
}
```

## Pre-Delivery Checklist

- [ ] No horizontal scroll at 320px width
- [ ] Text readable without zoom (≥ 16px base on mobile)
- [ ] Focus states visible on all interactive elements
- [ ] Images have appropriate `alt` and don't overflow
- [ ] Sticky/fixed elements don't obscure content or focus traps
- [ ] Dark mode tokens applied if project supports dark mode

## Additional Resources

- Token reference and breakpoint snippets: [reference.md](reference.md)
