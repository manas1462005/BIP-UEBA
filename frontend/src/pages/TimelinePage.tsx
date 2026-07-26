import { Card } from '../components/common/Card';
import { Badge } from '../components/common/Badge';
import { GitCommit, History } from 'lucide-react';

export function TimelinePage() {
  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between pb-4 border-b border-soc-border">
        <div>
          <h1 className="text-xl font-bold text-slate-100 flex items-center gap-2">
            <GitCommit className="w-5 h-5 text-indigo-400" />
            Attack Timeline
          </h1>
          <p className="text-xs text-soc-muted mt-0.5">Chronological incident sequence and forensic graph shell</p>
        </div>
        <Badge variant="primary">Placeholder View</Badge>
      </div>

      <Card title="Forensic Attack Timeline" subtitle="Event & AttackType schema placeholder">
        <div className="p-8 text-center border border-dashed border-soc-border rounded-xl bg-soc-bg/30">
          <History className="w-8 h-8 text-soc-subtle mx-auto mb-3" />
          <h4 className="text-sm font-semibold text-slate-200">Attack Sequence Shell</h4>
          <p className="text-xs text-soc-muted mt-1 max-w-sm mx-auto">
            MITRE ATT&CK timeline visualizer container. No attack simulation algorithms in Phase 1.
          </p>
        </div>
      </Card>
    </div>
  );
}
