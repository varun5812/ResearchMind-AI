/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,jsx}"],
  theme: {
    extend: {
      fontFamily: {
        sans: ["Inter", "ui-sans-serif", "system-ui", "sans-serif"],
        display: ["Space Grotesk", "Inter", "ui-sans-serif", "system-ui"],
      },
      colors: {
        void: "#050712",
        panel: "#0b1020",
        cyan: "#42f8ff",
        violet: "#8a5cff",
        green: "#9dff7a",
        pink: "#ff4fd8",
      },
      boxShadow: {
        glow: "0 0 42px rgba(66, 248, 255, 0.22)",
        violet: "0 0 42px rgba(138, 92, 255, 0.24)",
      },
      backgroundImage: {
        aurora:
          "radial-gradient(circle at 15% 15%, rgba(66,248,255,0.22), transparent 28%), radial-gradient(circle at 85% 10%, rgba(138,92,255,0.26), transparent 30%), radial-gradient(circle at 55% 95%, rgba(157,255,122,0.14), transparent 30%)",
      },
    },
  },
  plugins: [],
};
