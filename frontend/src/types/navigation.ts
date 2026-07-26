import { ReactNode } from 'react';
import { UserRole } from './auth';

export interface NavItem {
  label: string;
  path: string;
  icon: ReactNode;
  roles?: UserRole[];
}
