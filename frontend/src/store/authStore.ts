import { create } from 'zustand';
import { AuthState, User } from '../types/auth';

const TOKEN_KEY = 'bip_token';
const USER_KEY = 'bip_user';

export const useAuthStore = create<AuthState>((set) => {
  // Initialize state from localStorage if present
  const initialToken = localStorage.getItem(TOKEN_KEY);
  const initialUserRaw = localStorage.getItem(USER_KEY);
  let initialUser: User | null = null;
  if (initialUserRaw) {
    try {
      initialUser = JSON.parse(initialUserRaw);
    } catch {
      initialUser = null;
    }
  }

  return {
    token: initialToken,
    user: initialUser,
    isAuthenticated: !!initialToken,
    login: (token: string, user: User) => {
      localStorage.setItem(TOKEN_KEY, token);
      localStorage.setItem(USER_KEY, JSON.stringify(user));
      set({ token, user, isAuthenticated: true });
    },
    logout: () => {
      localStorage.removeItem(TOKEN_KEY);
      localStorage.removeItem(USER_KEY);
      set({ token: null, user: null, isAuthenticated: false });
    },
  };
});
