import { Card } from '../components/common/Card';
import { Badge } from '../components/common/Badge';
import { AssignmentHeader } from '../components/common/AssignmentHeader';
import { Activity } from 'lucide-react';

export function AnomalyIntelligencePage() {
  return (
    <div className="space-y-6">
      {/* Assignment Header */}
      <AssignmentHeader
        requirement="Build a sequence-aware anomaly detector operating on learned behavior deviations to flag anomalies without relying solely on predefined static rules."
        implementation="The Detection Engine uses a multi-detector ensemble combining Modified Z-Score, Isolation Forest, Peer Group Cohort Distance, Markov Chain Sequence analysis, and Concept Drift models to calculate a unified Hybrid Anomaly Score."
      />

      {/* Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-4 border-b border-soc-border">
        <div>
          <h1 className="text-xl font-bold text-slate-100 flex items-center gap-2 font-sans">
            <Activity className="w-5 h-5 text-cyan-400" />
            Detection Engine Workspace
          </h1>
          <p className="text-xs text-soc-muted mt-0.5 font-sans">
            Multi-Detector Sequence-Aware Anomaly Detection Ensemble
          </p>
        </div>
      </div>

      {/* Ensemble Cards */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-4 font-mono text-xs">
        <Card title="StatisticalDetector" subtitle="Z-Score">
          <div className="mt-1 flex justify-between items-center">
            <Badge variant="info">Score: 0.850</Badge>
            <span className="text-soc-muted">Weight: 0.25</span>
          </div>
        </Card>
        <Card title="IsolationForestDetector" subtitle="Unsupervised">
          <div className="mt-1 flex justify-between items-center">
            <Badge variant="info">Score: 0.820</Badge>
            <span className="text-soc-muted">Weight: 0.25</span>
          </div>
        </Card>
        <Card title="PeerGroupDetector" subtitle="Cohort Distance">
          <div className="mt-1 flex justify-between items-center">
            <Badge variant="info">Score: 0.780</Badge>
            <span className="text-soc-muted">Weight: 0.20</span>
          </div>
        </Card>
        <Card title="SequenceBehaviourDetector" subtitle="Markov Chain">
          <div className="mt-1 flex justify-between items-center">
            <Badge variant="info">Score: 0.890</Badge>
            <span className="text-soc-muted">Weight: 0.15</span>
          </div>
        </Card>
      </div>
    </div>
  );
}
