/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./src/**/*.{js,ts,jsx,tsx,html}'],
  theme: {
    extend: {
      screens: {
        xs: '475px',
      },
      spacing: {
        18: '4.5rem',
      },
      maxWidth: {
        content: '72rem',
        prose: '65ch',
      },
      fontSize: {
        display: ['3rem', { lineHeight: '1.1', fontWeight: '700' }],
      },
      colors: {
        bg: 'var(--color-bg)',
        'bg-muted': 'var(--color-bg-muted)',
        text: 'var(--color-text)',
        'text-muted': 'var(--color-text-muted)',
        border: 'var(--color-border)',
        accent: {
          DEFAULT: 'var(--color-accent)',
          hover: 'var(--color-accent-hover)',
        },
      },
      borderRadius: {
        sm: 'var(--radius-sm)',
        md: 'var(--radius-md)',
      },
    },
  },
  plugins: [],
};
