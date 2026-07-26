import { useState } from 'react';
import { Card } from '../components/common/Card';
import { Badge } from '../components/common/Badge';
import { GitCommit, ZoomIn, ZoomOut, RefreshCw, Layers, ShieldAlert, User, Server } from 'lucide-react';

export function EvidenceGraphPage() {
  const [selectedNode, setSelectedNode] = useState<any>(null);

  const nodes = [
    { id: 'user:alex.smith1', label: 'alex.smith1@bip.com', type: 'User', icon: User, color: 'text-cyan-400', border: 'border-cyan-500/40' },
    { id: 'device:dev_1001', label: 'dev_laptop_1001', type: 'Device', icon: Server, color: 'text-blue-400', border: 'border-blue-500/40' },
    { id: 'app:aws_console', label: 'AWS Production Console', type: 'Application', icon: Layers, color: 'text-amber-400', border: 'border-amber-500/40' },
    { id: 'threat:credential_spray', label: 'Credential Theft Attack', type: 'Threat', icon: ShieldAlert, color: 'text-red-400', border: 'border-red-500/40' }
  ];

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-4 border-b border-soc-border">
        <div>
          <h1 className="text-xl font-bold text-slate-100 flex items-center gap-2">
            <GitCommit className="w-5 h-5 text-cyan-400" />
            Evidence Graph Visualizer
          </h1>
          <p className="text-xs text-soc-muted mt-0.5">
            Interactive relational graph linking Users, Devices, Sessions, Applications, MITRE Techniques, & Threat Events
          </p>
        </div>

        <div className="flex items-center gap-2">
          <button className="p-2 bg-soc-border/40 hover:bg-soc-border text-slate-200 rounded-xl text-xs font-semibold">
            <ZoomIn className="w-4 h-4" />
          </button>
          <button className="p-2 bg-soc-border/40 hover:bg-soc-border text-slate-200 rounded-xl text-xs font-semibold">
            <ZoomOut className="w-4 h-4" />
          </button>
          <button className="p-2 bg-soc-border/40 hover:bg-soc-border text-slate-200 rounded-xl text-xs font-semibold">
            <RefreshCw className="w-4 h-4" />
          </button>
        </div>
      </div>

      {/* Canvas & Node Detail Grid */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {/* Interactive Canvas Simulator (Span 2) */}
        <div className="md:col-span-2">
          <Card title="Interactive Node-Link Evidence Graph" subtitle="Click any node to inspect relationship graph details">
            <div className="h-96 bg-soc-bg/80 border border-soc-border rounded-xl p-6 relative flex items-center justify-center overflow-hidden">
              {/* Grid backdrop */}
              <div className="absolute inset-0 bg-[radial-gradient(#1e293b_1px,transparent_1px)] [background-size:16px_16px] opacity-40"></div>

              {/* Node Layout Canvas */}
              <div className="relative z-10 grid grid-cols-2 gap-12 items-center">
                {nodes.map((node) => {
                  const Icon = node.icon;
                  const isSelected = selectedNode?.id === node.id;
                  return (
                    <button
                      key={node.id}
                      onClick={() => setSelectedNode(node)}
                      className={`p-4 bg-soc-panel border ${node.border} rounded-2xl shadow-xl flex items-center gap-3 transition-all transform hover:scale-105 ${
                        isSelected ? 'ring-2 ring-blue-500 scale-105' : ''
                      }`}
                    >
                      <div className={`w-10 h-10 rounded-xl bg-soc-bg flex items-center justify-center ${node.color}`}>
                        <Icon className="w-5 h-5" />
                      </div>
                      <div className="text-left font-mono text-xs">
                        <span className="text-soc-muted text-[10px] block">{node.type}</span>
                        <span className="text-slate-100 font-bold block">{node.label}</span>
                      </div>
                    </button>
                  );
                })}
              </div>
            </div>
          </Card>
        </div>

        {/* Node Inspector Panel */}
        <div>
          <Card title="Node Inspector & Metadata" subtitle="Graph element details">
            {selectedNode ? (
              <div className="space-y-3 font-mono text-xs">
                <div className="p-3 bg-soc-bg/50 border border-soc-border rounded-lg space-y-1">
                  <span className="text-soc-muted text-[10px]">Node ID:</span>
                  <p className="text-cyan-400 font-bold">{selectedNode.id}</p>
                </div>
                <div className="p-3 bg-soc-bg/50 border border-soc-border rounded-lg space-y-1">
                  <span className="text-soc-muted text-[10px]">Type:</span>
                  <Badge variant="info">{selectedNode.type}</Badge>
                </div>
                <div className="p-3 bg-soc-bg/50 border border-soc-border rounded-lg space-y-1">
                  <span className="text-soc-muted text-[10px]">Active Edges:</span>
                  <p className="text-slate-200">Authenticated (1), Accessed (1), Correlated (1)</p>
                </div>
              </div>
            ) : (
              <p className="text-xs font-mono text-soc-muted p-4 text-center">
                Click any graph node on the canvas to inspect entity properties and active relationships.
              </p>
            )}
          </Card>
        </div>
      </div>
    </div>
  );
}
