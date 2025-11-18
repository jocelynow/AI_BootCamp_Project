import streamlit as st
from utility import check_password 

st.set_page_config(page_title="TravelPal", page_icon="🌍", layout="wide")

# Check if the password is correct.  
if not check_password():  
    st.stop()

# ---------- HIDE SIDEBAR FOR HOME PAGE ----------
hide_sidebar_style = """
<style>
[data-testid="stSidebar"] {
    display: none;
}
</style>
"""
st.markdown(hide_sidebar_style, unsafe_allow_html=True)

# ---------- Page Title ----------
st.title("🤖 TravelPal – Intelligent Travel Advisory Assistant")

# ---------- HEADER WITH PLACEHOLDER LOGO ----------
st.markdown(
    """
    <div style="margin-top:20px; padding:10px; background-color:#e8f0fe; border-left:5px solid #1a73e8; border-radius:5px; margin-bottom:30px;">
        <b>Notice:</b> This is a <i>prototype demonstration</i>. Always verify travel information via official government sources.
    </div>
    """,
    unsafe_allow_html=True
)

# ---------- CARD STYLES ----------
card_style = """
<style>
.cards-container {
    display: flex;
    flex-wrap: nowrap;
    overflow-x: auto;
    gap: 30px;
    padding-bottom: 20px;
}

.card-link {
    text-decoration: none; /* Remove underline */
    color: inherit;
}

.card-link:hover {
    text-decoration: none; /* Prevent underline on hover */
}

.card {
    background-color: #f8f9fa;
    border-radius: 12px;
    padding: 20px;
    width: 255px;
    height: 250px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.08);
    transition: 0.3s ease;
    cursor: pointer;
    border: 1px solid #e6e6e6;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    flex-shrink: 0;
}

.card:hover {
    transform: translateY(-6px);
    box-shadow: 0 10px 20px rgba(0,0,0,0.15);
}

.card-icon {
    font-size: 60px;
    margin-bottom: 15px;
    transition: 0.3s ease;
}

.card-title {
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 8px;
    transition: 0.3s ease;
}

.card-desc {
    font-size: 18px;
    color: #555;
    transition: 0.3s ease;
}

/* Hover effect: increase icon and title size */
.card:hover .card-icon {
    font-size: 60px;
}

.card:hover .card-title {
    font-size: 24px;
}

.card:hover .card-desc {
    font-size: 16px;
}
</style>
"""
st.markdown(card_style, unsafe_allow_html=True)

# ---------- All Cards HTML ----------
cards_html = """
<div class="cards-container">
    <a href="/About_Us" class="card-link">
        <div class="card">
            <div class="card-icon">👥</div>
            <div class="card-title">About Us</div>
            <div class="card-desc">Learn about the project and its purpose.</div>
        </div>
    </a>
    <a href="/Sample_Chat" class="card-link">
        <div class="card">
            <div class="card-icon">🗣️</div>
            <div class="card-title">Sample Chat</div>
            <div class="card-desc">Example conversation to demonstrate how the chatbot works.</div>
        </div>
    </a>
    <a href="/Chatbot" class="card-link">
        <div class="card">
            <div class="card-icon">💬</div>
            <div class="card-title">Chatbot</div>
            <div class="card-desc">Talk to the TravelPal AI assistant.</div>
        </div>
    </a>
    <a href="/Methodology" class="card-link">
        <div class="card">
            <div class="card-icon">⚙️</div>
            <div class="card-title">Methodology</div>
            <div class="card-desc">Understand how data flows and implementation details.</div>
        </div>
    </a>
</div>
"""

st.markdown(cards_html, unsafe_allow_html=True)

# ---------- FOOTER ----------
st.markdown(
    """
    <hr>
    <p style="font-size:14px; color:#555;">
        © 2025 TravelPal | AI Champions BootCamp (Aug - Nov 2025)  | Developed by Jocelyn Ow 
    </p>
    """,
    unsafe_allow_html=True
)
