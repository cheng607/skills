# Accessibility Guide for UI Components

## Semantic HTML First

| Use case | Element | Avoid |
|----------|---------|-------|
| Click action | `<button type="button">` | `<div onClick>` |
| Navigation | `<a href="...">` | `<span onClick>` |
| Text input | `<input>` + `<label>` | placeholder-only label |
| Toggle | `<button aria-pressed>` | checkbox styled as switch without role |
| Expand/collapse | `<button aria-expanded>` | div with click handler |

## ARIA Usage Rules

1. **No ARIA is better than wrong ARIA** — prefer native elements
2. **Don't duplicate** — no `role="button"` on `<button>`
3. **Keep labels visible** when possible; `aria-label` for icon-only controls
4. **Live regions** for async updates: `aria-live="polite"` on toast/status areas

## Keyboard Patterns

| Component | Keys |
|-----------|------|
| Button | Enter, Space |
| Menu / Listbox | Arrow keys, Home, End, Escape |
| Tabs | Arrow Left/Right, Home, End |
| Dialog | Escape to close, focus trap inside |
| Combobox | Arrow Down to open, type to filter |

## Focus Management

```tsx
// Open dialog → move focus to first focusable element
useEffect(() => {
  if (isOpen) firstFocusableRef.current?.focus();
}, [isOpen]);

// Close dialog → restore focus to trigger
onClose={() => {
  setIsOpen(false);
  triggerRef.current?.focus();
}}
```

Focus ring (never remove without replacement):

```css
:focus-visible {
  outline: 2px solid var(--color-accent);
  outline-offset: 2px;
}
```

## Form Accessibility

- Every input has an associated `<label htmlFor={id}>`
- Group related fields with `<fieldset>` + `<legend>`
- Surface errors with `aria-invalid="true"` + `aria-describedby` pointing to error text
- Required fields: `required` attribute + visible indicator (not color alone)

## Component Audit Checklist

```
- [ ] Tab order is logical
- [ ] All interactive elements reachable by keyboard
- [ ] Focus visible on every interactive element
- [ ] Screen reader announces name, role, state
- [ ] Dynamic content updates announced when needed
- [ ] Color contrast ≥ 4.5:1 for text
- [ ] Touch targets ≥ 44px where applicable
```

Run `python scripts/validate.py <file-or-directory>` for automated checks.
