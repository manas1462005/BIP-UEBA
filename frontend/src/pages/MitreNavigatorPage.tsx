import { useState } from 'react';
import { Card } from '../components/common/Card';
import { Badge } from '../components/common/Badge';
import { Flame } from 'lucide-react';

export function MitreNavigatorPage() {
  const [selectedTech, setSelectedTech] = useState<any>(null);

  const tactics = [
    {
      name: 'Initial Access',
      id: 'TA0001',
      techniques: [{ id: 'T1078.004', name: 'Valid Accounts: Cloud', count: 14, observed: true }]
    },
    {
      name: 'Execution',
      id: 'TA0002',
      techniques: [{ id: 'T1059', name: 'Command & Scripting Interpreter', count: 3, observed: false }]
    },
    {
      name: 'Privilege Escalation',
      id: 'TA0004',
      techniques: [{ id: 'T1548', name: 'Abuse Elevation Mechanism', count: 8, observed: true }]
    },
    {
      name: 'Credential Access',
      id: 'TA0006',
      techniques: [{ id: 'T1110.003', name: 'Password Spraying', count: 22, observed: true }]
    },
    {
      name: 'Exfiltration',
      id: 'TA0010',
      techniques: [{ id: 'T1041', name: 'Exfiltration Over C2 Channel', count: 5, observed: true }]
    }
  ];

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-4 border-b border-soc-border">
        <div>
          <h1 className="text-xl font-bold text-slate-100 flex items-center gap-2">
            <Flame className="w-5 h-5 text-amber-400" />
            MITRE ATT&CK Matrix Navigator
          </h1>
          <p className="text-xs text-soc-muted mt-0.5">
            Interactive matrix visualizing enterprise adversary tactics, technique frequencies, & detection heatmaps
          </p>
        </div>
      </div>

      {/* ATT&CK Matrix Layout */}
      <div className="grid grid-cols-1 md:grid-cols-5 gap-4">
        {tactics.map((tactic) => (
          <div key={tactic.id} className="space-y-2">
            <div className="p-3 bg-soc-header border border-soc-border rounded-xl text-center">
              <span className="text-[10px] text-cyan-400 font-mono block">{tactic.id}</span>
              <span className="text-xs font-bold text-slate-100">{tactic.name}</span>
            </div>

            <div className="space-y-2">
              {tactic.techniques.map((tech) => (
                <button
                  key={tech.id}
                  onClick={() => setSelectedTech(tech)}
                  className={`w-full p-3 text-left rounded-xl border font-mono text-xs transition-all ${
                    tech.observed
                      ? 'bg-red-950/30 border-red-500/40 text-slate-100 hover:bg-red-900/40'
                      : 'bg-soc-panel border-soc-border text-soc-subtle opacity-60'
                  }`}
                >
                  <div className="flex justify-between items-center">
                    <span className="text-[10px] text-cyan-400 font-bold">{tech.id}</span>
                    {tech.observed && <Badge variant="danger">{tech.count} Hits</Badge>}
                  </div>
                  <p className="mt-1 font-semibold text-[11px] leading-tight">{tech.name}</p>
                </button>
              ))}
            </div>
          </div>
        ))}
      </div>

      {/* Drill-down Panel */}
      {selectedTech && (
        <Card title={`Technique Details: ${selectedTech.id}`} subtitle={selectedTech.name}>
          <div className="space-y-2 font-mono text-xs text-slate-200">
            <p><strong>Observed Frequency:</strong> {selectedTech.count} detections across 30 days</p>
            <p><strong>Primary Data Source:</strong> DS0015 (User Account Authentication Logs)</p>
            <p><strong>Mitigation Strategy:</strong> M1032 (Multi-Factor Authentication & Conditional Access)</p>
          </div>
        </Card>
      )}
    </div>
  );
}
