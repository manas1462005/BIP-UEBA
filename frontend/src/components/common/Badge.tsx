import { ReactNode } from 'react';
import { cn } from '../../utils/cn';

export type BadgeVariant = 'default' | 'primary' | 'success' | 'warning' | 'danger' | 'info';

interface BadgeProps {
  children: ReactNode;
  variant?: BadgeVariant;
  className?: string;
}

const variantStyles: Record<BadgeVariant, string> = {
  default: 'bg-slate-800 text-slate-300 border-slate-700',
  primary: 'bg-blue-950/60 text-blue-400 border-blue-800/60',
  success: 'bg-emerald-950/60 text-emerald-400 border-emerald-800/60',
  warning: 'bg-amber-950/60 text-amber-400 border-amber-800/60',
  danger: 'bg-rose-950/60 text-rose-400 border-rose-800/60',
  info: 'bg-cyan-950/60 text-cyan-400 border-cyan-800/60',
};

export function Badge({ children, variant = 'default', className }: BadgeProps) {
  return (
    <span className={cn('inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium border', variantStyles[variant], className)}>
      {children}
    </span>
  );
}
