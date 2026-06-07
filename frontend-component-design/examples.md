# Component Design Examples

## Example 1: Button with variants

**Input:** Need a reusable button with primary/secondary variants and loading state.

**API design:**

```tsx
type ButtonProps = {
  variant?: 'primary' | 'secondary' | 'ghost';
  size?: 'sm' | 'md' | 'lg';
  isLoading?: boolean;
  disabled?: boolean;
  children: React.ReactNode;
} & React.ButtonHTMLAttributes<HTMLButtonElement>;
```

**Implementation notes:**

- `disabled={disabled || isLoading}`
- Loading: show spinner + `aria-busy="true"`, keep button width stable
- Forward `...rest` to `<button>`

---

## Example 2: Compound Tabs

**Input:** Tab bar where consumers control tab labels and panels.

```tsx
<Tabs defaultValue="profile">
  <Tabs.List aria-label="Account settings">
    <Tabs.Trigger value="profile">Profile</Tabs.Trigger>
    <Tabs.Trigger value="security">Security</Tabs.Trigger>
  </Tabs.List>
  <Tabs.Content value="profile"><ProfileForm /></Tabs.Content>
  <Tabs.Content value="security"><SecurityForm /></Tabs.Content>
</Tabs>
```

**Context shape (internal):**

```tsx
{ activeValue, onChange, registerTrigger, registerContent }
```

**A11y:** `role="tablist"`, triggers `role="tab"` with `aria-selected`, panels `role="tabpanel"` + `aria-labelledby`.

---

## Example 3: Refactor god component

**Before:** `UserDashboard.tsx` — 400 lines, fetch + table + filters + modal.

**After:**

```
UserDashboard.tsx          # fetch + layout
├── useUserFilters.ts      # filter state
├── UserTable.tsx          # presentational table
├── UserFilterBar.tsx      # filter UI
└── UserEditModal.tsx      # modal + form
```

Each file under 120 lines; `UserDashboard` only wires hooks to children.

---

## Example 4: Headless disclosure

```tsx
// useDisclosure.ts
export function useDisclosure(initial = false) {
  const [isOpen, setIsOpen] = useState(initial);
  return {
    isOpen,
    open: () => setIsOpen(true),
    close: () => setIsOpen(false),
    toggle: () => setIsOpen(v => !v),
  };
}

// AccordionItem.tsx — uses hook + project styling
function AccordionItem({ title, children }) {
  const { isOpen, toggle } = useDisclosure();
  return (
    <div>
      <button type="button" aria-expanded={isOpen} onClick={toggle}>
        {title}
      </button>
      {isOpen && <div>{children}</div>}
    </div>
  );
}
```

---

## Example 5: Props API review feedback

**User request:** Review a `<Select>` with 20 boolean props.

**Output format:**

```
🔴 Critical: Replace isMulti + isSearchable + isClearable + ... with variant="multi-search"
🟡 Suggestion: Split into Select.Root / Select.Trigger / Select.Options
🟢 Nice to have: Export SelectOption type for consumers
```
