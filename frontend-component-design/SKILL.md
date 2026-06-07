---
name: frontend-component-design
description: >-
  Designs and implements reusable frontend UI components with clear props APIs,
  composition patterns, accessibility, and state boundaries. Use when building
  React/Vue/Svelte components, designing component libraries, refactoring UI
  into smaller pieces, or when the user mentions component design, props API,
  compound components, 组件设计, 组件拆分, or UI 组件封装.
---

# Frontend Component Design

## Quick Start

Before writing code:

1. **Define responsibility** — one primary job per component
2. **Design the public API** — props, slots/children, events/callbacks
3. **Choose composition pattern** — simple, compound, or headless
4. **Plan accessibility** — roles, labels, keyboard, focus
5. **Implement smallest useful version**, then extend via variants

Match the project's existing stack (React/Vue/Svelte), styling approach, and file conventions.

## Directory Layout

```
frontend-component-design/
├── SKILL.md
├── scripts/
│   ├── validate.py          # Scan components for a11y/API issues
│   └── scaffold.sh          # Generate component from template
├── references/
│   ├── examples.md
│   ├── patterns-guide.md
│   └── accessibility-guide.md
└── assets/
    └── component-props-template.ts
```

Workflow:

```bash
# 1. Scaffold a new component
bash scripts/scaffold.sh Button src/components/Button.tsx

# 2. Implement and validate
python scripts/validate.py src/components/
```

## Component API Design

### Props checklist

| Concern | Guideline |
|---------|-----------|
| Naming | `onXxx` for callbacks, `isXxx`/`hasXxx` for booleans, avoid abbreviations |
| Variants | Prefer `variant="primary"` over multiple booleans (`primary`, `danger`) |
| Size | Standardize: `sm` / `md` / `lg` (or project tokens) |
| Polymorphism | Support `as`/`component` prop when semantic HTML matters |
| Defaults | Sensible defaults; required props only when truly required |
| Spread | Forward native HTML attrs to the root element |

### Prefer composition over configuration

```tsx
// ❌ Too many props
<Card title="..." subtitle="..." footer="..." headerAction={...} />

// ✅ Composition
<Card>
  <Card.Header action={<Button>Save</Button>}>Title</Card.Header>
  <Card.Body>Content</Card.Body>
  <Card.Footer>Actions</Card.Footer>
</Card>
```

### Controlled vs uncontrolled

- **Controlled**: parent owns value via `value` + `onChange`
- **Uncontrolled**: internal state + optional `defaultValue`
- Document which mode; support both when the pattern is common (Input, Select, Tabs)

## Patterns

### 1. Simple presentational

Stateless, receives all data via props. Best for Button, Badge, Avatar.

### 2. Compound components

Shared context between sub-components. Best for Tabs, Accordion, Menu, Form.

```
Tabs → Tabs.List, Tabs.Trigger, Tabs.Content
```

Keep context private; export only the compound API.

### 3. Headless + styled

Separate logic hook from markup:

```
useDisclosure()  →  { isOpen, open, close, toggle }
<Disclosure />   →  styled wrapper using the hook
```

Use when behavior is reused across different visual designs.

### 4. Render props / slots

When consumers need full control of a sub-region without forking the component.

## State Boundaries

```
Page/Route
  └── Container (data fetching, orchestration)
        └── Presentational components (props only)
              └── Leaf UI (Button, Input)
```

Rules:

- Fetch and route-level state stay in containers or hooks at page level
- UI components receive data + callbacks; avoid fetching inside leaf components
- Extract custom hooks when logic exceeds ~15 lines or is reused twice

## Accessibility (required)

Every interactive component must pass:

- [ ] Correct semantic element or `role`
- [ ] Visible focus indicator (`:focus-visible`)
- [ ] Keyboard operable (Enter/Space for buttons, arrows for menus/tabs)
- [ ] `aria-label` or associated `<label>` for inputs
- [ ] `aria-expanded`, `aria-selected`, `aria-current` where state is visual-only
- [ ] Color is not the only indicator of state

Run through: Tab-only navigation, screen reader label check.

## File Structure

Pick one convention and stay consistent:

```
components/Button/
├── Button.tsx
├── Button.test.tsx
├── Button.stories.tsx   # optional
└── index.ts             # re-export public API
```

Or colocated: `Button.tsx` + `Button.module.css` at feature level for app-specific UI.

## TypeScript (when applicable)

```tsx
type ButtonProps = React.ComponentPropsWithoutRef<'button'> & {
  variant?: 'primary' | 'secondary' | 'ghost';
  size?: 'sm' | 'md' | 'lg';
  isLoading?: boolean;
};
```

- Extend native element props for the root element
- Use discriminated unions for mutually exclusive props
- Export prop types consumers need

## Anti-Patterns

| Avoid | Instead |
|-------|---------|
| God components (500+ lines) | Split by responsibility |
| Prop drilling 5+ levels | Context or composition |
| `useEffect` for derived state | Compute during render |
| Index as `key` in dynamic lists | Stable unique id |
| Inline anonymous functions in lists passed to memoized children | Stable callbacks |

## Delivery Checklist

Before marking done:

- [ ] Public API documented (JSDoc or Storybook)
- [ ] Empty/loading/error states handled where relevant
- [ ] Responsive behavior verified
- [ ] No hardcoded user-facing strings (i18n-ready if project uses i18n)
- [ ] Linter passes on touched files

## Additional Resources

| Resource | Purpose |
|----------|---------|
| [references/examples.md](references/examples.md) | Real-world component API examples |
| [references/patterns-guide.md](references/patterns-guide.md) | Compound, headless, and state patterns |
| [references/accessibility-guide.md](references/accessibility-guide.md) | ARIA, keyboard, focus management |
| [assets/component-props-template.ts](assets/component-props-template.ts) | Typed component starter template |
| [scripts/validate.py](scripts/validate.py) | Automated component lint checks |
| [scripts/scaffold.sh](scripts/scaffold.sh) | Generate typed component from template |
