import { Card } from '../components/common/Card';
import { Badge } from '../components/common/Badge';
import { Settings, Sliders } from 'lucide-react';

export function SettingsPage() {
  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between pb-4 border-b border-soc-border">
        <div>
          <h1 className="text-xl font-bold text-slate-100 flex items-center gap-2">
            <Settings className="w-5 h-5 text-slate-300" />
            System Settings
          </h1>
          <p className="text-xs text-soc-muted mt-0.5">Platform configuration, integrations, and RBAC rules</p>
        </div>
        <Badge variant="primary">Placeholder View</Badge>
      </div>

      <Card title="System Configurations" subtitle="Platform settings placeholder">
        <div className="p-8 text-center border border-dashed border-soc-border rounded-xl bg-soc-bg/30">
          <Sliders className="w-8 h-8 text-soc-subtle mx-auto mb-3" />
          <h4 className="text-sm font-semibold text-slate-200">System Configuration Shell</h4>
          <p className="text-xs text-soc-muted mt-1 max-w-sm mx-auto">
            Environment config, JWT parameters, CORS origins, and PostgreSQL database settings management.
          </p>
        </div>
      </Card>
    </div>
  );
}
