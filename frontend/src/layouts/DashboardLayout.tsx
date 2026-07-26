import { ReactNode } from 'react';
import { DashboardShell } from '../components/layout/DashboardShell';

export interface DashboardLayoutProps {
  children: ReactNode;
}

export function DashboardLayout({ children }: DashboardLayoutProps) {
  return <DashboardShell>{children}</DashboardShell>;
}

export default DashboardLayout;
