import { create } from 'zustand';

interface ThemeState {
  isSidebarCollapsed: boolean;
  toggleSidebar: () => void;
}

export const useThemeStore = create<ThemeState>((set) => ({
  isSidebarCollapsed: false,
  toggleSidebar: () => set((state) => ({ isSidebarCollapsed: !state.isSidebarCollapsed })),
}));
