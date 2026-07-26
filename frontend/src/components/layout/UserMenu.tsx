import { useState, useRef, useEffect } from 'react';
import { useAuthStore } from '../../store/authStore';
import { LogOut, ShieldCheck, ChevronDown } from 'lucide-react';
import { Badge } from '../common/Badge';

export function UserMenu() {
  const { user, logout } = useAuthStore();
  const [isOpen, setIsOpen] = useState(false);
  const menuRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    function handleClickOutside(event: MouseEvent) {
      if (menuRef.current && !menuRef.current.contains(event.target as Node)) {
        setIsOpen(false);
      }
    }
    document.addEventListener('mousedown', handleClickOutside);
    return () => document.removeEventListener('mousedown', handleClickOutside);
  }, []);

  if (!user) return null;

  return (
    <div className="relative" ref={menuRef}>
      <button
        onClick={() => setIsOpen(!isOpen)}
        className="flex items-center gap-3 p-2 rounded-lg hover:bg-soc-border/50 transition-colors duration-150 text-left focus:outline-none focus:ring-1 focus:ring-soc-accent/50"
      >
        <div className="w-8 h-8 rounded-full bg-gradient-to-tr from-blue-600 to-cyan-500 flex items-center justify-center text-white font-semibold text-xs shadow-md shadow-blue-900/30">
          {user.fullName ? user.fullName.charAt(0).toUpperCase() : 'U'}
        </div>
        <div className="hidden md:block">
          <div className="text-xs font-semibold text-slate-200">{user.fullName}</div>
          <div className="text-[10px] text-soc-muted">{user.email}</div>
        </div>
        <ChevronDown className="w-4 h-4 text-soc-subtle hidden md:block" />
      </button>

      {isOpen && (
        <div className="absolute right-0 mt-2 w-64 bg-soc-panel border border-soc-border rounded-xl shadow-2xl p-2 z-50 animate-in fade-in slide-in-from-top-2 duration-150">
          <div className="p-3 border-b border-soc-border mb-1">
            <p className="text-xs text-soc-muted">Signed in as</p>
            <p className="text-sm font-medium text-slate-100 truncate">{user.email}</p>
            <div className="mt-2 flex items-center justify-between">
              <span className="text-xs text-soc-subtle">Role</span>
              <Badge variant={user.role === 'Admin' ? 'danger' : user.role === 'Analyst' ? 'primary' : 'default'}>
                {user.role}
              </Badge>
            </div>
          </div>

          <div className="px-3 py-2 text-xs text-soc-subtle flex items-center gap-2">
            <ShieldCheck className="w-4 h-4 text-emerald-400" />
            <span>MFA Protected Session</span>
          </div>

          <button
            onClick={() => {
              setIsOpen(false);
              logout();
            }}
            className="w-full flex items-center gap-2 px-3 py-2.5 mt-1 text-xs font-medium text-rose-400 hover:bg-rose-950/40 rounded-lg transition-colors duration-150"
          >
            <LogOut className="w-4 h-4" />
            <span>Sign Out Session</span>
          </button>
        </div>
      )}
    </div>
  );
}
