export type UserRole = 'Admin' | 'Analyst' | 'Viewer';

export interface User {
  email: string;
  fullName: string;
  role: UserRole;
}

export interface AuthState {
  token: string | null;
  user: User | null;
  isAuthenticated: boolean;
  login: (token: string, user: User) => void;
  logout: () => void;
}
