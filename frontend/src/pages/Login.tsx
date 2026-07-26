import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuthStore } from '../store/authStore';
import { axiosClient } from '../api/axiosClient';
import { ShieldCheck, Lock, Mail, ArrowRight, KeyRound } from 'lucide-react';

export function Login() {
  const [email, setEmail] = useState('admin@bip.com');
  const [password, setPassword] = useState('Admin123!');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  
  const { login } = useAuthStore();
  const navigate = useNavigate();

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError('');

    try {
      const response = await axiosClient.post('/auth/login', {
        username: email,
        password: password,
      });

      const { access_token, role, user_email, user_full_name } = response.data;
      
      login(access_token, {
        email: user_email,
        fullName: user_full_name,
        role: role,
      });

      navigate('/dashboard');
    } catch (err: any) {
      setError(err.response?.data?.detail || 'Authentication failed. Please check credentials.');
    } finally {
      setLoading(false);
    }
  };

  const fillMock = (mockEmail: string, mockPass: string) => {
    setEmail(mockEmail);
    setPassword(mockPass);
  };

  return (
    <div className="min-h-screen w-full flex items-center justify-center bg-soc-bg p-4 relative overflow-hidden">
      {/* Background SOC Ambient Glows */}
      <div className="absolute top-1/4 left-1/4 w-96 h-96 bg-blue-600/10 rounded-full blur-3xl pointer-events-none" />
      <div className="absolute bottom-1/4 right-1/4 w-96 h-96 bg-cyan-600/10 rounded-full blur-3xl pointer-events-none" />

      <div className="w-full max-w-md bg-soc-panel border border-soc-border rounded-2xl shadow-2xl p-8 z-10 relative backdrop-blur-md">
        {/* Header */}
        <div className="text-center mb-8">
          <div className="w-14 h-14 rounded-2xl bg-gradient-to-tr from-blue-600 via-indigo-600 to-cyan-500 flex items-center justify-center text-white mx-auto mb-4 shadow-xl shadow-blue-900/40">
            <ShieldCheck className="w-8 h-8" />
          </div>
          <h1 className="text-xl font-bold text-white tracking-tight">Behavioral Intelligence Platform</h1>
          <p className="text-xs text-soc-muted mt-1 font-mono">UEBA SOC Security Operator Login</p>
        </div>

        {error && (
          <div className="mb-6 p-3 bg-rose-950/50 border border-rose-800/60 rounded-xl text-rose-300 text-xs flex items-center gap-2">
            <KeyRound className="w-4 h-4 shrink-0 text-rose-400" />
            <span>{error}</span>
          </div>
        )}

        {/* Login Form */}
        <form onSubmit={handleLogin} className="space-y-4">
          <div>
            <label className="block text-xs font-semibold text-slate-300 mb-1.5">User Email</label>
            <div className="relative">
              <Mail className="w-4 h-4 text-soc-subtle absolute left-3 top-3" />
              <input
                type="email"
                required
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                className="w-full pl-9 pr-4 py-2.5 bg-soc-bg border border-soc-border rounded-xl text-xs text-slate-100 placeholder-soc-subtle focus:outline-none focus:border-soc-accent focus:ring-1 focus:ring-soc-accent transition-colors"
                placeholder="operator@bip.com"
              />
            </div>
          </div>

          <div>
            <label className="block text-xs font-semibold text-slate-300 mb-1.5">Password</label>
            <div className="relative">
              <Lock className="w-4 h-4 text-soc-subtle absolute left-3 top-3" />
              <input
                type="password"
                required
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                className="w-full pl-9 pr-4 py-2.5 bg-soc-bg border border-soc-border rounded-xl text-xs text-slate-100 placeholder-soc-subtle focus:outline-none focus:border-soc-accent focus:ring-1 focus:ring-soc-accent transition-colors"
                placeholder="••••••••"
              />
            </div>
          </div>

          <button
            type="submit"
            disabled={loading}
            className="w-full py-3 bg-blue-600 hover:bg-blue-500 text-white rounded-xl text-xs font-semibold tracking-wide flex items-center justify-center gap-2 shadow-lg shadow-blue-900/30 transition-all duration-150 disabled:opacity-50"
          >
            {loading ? 'Authenticating Token...' : 'Authenticate & Enter Console'}
            {!loading && <ArrowRight className="w-4 h-4" />}
          </button>
        </form>

        {/* Quick Mock Credentials Autofill */}
        <div className="mt-8 pt-6 border-t border-soc-border">
          <p className="text-[11px] font-semibold text-soc-subtle uppercase tracking-wider mb-3 text-center">
            Phase 1 Quick Mock Roles
          </p>
          <div className="grid grid-cols-3 gap-2">
            <button
              onClick={() => fillMock('admin@bip.com', 'Admin123!')}
              className="px-2 py-1.5 bg-soc-bg border border-soc-border hover:border-blue-500/50 rounded-lg text-[10px] text-slate-300 font-mono transition-colors"
            >
              Admin
            </button>
            <button
              onClick={() => fillMock('analyst@bip.com', 'Analyst123!')}
              className="px-2 py-1.5 bg-soc-bg border border-soc-border hover:border-blue-500/50 rounded-lg text-[10px] text-slate-300 font-mono transition-colors"
            >
              Analyst
            </button>
            <button
              onClick={() => fillMock('viewer@bip.com', 'Viewer123!')}
              className="px-2 py-1.5 bg-soc-bg border border-soc-border hover:border-blue-500/50 rounded-lg text-[10px] text-slate-300 font-mono transition-colors"
            >
              Viewer
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
