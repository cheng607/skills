# Layout Patterns Reference

## Page Shell

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

## Centered Page Container

```html
<main class="mx-auto w-full max-w-6xl px-4 py-8 md:px-6 md:py-12">
  ...
</main>
```

```css
.container {
  width: min(100% - 2rem, 72rem);
  margin-inline: auto;
}
```

## Holy Grail Layout

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

## Responsive Card Grid

```html
<div class="grid grid-cols-[repeat(auto-fit,minmax(min(100%,280px),1fr))] gap-6">
  <!-- cards -->
</div>
```

## Stack → Row Pattern

```html
<div class="flex flex-col md:flex-row md:items-center gap-4">
  <div class="flex-1">...</div>
  <div class="shrink-0">...</div>
</div>
```

## Responsive Table → Cards

```html
<table class="hidden md:table w-full">...</table>

<div class="md:hidden space-y-4">
  <article class="rounded-lg border p-4">...</article>
</div>
```

## Sticky Header with Safe Area

```css
.header {
  position: sticky;
  top: 0;
  z-index: 50;
  padding-top: env(safe-area-inset-top);
}
```

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

## PageSection Component Pattern

```tsx
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

## Visual Hierarchy Checklist

Squint test — at a glance, can you identify:

1. **Primary action** (one per viewport section)
2. **Page title** vs section headings vs body
3. **Grouped related content** (spacing + borders/background)
4. **Secondary/destructive actions** visually de-emphasized

If everything looks the same weight, increase contrast between levels: size, weight, color, or whitespace.
