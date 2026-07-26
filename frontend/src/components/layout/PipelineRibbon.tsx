import { useLocation, Link } from 'react-router-dom';
import { Database, BrainCircuit, Activity, ShieldAlert, BookOpen, Radio, BarChart2 } from 'lucide-react';

export function PipelineRibbon() {
  const location = useLocation();

  const steps = [
    { name: 'Synthetic Data', path: '/simulation', icon: Database },
    { name: 'Behaviour Profile', path: '/behaviour-explorer', icon: BrainCircuit },
    { name: 'Detection', path: '/anomaly-intelligence', icon: Activity },
    { name: 'Classification', path: '/threat-intelligence', icon: ShieldAlert },
    { name: 'Explainability', path: '/explainability', icon: BookOpen },
    { name: 'Dashboard', path: '/live-feed', icon: Radio },
    { name: 'Evaluation', path: '/analytics-dashboard', icon: BarChart2 }
  ];

  const getActiveIndex = () => {
    const current = location.pathname;
    if (current === '/simulation') return 0;
    if (current === '/behaviour-explorer') return 1;
    if (current === '/anomaly-intelligence') return 2;
    if (current === '/threat-intelligence') return 3;
    if (current === '/explainability') return 4;
    if (current === '/live-feed' || current === '/' || current === '/incident-workspace') return 5;
    if (current === '/analytics-dashboard') return 6;
    return -1;
  };

  const activeIdx = getActiveIndex();

  return (
    <div className="bg-soc-panel border-b border-soc-border px-6 py-2.5 font-mono text-xs">
      <div className="flex items-center justify-between overflow-x-auto gap-2">
        {steps.map((step, idx) => {
          const isActive = idx === activeIdx;
          const isPassed = activeIdx > idx;
          const Icon = step.icon;

          return (
            <div key={step.name} className="flex items-center gap-2 flex-shrink-0">
              <Link
                to={step.path}
                className={`flex items-center gap-1.5 px-3 py-1 rounded-xl transition-all font-sans ${
                  isActive
                    ? 'bg-blue-600/20 text-blue-400 border border-blue-500/40 font-bold shadow-sm'
                    : isPassed
                    ? 'text-emerald-400 hover:text-emerald-300'
                    : 'text-soc-muted hover:text-slate-200'
                }`}
              >
                <Icon className={`w-3.5 h-3.5 ${isActive ? 'text-blue-400 animate-pulse' : isPassed ? 'text-emerald-400' : 'text-soc-subtle'}`} />
                <span>{step.name}</span>
              </Link>
              {idx < steps.length - 1 && (
                <span className="text-soc-border text-xs font-mono">→</span>
              )}
            </div>
          );
        })}
      </div>
    </div>
  );
}
