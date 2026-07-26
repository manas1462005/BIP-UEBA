import { useLocation, Link } from 'react-router-dom';
import { ChevronRight, Home } from 'lucide-react';

const routeNames: Record<string, string> = {
  dashboard: 'SOC Overview',
  users: 'User Analytics',
  devices: 'Device Inventory',
  alerts: 'Alert Queue',
  profiles: 'Behaviour Profiles',
  timeline: 'Attack Timeline',
  executive: 'Executive View',
  settings: 'System Settings',
};

export function Breadcrumb() {
  const location = useLocation();
  const pathnames = location.pathname.split('/').filter((x) => x);

  return (
    <nav className="flex items-center text-xs text-soc-subtle space-x-2">
      <Link to="/dashboard" className="hover:text-slate-200 transition-colors flex items-center gap-1">
        <Home className="w-3.5 h-3.5" />
        <span className="hidden sm:inline">Platform</span>
      </Link>
      {pathnames.map((value, index) => {
        const to = `/${pathnames.slice(0, index + 1).join('/')}`;
        const isLast = index === pathnames.length - 1;
        const displayName = routeNames[value] || value;

        return (
          <div key={to} className="flex items-center space-x-2">
            <ChevronRight className="w-3.5 h-3.5 text-soc-border" />
            {isLast ? (
              <span className="font-medium text-blue-400">{displayName}</span>
            ) : (
              <Link to={to} className="hover:text-slate-200 transition-colors">
                {displayName}
              </Link>
            )}
          </div>
        );
      })}
    </nav>
  );
}
