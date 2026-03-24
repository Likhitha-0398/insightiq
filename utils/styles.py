import streamlit as st

def apply_styles():
    st.markdown("""
    <style>
    /* ===== IMPORT FONT ===== */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');

    /* ===== GLOBAL ===== */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    /* ===== BACKGROUND ===== */
    .stApp {
        background: linear-gradient(135deg, #EBF3FB 0%, #FFFFFF 50%, #E8F4FD 100%);
        background-attachment: fixed;
    }

    /* ===== SIDEBAR ===== */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1F4E79 0%, #2E75B6 100%) !important;
        border-right: 3px solid #2E75B6;
    }

    [data-testid="stSidebar"] * {
        color: white !important;
        font-weight: 700 !important;
    }

    [data-testid="stSidebar"] .stMarkdown p {
        color: white !important;
        font-weight: 800 !important;
        font-size: 18px !important;
    }

    [data-testid="stSidebarNav"] a {
        color: white !important;
        font-weight: 700 !important;
        font-size: 15px !important;
        border-radius: 8px !important;
        padding: 8px 12px !important;
        transition: all 0.3s ease !important;
    }

    [data-testid="stSidebarNav"] a:hover {
        background-color: rgba(255,255,255,0.2) !important;
        color: white !important;
        transform: translateX(5px) !important;
    }

    [data-testid="stSidebarNav"] a[aria-selected="true"] {
        background-color: rgba(255,255,255,0.3) !important;
        color: white !important;
        border-left: 4px solid white !important;
    }

    /* ===== SIDEBAR TITLE ===== */
    .sidebar-title {
        color: white !important;
        font-size: 26px !important;
        font-weight: 800 !important;
        text-align: center !important;
        padding: 20px 0 10px 0 !important;
        letter-spacing: 2px !important;
        border-bottom: 2px solid rgba(255,255,255,0.3) !important;
        margin-bottom: 20px !important;
    }

    /* ===== METRIC CARDS ===== */
    [data-testid="stMetric"] {
        background: white !important;
        border-radius: 12px !important;
        padding: 20px !important;
        box-shadow: 0 4px 15px rgba(46, 117, 182, 0.15) !important;
        border-top: 4px solid #2E75B6 !important;
        transition: transform 0.2s ease !important;
    }

    [data-testid="stMetric"]:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 8px 25px rgba(46, 117, 182, 0.25) !important;
    }

    [data-testid="stMetricLabel"] {
        color: #666666 !important;
        font-weight: 600 !important;
        font-size: 13px !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
    }

    [data-testid="stMetricValue"] {
        color: #1F4E79 !important;
        font-weight: 800 !important;
        font-size: 30px !important;
    }

    /* ===== PAGE TITLES ===== */
    h1 {
        color: #1F4E79 !important;
        font-weight: 800 !important;
        font-size: 38px !important;
        border-bottom: 3px solid #2E75B6 !important;
        padding-bottom: 10px !important;
    }

    h2, h3 {
        color: #2E75B6 !important;
        font-weight: 700 !important;
    }

    /* ===== BUTTONS ===== */
    .stButton > button {
        background: linear-gradient(135deg, #1F4E79, #2E75B6) !important;
        color: white !important;
        font-weight: 700 !important;
        font-size: 16px !important;
        border-radius: 10px !important;
        border: none !important;
        padding: 12px 30px !important;
        box-shadow: 0 4px 15px rgba(46, 117, 182, 0.3) !important;
        transition: all 0.3s ease !important;
        width: 100% !important;
    }

    .stButton > button:hover {
        background: linear-gradient(135deg, #2E75B6, #1F4E79) !important;
        box-shadow: 0 6px 20px rgba(46, 117, 182, 0.5) !important;
        transform: translateY(-2px) !important;
    }

    /* ===== INPUT FIELDS ===== */
    .stTextInput > div > div > input {
        border: 2px solid #2E75B6 !important;
        border-radius: 10px !important;
        font-size: 15px !important;
        padding: 10px 15px !important;
        transition: all 0.3s ease !important;
        color: #1F4E79 !important;
        background-color: white !important;
    }

    .stTextInput > div > div > input:focus {
        border-color: #1F4E79 !important;
        box-shadow: 0 0 0 3px rgba(46, 117, 182, 0.2) !important;
    }

    /* ===== SLIDERS ===== */
    .stSlider > div > div > div > div {
        background: linear-gradient(135deg, #1F4E79, #2E75B6) !important;
    }

    /* ===== ALERTS ===== */
    .stSuccess {
        background-color: #d4edda !important;
        border-left: 5px solid #28a745 !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
    }

    .stError {
        background-color: #f8d7da !important;
        border-left: 5px solid #dc3545 !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
    }

    .stInfo {
        background-color: #E6F1FB !important;
        border-left: 5px solid #2E75B6 !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
    }

    /* ===== CHARTS ===== */
    .js-plotly-plot {
        border-radius: 12px !important;
        box-shadow: 0 4px 15px rgba(46, 117, 182, 0.1) !important;
    }

    /* ===== DIVIDER ===== */
    hr {
        border-color: #2E75B6 !important;
        opacity: 0.3 !important;
    }

    /* ===== BLOCK CONTAINER ===== */
    .block-container {
        padding-top: 2rem !important;
        max-width: 1200px !important;
    }

    /* ===== NUMBER INPUT ===== */
    .stNumberInput > div > div > input {
        border: 2px solid #2E75B6 !important;
        border-radius: 8px !important;
        color: #1F4E79 !important;
        background-color: white !important;
    }

    /* ===== SPINNER ===== */
    .stSpinner > div {
        border-top-color: #2E75B6 !important;
    }

    /* ===== FIX INPUT TEXT AND LABEL VISIBILITY ===== */
    [data-testid="stNumberInput"] input {
        color: #1F4E79 !important;
        background-color: white !important;
        font-weight: 600 !important;
    }

    [data-testid="stTextInput"] input {
        color: #1F4E79 !important;
        background-color: white !important;
        font-weight: 600 !important;
    }

    .stNumberInput label {
        color: #1F4E79 !important;
        font-weight: 700 !important;
    }

    .stTextInput label {
        color: #1F4E79 !important;
        font-weight: 700 !important;
    }

    .stSlider label {
        color: #1F4E79 !important;
        font-weight: 700 !important;
    }

    </style>
    """, unsafe_allow_html=True)