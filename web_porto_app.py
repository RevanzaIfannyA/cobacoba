"""
Portfolio Website Interaktif - Alex Rivera
Data Analyst | Data Scientist | ML Engineer | AI Engineer
Jalankan dengan: streamlit run app.py
"""

import streamlit as st

# ─────────────────────────────────────────────
# KONFIGURASI HALAMAN
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Portfolio | Alex Rivera",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",  # Collapse sidebar untuk single page
)

# ─────────────────────────────────────────────
# DATA PROYEK
# ─────────────────────────────────────────────
PROJECTS = [
    {
        "id": 1,
        "name": "Dashboard Penjualan Real-time",
        "category": ["Data Analyst"],
        "emoji": "📊",
        "description": "Dashboard interaktif untuk memantau KPI penjualan harian, mingguan, dan bulanan dengan drill-down per region dan produk.",
        "tech": ["Tableau", "SQL", "Python", "PostgreSQL"],
        "detail": "Membangun pipeline ETL dari database OLTP ke Tableau. Dashboard mencakup 15+ visualisasi interaktif, alert otomatis via email, dan laporan PDF terjadwal. Mengurangi waktu pelaporan manual dari 3 jam menjadi 5 menit.",
        "github": "https://github.com/alexrivera/sales-dashboard",
        "demo": "https://sales-dashboard-demo.herokuapp.com",
    },
    {
        "id": 2,
        "name": "Analisis Churn Pelanggan",
        "category": ["Data Analyst", "Data Scientist"],
        "emoji": "🔍",
        "description": "Analisis mendalam pola churn pelanggan menggunakan cohort analysis dan funnel visualization untuk menemukan titik kritis retensi.",
        "tech": ["Python", "Pandas", "Seaborn", "Plotly", "SQL"],
        "detail": "Menganalisis 500K+ record pelanggan selama 2 tahun. Menemukan bahwa 68% churn terjadi di bulan ke-3 onboarding. Rekomendasi strategi retensi berhasil menurunkan churn rate sebesar 22%.",
        "github": "https://github.com/alexrivera/churn-analysis",
        "demo": "https://churn-analysis-demo.streamlit.app",
    },
    {
        "id": 3,
        "name": "Prediksi Harga Saham LSTM",
        "category": ["Data Scientist"],
        "emoji": "📈",
        "description": "Model deep learning LSTM multi-variate untuk memprediksi harga penutupan saham 7 hari ke depan dengan fitur teknikal dan sentimen berita.",
        "tech": ["Python", "TensorFlow", "Keras", "NLTK", "Yahoo Finance API"],
        "detail": "Arsitektur LSTM 3-layer dengan attention mechanism. Mengintegrasikan 50+ indikator teknikal dan skor sentimen dari 10K+ artikel berita harian. Mencapai MAPE 3.2% pada data uji out-of-sample.",
        "github": "",  # Tidak ada link github
        "demo": "https://stock-prediction-lstm.herokuapp.com",
    },
    {
        "id": 4,
        "name": "Clustering Segmentasi Pelanggan",
        "category": ["Data Scientist", "Data Analyst"],
        "emoji": "🎯",
        "description": "Segmentasi pelanggan e-commerce menggunakan RFM analysis dan K-Means clustering untuk personalisasi strategi marketing.",
        "tech": ["Python", "Scikit-learn", "Pandas", "Plotly", "Power BI"],
        "detail": "Mengidentifikasi 6 segmen pelanggan unik dari 200K+ transaksi. Segment 'Champions' (8% pelanggan) berkontribusi 43% revenue. Strategi targeted marketing meningkatkan conversion rate sebesar 35%.",
        "github": "https://github.com/alexrivera/customer-segmentation",
        "demo": "",  # Tidak ada link demo
    },
    {
        "id": 5,
        "name": "Deployment Model via FastAPI",
        "category": ["ML Engineer"],
        "emoji": "🚀",
        "description": "Production-ready API untuk serving model machine learning Scikit-learn dengan autoscaling, monitoring, dan A/B testing framework.",
        "tech": ["FastAPI", "Docker", "Scikit-learn", "MLflow", "Redis", "Nginx"],
        "detail": "Membangun RESTful API dengan latency P95 < 50ms. Implementasi canary deployment untuk A/B testing model. Monitoring dengan Prometheus + Grafana. Throughput 1000+ request/detik.",
        "github": "",  # Tidak ada link github
        "demo": "",  # Tidak ada link demo
    },
    {
        "id": 6,
        "name": "Pipeline Otomatis dengan Airflow",
        "category": ["ML Engineer", "Data Engineer"],
        "emoji": "⚙️",
        "description": "Orkestrasi pipeline ML end-to-end mulai dari ingestion data, preprocessing, training, validasi, hingga deployment otomatis ke production.",
        "tech": ["Apache Airflow", "Python", "Docker", "MLflow", "PostgreSQL", "S3"],
        "detail": "Pipeline 15-tahap dengan retry logic dan alerting. Retraining model otomatis setiap minggu dengan data drift detection. Mengurangi waktu deployment dari 2 hari menjadi 4 jam.",
        "github": "https://github.com/alexrivera/airflow-pipeline",
        "demo": "https://airflow-pipeline-demo.herokuapp.com",
    },
    {
        "id": 7,
        "name": "Chatbot RAG untuk Dokumen Hukum",
        "category": ["AI Engineer"],
        "emoji": "⚖️",
        "description": "Sistem tanya-jawab cerdas berbasis Retrieval-Augmented Generation untuk mengekstrak dan menjawab pertanyaan dari ribuan dokumen hukum.",
        "tech": ["LangChain", "OpenAI GPT-4", "Pinecone", "FastAPI", "Streamlit"],
        "detail": "Mengindeks 50K+ halaman dokumen hukum ke vector database. Hybrid search (BM25 + semantic) dengan reranking. Akurasi jawaban 91% pada benchmark internal. Mengurangi waktu riset hukum 70%.",
        "github": "https://github.com/alexrivera/legal-rag-chatbot",
        "demo": "",  # Tidak ada link demo
    },
    {
        "id": 8,
        "name": "Sistem Deteksi Objek YOLOv8",
        "category": ["AI Engineer", "ML Engineer"],
        "emoji": "👁️",
        "description": "Real-time object detection system untuk monitoring keamanan pabrik — mendeteksi APD (helm, rompi) dan pelanggaran zona berbahaya.",
        "tech": ["YOLOv8", "OpenCV", "Python", "FastAPI", "MQTT", "React"],
        "detail": "Fine-tuning YOLOv8x pada 15K gambar custom. Inference 45 FPS pada edge device NVIDIA Jetson. Integrasi dengan CCTV eksisting via RTSP stream. Alert real-time ke operator via dashboard dan notifikasi.",
        "github": "https://github.com/alexrivera/yolo-safety-system",
        "demo": "https://yolo-demo.streamlit.app",
    },
]

# ─────────────────────────────────────────────
# DATA PENGALAMAN KERJA
# ─────────────────────────────────────────────
EXPERIENCES = [
    {
        "title": "AI Engineer",
        "company": "TechCorp Indonesia",
        "period": "Jan 2023 – Sekarang",
        "location": "Jakarta, Indonesia",
        "emoji": "🤖",
        "color": "#7C3AED",
        "points": [
            "Membangun dan men-deploy sistem RAG untuk 3 klien enterprise dengan akurasi rata-rata 89%",
            "Mengembangkan pipeline fine-tuning LLM (LLaMA, Mistral) untuk domain spesifik industri",
            "Memimpin tim 4 engineer dalam project computer vision untuk manufaktur",
            "Mengintegrasikan solusi AI ke sistem legacy klien dengan zero downtime migration",
        ],
    },
    {
        "title": "ML Engineer",
        "company": "DataLabs Nusantara",
        "period": "Mar 2021 – Des 2022",
        "location": "Bandung, Indonesia (Hybrid)",
        "emoji": "⚙️",
        "color": "#2563EB",
        "points": [
            "Membangun MLOps platform menggunakan MLflow, Airflow, dan Kubernetes",
            "Men-deploy 12+ model ML ke production dengan SLA 99.9% uptime",
            "Menurunkan inference latency rata-rata 60% melalui model quantization dan optimization",
            "Mendokumentasikan dan standardisasi proses ML deployment seluruh perusahaan",
        ],
    },
    {
        "title": "Data Analyst",
        "company": "StartupX (Series B)",
        "period": "Jun 2019 – Feb 2021",
        "location": "Surabaya, Indonesia",
        "emoji": "📊",
        "color": "#059669",
        "points": [
            "Membangun data warehouse dari nol menggunakan BigQuery dan dbt",
            "Membuat 20+ dashboard Tableau untuk C-level executives dan tim operasional",
            "Melakukan analisis A/B testing untuk fitur produk baru, meningkatkan conversion 18%",
            "Mengautomasi laporan mingguan, menghemat 15 jam kerja manual per minggu",
        ],
    },
]

# ─────────────────────────────────────────────
# DATA SERTIFIKASI
# ─────────────────────────────────────────────
CERTIFICATIONS = [
    {"name": "TensorFlow Developer Certificate", "issuer": "Google", "year": "2023", "emoji": "🧠", "color": "#FF6F00", "link": "https://www.credential.net/tensorflow"},
    {"name": "AWS Certified ML Specialty", "issuer": "Amazon Web Services", "year": "2022", "emoji": "☁️", "color": "#FF9900", "link": "https://www.credly.com/aws-ml"},
    {"name": "Databricks ML Associate", "issuer": "Databricks", "year": "2022", "emoji": "🔥", "color": "#FF3621", "link": "https://credentials.databricks.com"},
    {"name": "Tableau Desktop Specialist", "issuer": "Tableau (Salesforce)", "year": "2021", "emoji": "📊", "color": "#1F77B4", "link": "https://www.tableau.com/specialist"},
    {"name": "Professional Data Engineer", "issuer": "Google Cloud", "year": "2021", "emoji": "🔧", "color": "#4285F4", "link": "https://cloud.google.com/certification"},
    {"name": "Deep Learning Specialization", "issuer": "DeepLearning.AI", "year": "2020", "emoji": "🤖", "color": "#00BCD4", "link": "https://coursera.org/verify/deeplearning"},
]

# ─────────────────────────────────────────────
# DATA SKILLS
# ─────────────────────────────────────────────
SKILLS = {
    "💻 Programming": [
        ("Python", 95), ("SQL", 90), ("R", 75), ("Julia", 60), ("Bash/Shell", 80),
    ],
    "🤖 ML / Deep Learning": [
        ("TensorFlow / Keras", 90), ("PyTorch", 85), ("Scikit-learn", 95),
        ("XGBoost / LightGBM", 88), ("Hugging Face", 82),
    ],
    "🧠 AI / LLM": [
        ("LangChain", 88), ("OpenAI API", 90), ("RAG Systems", 85),
        ("Computer Vision", 82), ("NLP / Text Mining", 85),
    ],
    "📊 Data Viz & BI": [
        ("Tableau", 88), ("Power BI", 80), ("Plotly / Dash", 85), ("Streamlit", 92),
    ],
    "⚙️ MLOps & Engineering": [
        ("Docker / Kubernetes", 80), ("Apache Airflow", 82), ("MLflow", 85),
        ("FastAPI", 88), ("Git / GitHub", 92),
    ],
    "🗄️ Data & Cloud": [
        ("PostgreSQL", 88), ("BigQuery", 82), ("Apache Spark", 75),
        ("AWS", 78), ("Google Cloud", 80),
    ],
}

# ─────────────────────────────────────────────
# FUNGSI CSS TEMA (DARK MODE ONLY)
# ─────────────────────────────────────────────
def apply_theme():
    bg_primary = "#0E1117"
    bg_secondary = "#161B22"
    bg_card = "#1A2332"
    bg_card_hover = "#1E2A3B"
    text_primary = "#B4BAC0"
    text_secondary = "#8B949E"
    text_muted = "#6E7681"
    accent = "#7C3AED"
    accent_light = "#A78BFA"
    accent_secondary = "#2563EB"
    border_color = "#30363D"
    badge_bg = "#21262D"
    hero_gradient = "linear-gradient(135deg, #0E1117 0%, #1A1040 50%, #0E1117 100%)"
    timeline_bg = "#161B22"

    css = f"""
    <style>
    /* ===== GLOBAL RESET & BASE ===== */
    @import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');

    html, body, [class*="css"] {{
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }}

    .stApp {{
        background-color: {bg_primary} !important;
        color: {text_primary} !important;
    }}

    /* Sembunyikan sidebar default */
    section[data-testid="stSidebar"] {{
        display: none !important;
    }}

    /* Main content area - full width */
    .main .block-container {{
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1200px;
    }}

    /* Sembunyikan header default streamlit */
    header[data-testid="stHeader"] {{
        background: transparent !important;
    }}

    /* ===== HERO SECTION ===== */
    .hero-section {{
        background: {hero_gradient};
        border-radius: 20px;
        padding: 4rem 3rem;
        margin-bottom: 3rem;
        border: 1px solid {border_color};
        position: relative;
        overflow: hidden;
        text-align: center;
    }}
    .hero-section::before {{
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle at 30% 50%, {accent}15 0%, transparent 50%),
                    radial-gradient(circle at 70% 50%, {accent_secondary}10 0%, transparent 50%);
        pointer-events: none;
    }}
    .hero-name {{
        font-family: 'Space Mono', monospace !important;
        font-size: clamp(2rem, 5vw, 3.5rem);
        font-weight: 700;
        color: {text_primary};
        margin-bottom: 0.5rem;
        position: relative;
    }}
    .hero-name span {{
        color: {accent};
    }}
    .hero-subtitle {{
        font-size: 1.1rem;
        color: {text_secondary};
        margin-bottom: 2rem;
        letter-spacing: 0.05em;
    }}
    .hero-roles {{
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        gap: 0.75rem;
        margin-bottom: 2.5rem;
    }}
    .role-badge {{
        background: {badge_bg};
        border: 1px solid {border_color};
        color: {accent_light};
        padding: 0.4rem 1rem;
        border-radius: 50px;
        font-size: 0.85rem;
        font-weight: 600;
        letter-spacing: 0.03em;
    }}

    /* ===== NAVIGATION BUTTONS ===== */
    .nav-buttons {{
        display: flex;
        justify-content: center;
        gap: 1rem;
        margin-bottom: 3rem;
        flex-wrap: wrap;
    }}
    .nav-btn {{
        display: inline-block;
        padding: 0.6rem 1.5rem;
        border-radius: 50px;
        font-weight: 600;
        font-size: 0.9rem;
        text-decoration: none;
        cursor: pointer;
        border: 1px solid {border_color};
        background: {bg_secondary};
        color: {text_secondary};
        transition: all 0.2s ease;
    }}
    .nav-btn:hover {{
        background: {accent}15;
        border-color: {accent};
        color: {accent};
        transform: translateY(-2px);
    }}
    .nav-btn.active {{
        background: {accent};
        border-color: {accent};
        color: white;
    }}

    /* ===== SECTION HEADER ===== */
    .section-header {{
        margin-bottom: 2rem;
        padding-bottom: 1rem;
        border-bottom: 1px solid {border_color};
    }}
    .section-title {{
        font-family: 'Space Mono', monospace !important;
        font-size: 1.8rem;
        font-weight: 700;
        color: {text_primary};
        margin: 0;
    }}
    .section-title span {{
        color: {accent};
    }}
    .section-subtitle {{
        color: {text_secondary};
        margin-top: 0.25rem;
        font-size: 0.95rem;
    }}

    /* ===== PROJECT CARDS ===== */
    .project-card {{
        background: {bg_card};
        border: 1px solid {border_color};
        border-radius: 16px;
        padding: 1.5rem;
        height: 100%;
        transition: all 0.25s ease;
        position: relative;
        overflow: hidden;
    }}
    .project-card:hover {{
        background: {bg_card_hover};
        border-color: {accent}60;
        transform: translateY(-3px);
        box-shadow: 0 8px 25px {accent}20;
    }}
    .project-card::before {{
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 3px;
        background: linear-gradient(90deg, {accent}, {accent_secondary});
        border-radius: 16px 16px 0 0;
        opacity: 0;
        transition: opacity 0.25s ease;
    }}
    .project-card:hover::before {{
        opacity: 1;
    }}
    .project-emoji {{
        font-size: 2.5rem;
        margin-bottom: 0.75rem;
        display: block;
    }}
    .project-title {{
        font-weight: 700;
        font-size: 1.05rem;
        color: {text_primary};
        margin-bottom: 0.5rem;
    }}
    .project-categories {{
        display: flex;
        flex-wrap: wrap;
        gap: 0.5rem;
        margin-bottom: 0.75rem;
    }}
    .project-category-badge {{
        display: inline-block;
        padding: 0.2rem 0.7rem;
        border-radius: 50px;
        font-size: 0.72rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }}
    .cat-da {{ background: #05966920; color: #34D399; border: 1px solid #05966940; }}
    .cat-ds {{ background: #2563EB20; color: #60A5FA; border: 1px solid #2563EB40; }}
    .cat-mle {{ background: #D9770620; color: #FB923C; border: 1px solid #D9770640; }}
    .cat-aie {{ background: #7C3AED20; color: {accent_light}; border: 1px solid #7C3AED40; }}
    .cat-de {{ background: #0EA5E920; color: #7DD3FC; border: 1px solid #0EA5E940; }}
    
    .project-description {{
        color: {text_secondary};
        font-size: 0.875rem;
        line-height: 1.6;
        margin-bottom: 1rem;
    }}
    .tech-tags {{
        display: flex;
        flex-wrap: wrap;
        gap: 0.4rem;
        margin-bottom: 1rem;
    }}
    .tech-tag {{
        background: {badge_bg};
        border: 1px solid {border_color};
        color: {text_muted};
        padding: 0.2rem 0.6rem;
        border-radius: 6px;
        font-size: 0.72rem;
        font-weight: 500;
        font-family: 'Space Mono', monospace;
    }}
    
    /* Project Buttons */
    .project-buttons {{
        display: flex;
        gap: 0.75rem;
        margin-top: 1rem;
    }}
    .project-btn {{
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        padding: 0.5rem 1rem;
        border-radius: 8px;
        font-size: 0.85rem;
        font-weight: 600;
        text-decoration: none;
        transition: all 0.2s ease;
        cursor: pointer;
        border: 1px solid;
    }}
    .project-btn-github {{
        background: {badge_bg};
        border-color: {border_color};
        color: {text_primary};
    }}
    .project-btn-github:hover {{
        background: #6e5494;
        border-color: #6e5494;
        color: white;
        transform: translateY(-2px);
    }}
    .project-btn-demo {{
        background: {badge_bg};
        border-color: {border_color};
        color: {text_primary};
    }}
    .project-btn-demo:hover {{
        background: {accent};
        border-color: {accent};
        color: white;
        transform: translateY(-2px);
    }}

    /* ===== FIX: EXPANDER BACKGROUND ===== */
    div[data-testid="stExpander"] {{
        background: {bg_card} !important;
        border: 1px solid {border_color} !important;
        border-radius: 12px !important;
        margin-top: 1rem;
    }}
    div[data-testid="stExpander"] summary {{
        color: {text_primary} !important;
        background: {bg_card} !important;
        border-radius: 12px !important;
    }}
    div[data-testid="stExpander"] div[data-testid="stExpanderDetails"] {{
        background: {bg_secondary} !important;
        border-top: 1px solid {border_color} !important;
        border-radius: 0 0 12px 12px !important;
        padding: 1rem !important;
    }}

    /* ===== SKILL SECTION ===== */
    .skill-category {{
        background: {bg_card};
        border: 1px solid {border_color};
        border-radius: 16px;
        padding: 1.5rem;
        margin-bottom: 1.25rem;
    }}
    .skill-category-title {{
        font-weight: 700;
        font-size: 1rem;
        color: {text_primary};
        margin-bottom: 1rem;
    }}
    .skill-item {{
        margin-bottom: 0.75rem;
    }}
    .skill-label {{
        display: flex;
        justify-content: space-between;
        color: {text_secondary};
        font-size: 0.85rem;
        margin-bottom: 0.3rem;
        font-weight: 500;
    }}
    .skill-bar-bg {{
        background: {badge_bg};
        border-radius: 50px;
        height: 6px;
        overflow: hidden;
    }}
    .skill-bar-fill {{
        height: 100%;
        border-radius: 50px;
        background: linear-gradient(90deg, {accent}, {accent_secondary});
        transition: width 0.5s ease;
    }}

    /* ===== TIMELINE ===== */
    .timeline-item {{
        background: {timeline_bg};
        border: 1px solid {border_color};
        border-radius: 16px;
        padding: 1.75rem;
        margin-bottom: 1.25rem;
        position: relative;
        border-left: 4px solid {accent};
    }}
    .timeline-header {{
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        flex-wrap: wrap;
        gap: 0.5rem;
        margin-bottom: 0.5rem;
    }}
    .timeline-title {{
        font-weight: 700;
        font-size: 1.1rem;
        color: {text_primary};
    }}
    .timeline-company {{
        color: {accent};
        font-weight: 600;
        font-size: 0.95rem;
    }}
    .timeline-period {{
        background: {badge_bg};
        color: {text_secondary};
        padding: 0.25rem 0.75rem;
        border-radius: 50px;
        font-size: 0.78rem;
        font-weight: 600;
        font-family: 'Space Mono', monospace;
        white-space: nowrap;
    }}
    .timeline-location {{
        color: {text_muted};
        font-size: 0.82rem;
        margin-bottom: 1rem;
    }}
    .timeline-points {{
        list-style: none;
        padding: 0;
        margin: 0;
    }}
    .timeline-points li {{
        color: {text_secondary};
        font-size: 0.875rem;
        padding: 0.3rem 0;
        padding-left: 1.25rem;
        position: relative;
        line-height: 1.6;
    }}
    .timeline-points li::before {{
        content: '▸';
        position: absolute;
        left: 0;
        color: {accent};
        font-size: 0.8rem;
    }}

    /* ===== CERTIFICATION CARD ===== */
    .cert-card {{
        background: {bg_card};
        border: 1px solid {border_color};
        border-radius: 12px;
        padding: 1.25rem;
        display: flex;
        align-items: center;
        gap: 1rem;
        transition: all 0.2s ease;
        margin-bottom: 0.75rem;
        cursor: pointer;
    }}
    .cert-card:hover {{
        border-color: {accent}50;
        background: {bg_card_hover};
        transform: translateX(4px);
    }}
    .cert-emoji {{
        font-size: 2rem;
        width: 3rem;
        text-align: center;
        flex-shrink: 0;
    }}
    .cert-info {{
        flex: 1;
    }}
    .cert-name {{
        font-weight: 700;
        font-size: 0.9rem;
        color: {text_primary};
        margin-bottom: 0.2rem;
    }}
    .cert-issuer {{
        color: {text_secondary};
        font-size: 0.8rem;
    }}
    .cert-year {{
        font-family: 'Space Mono', monospace;
        color: {accent};
        font-weight: 700;
        font-size: 0.85rem;
        flex-shrink: 0;
    }}
    .cert-link {{
        color: {accent_light};
        text-decoration: none;
        font-size: 0.8rem;
        margin-left: 0.5rem;
    }}
    .cert-link:hover {{
        text-decoration: underline;
    }}

    /* ===== ABOUT SECTION ===== */
    .about-card {{
        background: {bg_card};
        border: 1px solid {border_color};
        border-radius: 16px;
        padding: 2rem;
    }}
    .about-text {{
        color: {text_secondary};
        font-size: 0.95rem;
        line-height: 1.8;
        margin-bottom: 1rem;
    }}
    .stat-box {{
        background: {badge_bg};
        border: 1px solid {border_color};
        border-radius: 12px;
        padding: 1.25rem;
        text-align: center;
    }}
    .stat-number {{
        font-family: 'Space Mono', monospace;
        font-size: 2rem;
        font-weight: 700;
        color: {accent};
        display: block;
    }}
    .stat-label {{
        color: {text_secondary};
        font-size: 0.8rem;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.08em;
    }}

    /* ===== CONTACT SECTION ===== */
    .social-link {{
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        padding: 0.75rem 1.25rem;
        background: {badge_bg};
        border: 1px solid {border_color};
        border-radius: 10px;
        color: {text_primary} !important;
        text-decoration: none !important;
        font-weight: 600;
        font-size: 0.875rem;
        transition: all 0.2s ease;
        margin: 0.3rem;
    }}
    .social-link:hover {{
        background: {accent}15;
        border-color: {accent};
        color: {accent} !important;
        transform: translateY(-2px);
    }}

    /* ===== FORM INPUT STYLES ===== */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea,
    .stSelectbox > div > div {{
        background: {bg_secondary} !important;
        color: {text_primary} !important;
        border: 1px solid {border_color} !important;
        border-radius: 10px !important;
    }}
    .stTextInput > div > div > input::placeholder,
    .stTextArea > div > div > textarea::placeholder {{
        color: {text_secondary} !important;
        opacity: 0.7 !important;
    }}
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus {{
        border-color: {accent} !important;
        box-shadow: 0 0 0 2px {accent}20 !important;
    }}
    .stSelectbox > div > div {{
        background: {bg_secondary} !important;
        color: {text_primary} !important;
        border: 1px solid {border_color} !important;
        border-radius: 10px !important;
    }}
    label[data-testid="stWidgetLabel"] p {{
        color: {text_primary} !important;
        font-weight: 600 !important;
    }}

    /* ===== SUBMIT BUTTON ===== */
    .stButton > button {{
        background: {bg_secondary} !important;
        color: {text_primary} !important;
        border: 1px solid {accent} !important;
        border-radius: 50px !important;
        font-weight: 700 !important;
        padding: 0.6rem 2rem !important;
        transition: all 0.2s ease !important;
    }}
    .stButton > button:hover {{
        background: {accent} !important;
        color: white !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 4px 15px {accent}40 !important;
        border-color: {accent} !important;
    }}
    .stRadio > div {{
        gap: 0.5rem;
    }}
    hr {{
        border-color: {border_color} !important;
    }}
    div[data-testid="stMetric"] {{
        background: {bg_card};
        border: 1px solid {border_color};
        border-radius: 12px;
        padding: 1rem;
    }}
    div[data-testid="stMetricValue"] {{
        color: {accent} !important;
        font-family: 'Space Mono', monospace !important;
    }}
    div[data-testid="stMetricLabel"] {{
        color: {text_secondary} !important;
    }}
    div[data-testid="stAlert"] {{
        border-radius: 12px !important;
    }}
    ::-webkit-scrollbar {{ width: 6px; height: 6px; }}
    ::-webkit-scrollbar-track {{ background: {bg_secondary}; }}
    ::-webkit-scrollbar-thumb {{ background: {border_color}; border-radius: 3px; }}
    ::-webkit-scrollbar-thumb:hover {{ background: {accent}; }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)


# ─────────────────────────────────────────────
# HELPER: CATEGORY CSS CLASS
# ─────────────────────────────────────────────
def cat_class(category):
    mapping = {
        "Data Analyst": "cat-da",
        "Data Scientist": "cat-ds",
        "ML Engineer": "cat-mle",
        "AI Engineer": "cat-aie",
        "Data Engineer": "cat-de",
    }
    return mapping.get(category, "cat-da")


# ─────────────────────────────────────────────
# HELPER: GENERATE PROJECT BUTTONS HTML
# ─────────────────────────────────────────────
def generate_project_buttons(proj):
    buttons_html = '<div class="project-buttons">'
    
    # Tambahkan tombol GitHub jika link tersedia
    if proj.get("github") and proj["github"].strip():
        buttons_html += f'<a href="{proj["github"]}" target="_blank" class="project-btn project-btn-github">🐙 GitHub</a>'
    
    # Tambahkan tombol Demo jika link tersedia
    if proj.get("demo") and proj["demo"].strip():
        buttons_html += f'<a href="{proj["demo"]}" target="_blank" class="project-btn project-btn-demo">🚀 Live Demo</a>'
    
    buttons_html += '</div>'
    
    # Jika tidak ada tombol sama sekali, return string kosong
    if buttons_html == '<div class="project-buttons"></div>':
        return ""
    
    return buttons_html


# ─────────────────────────────────────────────
# HALAMAN: BERANDA
# ─────────────────────────────────────────────
def page_home():
    # Hero Section
    st.markdown("""
    <div class="hero-section">
        <div class="hero-name">Halo, saya <span>Alex Rivera</span> 👋</div>
        <p class="hero-subtitle">Membangun solusi berbasis data yang berdampak nyata</p>
        <div class="hero-roles">
            <span class="role-badge">📊 Data Analyst</span>
            <span class="role-badge">🔬 Data Scientist</span>
            <span class="role-badge">⚙️ ML Engineer</span>
            <span class="role-badge">🤖 AI Engineer</span>
        </div>
        <p style="color: #8B949E; font-size: 0.95rem; max-width: 600px; margin: 0 auto 2rem;">
            5+ tahun pengalaman membangun pipeline data, model ML, dan sistem AI — 
            dari exploratory analysis hingga production deployment.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Quick Stats
    st.markdown('<div class="section-header"><p class="section-title">📈 Quick <span>Stats</span></p></div>', unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    stats = [("5+", "Tahun Pengalaman"), ("30+", "Proyek Selesai"), ("12+", "Model Production"), ("6", "Sertifikasi")]
    for col, (num, label) in zip([c1, c2, c3, c4], stats):
        with col:
            st.markdown(f"""
            <div class="stat-box">
                <span class="stat-number">{num}</span>
                <span class="stat-label">{label}</span>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Featured Projects
    st.markdown('<div class="section-header"><p class="section-title">🌟 Proyek <span>Unggulan</span></p><p class="section-subtitle">Beberapa karya terbaik pilihan</p></div>', unsafe_allow_html=True)

    featured = [p for p in PROJECTS if p["id"] in [1, 3, 5, 7]]
    cols = st.columns(2)
    for i, proj in enumerate(featured):
        with cols[i % 2]:
            # Buat badge untuk setiap kategori
            cat_badges = "".join(f'<span class="project-category-badge {cat_class(cat)}">{cat}</span>' for cat in proj["category"])
            tech_html = "".join(f'<span class="tech-tag">{t}</span>' for t in proj["tech"][:4])
            buttons_html = generate_project_buttons(proj)
            
            st.markdown(f"""
            <div class="project-card">
                <span class="project-emoji">{proj['emoji']}</span>
                <div class="project-title">{proj['name']}</div>
                <div class="project-categories">{cat_badges}</div>
                <p class="project-description">{proj['description']}</p>
                <div class="tech-tags">{tech_html}</div>
                {buttons_html}
            </div>
            """, unsafe_allow_html=True)
            with st.expander("📂 Lihat Detail"):
                st.markdown(f"**{proj['name']}**")
                st.write(proj["detail"])
                

# ─────────────────────────────────────────────
# HALAMAN: TENTANG SAYA
# ─────────────────────────────────────────────
def page_about():
    st.markdown('<div class="section-header"><p class="section-title">👤 Tentang <span>Saya</span></p></div>', unsafe_allow_html=True)

    col_bio, col_photo = st.columns([3, 1])
    with col_bio:
        st.markdown("""
        <div class="about-card">
            <p class="about-text">
                Halo! Saya <strong>Alex Rivera</strong>, seorang profesional data yang bersemangat dalam mengubah
                data mentah menjadi insight yang bermakna dan solusi AI yang berdampak.
            </p>
            <p class="about-text">
                Saya memulai perjalanan sebagai <strong>Data Analyst</strong> di StartupX, di mana saya belajar
                bercerita melalui data. Rasa ingin tahu yang besar mendorong saya untuk mendalami machine learning,
                hingga akhirnya berkembang menjadi <strong>ML Engineer</strong> dan kini <strong>AI Engineer</strong>
                yang membangun sistem berbasis LLM dan computer vision.
            </p>
            <p class="about-text">
                Lulus dari Universitas Indonesia dengan jurusan Ilmu Komputer (2019), saya percaya bahwa
                kekuatan sejati data terletak bukan hanya pada analisis — tetapi pada kemampuannya untuk
                membuat keputusan bisnis yang lebih cerdas dan produk yang lebih baik.
            </p>
            <p class="about-text">
                Di luar pekerjaan, saya aktif sebagai <strong>open-source contributor</strong>, penulis
                blog teknis, dan pembicara di beberapa meetup komunitas data Indonesia.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col_photo:
        st.markdown("""
        <div style="text-align: center; padding: 2rem 0;">
            <div style="width: 140px; height: 140px; border-radius: 50%; background: linear-gradient(135deg, #7C3AED, #2563EB);
                        display: flex; align-items: center; justify-content: center; font-size: 4rem;
                        margin: 0 auto 1rem; border: 4px solid #30363D; box-shadow: 0 8px 25px #7C3AED40;">
                👨‍💻
            </div>
            <div style="font-weight: 700; font-size: 1rem; margin-bottom: 0.25rem;">Alex Rivera</div>
            <div style="color: #8B949E; font-size: 0.8rem;">Surabaya, Indonesia 🇮🇩</div>
            <div style="color: #7C3AED; font-size: 0.8rem; margin-top: 0.25rem;">● Available for hire</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Skills
    st.markdown('<div class="section-header"><p class="section-title">🛠️ Skill & <span>Teknologi</span></p></div>', unsafe_allow_html=True)

    skill_keys = list(SKILLS.keys())
    col1, col2 = st.columns(2)
    for i, key in enumerate(skill_keys):
        col = col1 if i % 2 == 0 else col2
        with col:
            with st.container():
                st.markdown(f'<div class="skill-category"><div class="skill-category-title">{key}</div>', unsafe_allow_html=True)
                for skill_name, level in SKILLS[key]:
                    st.markdown(f"""
                    <div class="skill-item">
                        <div class="skill-label">
                            <span>{skill_name}</span>
                            <span>{level}%</span>
                        </div>
                        <div class="skill-bar-bg">
                            <div class="skill-bar-fill" style="width: {level}%;"></div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)


# ─────────────────────────────────────────────
# HALAMAN: PROYEK
# ─────────────────────────────────────────────
def page_projects():
    st.markdown('<div class="section-header"><p class="section-title">🗂️ Proyek-<span>Proyek</span></p><p class="section-subtitle">Klik kategori untuk filter</p></div>', unsafe_allow_html=True)

    categories = ["Semua", "Data Analyst", "Data Scientist", "ML Engineer", "AI Engineer", "Data Engineer"]
    selected = st.selectbox(
        "Filter Kategori:",
        options=categories,
    )

    if selected == "Semua":
        filtered = PROJECTS
    else:
        filtered = [p for p in PROJECTS if selected in p["category"]]

    st.markdown(f"<p style='color: #8B949E; font-size: 0.85rem; margin-bottom: 1.5rem;'>Menampilkan {len(filtered)} proyek</p>", unsafe_allow_html=True)

    cols = st.columns(2)
    for i, proj in enumerate(filtered):
        with cols[i % 2]:
            cat_badges = "".join(f'<span class="project-category-badge {cat_class(cat)}">{cat}</span>' for cat in proj["category"])
            tech_html = "".join(f'<span class="tech-tag">{t}</span>' for t in proj["tech"])
            buttons_html = generate_project_buttons(proj)
            
            st.markdown(f"""
            <div class="project-card">
                <span class="project-emoji">{proj['emoji']}</span>
                <div class="project-title">{proj['name']}</div>
                <div class="project-categories">{cat_badges}</div>
                <p class="project-description">{proj['description']}</p>
                <div class="tech-tags">{tech_html}</div>
                {buttons_html}
            </div>
            """, unsafe_allow_html=True)
            with st.expander("📂 Lihat Detail Proyek"):
                st.markdown(f"#### {proj['emoji']} {proj['name']}")
                st.write(proj["detail"])
                

# ─────────────────────────────────────────────
# HALAMAN: PENGALAMAN & SERTIFIKASI
# ─────────────────────────────────────────────
def page_experience():
    st.markdown('<div class="section-header"><p class="section-title">💼 Pengalaman <span>Kerja</span></p></div>', unsafe_allow_html=True)

    for exp in EXPERIENCES:
        points_html = "".join(f"<li>{p}</li>" for p in exp["points"])
        st.markdown(f"""
        <div class="timeline-item" style="border-left-color: {exp['color']};">
            <div class="timeline-header">
                <div>
                    <div class="timeline-title">{exp['emoji']} {exp['title']}</div>
                    <div class="timeline-company">🏢 {exp['company']}</div>
                </div>
                <span class="timeline-period">{exp['period']}</span>
            </div>
            <div class="timeline-location">📍 {exp['location']}</div>
            <ul class="timeline-points">
                {points_html}
            </ul>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="section-header"><p class="section-title">🏆 Sertifikasi <span>& Pendidikan</span></p></div>', unsafe_allow_html=True)

    col_cert, col_edu = st.columns([3, 2])

    with col_cert:
        st.markdown("**📜 Sertifikasi Profesional**")
        for cert in CERTIFICATIONS:
            # Tambahkan link jika ada
            link_html = f'<a href="{cert["link"]}" target="_blank" class="cert-link">🔗 Lihat Sertifikat</a>' if cert.get("link") else ""
            st.markdown(f"""
            <a href="{cert.get('link', '#')}" target="_blank" style="text-decoration: none;">
                <div class="cert-card">
                    <div class="cert-emoji">{cert['emoji']}</div>
                    <div class="cert-info">
                        <div class="cert-name">{cert['name']} {link_html}</div>
                        <div class="cert-issuer">{cert['issuer']}</div>
                    </div>
                    <div class="cert-year">{cert['year']}</div>
                </div>
            </a>
            """, unsafe_allow_html=True)

    with col_edu:
        st.markdown("**🎓 Pendidikan**")
        st.markdown("""
        <div class="timeline-item" style="border-left-color: #7C3AED;">
            <div class="timeline-title">🎓 S1 Ilmu Komputer</div>
            <div class="timeline-company">Universitas Indonesia</div>
            <div class="timeline-location">📍 Depok, 2015 – 2019 · IPK 3.72</div>
            <ul class="timeline-points">
                <li>Spesialisasi Machine Learning & Data Mining</li>
                <li>Skripsi: Deteksi Fraud Keuangan menggunakan Ensemble Learning</li>
                <li>Ketua Divisi AI di UKM Computing UI</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("**🌏 Bahasa**")
        langs = [("Bahasa Indonesia", "Native", 100), ("Inggris", "Professional", 90), ("Mandarin", "Conversational", 45)]
        for lang, level, pct in langs:
            st.markdown(f"""
            <div class="skill-item" style="margin-bottom: 0.75rem;">
                <div class="skill-label"><span>{lang}</span><span style="font-size:0.75rem;">{level}</span></div>
                <div class="skill-bar-bg">
                    <div class="skill-bar-fill" style="width: {pct}%;"></div>
                </div>
            </div>
            """, unsafe_allow_html=True)


# ─────────────────────────────────────────────
# HALAMAN: KONTAK
# ─────────────────────────────────────────────
def page_contact():
    import requests
    st.markdown('<div class="section-header"><p class="section-title">📬 Hubungi <span>Saya</span></p><p class="section-subtitle">Ada proyek menarik? Mari ngobrol!</p></div>', unsafe_allow_html=True)

    col_form, col_info = st.columns([3, 2])

    with col_form:
        with st.form("contact_form"):
            st.markdown("#### ✉️ Kirim Pesan")
            name = st.text_input("Nama Lengkap", placeholder="Contoh: Budi Santoso")
            email = st.text_input("Alamat Email", placeholder="budi@email.com")
            subject = st.selectbox("Topik", [
                "Kolaborasi Proyek",
                "Penawaran Freelance",
                "Peluang Full-time",
                "Pertanyaan Teknis",
                "Lainnya",
            ])
            message = st.text_area("Pesan", placeholder="Ceritakan detail proyek atau pertanyaan Anda...", height=150)
            submitted = st.form_submit_button("🚀 Kirim Pesan", use_container_width=True)

            if submitted:
                if name and email and message:
                    # Kirim ke FormSubmit
                    webhook_url = "https://formsubmit.co/ajax/primaazhari16@gmail.com"  # Ganti dengan email Anda
                    
                    data = {
                        "name": name,
                        "email": email,
                        "subject": subject,
                        "message": message,
                        "_subject": f"[Portfolio] {subject} dari {name}",
                        "_captcha": "false",  # Nonaktifkan captcha (opsional)
                        "_template": "table",  # Template email yang rapi
                    }
                    
                    try:
                        response = requests.post(webhook_url, data=data)
                        if response.status_code == 200:
                            st.success(f"✅ Terima kasih, **{name}**! Pesan Anda telah terkirim. Saya akan merespon dalam 1x24 jam.")
                            st.balloons()
                        else:
                            st.error("❌ Gagal mengirim pesan. Silakan coba lagi nanti.")
                    except Exception as e:
                        st.error(f"❌ Terjadi kesalahan: {str(e)}")
                else:
                    st.warning("⚠️ Mohon lengkapi semua field yang wajib diisi.")

    with col_info:
        st.markdown("""
        <div class="about-card">
            <p style="font-weight: 700; font-size: 1rem; margin-bottom: 1rem;">📍 Info Kontak</p>
            <p style="font-size: 0.875rem; margin-bottom: 0.5rem;">📧 alex.rivera@email.com</p>
            <p style="font-size: 0.875rem; margin-bottom: 0.5rem;">📱 +62 812-3456-7890</p>
            <p style="font-size: 0.875rem; margin-bottom: 0.5rem;">📍 Surabaya, Jawa Timur, Indonesia</p>
            <p style="font-size: 0.875rem; margin-bottom: 1.5rem;">⏰ Responsif dalam 24 jam</p>
            <hr style="margin: 1rem 0;">
            <p style="font-weight: 700; font-size: 0.9rem; margin-bottom: 0.75rem;">🌐 Media Sosial</p>
        </div>
        """, unsafe_allow_html=True)

        socials = [
            ("💼 LinkedIn", "#", "linkedin"),
            ("🐙 GitHub", "#", "github"),
            ("🐦 Twitter / X", "#", "twitter"),
            ("📝 Medium Blog", "#", "medium"),
            ("🎥 YouTube", "#", "youtube"),
        ]
        links_html = "".join(
            f'<a href="{url}" class="social-link" target="_blank">{label}</a>'
            for label, url, _ in socials
        )
        st.markdown(f'<div style="display:flex; flex-wrap:wrap; gap:0.5rem;">{links_html}</div>', unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("""
        <div class="stat-box" style="margin-top: 1rem;">
            <span class="stat-number">🟢</span>
            <span class="stat-label">Open to Opportunities</span>
            <p style="font-size: 0.8rem; color: #8B949E; margin-top: 0.5rem;">
                Freelance · Remote · Full-time
            </p>
        </div>
        """, unsafe_allow_html=True)


# ─────────────────────────────────────────────
# NAVIGASI COMPONENT
# ─────────────────────────────────────────────
def render_navigation():
    # Inisialisasi session state untuk halaman aktif
    if 'current_page' not in st.session_state:
        st.session_state.current_page = 'home'
    
    # CSS untuk tombol navigasi sudah didefinisikan di apply_theme()
    
    # Buat tombol navigasi
    col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])
    
    with col1:
        if st.button("🏠 Beranda", key="nav_home", use_container_width=True):
            st.session_state.current_page = 'home'
            st.rerun()
    
    with col2:
        if st.button("👤 Tentang", key="nav_about", use_container_width=True):
            st.session_state.current_page = 'about'
            st.rerun()
    
    with col3:
        if st.button("🗂️ Proyek", key="nav_projects", use_container_width=True):
            st.session_state.current_page = 'projects'
            st.rerun()
    
    with col4:
        if st.button("💼 Pengalaman", key="nav_experience", use_container_width=True):
            st.session_state.current_page = 'experience'
            st.rerun()
    
    with col5:
        if st.button("📬 Kontak", key="nav_contact", use_container_width=True):
            st.session_state.current_page = 'contact'
            st.rerun()
    
    st.markdown("---")


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────
def main():
    # Terapkan tema
    apply_theme()
    
    # Hapus sidebar default
    st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            display: none;
        }
        [data-testid="collapsedControl"] {
            display: none;
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Header dengan info kontak sederhana
    st.markdown("""
    <div style="display: flex; justify-content: space-between; align-items: center; padding: 1rem 0; border-bottom: 1px solid #30363D; margin-bottom: 2rem;">
        <div>
            <span style="font-family: 'Space Mono', monospace; font-weight: 700; font-size: 1.2rem;">Alex Rivera</span>
            <span style="color: #7C3AED; margin-left: 0.5rem;">|</span>
            <span style="color: #8B949E; font-size: 0.9rem;">Data & AI Professional</span>
        </div>
        <div style="color: #8B949E; font-size: 0.85rem;">
            📧 alex.rivera@email.com | 📍 Surabaya
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Render navigasi
    render_navigation()
    
    # Tampilkan halaman berdasarkan session state
    if st.session_state.current_page == 'home':
        page_home()
    elif st.session_state.current_page == 'about':
        page_about()
    elif st.session_state.current_page == 'projects':
        page_projects()
    elif st.session_state.current_page == 'experience':
        page_experience()
    elif st.session_state.current_page == 'contact':
        page_contact()
    
    # Footer
    st.markdown("""
    <div style="text-align: center; padding: 2rem 0 1rem 0; margin-top: 2rem; border-top: 1px solid #30363D; color: #6E7681; font-size: 0.8rem;">
        © 2025 Alex Rivera | Built with Streamlit 💜
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
