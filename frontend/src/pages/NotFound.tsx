import { Link } from 'react-router-dom';
import { ShieldAlert, ArrowLeft } from 'lucide-react';

export function NotFound() {
  return (
    <div className="min-h-screen w-full flex items-center justify-center bg-soc-bg p-4">
      <div className="max-w-md w-full bg-soc-panel border border-soc-border rounded-2xl p-8 text-center shadow-2xl">
        <div className="w-12 h-12 rounded-2xl bg-rose-950/60 border border-rose-800/60 text-rose-400 flex items-center justify-center mx-auto mb-4">
          <ShieldAlert className="w-6 h-6" />
        </div>
        <h1 className="text-3xl font-bold text-slate-100 font-mono">404</h1>
        <h2 className="text-sm font-semibold text-slate-300 mt-1">SOC Console Route Not Found</h2>
        <p className="text-xs text-soc-muted mt-2">
          The requested SOC navigation path does not exist or has restricted access.
        </p>
        <Link
          to="/dashboard"
          className="inline-flex items-center gap-2 mt-6 px-4 py-2.5 bg-blue-600 hover:bg-blue-500 text-white rounded-xl text-xs font-semibold transition-colors"
        >
          <ArrowLeft className="w-4 h-4" />
          <span>Return to SOC Console</span>
        </Link>
      </div>
    </div>
  );
}
