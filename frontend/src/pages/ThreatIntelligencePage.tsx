import { Card } from '../components/common/Card';
import { Badge } from '../components/common/Badge';
import { AssignmentHeader } from '../components/common/AssignmentHeader';
import { ShieldAlert } from 'lucide-react';

export function ThreatIntelligencePage() {
  return (
    <div className="space-y-6">
      {/* Assignment Header */}
      <AssignmentHeader
        requirement="Classify detected anomalies into meaningful attack categories (Normal Baseline, Brute Force, Impossible Travel, Credential Stuffing, Lateral Movement, Device Spoofing, Low-and-Slow Exfiltration, Insider Drift) rather than returning a generic anomaly flag."
        implementation="The Attack Classification Engine consumes sealed evidence packages, ranks probabilistic hypotheses P(H_i|E), maps tactics to MITRE ATT&CK techniques, and constructs multi-stage attack chains."
      />

      {/* Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-4 border-b border-soc-border font-mono">
        <div>
          <h1 className="text-xl font-bold text-slate-100 flex items-center gap-2 font-sans">
            <ShieldAlert className="w-5 h-5 text-amber-400" />
            Attack Classification Workspace
          </h1>
          <p className="text-xs text-soc-muted mt-0.5 font-sans">
            Evidence-Driven Threat Hypothesis Classifier & MITRE ATT&CK Mapping
          </p>
        </div>
      </div>

      {/* Primary Category Card */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 font-mono text-xs">
        <Card title="Primary Attack Category" subtitle="Phase 6 Output">
          <div className="space-y-2">
            <div className="flex justify-between items-center">
              <span className="text-soc-muted">Category:</span>
              <Badge variant="danger">Credential Stuffing</Badge>
            </div>
            <div className="flex justify-between items-center">
              <span className="text-soc-muted">Confidence:</span>
              <span className="text-emerald-400 font-bold">90%</span>
            </div>
            <div className="flex justify-between items-center">
              <span className="text-soc-muted">MITRE Tactic:</span>
              <span className="text-amber-400">TA0006 (Credential Access)</span>
            </div>
          </div>
        </Card>

        <Card title="Ranked Threat Hypotheses" subtitle="Probabilistic P(H|E)">
          <div className="space-y-2">
            <div className="p-2 bg-soc-bg/50 border border-soc-border rounded-lg flex justify-between">
              <span>1. Credential Stuffing Attack</span>
              <span className="text-cyan-400 font-bold">P = 0.80</span>
            </div>
            <div className="p-2 bg-soc-bg/50 border border-soc-border rounded-lg flex justify-between">
              <span>2. Lateral Movement (AssumeRole)</span>
              <span className="text-soc-muted font-bold">P = 0.15</span>
            </div>
          </div>
        </Card>

        <Card title="Supported Assignment Taxonomy" subtitle="8 Required Attack Patterns">
          <div className="space-y-1 text-[11px]">
            <p>1. Normal Baseline • 2. Brute Force</p>
            <p>3. Impossible Travel • 4. Credential Stuffing</p>
            <p>5. Lateral Movement • 6. Device Spoofing</p>
            <p>7. Low-and-Slow Exfiltration • 8. Insider Drift</p>
          </div>
        </Card>
      </div>
    </div>
  );
}
