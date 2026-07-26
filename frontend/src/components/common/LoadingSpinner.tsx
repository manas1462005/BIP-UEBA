export function LoadingSpinner({ label = 'Loading SOC Platform...' }: { label?: string }) {
  return (
    <div className="flex flex-col items-center justify-center min-h-[300px] w-full p-8">
      <div className="relative flex items-center justify-center">
        <div className="w-12 h-12 rounded-full border-2 border-soc-border border-t-soc-accent animate-spin" />
        <div className="absolute w-6 h-6 rounded-full border-2 border-transparent border-t-soc-cyan animate-spin duration-500" />
      </div>
      <p className="mt-4 text-sm font-medium text-soc-muted tracking-wide animate-pulse">{label}</p>
    </div>
  );
}
