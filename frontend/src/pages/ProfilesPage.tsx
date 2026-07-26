import { Card } from '../components/common/Card';
import { Badge } from '../components/common/Badge';
import { Fingerprint, Dna } from 'lucide-react';

export function ProfilesPage() {
  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between pb-4 border-b border-soc-border">
        <div>
          <h1 className="text-xl font-bold text-slate-100 flex items-center gap-2">
            <Fingerprint className="w-5 h-5 text-cyan-400" />
            Behaviour Profiles
          </h1>
          <p className="text-xs text-soc-muted mt-0.5">Entity baselines and behavioral vector schemas</p>
        </div>
        <Badge variant="primary">Placeholder View</Badge>
      </div>

      <Card title="Behavioral Baselines" subtitle="BehaviourProfile model schema placeholder">
        <div className="p-8 text-center border border-dashed border-soc-border rounded-xl bg-soc-bg/30">
          <Dna className="w-8 h-8 text-soc-subtle mx-auto mb-3" />
          <h4 className="text-sm font-semibold text-slate-200">Behavioral Profiling Shell</h4>
          <p className="text-xs text-soc-muted mt-1 max-w-sm mx-auto">
            Entity baseline vector storage schema defined in PostgreSQL (`behaviourprofiles`). No ML modeling in Phase 1.
          </p>
        </div>
      </Card>
    </div>
  );
}
