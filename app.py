import html
import time

import streamlit as st

from pipeline import run_research_pipeline


st.set_page_config(
    page_title="ResearchMind - Multi-Agent Research",
    page_icon="RM",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;600;700&display=swap');

:root {
    --bg: #050712;
    --panel: rgba(255,255,255,0.065);
    --line: rgba(255,255,255,0.13);
    --text: #f8fbff;
    --muted: #9aa7bb;
    --cyan: #42f8ff;
    --violet: #8a5cff;
    --green: #9dff7a;
}

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    color: var(--text);
}

.stApp {
    background:
        radial-gradient(circle at 12% 8%, rgba(66,248,255,0.20), transparent 28%),
        radial-gradient(circle at 82% 0%, rgba(138,92,255,0.24), transparent 32%),
        radial-gradient(circle at 55% 100%, rgba(157,255,122,0.10), transparent 28%),
        #050712;
}

#MainMenu, footer, header { visibility: hidden; }
.block-container { max-width: 1180px; padding: 2rem 2rem 4rem; }

.hero {
    position: relative;
    overflow: hidden;
    min-height: 430px;
    border: 1px solid var(--line);
    border-radius: 18px;
    padding: 3rem;
    background:
        linear-gradient(120deg, rgba(5,7,18,0.92), rgba(5,7,18,0.72)),
        linear-gradient(rgba(255,255,255,0.045) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255,255,255,0.045) 1px, transparent 1px);
    background-size: auto, 54px 54px, 54px 54px;
    box-shadow: 0 24px 90px rgba(0,0,0,0.38), 0 0 70px rgba(66,248,255,0.10);
}

.hero::before {
    content: "";
    position: absolute;
    inset: -20%;
    background:
        conic-gradient(from 180deg, transparent, rgba(66,248,255,0.18), transparent, rgba(138,92,255,0.18), transparent);
    animation: spinGlow 18s linear infinite;
    opacity: 0.8;
}

.hero-content { position: relative; z-index: 1; max-width: 780px; }
.eyebrow {
    display: inline-flex;
    border: 1px solid rgba(66,248,255,0.35);
    border-radius: 999px;
    padding: 0.45rem 0.8rem;
    background: rgba(66,248,255,0.08);
    color: var(--cyan);
    font-family: 'Space Grotesk', sans-serif;
    font-size: 0.78rem;
    font-weight: 700;
    letter-spacing: 0.14em;
    text-transform: uppercase;
}

.hero h1 {
    margin: 1.25rem 0 1rem;
    font-family: 'Space Grotesk', sans-serif;
    font-size: clamp(2.8rem, 7vw, 5.8rem);
    line-height: 0.95;
    letter-spacing: 0;
    color: white;
}

.hero h1 span {
    color: var(--cyan);
    text-shadow: 0 0 36px rgba(66,248,255,0.45);
}

.hero p {
    max-width: 650px;
    color: #b8c2d6;
    font-size: 1.08rem;
    line-height: 1.8;
}

.search-shell {
    position: relative;
    z-index: 2;
    margin-top: -72px;
    margin-bottom: 2rem;
    border: 1px solid rgba(66,248,255,0.28);
    border-radius: 16px;
    padding: 1.3rem;
    background: rgba(8,12,26,0.78);
    backdrop-filter: blur(24px);
    box-shadow: 0 24px 70px rgba(0,0,0,0.34), 0 0 55px rgba(66,248,255,0.14);
}

.search-title {
    display: flex;
    align-items: center;
    gap: 0.7rem;
    margin-bottom: 1rem;
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.05rem;
    font-weight: 700;
    color: white;
}

.pulse-dot {
    width: 10px;
    height: 10px;
    border-radius: 999px;
    background: var(--green);
    box-shadow: 0 0 18px rgba(157,255,122,0.8);
    animation: pulse 1.7s ease-in-out infinite;
}

.stTextInput label {
    color: var(--cyan) !important;
    font-family: 'Space Grotesk', sans-serif !important;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    font-size: 0.72rem !important;
}

.stTextInput input,
div[data-baseweb="input"] input,
input[type="text"] {
    min-height: 58px;
    border: 1px solid rgba(255,255,255,0.14) !important;
    border-radius: 10px !important;
    background: #0b1020 !important;
    color: white !important;
    -webkit-text-fill-color: white !important;
    caret-color: var(--cyan) !important;
    font-size: 1rem !important;
}

.stTextInput input::placeholder,
div[data-baseweb="input"] input::placeholder,
input[type="text"]::placeholder {
    color: #7f8ca3 !important;
    -webkit-text-fill-color: #7f8ca3 !important;
    opacity: 1 !important;
}

.stTextInput input:focus,
div[data-baseweb="input"] input:focus,
input[type="text"]:focus {
    border-color: rgba(66,248,255,0.75) !important;
    box-shadow: 0 0 0 4px rgba(66,248,255,0.10) !important;
}

.stButton button, .stDownloadButton button {
    min-height: 54px;
    border: 0 !important;
    border-radius: 10px !important;
    background: linear-gradient(135deg, var(--cyan), var(--violet)) !important;
    color: #050712 !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-weight: 800 !important;
    transition: transform 0.18s ease, box-shadow 0.18s ease !important;
    box-shadow: 0 0 34px rgba(66,248,255,0.25) !important;
}

.stButton button:hover, .stDownloadButton button:hover {
    transform: translateY(-2px);
    box-shadow: 0 0 44px rgba(66,248,255,0.38) !important;
}

.metric-grid {
    display: grid;
    grid-template-columns: repeat(4, minmax(0, 1fr));
    gap: 1rem;
    margin: 1.5rem 0 2.2rem;
}

.metric-card, .result-card {
    border: 1px solid var(--line);
    border-radius: 14px;
    background: var(--panel);
    backdrop-filter: blur(18px);
    padding: 1.2rem;
}

.metric-card strong {
    display: block;
    color: white;
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.35rem;
}

.metric-card span { color: var(--muted); font-size: 0.88rem; }

.section-title {
    margin: 2rem 0 1rem;
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.8rem;
    font-weight: 700;
    color: white;
}

.result-card {
    margin-top: 1rem;
    padding: 1.8rem;
}

.stMarkdown, .stExpander {
    color: #d8e0ef;
}

@keyframes spinGlow {
    to { transform: rotate(360deg); }
}

@keyframes pulse {
    0%, 100% { transform: scale(0.9); opacity: 0.55; }
    50% { transform: scale(1.25); opacity: 1; }
}

@media (max-width: 780px) {
    .block-container { padding: 1rem 1rem 3rem; }
    .hero { padding: 2rem 1.2rem; min-height: 380px; }
    .search-shell { margin-top: -36px; }
    .metric-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
}
</style>
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="hero">
  <div class="hero-content">
    <div class="eyebrow">Tavily Powered Research Pipeline</div>
    <h1>Search a topic.<br><span>Get a report.</span></h1>
    <p>
      ResearchMind searches the web, reads the best source, extracts clean content,
      and builds a downloadable research report from real sources.
    </p>
  </div>
</div>
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="search-shell">
  <div class="search-title"><span class="pulse-dot"></span> Type your research topic here</div>
</div>
""",
    unsafe_allow_html=True,
)

with st.container():
    topic_col, button_col = st.columns([4, 1.25])
    with topic_col:
        topic = st.text_input(
            "Research Topic",
            placeholder="Example: AI agents in healthcare 2026",
            label_visibility="collapsed",
        )
    with button_col:
        run_btn = st.button("Run Research", type="primary", use_container_width=True)

st.markdown(
    """
<div class="metric-grid">
  <div class="metric-card"><strong>01</strong><span>Tavily web search</span></div>
  <div class="metric-card"><strong>02</strong><span>Source reading</span></div>
  <div class="metric-card"><strong>03</strong><span>Report building</span></div>
  <div class="metric-card"><strong>04</strong><span>Markdown export</span></div>
</div>
""",
    unsafe_allow_html=True,
)

if run_btn:
    if not topic.strip():
        st.warning("Please enter a research topic first.")
    else:
        try:
            with st.spinner("ResearchMind is searching, reading, and building your report..."):
                st.session_state.results = run_research_pipeline(topic.strip())
                st.session_state.last_topic = topic.strip()
        except Exception as exc:
            st.error(str(exc))

results = st.session_state.get("results")

if results:
    safe_topic = html.escape(st.session_state.get("last_topic", "Research topic"))
    st.markdown(f'<div class="section-title">Research Report: {safe_topic}</div>', unsafe_allow_html=True)

    st.markdown('<div class="result-card">', unsafe_allow_html=True)
    st.markdown(results["writer"])
    st.markdown("</div>", unsafe_allow_html=True)

    st.download_button(
        label="Download Report (.md)",
        data=results["writer"],
        file_name=f"research_report_{int(time.time())}.md",
        mime="text/markdown",
        use_container_width=True,
    )

    with st.expander("View Tavily search results"):
        st.text(results["search"])

    with st.expander("View scraped source content"):
        st.text(results["reader"])

    with st.expander("View source check"):
        st.markdown(results["critic"])
