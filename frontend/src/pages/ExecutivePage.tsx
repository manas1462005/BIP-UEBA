import { Card } from '../components/common/Card';
import { Badge } from '../components/common/Badge';
import { PieChart, ShieldAlert } from 'lucide-react';

export function ExecutivePage() {
  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between pb-4 border-b border-soc-border">
        <div>
          <h1 className="text-xl font-bold text-slate-100 flex items-center gap-2">
            <PieChart className="w-5 h-5 text-emerald-400" />
            Executive Dashboard
          </h1>
          <p className="text-xs text-soc-muted mt-0.5">CISO risk posture and organizational metrics</p>
        </div>
        <Badge variant="primary">Placeholder View</Badge>
      </div>

      <Card title="Executive Risk Summary" subtitle="Organization & RiskScore schema placeholder">
        <div className="p-8 text-center border border-dashed border-soc-border rounded-xl bg-soc-bg/30">
          <ShieldAlert className="w-8 h-8 text-soc-subtle mx-auto mb-3" />
          <h4 className="text-sm font-semibold text-slate-200">Executive Risk Shell</h4>
          <p className="text-xs text-soc-muted mt-1 max-w-sm mx-auto">
            High-level executive metrics layout. Charts and analytical widgets will be integrated in future phases.
          </p>
        </div>
      </Card>
    </div>
  );
}
