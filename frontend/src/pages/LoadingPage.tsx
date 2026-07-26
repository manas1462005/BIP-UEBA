import { LoadingSpinner } from '../components/common/LoadingSpinner';

export function LoadingPage() {
  return (
    <div className="min-h-screen w-full flex items-center justify-center bg-soc-bg">
      <LoadingSpinner label="Initializing SOC Behavioral Platform..." />
    </div>
  );
}
