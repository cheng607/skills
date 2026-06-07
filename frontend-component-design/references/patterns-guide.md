# Component Patterns Reference

## Pattern Selection Matrix

| Scenario | Pattern | Example |
|----------|---------|---------|
| Single visual + behavior | Simple | Badge, Tag, Spinner |
| Multiple sub-parts sharing state | Compound | Tabs, Menu, Form |
| Reuse logic, swap UI | Headless hook + styled wrapper | Disclosure, Combobox |
| Consumer controls markup | Slot / children / render prop | Modal body, Table cell |

## Compound Component Template

```tsx
const TabsContext = createContext<TabsContextValue | null>(null);

function Tabs({ defaultValue, children }: TabsProps) {
  const [value, setValue] = useState(defaultValue);
  return (
    <TabsContext.Provider value={{ value, setValue }}>
      {children}
    </TabsContext.Provider>
  );
}

function useTabsContext() {
  const ctx = useContext(TabsContext);
  if (!ctx) throw new Error('Tabs sub-components must be used within <Tabs>');
  return ctx;
}

Tabs.List = TabsList;
Tabs.Trigger = TabsTrigger;
Tabs.Content = TabsContent;
export { Tabs };
```

**Rules:**

- Context is internal; only export the compound root
- Sub-components validate context presence
- Attach static sub-components to root: `Tabs.List = TabsList`

## Headless Hook Template

```tsx
export function useToggle(initial = false) {
  const [on, setOn] = useState(initial);
  return {
    on,
    toggle: () => setOn(v => !v),
    setOn,
    props: {
      'aria-pressed': on,
      onClick: () => setOn(v => !v),
    },
  };
}
```

Separate `useXxx` (logic) from `Xxx` (styled UI) so teams can reskin without rewriting behavior.

## Props API Design Patterns

### Variant enum (preferred)

```tsx
variant?: 'primary' | 'secondary' | 'danger';
size?: 'sm' | 'md' | 'lg';
```

### Polymorphic root

```tsx
type Props<T extends React.ElementType = 'button'> = {
  as?: T;
} & React.ComponentPropsWithoutRef<T>;
```

### Discriminated union for exclusive modes

```tsx
type Props =
  | { href: string; onClick?: never }
  | { href?: never; onClick: () => void };
```

## State Location Rules

| State type | Location |
|------------|----------|
| URL-synced (filters, pagination) | Route/search params |
| Server data | React Query / SWR / loader |
| Form draft | Form library or local state in form container |
| UI ephemeral (open/closed, hover) | Component or colocated hook |
| Shared UI (theme, locale) | App-level context |

## File Naming Conventions

```
components/
├── Button/
│   ├── Button.tsx
│   ├── Button.test.tsx
│   ├── useButton.ts        # only if logic is extracted
│   └── index.ts
└── index.ts                # barrel export (optional)
```

Copy starter structure from [assets/component-props-template.ts](../assets/component-props-template.ts).
