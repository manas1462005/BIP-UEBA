import React from 'react';
import { Sidebar } from './Sidebar';
import { PipelineRibbon } from './PipelineRibbon';

interface DashboardShellProps {
  children: React.ReactNode;
}

export function DashboardShell({ children }: DashboardShellProps) {
  return (
    <div className="flex h-screen bg-soc-bg text-slate-100 overflow-hidden font-sans">
      {/* Reorganized Sidebar */}
      <Sidebar />

      {/* Main Content Area */}
      <div className="flex-1 flex flex-col min-w-0 overflow-hidden">
        {/* Horizontal Pipeline Progress Ribbon */}
        <PipelineRibbon />

        {/* Content Body */}
        <main className="flex-1 overflow-y-auto p-6 bg-soc-bg/95">
          <div className="max-w-7xl mx-auto space-y-6">
            {children}
          </div>
        </main>
      </div>
    </div>
  );
}
