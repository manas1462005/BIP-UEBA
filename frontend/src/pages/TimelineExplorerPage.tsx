import { Card } from '../components/common/Card';
import { Badge } from '../components/common/Badge';
import { Clock } from 'lucide-react';

export function TimelineExplorerPage() {
  const events = [
    { time: '03:14:02 UTC', title: 'SAML SSO Login Attempt', actor: 'alex.smith1@bip.com', type: 'Authentication', impact: 'Off-Hours Login Deviation' },
    { time: '03:14:15 UTC', title: 'MFA Verification Skipped', actor: 'alex.smith1@bip.com', type: 'Trust Warning', impact: 'Untrusted Hardware' },
    { time: '03:15:08 UTC', title: 'AWS Production Console Granted', actor: 'alex.smith1@bip.com', type: 'App Access', impact: 'Mission Critical Target' },
    { time: '03:18:22 UTC', title: 'STS AssumeRole Privilege Elevation', actor: 'alex.smith1@bip.com', type: 'Escalation', impact: 'MITRE T1548' }
  ];

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-4 border-b border-soc-border">
        <div>
          <h1 className="text-xl font-bold text-slate-100 flex items-center gap-2">
            <Clock className="w-5 h-5 text-cyan-400" />
            Chronological Timeline Explorer
          </h1>
          <p className="text-xs text-soc-muted mt-0.5">
            Step-by-step investigation timeline detailing user actions, system responses, & security anomalies
          </p>
        </div>
      </div>

      {/* Timeline Stream */}
      <Card title="Investigation Sequence Stream">
        <div className="space-y-4 font-mono text-xs mt-2">
          {events.map((evt, idx) => (
            <div key={idx} className="flex items-start gap-4 p-3 bg-soc-bg/50 border border-soc-border rounded-xl">
              <div className="w-24 text-cyan-400 font-bold text-[11px] flex-shrink-0">{evt.time}</div>
              <div className="flex-1 space-y-1">
                <div className="flex justify-between items-center">
                  <span className="text-slate-100 font-bold">{evt.title}</span>
                  <Badge variant="info">{evt.type}</Badge>
                </div>
                <p className="text-soc-muted text-[11px]">Actor: {evt.actor}</p>
                <p className="text-amber-400 text-[11px]">Significance: {evt.impact}</p>
              </div>
            </div>
          ))}
        </div>
      </Card>
    </div>
  );
}
