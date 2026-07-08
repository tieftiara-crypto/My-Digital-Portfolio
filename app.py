import streamlit as st

# Setup Halaman
st.set_page_config(page_title="Portofolio | Eftiara", page_icon="✨", layout="wide")

# Custom CSS biar estetik (Dark Mode Elegan)
st.markdown("""
<style>
    .stApp { background-color: #121212; }
    h1, h2, h3, p, li { color: #E0E0E0 !important; }
    
    /* Bikin kotak project biar rapi */
    .project-box {
        background-color: #1E1E1E;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #00FFAA;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# --- BAGIAN HERO (PERKENALAN) ---
st.title("Halo, Saya Eftiara! 👋")
st.subheader("🚀 AI Engineer & Web Developer")
st.write("Selamat datang di CV Digital saya. Saya memiliki *passion* dalam merancang dan membangun aplikasi *Artificial Intelligence* (AI) interaktif yang berfokus pada asisten pintar dan otomatisasi analisis data bisnis.")

st.markdown("---")

# --- BAGIAN ETALASE PROYEK ---
st.header("💻 Etalase Proyek AI Terkini")
st.write("Berikut adalah aplikasi *Full-Stack AI* yang telah saya kembangkan dan *deploy* ke publik:")

# Bikin 2 kolom berdampingan
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="project-box">
        <h3>🤖 Efti-Bot: Ultimate AI</h3>
        <p>Asisten AI multifungsi dengan gaya bahasa kasual. Dilengkapi memori percakapan, kemampuan membaca gambar (AI Vision), dan fitur pelukis digital (Text-to-Image) bertenaga Imagen 3.</p>
    </div>
    """, unsafe_allow_html=True)
    # LINK KE WEB PERTAMA LU
    st.markdown("[**👉 KLIK DI SINI UNTUK COBA APLIKASI**](https://web-ai-eftiara.streamlit.app)")

with col2:
    st.markdown("""
    <div class="project-box">
        <h3>📊 AI Business Analyzer</h3>
        <p>Alat cerdas pembedah data ulasan bisnis (Excel/CSV). Secara otomatis mendeteksi rasio sentimen pelanggan dan merumuskan rekomendasi strategi bisnis layaknya konsultan profesional.</p>
    </div>
    """, unsafe_allow_html=True)
    # LINK KE WEB KEDUA LU (Ganti tulisan di dalam kurung URL dengan link web lu yang kedua tadi)
    st.markdown("[**👉 KLIK DI SINI UNTUK COBA APLIKASI**](https://review-analyzer-eftiara.streamlit.app/)")

st.markdown("---")

# --- BAGIAN KONTAK ---
st.header("📬 Mari Terhubung")
st.write("Tertarik untuk berkolaborasi atau mendiskusikan peluang karir? Jangan ragu untuk menghubungi saya melalui tautan di bawah ini:")

st.write("- 💼 **LinkedIn:** [Kunjungi Profil LinkedIn Saya](#)") 
st.write("- 🐙 **GitHub:** [Lihat Source Code Proyek Saya](https://github.com/tieftiara-crypto)")
st.write("- ✉️ **Email:** eftiara@email.com")

st.caption("Dibuat dengan ❤️ menggunakan Python dan Streamlit")
