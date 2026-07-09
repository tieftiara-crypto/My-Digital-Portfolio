import streamlit as st

# Setup Page
st.set_page_config(page_title="Eftiara | AI Engineer", page_icon="✨", layout="wide")

# Custom CSS for aesthetic Dark Mode & Marquee Loop
st.markdown("""
<style>
    .stApp { background-color: #121212; }
    h1, h2, h3, p, li { color: #E0E0E0 !important; }
    
    /* Project box styling biar tingginya seragam */
    .project-box {
        background-color: #1E1E1E;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #00FFAA;
        margin-bottom: 20px;
        min-height: 260px;
    }
    
    /* Marquee styling (Teks Berjalan ala Startup Web) */
    .marquee-container {
        width: 100%;
        overflow: hidden;
        white-space: nowrap;
        background-color: #0a0a0a;
        padding: 10px 0;
        margin-bottom: 30px;
        border-top: 1px solid #333;
        border-bottom: 1px solid #333;
    }
    .marquee-text {
        display: inline-block;
        padding-left: 100%;
        animation: marquee 15s linear infinite;
        color: #00FFAA;
        font-size: 20px;
        font-weight: bold;
        letter-spacing: 2px;
    }
    @keyframes marquee {
        0% { transform: translate(0, 0); }
        100% { transform: translate(-100%, 0); }
    }
</style>

<div class="marquee-container">
    <span class="marquee-text">✦ EFTIARA PORTFOLIO ✦ AI ENGINEER ✦ WEB DEVELOPER ✦ PYTHON ENTHUSIAST ✦ DATA ANALYST ✦</span>
</div>
""", unsafe_allow_html=True)

# --- HERO SECTION ---
st.title("Hi, I'm Eftiara! 👋")
st.subheader("🚀 AI Engineer & Web Developer")
st.write("Welcome to my digital space. I am passionate about designing and building interactive Artificial Intelligence (AI) applications focused on smart assistants and data-driven business solutions.")

st.markdown("---")

# --- PROJECTS SHOWCASE ---
st.header("💻 Featured AI Projects")
st.write("Here are the Full-Stack AI applications I have developed and deployed:")

# SEKARANG PAKAI 3 KOLOM BIAR MUAT SEMUA 🚀
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="project-box">
        <h3>🤖 Efti-Bot: Ultimate AI</h3>
        <p>A multifunctional AI assistant featuring conversational memory, AI Vision for image analysis, and a digital painter (Text-to-Image) powered by Imagen 3.</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("[**👉 TRY THE APP HERE**](https://web-ai-eftiara.streamlit.app)")

with col2:
    st.markdown("""
    <div class="project-box">
        <h3>📊 AI Business Analyzer</h3>
        <p>A smart data tool that extracts business insights from customer reviews (Excel/CSV). Automatically detects sentiment ratios and formulates strategic executive recommendations.</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("[**👉 TRY THE APP HERE**](https://review-analyzer-eftiara.streamlit.app/)")

with col3:
    st.markdown("""
    <div class="project-box">
        <h3>🎵 AI Lyrics Analyzer</h3>
        <p>A smart music tool based on AI. It doesn't just find lyrics from any genre globally, but also dissects the philosophical meaning and unique facts behind the song.</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("[**👉 TRY THE APP HERE**](https://lirik-ai-eftiara.streamlit.app)")

st.markdown("---")

# --- CONTACT SECTION ---
st.header("📬 Let's Connect")
st.write("Interested in collaborating or discussing career opportunities? Feel free to reach out through the links below:")

st.write("- 💼 **LinkedIn:** [Visit My LinkedIn Profile](#)") 
st.write("- 🐙 **GitHub:** [Check Out My Repositories](https://github.com/tieftiara-crypto)")
st.write("- ✉️ **Email:** tieftiara@email.com")

st.caption("Built with ❤️ using Python and Streamlit")
