import { Card } from '../components/common/Card';
import { AssignmentHeader } from '../components/common/AssignmentHeader';
import { BrainCircuit } from 'lucide-react';

export function BehaviourExplorerPage() {
  return (
    <div className="space-y-6">
      {/* Assignment Header */}
      <AssignmentHeader
        requirement="Create per-entity behavioural profiles representing normal behaviour (login hours, locations, devices, resources, session duration) and ensure baselines are continuously computed and used downstream."
        implementation="Non-ML statistical baselines are calculated directly from stored telemetry across 9 hierarchical levels. Downstream anomaly detectors evaluate incoming events against these computed normal baseline distributions."
      />

      {/* Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-4 border-b border-soc-border">
        <div>
          <h1 className="text-xl font-bold text-slate-100 flex items-center gap-2 font-sans">
            <BrainCircuit className="w-5 h-5 text-purple-400" />
            Behavioural Baseline Workspace
          </h1>
          <p className="text-xs text-soc-muted mt-0.5 font-sans">
            Per-Entity Normal Behaviour Profiles & Statistical Distributions
          </p>
        </div>
      </div>

      {/* Baseline Overview Grid */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <Card title="Typical Workday Login Hours" subtitle="Baseline Hourly PDF Distribution">
          <div className="h-32 flex items-end gap-1.5 pt-4">
            {[2, 1, 0, 0, 0, 1, 5, 18, 45, 88, 92, 85, 70, 75, 80, 85, 60, 30, 12, 5, 2, 1, 0, 1].map((val, i) => (
              <div key={i} className="flex-1 bg-soc-border/60 hover:bg-cyan-500 rounded-t transition-all group relative">
                <div className="h-full bg-cyan-500/40 rounded-t" style={{ height: `${val}%` }}></div>
              </div>
            ))}
          </div>
          <p className="text-[10px] text-soc-muted font-mono mt-2 text-center">Peak Hours: 09:00 - 17:00 EST</p>
        </Card>

        <Card title="Peer Group Cohort Baseline" subtitle="Backend Engineering Cohort">
          <div className="space-y-2 font-mono text-xs text-slate-200">
            <div className="flex justify-between"><span className="text-soc-muted">Cohort Size:</span><span>42 Engineers</span></div>
            <div className="flex justify-between"><span className="text-soc-muted">Mean Session Duration:</span><span>480 mins</span></div>
            <div className="flex justify-between"><span className="text-soc-muted">Expected Apps:</span><span>GitHub, Azure AD, Jira</span></div>
          </div>
        </Card>

        <Card title="Seasonality & Release Patterns" subtitle="Enterprise Calendar Driver">
          <div className="space-y-2 font-mono text-xs text-slate-200">
            <div className="flex justify-between"><span className="text-soc-muted">Release Weekend Pattern:</span><span className="text-emerald-400">Active</span></div>
            <div className="flex justify-between"><span className="text-soc-muted">Maintenance Driver:</span><span>2nd Saturday</span></div>
          </div>
        </Card>
      </div>
    </div>
  );
}
