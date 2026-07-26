import { ReactNode } from 'react';
import { cn } from '../../utils/cn';

interface CardProps {
  title?: string;
  subtitle?: string;
  children: ReactNode;
  className?: string;
  headerAction?: ReactNode;
}

export function Card({ title, subtitle, children, className, headerAction }: CardProps) {
  return (
    <div className={cn("bg-soc-panel border border-soc-border rounded-xl p-6 shadow-lg shadow-black/20 backdrop-blur-sm transition-all duration-200", className)}>
      {(title || subtitle || headerAction) && (
        <div className="flex items-center justify-between pb-4 mb-4 border-b border-soc-border/60">
          <div>
            {title && <h3 className="text-lg font-semibold text-slate-100 tracking-tight">{title}</h3>}
            {subtitle && <p className="text-sm text-soc-muted mt-0.5">{subtitle}</p>}
          </div>
          {headerAction && <div>{headerAction}</div>}
        </div>
      )}
      {children}
    </div>
  );
}
