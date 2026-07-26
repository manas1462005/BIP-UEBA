/** @type {import('tailwindcss').Config} */
export default {
  darkMode: 'class',
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        soc: {
          bg: '#090d16',
          panel: '#111827',
          header: '#0f172a',
          sidebar: '#0b1120',
          border: '#1f2937',
          accent: '#3b82f6',
          cyan: '#06b6d4',
          muted: '#94a3b8',
          subtle: '#64748b'
        }
      }
    },
  },
  plugins: [],
}
