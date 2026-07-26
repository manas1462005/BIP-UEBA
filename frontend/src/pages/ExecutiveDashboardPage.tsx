import { Card } from '../components/common/Card';
import { Badge } from '../components/common/Badge';
import { ShieldCheck } from 'lucide-react';

export function ExecutiveDashboardPage() {
  return (
    <div className="space-y-6">
      {/* CISO Executive Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-4 border-b border-soc-border">
        <div>
          <h1 className="text-xl font-bold text-slate-100 flex items-center gap-2">
            <ShieldCheck className="w-5 h-5 text-emerald-400" />
            CISO Executive Security Posture Dashboard
          </h1>
          <p className="text-xs text-soc-muted mt-0.5">
            High-level executive security metrics, department risk heatmaps, & business unit compliance snapshots
          </p>
        </div>

        <div className="flex items-center gap-2">
          <Badge variant="success">Posture Index: 92/100 (Strong)</Badge>
        </div>
      </div>

      {/* High-Level CISO Metrics */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
        <Card title="Overall Posture Score" subtitle="Enterprise Security Index">
          <div className="text-2xl font-bold text-emerald-400 font-mono">92.4 / 100</div>
        </Card>
        <Card title="Mean Time To Resolve" subtitle="SLA Performance">
          <div className="text-2xl font-bold text-cyan-400 font-mono">14.2 mins</div>
        </Card>
        <Card title="Critical Assets At Risk" subtitle="Mission Critical Targets">
          <div className="text-2xl font-bold text-amber-400 font-mono">2 Systems</div>
        </Card>
        <Card title="Policy Compliance Rate" subtitle="RBAC & JIT Alignment">
          <div className="text-2xl font-bold text-slate-200 font-mono">98.6%</div>
        </Card>
      </div>

      {/* Department Risk Heatmap & Business Unit Breakdown */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <Card title="Department Risk Heatmap" subtitle="Risk Index across organizational units">
          <div className="space-y-3 font-mono text-xs">
            <div className="p-3 bg-soc-bg/50 border border-soc-border rounded-lg flex justify-between items-center">
              <span className="text-slate-100 font-bold">Engineering Department</span>
              <Badge variant="danger">Risk Score: 78 (High)</Badge>
            </div>
            <div className="p-3 bg-soc-bg/50 border border-soc-border rounded-lg flex justify-between items-center">
              <span className="text-slate-100 font-bold">DevOps Infrastructure</span>
              <Badge variant="warning">Risk Score: 45 (Moderate)</Badge>
            </div>
            <div className="p-3 bg-soc-bg/50 border border-soc-border rounded-lg flex justify-between items-center">
              <span className="text-slate-100 font-bold">Human Resources</span>
              <Badge variant="success">Risk Score: 12 (Low)</Badge>
            </div>
          </div>
        </Card>

        <Card title="Executive Summary Highlights" subtitle="Monthly Threat Trends">
          <div className="space-y-2 font-mono text-xs text-slate-200">
            <p>• <strong>Credential Compromise</strong> accounts for 58% of all high-severity alerts this month.</p>
            <p>• <strong>Context Intelligence Engine</strong> successfully suppressed 142 false-positive alerts during Release Deployment Windows.</p>
            <p>• Zero unmitigated exfiltration incidents recorded.</p>
          </div>
        </Card>
      </div>
    </div>
  );
}
