import { Card } from '../components/common/Card';
import { Badge } from '../components/common/Badge';
import { Laptop, HardDrive } from 'lucide-react';

export function DevicesPage() {
  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between pb-4 border-b border-soc-border">
        <div>
          <h1 className="text-xl font-bold text-slate-100 flex items-center gap-2">
            <Laptop className="w-5 h-5 text-blue-400" />
            Device Inventory
          </h1>
          <p className="text-xs text-soc-muted mt-0.5">Host asset inventory and endpoint tracking</p>
        </div>
        <Badge variant="primary">Placeholder View</Badge>
      </div>

      <Card title="Managed Device Inventory" subtitle="Device model schema placeholder">
        <div className="p-8 text-center border border-dashed border-soc-border rounded-xl bg-soc-bg/30">
          <HardDrive className="w-8 h-8 text-soc-subtle mx-auto mb-3" />
          <h4 className="text-sm font-semibold text-slate-200">Device Telemetry Module Shell</h4>
          <p className="text-xs text-soc-muted mt-1 max-w-sm mx-auto">
            Host asset monitoring and network endpoint mapping architecture ready for Phase 2.
          </p>
        </div>
      </Card>
    </div>
  );
}
