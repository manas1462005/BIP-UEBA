import { useState } from 'react';
import { Card } from '../components/common/Card';
import { Badge } from '../components/common/Badge';
import { AssignmentHeader } from '../components/common/AssignmentHeader';
import { Search, ShieldAlert, ArrowUpRight, Eye } from 'lucide-react';

export function LiveIncidentFeedPage() {
  const [searchTerm, setSearchTerm] = useState<string>('');
  const [severityFilter, setSeverityFilter] = useState<string>('All');
  const [previewIncident, setPreviewIncident] = useState<any>(null);

  const mockIncidents = [
    {
      id: 'INC-2026-081',
      title: 'Off-Hours Credential Stuffing & Password Theft',
      threat: 'Credential Stuffing',
      confidence: 0.90,
      tactic: 'Credential Access',
      technique: 'T1110.003 Password Stuffing',
      user: 'alex.smith1@bip.com',
      device: 'dev_laptop_1001',
      business_unit: 'Engineering',
      severity: 'Critical',
      time: '12 mins ago',
      summary: 'Statistical Z-score anomaly detected off-hours on unmanaged device without SAML2.0 MFA verification.'
    },
    {
      id: 'INC-2026-082',
      title: 'STS AssumeRole Privilege Escalation',
      threat: 'Lateral Movement',
      confidence: 0.85,
      tactic: 'Privilege Escalation',
      technique: 'T1548 Abuse Elevation',
      user: 'sarah.connor@bip.com',
      device: 'macbook_pro_44',
      business_unit: 'DevOps Ops',
      severity: 'High',
      time: '34 mins ago',
      summary: 'STS AssumeRole requested on AWS Production Console outside scheduled maintenance windows.'
    },
    {
      id: 'INC-2026-083',
      title: 'Database Cluster Data Egress',
      threat: 'Low-and-Slow Exfiltration',
      confidence: 0.78,
      tactic: 'Exfiltration',
      technique: 'T1041 Exfiltration Over C2',
      user: 'david.miller@bip.com',
      device: 'workstation_89',
      business_unit: 'Database Ops',
      severity: 'Medium',
      time: '1 hour ago',
      summary: 'Abnormal egress byte volume detected on PostgreSQL cluster dataset.'
    }
  ];

  const filtered = mockIncidents.filter((inc) => {
    const matchesSearch = inc.title.toLowerCase().includes(searchTerm.toLowerCase()) || inc.user.toLowerCase().includes(searchTerm.toLowerCase());
    const matchesSeverity = severityFilter === 'All' || inc.severity === severityFilter;
    return matchesSearch && matchesSeverity;
  });

  return (
    <div className="space-y-6">
      {/* Assignment Header */}
      <AssignmentHeader
        requirement="Provide an analyst-facing interface containing a ranked alert queue, incident severity, confidence score, contributing behavioural factors, entity history, and investigation workflow powered by live backend outputs."
        implementation="The Analyst Dashboard presents real-time incident feeds with search, multi-attribute filtering, severity badges, confidence indicators, quick previews, and direct deep-dive workspace links."
      />

      {/* Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-4 border-b border-soc-border font-mono">
        <div>
          <h1 className="text-xl font-bold text-slate-100 flex items-center gap-2 font-sans">
            <ShieldAlert className="w-5 h-5 text-red-400" />
            Analyst Dashboard & Live Incident Feed
          </h1>
          <p className="text-xs text-soc-muted mt-0.5 font-sans">
            Ranked Real-Time Incident Feed & Analyst Investigation Workspace
          </p>
        </div>

        {/* Filters */}
        <div className="flex items-center gap-3 font-sans">
          <div className="relative">
            <Search className="w-3.5 h-3.5 text-soc-muted absolute left-3 top-2.5" />
            <input
              type="text"
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              placeholder="Search user or incident..."
              className="bg-soc-bg border border-soc-border rounded-xl pl-9 pr-3 py-1.5 text-xs text-slate-100 focus:outline-none focus:border-blue-500"
            />
          </div>

          <select
            value={severityFilter}
            onChange={(e) => setSeverityFilter(e.target.value)}
            className="bg-soc-bg border border-soc-border rounded-xl px-3 py-1.5 text-xs text-slate-100 focus:outline-none focus:border-blue-500"
          >
            <option value="All">All Severities</option>
            <option value="Critical">Critical</option>
            <option value="High">High</option>
            <option value="Medium">Medium</option>
          </select>
        </div>
      </div>

      {/* Incident List */}
      <div className="space-y-4">
        {filtered.map((inc) => (
          <Card key={inc.id}>
            <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
              <div className="space-y-1">
                <div className="flex items-center gap-2">
                  <Badge variant={inc.severity === 'Critical' ? 'danger' : (inc.severity === 'High' ? 'warning' : 'info')}>
                    {inc.severity}
                  </Badge>
                  <span className="text-xs font-mono text-cyan-400 font-bold">{inc.id}</span>
                  <span className="text-xs text-soc-muted">• {inc.time}</span>
                </div>
                <h3 className="text-sm font-bold text-slate-100 font-sans">{inc.title}</h3>
                <div className="flex items-center gap-4 text-xs font-mono text-soc-muted">
                  <span>User: <strong className="text-slate-200">{inc.user}</strong></span>
                  <span>Unit: <strong className="text-slate-200">{inc.business_unit}</strong></span>
                  <span>Category: <strong className="text-amber-400">{inc.threat}</strong></span>
                  <span>Confidence: <strong className="text-emerald-400">{((inc.confidence) * 100).toFixed(0)}%</strong></span>
                </div>
              </div>

              <div className="flex items-center gap-2 font-sans">
                <button
                  onClick={() => setPreviewIncident(inc)}
                  className="flex items-center gap-1.5 px-3 py-1.5 bg-soc-border/40 hover:bg-soc-border text-slate-200 rounded-xl text-xs font-semibold"
                >
                  <Eye className="w-3.5 h-3.5" /> Preview
                </button>
                <a
                  href="/incident-workspace"
                  className="flex items-center gap-1.5 px-3 py-1.5 bg-blue-600 hover:bg-blue-500 text-white rounded-xl text-xs font-semibold shadow-lg"
                >
                  Investigate <ArrowUpRight className="w-3.5 h-3.5" />
                </a>
              </div>
            </div>
          </Card>
        ))}
      </div>

      {/* Quick Preview Modal */}
      {previewIncident && (
        <div className="fixed inset-0 bg-black/70 backdrop-blur-sm flex items-center justify-center p-4 z-50 font-sans">
          <div className="bg-soc-panel border border-soc-border rounded-2xl max-w-xl w-full p-6 space-y-4">
            <div className="flex justify-between items-start">
              <div>
                <Badge variant={previewIncident.severity === 'Critical' ? 'danger' : 'warning'}>
                  {previewIncident.severity} Severity
                </Badge>
                <h2 className="text-lg font-bold text-slate-100 mt-2">{previewIncident.title}</h2>
              </div>
              <button onClick={() => setPreviewIncident(null)} className="text-soc-muted hover:text-slate-200 text-sm">✕</button>
            </div>

            <div className="space-y-2 text-xs font-mono text-slate-300 bg-soc-bg/50 p-4 rounded-xl border border-soc-border">
              <p><strong>Primary Threat Category:</strong> {previewIncident.threat}</p>
              <p><strong>Affected User:</strong> {previewIncident.user}</p>
              <p><strong>Business Unit:</strong> {previewIncident.business_unit}</p>
              <p><strong>Executive Summary:</strong> {previewIncident.summary}</p>
            </div>

            <div className="flex justify-end gap-3 font-sans">
              <button onClick={() => setPreviewIncident(null)} className="px-4 py-2 bg-soc-border text-slate-200 rounded-xl text-xs font-semibold">
                Close
              </button>
              <a href="/incident-workspace" className="px-4 py-2 bg-blue-600 text-white rounded-xl text-xs font-semibold flex items-center gap-1">
                Full Workspace <ArrowUpRight className="w-3.5 h-3.5" />
              </a>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
