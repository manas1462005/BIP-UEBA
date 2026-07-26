import { useThemeStore } from '../../store/themeStore';
import { Menu, Bell, Radio } from 'lucide-react';
import { Breadcrumb } from './Breadcrumb';
import { UserMenu } from './UserMenu';

export function Navbar() {
  const { toggleSidebar } = useThemeStore();

  return (
    <header className="h-16 bg-soc-header/80 backdrop-blur-md border-b border-soc-border px-4 lg:px-6 flex items-center justify-between sticky top-0 z-30">
      <div className="flex items-center gap-4">
        <button
          onClick={toggleSidebar}
          className="p-2 text-soc-subtle hover:text-slate-100 hover:bg-soc-border/50 rounded-lg transition-colors focus:outline-none"
          aria-label="Toggle Sidebar"
        >
          <Menu className="w-5 h-5" />
        </button>

        <Breadcrumb />
      </div>

      <div className="flex items-center gap-4">
        {/* SOC System Health Badge */}
        <div className="hidden md:flex items-center gap-2 px-3 py-1 bg-emerald-950/40 border border-emerald-800/50 rounded-full">
          <Radio className="w-3.5 h-3.5 text-emerald-400 animate-pulse" />
          <span className="text-[11px] font-mono font-medium text-emerald-400">UEBA INGESTION ACTIVE</span>
        </div>

        {/* Notifications Mock Icon */}
        <button className="relative p-2 text-soc-subtle hover:text-slate-100 hover:bg-soc-border/50 rounded-lg transition-colors">
          <Bell className="w-5 h-5" />
          <span className="absolute top-1.5 right-1.5 w-2 h-2 rounded-full bg-blue-500 ring-2 ring-soc-header" />
        </button>

        <div className="h-5 w-px bg-soc-border" />

        {/* User Menu */}
        <UserMenu />
      </div>
    </header>
  );
}
