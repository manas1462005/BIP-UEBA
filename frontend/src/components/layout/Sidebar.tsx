import { Link, useLocation } from 'react-router-dom';
import { LayoutDashboard, Database, BrainCircuit, Activity, ShieldAlert, BookOpen, Radio, BarChart2, ShieldCheck, HeartPulse, Layers, GitCommit, Clock, User, Compass, Flame } from 'lucide-react';

export function Sidebar() {
  const location = useLocation();

  const sections = [
    {
      title: 'Assignment Workflow',
      items: [
        { name: 'Assignment Overview', href: '/', icon: LayoutDashboard },
        { name: 'Synthetic Data Generator', href: '/simulation', icon: Database },
        { name: 'Behavioural Baseline', href: '/behaviour-explorer', icon: BrainCircuit },
        { name: 'Detection Engine', href: '/anomaly-intelligence', icon: Activity },
        { name: 'Attack Classification', href: '/threat-intelligence', icon: ShieldAlert },
        { name: 'Explainability', href: '/explainability', icon: BookOpen },
        { name: 'Analyst Dashboard', href: '/live-feed', icon: Radio },
        { name: 'Evaluation Metrics', href: '/analytics-dashboard', icon: BarChart2 }
      ]
    },
    {
      title: 'Investigation Workflow',
      items: [
        { name: 'Incident Workspace', href: '/incident-workspace', icon: ShieldCheck },
        { name: 'Timeline Explorer', href: '/timeline-explorer', icon: Clock },
        { name: 'Evidence Graph', href: '/evidence-graph', icon: GitCommit },
        { name: 'Entity Explorer', href: '/entity-explorer', icon: User },
        { name: 'MITRE Navigator', href: '/mitre-navigator', icon: Flame }
      ]
    },
    {
      title: 'Platform',
      items: [
        { name: 'Real-Time Processing Pipeline', href: '/pipeline-monitor', icon: Layers },
        { name: 'Detection & Context Engine', href: '/context-intelligence', icon: Compass },
        { name: 'System Health', href: '/system-health', icon: HeartPulse }
      ]
    }
  ];

  return (
    <aside className="w-64 bg-soc-panel border-r border-soc-border flex flex-col h-full flex-shrink-0 font-mono">
      {/* Brand Header */}
      <div className="h-16 flex items-center px-6 border-b border-soc-border space-x-3">
        <div className="w-8 h-8 rounded-lg bg-blue-600/20 border border-blue-500/30 flex items-center justify-center">
          <Activity className="w-5 h-5 text-blue-400" />
        </div>
        <div>
          <span className="font-bold text-sm text-slate-100 tracking-wide block font-sans">BIP UEBA</span>
          <span className="text-[10px] text-cyan-400 font-mono tracking-widest uppercase block font-mono">Assignment Platform</span>
        </div>
      </div>

      {/* Navigation Menu */}
      <nav className="flex-1 px-4 py-4 space-y-6 overflow-y-auto">
        {sections.map((sec) => (
          <div key={sec.title} className="space-y-1">
            <h3 className="px-3 text-[10px] font-bold text-soc-muted uppercase tracking-wider font-mono">
              {sec.title}
            </h3>
            {sec.items.map((item) => {
              const isActive = location.pathname === item.href;
              const Icon = item.icon;

              return (
                <Link
                  key={item.name}
                  to={item.href}
                  className={`flex items-center px-3 py-2 rounded-xl text-xs font-medium transition-all duration-200 ${
                    isActive
                      ? 'bg-blue-600/15 text-blue-400 border border-blue-500/20 shadow-sm font-semibold'
                      : 'text-soc-muted hover:text-slate-200 hover:bg-soc-hover'
                  }`}
                >
                  <Icon className={`w-4 h-4 mr-3 flex-shrink-0 ${isActive ? 'text-blue-400' : 'text-soc-subtle'}`} />
                  <span className="font-sans truncate">{item.name}</span>
                </Link>
              );
            })}
          </div>
        ))}
      </nav>

      {/* Footer / System Status */}
      <div className="p-4 border-t border-soc-border bg-soc-bg/40 font-sans">
        <div className="flex items-center space-x-2">
          <span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
          <span className="text-[11px] font-medium text-slate-300">Assignment Evaluator Flow</span>
        </div>
        <p className="text-[10px] text-soc-muted mt-1 font-mono">Evaluation Release v1.9.0</p>
      </div>
    </aside>
  );
}
