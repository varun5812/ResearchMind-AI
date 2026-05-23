import { useEffect, useState } from "react";
import { motion, useMotionValue, useSpring } from "framer-motion";
import {
  ArrowRight,
  Bot,
  CheckCircle2,
  DatabaseZap,
  Download,
  FileSearch,
  Github,
  Globe2,
  Layers3,
  Menu,
  Network,
  Rocket,
  Search,
  ShieldCheck,
  Sparkles,
  Terminal,
  X,
} from "lucide-react";
import heroImage from "./assets/researchmind-hero.png";

const navItems = ["Overview", "Workflow", "Agents", "Features", "Stack", "Run"];

const workflow = [
  {
    icon: Search,
    title: "Search",
    text: "Tavily gathers recent, reliable web results for the selected research topic.",
  },
  {
    icon: FileSearch,
    title: "Read",
    text: "The top source is scraped and converted into clean, readable context.",
  },
  {
    icon: Layers3,
    title: "Structure",
    text: "The system creates a markdown report with findings, summary, conclusion, and sources.",
  },
  {
    icon: Download,
    title: "Export",
    text: "The final report can be downloaded and reused as a clean research artifact.",
  },
];

const agents = [
  ["Research Scout", "Finds current sources and ranks useful links."],
  ["Source Reader", "Extracts page text and removes noisy website chrome."],
  ["Report Builder", "Turns search results into a structured research document."],
  ["Source Auditor", "Checks whether the output has enough source coverage."],
];

const features = [
  "Tavily-only mode with no OpenAI quota dependency",
  "Fast Streamlit app for local research workflows",
  "Source-backed markdown reports",
  "Clean download flow for generated research",
  "Responsive premium product website",
  "Deploy-ready project structure",
];

const stack = ["Python", "Streamlit", "Tavily API", "BeautifulSoup", "React", "Tailwind CSS", "Framer Motion", "Vite"];

function useCursor() {
  const x = useMotionValue(-100);
  const y = useMotionValue(-100);
  const springX = useSpring(x, { stiffness: 420, damping: 32 });
  const springY = useSpring(y, { stiffness: 420, damping: 32 });

  useEffect(() => {
    const move = (event) => {
      x.set(event.clientX - 10);
      y.set(event.clientY - 10);
    };
    window.addEventListener("mousemove", move);
    return () => window.removeEventListener("mousemove", move);
  }, [x, y]);

  return { springX, springY };
}

const reveal = {
  hidden: { opacity: 0, y: 28 },
  visible: { opacity: 1, y: 0, transition: { duration: 0.65, ease: "easeOut" } },
};

function Section({ id, eyebrow, title, children }) {
  return (
    <motion.section
      id={id}
      className="relative z-10 mx-auto max-w-7xl px-5 py-20 sm:px-8 lg:px-10"
      variants={reveal}
      initial="hidden"
      whileInView="visible"
      viewport={{ once: true, amount: 0.2 }}
    >
      <p className="font-mono text-xs uppercase tracking-[0.28em] text-cyan">{eyebrow}</p>
      <h2 className="mt-3 max-w-4xl font-display text-3xl font-semibold leading-tight text-white sm:text-5xl">{title}</h2>
      <div className="mt-10">{children}</div>
    </motion.section>
  );
}

function GlassPanel({ children, className = "" }) {
  return (
    <motion.div
      whileHover={{ y: -6 }}
      transition={{ type: "spring", stiffness: 260, damping: 22 }}
      className={`glass-panel ${className}`}
    >
      {children}
    </motion.div>
  );
}

function Navigation() {
  const [open, setOpen] = useState(false);

  return (
    <header className="fixed inset-x-0 top-0 z-50 border-b border-white/10 bg-void/70 backdrop-blur-2xl">
      <nav className="mx-auto flex h-16 max-w-7xl items-center justify-between px-5 sm:px-8 lg:px-10">
        <a href="#home" className="flex items-center gap-2 font-display text-lg font-semibold text-white">
          <span className="grid h-8 w-8 place-items-center rounded border border-cyan/35 bg-cyan/10 text-cyan">
            <Network size={17} />
          </span>
          ResearchMind
        </a>
        <div className="hidden items-center gap-7 lg:flex">
          {navItems.map((item) => (
            <a className="nav-link" key={item} href={`#${item.toLowerCase()}`}>
              {item}
            </a>
          ))}
        </div>
        <a className="hidden items-center gap-2 rounded border border-cyan/40 px-4 py-2 text-sm font-semibold text-cyan shadow-glow transition hover:bg-cyan hover:text-void md:flex" href="#run">
          Launch locally <ArrowRight size={16} />
        </a>
        <button className="rounded border border-white/15 p-2 text-white lg:hidden" onClick={() => setOpen(!open)} aria-label="Toggle menu">
          {open ? <X size={20} /> : <Menu size={20} />}
        </button>
      </nav>
      {open && (
        <div className="border-t border-white/10 bg-void/95 px-5 py-4 lg:hidden">
          {navItems.map((item) => (
            <a key={item} className="block py-3 text-sm text-slate-200" href={`#${item.toLowerCase()}`} onClick={() => setOpen(false)}>
              {item}
            </a>
          ))}
        </div>
      )}
    </header>
  );
}

function Particles() {
  return (
    <div className="pointer-events-none fixed inset-0 z-0 overflow-hidden">
      {Array.from({ length: 34 }).map((_, index) => (
        <span
          className="particle"
          key={index}
          style={{
            left: `${(index * 31) % 100}%`,
            animationDelay: `${(index % 8) * 0.7}s`,
            animationDuration: `${9 + (index % 9)}s`,
          }}
        />
      ))}
    </div>
  );
}

function Hero() {
  return (
    <section id="home" className="relative min-h-screen overflow-hidden">
      <img className="absolute inset-0 h-full w-full object-cover opacity-35 mix-blend-screen" src={heroImage} alt="" />
      <div className="absolute inset-0 bg-[linear-gradient(90deg,#050712_0%,rgba(5,7,18,0.86)_48%,rgba(5,7,18,0.42)_100%)]" />
      <div className="absolute inset-0 bg-[linear-gradient(rgba(255,255,255,0.035)_1px,transparent_1px),linear-gradient(90deg,rgba(255,255,255,0.035)_1px,transparent_1px)] bg-[size:64px_64px] opacity-45" />
      <div className="relative z-10 mx-auto grid min-h-screen max-w-7xl items-center px-5 pt-20 sm:px-8 lg:grid-cols-[1.05fr_0.95fr] lg:px-10">
        <motion.div initial={{ opacity: 0, y: 34 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.75 }}>
          <div className="inline-flex items-center gap-2 rounded border border-cyan/30 bg-white/[0.055] px-4 py-2 text-sm text-cyan backdrop-blur-xl">
            <Sparkles size={16} />
            Multi-agent research system
          </div>
          <h1 className="mt-7 max-w-5xl font-display text-5xl font-bold leading-[0.96] text-white sm:text-7xl lg:text-8xl">
            Research that moves from web signal to report.
          </h1>
          <p className="mt-6 max-w-2xl text-lg leading-8 text-slate-300">
            ResearchMind combines Tavily search, source scraping, structured reporting, and a fast Streamlit interface into one clean local research workflow.
          </p>
          <div className="mt-8 flex flex-col gap-4 sm:flex-row">
            <a className="inline-flex items-center justify-center gap-2 rounded bg-cyan px-6 py-4 font-semibold text-void shadow-glow transition hover:-translate-y-1" href="#workflow">
              Explore workflow <ArrowRight size={18} />
            </a>
            <a className="inline-flex items-center justify-center gap-2 rounded border border-white/15 px-6 py-4 font-semibold text-white backdrop-blur-xl transition hover:border-violet hover:text-violet" href="#run">
              Run commands <Terminal size={18} />
            </a>
          </div>
        </motion.div>
        <motion.div className="mt-12 lg:mt-0" initial={{ opacity: 0, scale: 0.94 }} animate={{ opacity: 1, scale: 1 }} transition={{ delay: 0.2, duration: 0.75 }}>
          <div className="system-map">
            {["Topic", "Tavily", "Reader", "Report"].map((node, index) => (
              <div className="map-node" key={node} style={{ animationDelay: `${index * 0.35}s` }}>
                <span>{node}</span>
              </div>
            ))}
          </div>
        </motion.div>
      </div>
    </section>
  );
}

export default function App() {
  const { springX, springY } = useCursor();

  return (
    <main className="min-h-screen overflow-x-hidden bg-void text-slate-200">
      <motion.div className="custom-cursor hidden md:block" style={{ x: springX, y: springY }} />
      <Particles />
      <Navigation />
      <Hero />

      <Section id="overview" eyebrow="Overview" title="A polished product website for your actual research app.">
        <div className="grid gap-5 lg:grid-cols-[1.1fr_0.9fr]">
          <GlassPanel>
            <Globe2 className="mb-5 text-cyan" size={28} />
            <p className="text-lg leading-8 text-slate-300">
              This site presents your Multi-Agent Research System as a premium AI product: clear value, strong visuals, animated explanation, and a direct path to run the working Streamlit application.
            </p>
          </GlassPanel>
          <div className="grid gap-5 sm:grid-cols-2">
            {["Source-backed", "Local-first", "Fast workflow", "Export-ready"].map((item) => (
              <GlassPanel key={item}>
                <CheckCircle2 className="mb-4 text-green" />
                <p className="font-display text-xl font-semibold text-white">{item}</p>
              </GlassPanel>
            ))}
          </div>
        </div>
      </Section>

      <Section id="workflow" eyebrow="Workflow" title="Four clean stages, designed for fast research output.">
        <div className="grid gap-5 md:grid-cols-2 lg:grid-cols-4">
          {workflow.map((step, index) => {
            const Icon = step.icon;
            return (
              <GlassPanel key={step.title} className="min-h-64">
                <div className="mb-6 flex items-center justify-between">
                  <span className="font-mono text-xs text-slate-500">0{index + 1}</span>
                  <Icon className="text-cyan" size={26} />
                </div>
                <h3 className="font-display text-2xl font-semibold text-white">{step.title}</h3>
                <p className="mt-4 leading-7 text-slate-300">{step.text}</p>
              </GlassPanel>
            );
          })}
        </div>
      </Section>

      <Section id="agents" eyebrow="Agents" title="A research pipeline explained like a real AI product.">
        <div className="grid gap-5 lg:grid-cols-4">
          {agents.map(([name, text]) => (
            <GlassPanel key={name}>
              <Bot className="mb-5 text-violet" />
              <h3 className="font-display text-xl font-semibold text-white">{name}</h3>
              <p className="mt-3 leading-7 text-slate-300">{text}</p>
            </GlassPanel>
          ))}
        </div>
      </Section>

      <Section id="features" eyebrow="Features" title="Everything a viewer needs to understand the project quickly.">
        <div className="grid gap-4 md:grid-cols-2">
          {features.map((feature) => (
            <GlassPanel key={feature} className="flex items-center gap-4">
              <ShieldCheck className="shrink-0 text-green" />
              <span className="text-white">{feature}</span>
            </GlassPanel>
          ))}
        </div>
      </Section>

      <Section id="stack" eyebrow="Stack" title="Built with a practical AI and web development stack.">
        <div className="flex flex-wrap gap-3">
          {stack.map((item) => (
            <motion.span
              key={item}
              whileHover={{ y: -4, scale: 1.03 }}
              className="rounded border border-white/12 bg-white/[0.055] px-4 py-3 text-sm font-semibold text-slate-100 backdrop-blur-xl"
            >
              {item}
            </motion.span>
          ))}
        </div>
      </Section>

      <Section id="run" eyebrow="Run Locally" title="Launch the research app and the website from VS Code.">
        <div className="grid gap-5 lg:grid-cols-2">
          <GlassPanel>
            <div className="mb-5 flex items-center gap-3 text-cyan">
              <DatabaseZap />
              <h3 className="font-display text-2xl font-semibold text-white">Streamlit research app</h3>
            </div>
            <pre className="code-block">{`cd "C:\\Users\\varun\\Downloads\\Multi-agent-research-system-main\\Multi-agent-research-system-main"
python -m streamlit run app.py`}</pre>
          </GlassPanel>
          <GlassPanel>
            <div className="mb-5 flex items-center gap-3 text-violet">
              <Rocket />
              <h3 className="font-display text-2xl font-semibold text-white">Animated website</h3>
            </div>
            <pre className="code-block">{`cd "C:\\Users\\varun\\Downloads\\Multi-agent-research-system-main\\Multi-agent-research-system-main\\researchmind-site"
npm run dev`}</pre>
          </GlassPanel>
        </div>
      </Section>

      <footer className="relative z-10 border-t border-white/10 px-5 py-9 text-center text-sm text-slate-500">
        <Github className="mx-auto mb-3 text-cyan" size={20} />
        ResearchMind product website built for the Multi-Agent Research System.
      </footer>
    </main>
  );
}
