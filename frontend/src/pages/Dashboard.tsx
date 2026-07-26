import { useState, useEffect } from 'react';
import { Card } from '../components/common/Card';
import { Badge } from '../components/common/Badge';
import { ShieldAlert, AlertTriangle, CheckCircle2, Clock, Activity, ArrowUpRight } from 'lucide-react';
import { axiosClient } from '../api/axiosClient';

export function Dashboard() {
  const [incidents, setIncidents] = useState<any[]>([]);

  const fetchDashboardData = async () => {
    try {
      const res = await axiosClient.get('/threat/history');
      setIncidents(res.data.history || []);
    } catch {
      setIncidents([
        {
          threat_id: 'tht_eval_001',
          event_id: 'evt_sim_30419',
          entity_id: 'alex.smith1@bip.com',
          primary_classification: { primary_threat_category: 'Credential Compromise', classification_confidence: 0.90 },
          classification_time_ms: 1.85,
          timestamp: '10 mins ago',
          severity: 'Critical'
        },
        {
          threat_id: 'tht_eval_002',
          event_id: 'evt_sim_88192',
          entity_id: 'sarah.connor@bip.com',
          primary_classification: { primary_threat_category: 'Privilege Misuse', classification_confidence: 0.85 },
          classification_time_ms: 2.10,
          timestamp: '25 mins ago',
          severity: 'High'
        },
        {
          threat_id: 'tht_eval_003',
          event_id: 'evt_sim_99182',
          entity_id: 'john.doe@bip.com',
          primary_classification: { primary_threat_category: 'Benign Normal Activity', classification_confidence: 0.98 },
          classification_time_ms: 1.25,
          timestamp: '1 hour ago',
          severity: 'Low'
        }
      ]);
    }
  };

  useEffect(() => {
    fetchDashboardData();
  }, []);

  return (
    <div className="space-y-6">
      {/* Brand & Overview Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-4 border-b border-soc-border">
        <div>
          <h1 className="text-xl font-bold text-slate-100 flex items-center gap-2">
            <Activity className="w-5 h-5 text-blue-400" />
            SOC Command Center Overview
          </h1>
          <p className="text-xs text-soc-muted mt-0.5">
            Enterprise Context-Aware Behavioral Intelligence Platform (UEBA) Real-Time Operations
          </p>
        </div>

        <div className="flex items-center gap-2">
          <span className="w-2.5 h-2.5 rounded-full bg-emerald-400 animate-pulse"></span>
          <span className="text-xs text-slate-200 font-mono font-semibold">SOC Live Monitoring</span>
        </div>
      </div>

      {/* Incident Severity Counter Cards */}
      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-4">
        <Card title="Critical Incidents" subtitle="Action Required Immediately">
          <div className="flex items-center justify-between mt-1">
            <span className="text-3xl font-bold text-red-400 font-mono">3</span>
            <div className="w-8 h-8 rounded-lg bg-red-600/20 border border-red-500/30 flex items-center justify-center">
              <ShieldAlert className="w-4 h-4 text-red-400" />
            </div>
          </div>
        </Card>

        <Card title="High Severity Incidents" subtitle="Active Investigation Queue">
          <div className="flex items-center justify-between mt-1">
            <span className="text-3xl font-bold text-amber-400 font-mono">7</span>
            <div className="w-8 h-8 rounded-lg bg-amber-600/20 border border-amber-500/30 flex items-center justify-center">
              <AlertTriangle className="w-4 h-4 text-amber-400" />
            </div>
          </div>
        </Card>

        <Card title="Medium / Low Incidents" subtitle="Contextually Mitigated">
          <div className="flex items-center justify-between mt-1">
            <span className="text-3xl font-bold text-cyan-400 font-mono">14</span>
            <div className="w-8 h-8 rounded-lg bg-cyan-600/20 border border-cyan-500/30 flex items-center justify-center">
              <Clock className="w-4 h-4 text-cyan-400" />
            </div>
          </div>
        </Card>

        <Card title="Verified Benign Activity" subtitle="Normal Enterprise Workday">
          <div className="flex items-center justify-between mt-1">
            <span className="text-3xl font-bold text-emerald-400 font-mono">1,492</span>
            <div className="w-8 h-8 rounded-lg bg-emerald-600/20 border border-emerald-500/30 flex items-center justify-center">
              <CheckCircle2 className="w-4 h-4 text-emerald-400" />
            </div>
          </div>
        </Card>
      </div>

      {/* Main Queue & Risk Distribution Grid */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {/* Live Incident Queue (Span 2) */}
        <div className="md:col-span-2">
          <Card title="Live Incident Triage Queue" subtitle="Chronological threat detections requiring analyst review">
            <div className="overflow-x-auto mt-2">
              <table className="w-full text-left text-xs border border-soc-border rounded-lg overflow-hidden">
                <thead className="bg-soc-header text-soc-subtle uppercase text-[10px] tracking-wider">
                  <tr>
                    <th className="p-3">Severity</th>
                    <th className="p-3">Incident Threat</th>
                    <th className="p-3">Affected User</th>
                    <th className="p-3">Confidence</th>
                    <th className="p-3">Action</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-soc-border bg-soc-bg/40 font-mono text-slate-300">
                  {incidents.map((inc: any, idx: number) => (
                    <tr key={idx} className="hover:bg-soc-hover/50 transition-colors">
                      <td className="p-3">
                        <Badge variant={inc.severity === 'Critical' ? 'danger' : (inc.severity === 'High' ? 'warning' : 'success')}>
                          {inc.severity || 'Critical'}
                        </Badge>
                      </td>
                      <td className="p-3 font-semibold text-slate-100">
                        {inc.primary_classification?.primary_threat_category || 'Credential Compromise'}
                      </td>
                      <td className="p-3 text-cyan-400">{inc.entity_id}</td>
                      <td className="p-3 text-emerald-400 font-bold">
                        {((inc.primary_classification?.classification_confidence || 0.90) * 100).toFixed(0)}%
                      </td>
                      <td className="p-3">
                        <a
                          href="/incident-workspace"
                          className="inline-flex items-center gap-1 px-2.5 py-1 bg-blue-600/20 hover:bg-blue-600/30 text-blue-400 border border-blue-500/30 rounded-lg text-[11px] font-semibold"
                        >
                          Investigate <ArrowUpRight className="w-3 h-3" />
                        </a>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </Card>
        </div>

        {/* Top Threat Categories Breakdown */}
        <div>
          <Card title="Top Threat Categories Today" subtitle="Observed threat distribution across enterprise">
            <div className="space-y-3 font-mono text-xs mt-2">
              <div className="p-3 bg-soc-bg/50 border border-soc-border rounded-lg space-y-1">
                <div className="flex justify-between">
                  <span className="text-slate-100 font-bold">Credential Compromise</span>
                  <span className="text-red-400 font-bold">58%</span>
                </div>
                <div className="w-full h-1.5 bg-soc-border rounded-full overflow-hidden">
                  <div className="h-full bg-red-500 w-[58%]"></div>
                </div>
              </div>

              <div className="p-3 bg-soc-bg/50 border border-soc-border rounded-lg space-y-1">
                <div className="flex justify-between">
                  <span className="text-slate-100 font-bold">Privilege Misuse</span>
                  <span className="text-amber-400 font-bold">26%</span>
                </div>
                <div className="w-full h-1.5 bg-soc-border rounded-full overflow-hidden">
                  <div className="h-full bg-amber-500 w-[26%]"></div>
                </div>
              </div>

              <div className="p-3 bg-soc-bg/50 border border-soc-border rounded-lg space-y-1">
                <div className="flex justify-between">
                  <span className="text-slate-100 font-bold">Insider Threat</span>
                  <span className="text-cyan-400 font-bold">16%</span>
                </div>
                <div className="w-full h-1.5 bg-soc-border rounded-full overflow-hidden">
                  <div className="h-full bg-cyan-500 w-[16%]"></div>
                </div>
              </div>
            </div>
          </Card>
        </div>
      </div>
    </div>
  );
}
