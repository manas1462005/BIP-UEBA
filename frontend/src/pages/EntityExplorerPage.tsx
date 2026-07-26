import { useState } from 'react';
import { Card } from '../components/common/Card';
import { User, Search, Server, Laptop, MapPin, Network } from 'lucide-react';

export function EntityExplorerPage() {
  const [query, setQuery] = useState<string>('alex.smith1@bip.com');

  return (
    <div className="space-y-6">
      {/* Header & Search */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-4 border-b border-soc-border">
        <div>
          <h1 className="text-xl font-bold text-slate-100 flex items-center gap-2">
            <User className="w-5 h-5 text-cyan-400" />
            Entity Explorer Workspace
          </h1>
          <p className="text-xs text-soc-muted mt-0.5">
            Deep-dive behavioral profiling, risk history, known devices, networks, & organizational relationships
          </p>
        </div>

        <div className="relative">
          <Search className="w-3.5 h-3.5 text-soc-muted absolute left-3 top-2.5" />
          <input
            type="text"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="Search employee email or ID..."
            className="bg-soc-bg border border-soc-border rounded-xl pl-9 pr-3 py-1.5 text-xs text-slate-100 focus:outline-none focus:border-blue-500 font-mono"
          />
        </div>
      </div>

      {/* Entity Card Grid */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <Card title="Entity Profile Overview" subtitle="Employee Meta">
          <div className="space-y-2 font-mono text-xs text-slate-200">
            <div className="flex justify-between"><span className="text-soc-muted">Email:</span><span>{query}</span></div>
            <div className="flex justify-between"><span className="text-soc-muted">ID:</span><span>EMP-1001</span></div>
            <div className="flex justify-between"><span className="text-soc-muted">Department:</span><span>Engineering</span></div>
            <div className="flex justify-between"><span className="text-soc-muted">Role:</span><span>Principal Backend Engineer</span></div>
            <div className="flex justify-between"><span className="text-soc-muted">Manager:</span><span>michael.scott@bip.com</span></div>
          </div>
        </Card>

        <Card title="Known Devices & Hardware" subtitle="Phase 2.5 Inventory">
          <div className="space-y-2 font-mono text-xs text-slate-200">
            <div className="flex items-center gap-2 p-2 bg-soc-bg/50 rounded-lg">
              <Laptop className="w-4 h-4 text-cyan-400" />
              <span>dev_laptop_1001 (Managed Corporate)</span>
            </div>
            <div className="flex items-center gap-2 p-2 bg-soc-bg/50 rounded-lg">
              <Server className="w-4 h-4 text-amber-400" />
              <span>macbook_pro_44 (Unmanaged Personal)</span>
            </div>
          </div>
        </Card>

        <Card title="Known Networks & Locations" subtitle="IP Subnets">
          <div className="space-y-2 font-mono text-xs text-slate-200">
            <div className="flex items-center gap-2 p-2 bg-soc-bg/50 rounded-lg">
              <Network className="w-4 h-4 text-emerald-400" />
              <span>10.100.4.0/24 (HQ Corporate Office)</span>
            </div>
            <div className="flex items-center gap-2 p-2 bg-soc-bg/50 rounded-lg">
              <MapPin className="w-4 h-4 text-purple-400" />
              <span>New York Office, USA</span>
            </div>
          </div>
        </Card>
      </div>
    </div>
  );
}
