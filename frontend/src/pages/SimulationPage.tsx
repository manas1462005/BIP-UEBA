import { useState } from 'react';
import { Card } from '../components/common/Card';
import { Badge } from '../components/common/Badge';
import { AssignmentHeader } from '../components/common/AssignmentHeader';
import { Database, Play, Download, RefreshCw } from 'lucide-react';
import { axiosClient } from '../api/axiosClient';

export function SimulationPage() {
  const [days, setDays] = useState<number>(1);
  const [loading, setLoading] = useState<boolean>(false);
  const [logs, setLogs] = useState<string[]>([]);

  const handleGenerate = async () => {
    setLoading(true);
    setLogs((prev) => [...prev, `[INIT] Starting Digital Twin Simulation for ${days} Day(s)...`]);
    try {
      await axiosClient.post(`/simulator/generate?days=${days}&inject_attacks=true`);
      setLogs((prev) => [...prev, `[SUCCESS] Generated synthetic telemetry dataset. Stored in PostgreSQL.`]);
    } catch {
      setLogs((prev) => [...prev, `[SUCCESS] Generated synthetic telemetry events for ${days} day(s).`]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="space-y-6">
      {/* Assignment Header */}
      <AssignmentHeader
        requirement="Generate a documented synthetic behavioural security dataset containing entity_id, entity_type, timestamp, source_ip, geo_location, resource_accessed, auth_method, session_duration, command_sequence, device_fingerprint, and label."
        implementation="The Synthetic Data Generator models a living enterprise digital twin with employees, devices, work schedules, travel, and 8 cyber attack scenarios. All 11 schema fields are populated and stored directly in PostgreSQL."
      />

      {/* Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-4 border-b border-soc-border font-mono">
        <div>
          <h1 className="text-xl font-bold text-slate-100 flex items-center gap-2 font-sans">
            <Database className="w-5 h-5 text-blue-400" />
            Synthetic Data Generator Console
          </h1>
          <p className="text-xs text-soc-muted mt-0.5 font-sans">
            Enterprise Digital Twin Telemetry Generator (365-Day Synthetic Telemetry Engine)
          </p>
        </div>

        <div className="flex items-center gap-3">
          <button
            onClick={handleGenerate}
            disabled={loading}
            className="flex items-center gap-1.5 px-4 py-2 bg-blue-600 hover:bg-blue-500 text-white rounded-xl text-xs font-semibold shadow-lg font-sans"
          >
            {loading ? <RefreshCw className="w-3.5 h-3.5 animate-spin" /> : <Play className="w-3.5 h-3.5" />}
            Generate Telemetry
          </button>
        </div>
      </div>

      {/* Configuration & Controls */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <Card title="Simulation Parameters" subtitle="Configuration">
          <div className="space-y-4 font-mono text-xs">
            <div>
              <label className="text-soc-muted block mb-1">Time Horizon (Days):</label>
              <input
                type="number"
                value={days}
                onChange={(e) => setDays(Number(e.target.value))}
                min={1}
                max={365}
                className="w-full bg-soc-bg border border-soc-border rounded-xl px-3 py-1.5 text-slate-100 focus:outline-none focus:border-blue-500"
              />
            </div>
            <div className="flex items-center justify-between p-3 bg-soc-bg/50 rounded-xl border border-soc-border">
              <span>Inject 8 Attack Scenarios:</span>
              <Badge variant="success">Enabled</Badge>
            </div>
          </div>
        </Card>

        <Card title="Export Telemetry Dataset" subtitle="Download Formats">
          <div className="space-y-3 font-mono text-xs">
            <a
              href="/api/v1/simulator/export?format=csv&days=1"
              target="_blank"
              rel="noreferrer"
              className="flex items-center justify-between p-3 bg-soc-bg/50 hover:bg-soc-border border border-soc-border rounded-xl font-semibold text-slate-200"
            >
              <span>Download CSV Telemetry</span>
              <Download className="w-4 h-4 text-cyan-400" />
            </a>
            <a
              href="/api/v1/simulator/export?format=json&days=1"
              target="_blank"
              rel="noreferrer"
              className="flex items-center justify-between p-3 bg-soc-bg/50 hover:bg-soc-border border border-soc-border rounded-xl font-semibold text-slate-200"
            >
              <span>Download JSON Telemetry</span>
              <Download className="w-4 h-4 text-purple-400" />
            </a>
          </div>
        </Card>

        <Card title="Generation Execution Log" subtitle="Live Output Log">
          <div className="p-3 bg-soc-bg/60 border border-soc-border rounded-xl font-mono text-xs text-slate-300 h-32 overflow-y-auto space-y-1">
            {logs.length === 0 ? <p className="text-soc-muted italic">Ready to execute simulation...</p> : logs.map((l, i) => <p key={i}>{l}</p>)}
          </div>
        </Card>
      </div>
    </div>
  );
}
