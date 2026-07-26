import { ShieldCheck, Info } from 'lucide-react';

interface AssignmentHeaderProps {
  requirement: string;
  implementation: string;
}

export function AssignmentHeader({ requirement, implementation }: AssignmentHeaderProps) {
  return (
    <div className="bg-soc-panel/80 border border-blue-500/30 rounded-2xl p-4 space-y-2 shadow-sm font-sans mb-6">
      <div className="flex items-center gap-2">
        <ShieldCheck className="w-4 h-4 text-blue-400 flex-shrink-0" />
        <span className="text-xs font-mono font-bold uppercase tracking-wider text-blue-400">
          Assignment Requirement Compliance
        </span>
      </div>
      
      <h2 className="text-sm font-bold text-slate-100 font-mono">
        {requirement}
      </h2>

      <div className="flex items-start gap-2 bg-soc-bg/60 p-3 rounded-xl border border-soc-border">
        <Info className="w-4 h-4 text-cyan-400 mt-0.5 flex-shrink-0" />
        <p className="text-xs text-slate-300 leading-relaxed font-sans">
          <strong className="text-cyan-400 font-mono">Implementation: </strong>
          {implementation}
        </p>
      </div>
    </div>
  );
}
