/**
 * Starter template for a typed, accessible UI component.
 * Copy into your project and rename Button → YourComponent.
 */
import type { ComponentPropsWithoutRef, ElementType, ReactNode } from 'react';

type ButtonOwnProps = {
  variant?: 'primary' | 'secondary' | 'ghost';
  size?: 'sm' | 'md' | 'lg';
  isLoading?: boolean;
  children: ReactNode;
};

type ButtonProps<T extends ElementType = 'button'> = ButtonOwnProps & {
  as?: T;
} & Omit<ComponentPropsWithoutRef<T>, keyof ButtonOwnProps | 'as'>;

export function Button<T extends ElementType = 'button'>({
  as,
  variant = 'primary',
  size = 'md',
  isLoading = false,
  disabled,
  children,
  ...rest
}: ButtonProps<T>) {
  const Component = as ?? 'button';

  return (
    <Component
      type={Component === 'button' ? 'button' : undefined}
      disabled={disabled || isLoading}
      aria-busy={isLoading || undefined}
      data-variant={variant}
      data-size={size}
      {...rest}
    >
      {isLoading ? 'Loading…' : children}
    </Component>
  );
}

export type { ButtonProps, ButtonOwnProps };
