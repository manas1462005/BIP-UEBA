import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { DashboardShell } from './components/layout/DashboardShell';
import { AssignmentOverviewPage } from './pages/AssignmentOverviewPage';
import { SimulationPage } from './pages/SimulationPage';
import { BehaviourIntelligencePage } from './pages/BehaviourIntelligencePage';
import { AnomalyIntelligencePage } from './pages/AnomalyIntelligencePage';
import { ContextIntelligencePage } from './pages/ContextIntelligencePage';
import { ThreatIntelligencePage } from './pages/ThreatIntelligencePage';
import { ExplainabilityPage } from './pages/ExplainabilityPage';
import { LiveIncidentFeedPage } from './pages/LiveIncidentFeedPage';
import { IncidentWorkspacePage } from './pages/IncidentWorkspacePage';
import { EvidenceGraphPage } from './pages/EvidenceGraphPage';
import { TimelineExplorerPage } from './pages/TimelineExplorerPage';
import { MitreNavigatorPage } from './pages/MitreNavigatorPage';
import { EntityExplorerPage } from './pages/EntityExplorerPage';
import { BehaviourExplorerPage } from './pages/BehaviourExplorerPage';
import { ExecutiveDashboardPage } from './pages/ExecutiveDashboardPage';
import { AnalyticsDashboardPage } from './pages/AnalyticsDashboardPage';
import { SystemHealthPage } from './pages/SystemHealthPage';
import { PipelineMonitorPage } from './pages/PipelineMonitorPage';

export function App() {
  return (
    <Router>
      <DashboardShell>
        <Routes>
          <Route path="/" element={<AssignmentOverviewPage />} />
          <Route path="/simulation" element={<SimulationPage />} />
          <Route path="/behaviour-intelligence" element={<BehaviourIntelligencePage />} />
          <Route path="/anomaly-intelligence" element={<AnomalyIntelligencePage />} />
          <Route path="/context-intelligence" element={<ContextIntelligencePage />} />
          <Route path="/threat-intelligence" element={<ThreatIntelligencePage />} />
          <Route path="/explainability" element={<ExplainabilityPage />} />
          <Route path="/live-feed" element={<LiveIncidentFeedPage />} />
          <Route path="/incident-workspace" element={<IncidentWorkspacePage />} />
          <Route path="/evidence-graph" element={<EvidenceGraphPage />} />
          <Route path="/timeline-explorer" element={<TimelineExplorerPage />} />
          <Route path="/mitre-navigator" element={<MitreNavigatorPage />} />
          <Route path="/entity-explorer" element={<EntityExplorerPage />} />
          <Route path="/behaviour-explorer" element={<BehaviourExplorerPage />} />
          <Route path="/executive-dashboard" element={<ExecutiveDashboardPage />} />
          <Route path="/analytics-dashboard" element={<AnalyticsDashboardPage />} />
          <Route path="/system-health" element={<SystemHealthPage />} />
          <Route path="/pipeline-monitor" element={<PipelineMonitorPage />} />
        </Routes>
      </DashboardShell>
    </Router>
  );
}

export default App;
