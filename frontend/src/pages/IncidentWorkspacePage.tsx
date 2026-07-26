import { useState } from 'react';
import { Card } from '../components/common/Card';
import { Badge } from '../components/common/Badge';
import { CheckSquare, Bookmark, Send } from 'lucide-react';

export function IncidentWorkspacePage() {
  const [activeTab, setActiveTab] = useState<string>('summary');
  const [notes, setNotes] = useState<string>('Initial triage: Identity verification pending via out-of-band communication with engineering manager.');
  const [noteInput, setNoteInput] = useState<string>('');

  const handleAddNote = () => {
    if (!noteInput.trim()) return;
    setNotes((prev) => `${prev}\n\n[Analyst Note]: ${noteInput}`);
    setNoteInput('');
  };

  return (
    <div className="space-y-6">
      {/* Workspace Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-4 border-b border-soc-border">
        <div>
          <div className="flex items-center gap-2">
            <Badge variant="danger">CRITICAL SEVERITY</Badge>
            <span className="text-xs font-mono text-cyan-400 font-bold">INC-2026-081</span>
            <span className="text-xs text-soc-muted">• Assigned to SOC Tier 2 Analyst</span>
          </div>
          <h1 className="text-xl font-bold text-slate-100 mt-1">
            Off-Hours Credential Theft & Password Spray Attack Investigation
          </h1>
        </div>

        <div className="flex items-center gap-2">
          <button className="flex items-center gap-1.5 px-3 py-1.5 bg-soc-border/40 hover:bg-soc-border text-slate-200 rounded-xl text-xs font-semibold">
            <Bookmark className="w-3.5 h-3.5 text-amber-400" /> Bookmark Case
          </button>
          <button className="flex items-center gap-1.5 px-3 py-1.5 bg-emerald-600 hover:bg-emerald-500 text-white rounded-xl text-xs font-semibold shadow-lg">
            Resolve Incident
          </button>
        </div>
      </div>

      {/* Tab Navigation Menu */}
      <div className="flex border-b border-soc-border gap-2 text-xs font-semibold">
        <button
          onClick={() => setActiveTab('summary')}
          className={`pb-3 px-4 transition-all ${activeTab === 'summary' ? 'text-blue-400 border-b-2 border-blue-400' : 'text-soc-muted hover:text-slate-200'}`}
        >
          Executive & Technical Summary
        </button>
        <button
          onClick={() => setActiveTab('trace')}
          className={`pb-3 px-4 transition-all ${activeTab === 'trace' ? 'text-blue-400 border-b-2 border-blue-400' : 'text-soc-muted hover:text-slate-200'}`}
        >
          Reasoning Trace & Detectors
        </button>
        <button
          onClick={() => setActiveTab('mitre')}
          className={`pb-3 px-4 transition-all ${activeTab === 'mitre' ? 'text-blue-400 border-b-2 border-blue-400' : 'text-soc-muted hover:text-slate-200'}`}
        >
          MITRE & Attack Chain
        </button>
        <button
          onClick={() => setActiveTab('actions')}
          className={`pb-3 px-4 transition-all ${activeTab === 'actions' ? 'text-blue-400 border-b-2 border-blue-400' : 'text-soc-muted hover:text-slate-200'}`}
        >
          Analyst Action Checklist & Notes
        </button>
      </div>

      {/* Tab 1: Executive & Technical Summary */}
      {activeTab === 'summary' && (
        <div className="space-y-6">
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            <Card title="Executive Summary" subtitle="Business Impact">
              <div className="space-y-2 text-xs font-mono text-slate-200">
                <p><strong>What Happened:</strong> Off-hours security anomaly detected involving user alex.smith1@bip.com accessing AWS Production Console.</p>
                <p className="text-amber-400"><strong>Business Impact:</strong> High Impact: Potential unauthorized access to production cloud infrastructure.</p>
                <p><strong>Affected User:</strong> alex.smith1@bip.com (Engineering)</p>
              </div>
            </Card>

            <Card title="Technical Investigation Narrative" subtitle="Grounding Report">
              <div className="p-3 bg-soc-bg/50 border border-soc-border rounded-lg text-xs font-mono text-slate-200">
                StatisticalDetector recorded Modified Z-Score deviation of 0.850. Trust reasoning identified unmanaged hardware without SAML2.0 MFA.
              </div>
            </Card>

            <Card title="Threat Classification & Confidence" subtitle="Phase 6 Output">
              <div className="space-y-2 text-xs font-mono">
                <div className="flex justify-between">
                  <span className="text-soc-muted">Primary Category:</span>
                  <span className="text-red-400 font-bold">Credential Compromise</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-soc-muted">Classification Confidence:</span>
                  <span className="text-emerald-400 font-bold">90%</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-soc-muted">Hybrid Anomaly Score:</span>
                  <span className="text-cyan-400 font-bold">0.825</span>
                </div>
              </div>
            </Card>
          </div>
        </div>
      )}

      {/* Tab 2: Reasoning Trace & Detectors */}
      {activeTab === 'trace' && (
        <Card title="Machine-Readable Reasoning Trace" subtitle="Step-by-step contextual reasoning logs">
          <div className="overflow-x-auto">
            <table className="w-full text-left text-xs border border-soc-border rounded-lg overflow-hidden font-mono">
              <thead className="bg-soc-header text-soc-subtle uppercase text-[10px]">
                <tr>
                  <th className="p-3">Step</th>
                  <th className="p-3">Reasoning Factor</th>
                  <th className="p-3">Evaluation Result</th>
                  <th className="p-3">Impact</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-soc-border bg-soc-bg/40 text-slate-300">
                <tr>
                  <td className="p-3 text-cyan-400 font-bold">Step 1</td>
                  <td className="p-3 font-semibold text-slate-100">Hybrid Anomaly Input</td>
                  <td className="p-3">Raw Ensemble Score: 0.825</td>
                  <td className="p-3"><Badge variant="danger">Anomaly Input</Badge></td>
                </tr>
                <tr>
                  <td className="p-3 text-cyan-400 font-bold">Step 2</td>
                  <td className="p-3 font-semibold text-slate-100">Trust Reasoning</td>
                  <td className="p-3">Unmanaged Endpoint + MFA Bypass</td>
                  <td className="p-3"><Badge variant="danger">Amplifies Identity Risk</Badge></td>
                </tr>
                <tr>
                  <td className="p-3 text-cyan-400 font-bold">Step 3</td>
                  <td className="p-3 font-semibold text-slate-100">Calendar Reasoning</td>
                  <td className="p-3">Unscheduled Off-Hours Activity</td>
                  <td className="p-3"><Badge variant="warning">Amplifies Temporal Risk</Badge></td>
                </tr>
              </tbody>
            </table>
          </div>
        </Card>
      )}

      {/* Tab 3: MITRE & Attack Chain */}
      {activeTab === 'mitre' && (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <Card title="MITRE ATT&CK Mapping" subtitle="Framework IDs">
            <div className="space-y-2 font-mono text-xs">
              <div className="p-3 bg-soc-bg/50 border border-soc-border rounded-lg">
                <div className="flex justify-between">
                  <span className="text-cyan-400 font-bold">T1110.003</span>
                  <Badge variant="warning">Credential Access</Badge>
                </div>
                <p className="text-slate-100 font-semibold mt-1">Password Spraying</p>
                <p className="text-soc-muted text-[11px]">Mitigation: M1032 (Multi-Factor Authentication)</p>
              </div>
            </div>
          </Card>

          <Card title="Multi-Stage Attack Chain" subtitle="Temporal Progression">
            <div className="space-y-2 font-mono text-xs">
              <div className="p-3 bg-soc-bg/50 border border-soc-border rounded-lg flex items-center gap-3">
                <div className="w-6 h-6 rounded-full bg-blue-600/20 text-cyan-400 font-bold flex items-center justify-center text-xs">1</div>
                <div>
                  <p className="text-slate-100 font-bold">Initial Access (T1078 Valid Accounts)</p>
                  <p className="text-soc-muted text-[11px]">Confidence: 90%</p>
                </div>
              </div>
            </div>
          </Card>
        </div>
      )}

      {/* Tab 4: Analyst Actions & Notes */}
      {activeTab === 'actions' && (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <Card title="Recommended Analyst Actions" subtitle="Action Checklist">
            <div className="space-y-2 font-mono text-xs">
              <div className="p-3 bg-soc-bg/50 border border-soc-border rounded-lg flex items-center gap-3">
                <CheckSquare className="w-4 h-4 text-emerald-400" />
                <span className="text-slate-100 font-semibold">Verify user identity for alex.smith1@bip.com via out-of-band channel</span>
              </div>
              <div className="p-3 bg-soc-bg/50 border border-soc-border rounded-lg flex items-center gap-3">
                <CheckSquare className="w-4 h-4 text-emerald-400" />
                <span className="text-slate-100 font-semibold">Revoke active SAML SSO sessions and force password reset</span>
              </div>
            </div>
          </Card>

          <Card title="Analyst Investigation Notes" subtitle="Internal Triage Log">
            <div className="space-y-3">
              <div className="p-3 bg-soc-bg/50 border border-soc-border rounded-lg text-xs font-mono text-slate-200 whitespace-pre-wrap h-36 overflow-y-auto">
                {notes}
              </div>

              <div className="flex gap-2">
                <input
                  type="text"
                  value={noteInput}
                  onChange={(e) => setNoteInput(e.target.value)}
                  onKeyDown={(e) => e.key === 'Enter' && handleAddNote()}
                  placeholder="Add triage note..."
                  className="flex-1 bg-soc-bg border border-soc-border rounded-xl px-3 py-2 text-xs text-slate-100 focus:outline-none focus:border-blue-500 font-mono"
                />
                <button onClick={handleAddNote} className="px-3 py-2 bg-blue-600 text-white rounded-xl text-xs font-semibold flex items-center gap-1">
                  <Send className="w-3.5 h-3.5" /> Save
                </button>
              </div>
            </div>
          </Card>
        </div>
      )}
    </div>
  );
}
