# Breakpoints & Responsive Testing Guide

## Default Breakpoint Scale

| Name | Min width | Typical use |
|------|-----------|-------------|
| base | 0 | Mobile portrait |
| xs | 475px | Large phone (optional) |
| sm | 640px | Large phone / small tablet |
| md | 768px | Tablet |
| lg | 1024px | Laptop |
| xl | 1280px | Desktop |
| 2xl | 1536px | Wide screen |

## Mobile-First CSS

```css
/* Base: mobile */
.grid { grid-template-columns: 1fr; }

/* Enhance at breakpoints */
@media (min-width: 768px) {
  .grid { grid-template-columns: repeat(2, 1fr); }
}
@media (min-width: 1024px) {
  .grid { grid-template-columns: repeat(3, 1fr); }
}
```

Tailwind equivalent: `grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3`

## Viewport Testing Matrix

| Viewport | Check |
|----------|-------|
| 320×568 | No overflow, readable text, tappable buttons |
| 375×667 | iPhone SE layout |
| 768×1024 | Tablet two-column where intended |
| 1024×768 | Sidebar visible, content not cramped |
| 1440×900 | Max-width container centered, no overly wide lines |

## Accessibility at Each Breakpoint

| Requirement | Standard |
|-------------|----------|
| Body text contrast | 4.5:1 (WCAG AA) |
| Large text (≥18px bold / 24px) | 3:1 |
| Focus ring | 2px visible, 3:1 against adjacent colors |
| Touch target | 44px minimum dimension |
| Base font size (mobile) | ≥ 16px to prevent iOS zoom on focus |

## Motion Preferences

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

## Pre-Delivery Checklist

- [ ] No horizontal scroll at 320px width
- [ ] Text readable without zoom
- [ ] Focus states visible on all interactive elements
- [ ] Images have appropriate `alt` and don't overflow
- [ ] Sticky/fixed elements don't obscure content
- [ ] Dark mode tokens applied if supported
- [ ] Hover-only UI not required on touch devices

## Automated Validation

Run against HTML/CSS/TSX files:

```bash
python scripts/validate.py src/
```

Checks: viewport meta, overflow risks, touch target hints, reduced-motion support.
