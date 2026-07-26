import { Card } from '../components/common/Card';
import { Badge } from '../components/common/Badge';
import { Users, UserCheck } from 'lucide-react';

export function UsersPage() {
  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between pb-4 border-b border-soc-border">
        <div>
          <h1 className="text-xl font-bold text-slate-100 flex items-center gap-2">
            <Users className="w-5 h-5 text-blue-400" />
            User Behavioral Analytics
          </h1>
          <p className="text-xs text-soc-muted mt-0.5">Entity directory and account profile management</p>
        </div>
        <Badge variant="primary">Placeholder View</Badge>
      </div>

      <Card title="User Entities Directory" subtitle="User model schema placeholder">
        <div className="p-8 text-center border border-dashed border-soc-border rounded-xl bg-soc-bg/30">
          <UserCheck className="w-8 h-8 text-soc-subtle mx-auto mb-3" />
          <h4 className="text-sm font-semibold text-slate-200">User Analytics Module Shell</h4>
          <p className="text-xs text-soc-muted mt-1 max-w-sm mx-auto">
            User entity profiling and risk metrics ready for backend integration in future phases.
          </p>
        </div>
      </Card>
    </div>
  );
}
