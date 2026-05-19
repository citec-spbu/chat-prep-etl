import streamlit as st

def load_css():
    st.markdown("""
    <style>

    /* MAIN BACKGROUND */

    .stApp {
        background: linear-gradient(
            135deg,
            #0f172a 0%,
            #111827 50%,
            #1e1b4b 100%
        );
    }
    /* CARDS */

    [data-testid="column"] {

        background: rgba(30, 27, 75, 0.55);
        border-radius: 28px;
        padding: 28px;
        border: 1px solid rgba(139, 92, 246, 0.18);
        backdrop-filter: blur(18px);
    }
                
    /* TITLES */

    h1 {
        color: white !important;
        font-size: 42px !important;
        font-weight: 700 !important;
    }

    h2, h3 {
        color: #c084fc !important;
    }
    /* INPUTS */

    .stTextInput input,
    .stNumberInput input,
    .stSelectbox div[data-baseweb="select"] {

        background-color: rgba(255,255,255,0.03) !important;

        border-radius: 16px !important;

        border: 1px solid rgba(139,92,246,0.2) !important;

        color: white !important;
    }
    /* BUTTONS */

    .stButton button {

        width: 100%;

        height: 54px;

        border-radius: 18px;

        border: none;

        background: linear-gradient(
            90deg,
            #7c3aed,
            #8b5cf6
        );

        color: white;

        font-size: 17px;

        font-weight: 600;

        transition: 0.3s ease;
    }
    /* HOVER */

    .stButton button:hover {

        transform: scale(1.02);

        box-shadow: 0 0 24px rgba(139,92,246,0.35);
    }

    /* LABELS */

    label {
        color: #d1d5db !important;
    }

    /* SUCCESS */

    .stSuccess {
        border-radius: 16px;
    }

    /* WARNING */

    .stWarning {
        border-radius: 16px;
    }

    /* RESULTS BLOCK */

    .result-box {

        background: rgba(255,255,255,0.03);

        border-radius: 18px;

        padding: 18px;

        margin-bottom: 15px;

        border: 1px solid rgba(139,92,246,0.15);
    }

    </style>
    """, unsafe_allow_html=True)