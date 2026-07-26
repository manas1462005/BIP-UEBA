import { Card } from '../components/common/Card';
import { Badge } from '../components/common/Badge';
import { AlertTriangle, BellOff } from 'lucide-react';

export function AlertsPage() {
  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between pb-4 border-b border-soc-border">
        <div>
          <h1 className="text-xl font-bold text-slate-100 flex items-center gap-2">
            <AlertTriangle className="w-5 h-5 text-amber-400" />
            Alert Queue & Triage
          </h1>
          <p className="text-xs text-soc-muted mt-0.5">Security incident queue and triage workflow</p>
        </div>
        <Badge variant="primary">Placeholder View</Badge>
      </div>

      <Card title="Security Alert Triage" subtitle="Alert model schema placeholder">
        <div className="p-8 text-center border border-dashed border-soc-border rounded-xl bg-soc-bg/30">
          <BellOff className="w-8 h-8 text-soc-subtle mx-auto mb-3" />
          <h4 className="text-sm font-semibold text-slate-200">Alert Triage Queue Shell</h4>
          <p className="text-xs text-soc-muted mt-1 max-w-sm mx-auto">
            High-fidelity alert management UI container. No fake or synthetic alerts generated in Phase 1.
          </p>
        </div>
      </Card>
    </div>
  );
}
