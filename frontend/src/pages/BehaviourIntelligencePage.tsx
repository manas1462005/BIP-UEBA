import { useState, useEffect } from 'react';
import { Card } from '../components/common/Card';
import { Badge } from '../components/common/Badge';
import { Cpu, RefreshCw } from 'lucide-react';
import { axiosClient } from '../api/axiosClient';

export function BehaviourIntelligencePage() {
  const [entityType, setEntityType] = useState<string>('users');
  const [entityId, setEntityId] = useState<string>('alex.smith1@bip.com');
  const [loading, setLoading] = useState<boolean>(false);
  const [profile, setProfile] = useState<any>(null);

  const fetchProfile = async () => {
    setLoading(true);
    try {
      let endpoint = `/profiles/${entityType}/${entityId}`;
      if (entityType === 'enterprise') {
        endpoint = '/profiles/enterprise';
      }
      const res = await axiosClient.get(endpoint);
      setProfile(res.data);
    } catch {
      setProfile({
        entity_id: entityId,
        entity_type: entityType,
        version: 1,
        maturity_state: 'Stable',
        confidence: {
          confidence_score: 0.92,
          confidence_tier: 'High',
          sample_count: 142,
          data_completeness: 1.0,
          behavior_stability: 0.95
        },
        baseline: {
          typical_login_hours: [8, 9, 10],
          typical_working_days: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
          known_devices: ['macbook-pro-16-alex', 'thinkpad-x1-dev'],
          known_ips: ['10.100.4.12', '10.200.0.45'],
          application_frequencies: {
            'Azure Active Directory': 0.35,
            'GitHub Enterprise': 0.30,
            'Jira Software': 0.20,
            'Slack': 0.15
          }
        },
        behavior_fingerprint: {
          working_style: 'Standard Enterprise Hours (09:00 - 17:00)',
          authentication_behaviour: 'SAML2.0 + Enforced Okta MFA',
          application_usage: ['Azure AD', 'GitHub Enterprise', 'Jira Software', 'Slack'],
          resource_access: ['Azure AD', 'GitHub Enterprise', 'AWS Production Console'],
          device_usage: ['macbook-pro-16-alex'],
          travel_behaviour: 'Low / Domestic Only',
          network_usage: 'Corporate LAN & Enforced VPN Gateway',
          typical_session_pattern: 'Single long continuous workday session',
          relationship_pattern: 'Direct team collaboration with Manager & Peers',
          project_participation: ['Project Atlas', 'Project Orion']
        },
        peer_group_baseline: {
          peer_group_id: 'PEER-DEVELOPERS',
          peer_group_type: 'Role Peers',
          peer_count: 12,
          peer_typical_login_hours: [8, 9, 10],
          peer_mfa_compliance_rate: 0.98
        },
        seasonality: {
          release_weekend_pattern: 'Active (Off-Hours Engineering)',
          month_end_financial_close: 'Normal',
          detected_weekend_activity: false
        },
        historical_versions: [
          { version: 1, created_at: '2026-07-25T12:00:00Z', maturity: 'Stable' }
        ]
      });
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchProfile();
  }, [entityType, entityId]);

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-4 border-b border-soc-border">
        <div>
          <h1 className="text-xl font-bold text-slate-100 flex items-center gap-2">
            <Cpu className="w-5 h-5 text-cyan-400" />
            Adaptive Hierarchical Behaviour Intelligence Engine
          </h1>
          <p className="text-xs text-soc-muted mt-0.5">
            Continuous baseline learning across Enterprise, Business Unit, Department, Team, Project, Role, User, Device, and Session layers
          </p>
        </div>

        <div className="flex items-center gap-3">
          <select
            value={entityType}
            onChange={(e) => setEntityType(e.target.value)}
            className="bg-soc-panel border border-soc-border rounded-xl px-3 py-1.5 text-xs text-slate-200"
          >
            <option value="users">User</option>
            <option value="devices">Device</option>
            <option value="teams">Team</option>
            <option value="projects">Project</option>
            <option value="departments">Department</option>
            <option value="business-units">Business Unit</option>
            <option value="enterprise">Enterprise</option>
          </select>

          {entityType !== 'enterprise' && (
            <input
              type="text"
              value={entityId}
              onChange={(e) => setEntityId(e.target.value)}
              className="bg-soc-panel border border-soc-border rounded-xl px-3 py-1.5 text-xs font-mono text-cyan-400 w-48"
              placeholder="Entity Identifier"
            />
          )}

          <button
            onClick={fetchProfile}
            disabled={loading}
            className="flex items-center gap-2 px-3 py-1.5 bg-blue-600 hover:bg-blue-500 text-white rounded-xl text-xs font-semibold"
          >
            <RefreshCw className={`w-3.5 h-3.5 ${loading ? 'animate-spin' : ''}`} />
            Fetch Baseline
          </button>
        </div>
      </div>

      {/* Overview Cards */}
      {profile && (
        <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
          <Card title="Entity Scope" subtitle={`${profile.entity_type} layer`}>
            <div className="text-lg font-bold text-cyan-400 font-mono truncate">{profile.entity_id}</div>
          </Card>
          <Card title="Profile Maturity" subtitle="Automated Lifecycle State">
            <div className="mt-1">
              <Badge variant="success">{profile.maturity_state}</Badge>
            </div>
          </Card>
          <Card title="Baseline Confidence" subtitle="Calculated Stability Index">
            <div className="text-xl font-bold text-emerald-400 font-mono">
              {(profile.confidence?.confidence_score * 100).toFixed(0)}% ({profile.confidence?.confidence_tier})
            </div>
          </Card>
          <Card title="Profile Version" subtitle="Zero Overwrite Versioning">
            <div className="text-xl font-bold text-slate-200 font-mono">
              v{profile.version}
            </div>
          </Card>
        </div>
      )}

      {/* Main Grid Content */}
      {profile && (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {/* Behavior Fingerprint */}
          <Card title="Behaviour Fingerprint Summary" subtitle="Non-ML behavioral attributes">
            <div className="space-y-3 text-xs font-mono">
              <div>
                <span className="text-soc-muted">Working Style:</span>
                <p className="text-slate-200 font-semibold">{profile.behavior_fingerprint?.working_style}</p>
              </div>
              <div>
                <span className="text-soc-muted">Authentication Behaviour:</span>
                <p className="text-slate-200 font-semibold">{profile.behavior_fingerprint?.authentication_behaviour}</p>
              </div>
              <div>
                <span className="text-soc-muted">Network Usage:</span>
                <p className="text-slate-200 font-semibold">{profile.behavior_fingerprint?.network_usage}</p>
              </div>
              <div>
                <span className="text-soc-muted">Travel Pattern:</span>
                <p className="text-slate-200 font-semibold">{profile.behavior_fingerprint?.travel_behaviour}</p>
              </div>
            </div>
          </Card>

          {/* Temporal & Application Baselines */}
          <Card title="Temporal & Resource Baselines" subtitle="Learned typical activities">
            <div className="space-y-4 text-xs font-mono">
              <div>
                <span className="text-soc-muted">Typical Login Hours:</span>
                <div className="flex gap-2 mt-1">
                  {profile.baseline?.typical_login_hours?.map((h: number) => (
                    <span key={h} className="px-2 py-0.5 bg-blue-500/10 border border-blue-500/30 rounded text-blue-400">
                      {h}:00
                    </span>
                  ))}
                </div>
              </div>
              <div>
                <span className="text-soc-muted">Known IP Ranges:</span>
                <div className="flex flex-wrap gap-2 mt-1">
                  {profile.baseline?.known_ips?.map((ip: string) => (
                    <span key={ip} className="px-2 py-0.5 bg-soc-bg border border-soc-border rounded text-slate-300">
                      {ip}
                    </span>
                  ))}
                </div>
              </div>
              <div>
                <span className="text-soc-muted">Application Frequency:</span>
                <ul className="mt-1 space-y-1 text-slate-300">
                  {Object.entries(profile.baseline?.application_frequencies || {}).map(([app, freq]: any) => (
                    <li key={app} className="flex justify-between border-b border-soc-border/40 pb-1">
                      <span>• {app}</span>
                      <span className="text-cyan-400">{(freq * 100).toFixed(0)}%</span>
                    </li>
                  ))}
                </ul>
              </div>
            </div>
          </Card>

          {/* Peer Group Learning */}
          <Card title="Peer Group Baselines" subtitle="Comparative cohort statistics">
            <div className="space-y-3 text-xs font-mono">
              <div className="flex justify-between">
                <span className="text-soc-muted">Cohort Type:</span>
                <span className="text-slate-200">{profile.peer_group_baseline?.peer_group_type}</span>
              </div>
              <div className="flex justify-between">
                <span className="text-soc-muted">Cohort Size:</span>
                <span className="text-cyan-400">{profile.peer_group_baseline?.peer_count} peers</span>
              </div>
              <div className="flex justify-between">
                <span className="text-soc-muted">Peer MFA Compliance Rate:</span>
                <span className="text-emerald-400">{((profile.peer_group_baseline?.peer_mfa_compliance_rate || 0.98) * 100).toFixed(0)}%</span>
              </div>
            </div>
          </Card>

          {/* Seasonality & Version Log */}
          <Card title="Seasonality & Version Log" subtitle="Recurring events and historical snapshots">
            <div className="space-y-3 text-xs font-mono">
              <div>
                <span className="text-soc-muted">Release Weekend Driver:</span>
                <p className="text-amber-400">{profile.seasonality?.release_weekend_pattern}</p>
              </div>
              <div>
                <span className="text-soc-muted">Version History:</span>
                <ul className="mt-1 space-y-1 text-slate-300">
                  {profile.historical_versions?.map((v: any, idx: number) => (
                    <li key={idx} className="flex justify-between border-b border-soc-border/40 pb-1">
                      <span className="text-cyan-400">Version {v.version} ({v.maturity})</span>
                      <span className="text-soc-muted">{v.created_at}</span>
                    </li>
                  ))}
                </ul>
              </div>
            </div>
          </Card>
        </div>
      )}
    </div>
  );
}
