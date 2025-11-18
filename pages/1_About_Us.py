import streamlit as st


# -----------------------------------------------------
# Page Configuration
# -----------------------------------------------------
st.set_page_config(
    page_title="About Us | TravelPal Chatbot",
    page_icon="🌍",
    layout="wide"
)


# -----------------------------------------------------
# Title Section
# -----------------------------------------------------
st.title("🤖 About TravelPal")

st.markdown(
    """
Welcome to **TravelPal**, a smart Singapore-focused travel assistant designed to help users access official travel guidance from the **Ministry of Foreign Affairs (MFA)**, the **Immigration & Checkpoints Authority (ICA)**, weather data, and country-specific advisories — all in one place.

Below is a detailed overview of the **project scope**, **objectives**, **data sources**, and **key features**.
"""
)

st.markdown("---")

# -----------------------------------------------------
# Project Scope (Markdown)
# -----------------------------------------------------
st.header("📌 Project Scope")
st.markdown(
    """
TravelPal is designed as a **one-stop intelligent travel advisory platform** for Singaporean travellers. It focuses on delivering **official, reliable, and up-to-date travel information**, including:

- Singapore travel policies  
- Entry requirements & prohibited/controlled goods  
- Travel tips for Singaporeans  
- MFA country-specific advisories  
- Destination weather insights  

"""
)

# --- Out of Scope in Expander ---
with st.expander("❗ Out of Scope"):
    st.markdown(
        """
TravelPal does **not** provide:  
- Booking or purchasing of flights, hotels, or travel packages  
- Personalised itineraries beyond official advisory information  
- Financial, insurance, or legal advice unrelated to travel  
- Real-time emergency / consular support  

"""
    )

st.markdown("---")

# -----------------------------------------------------
# Project Objectives
# -----------------------------------------------------
st.header("🎯 Project Objectives")

col1, col2 = st.columns(2)

col1.markdown(
    """
- **Reliable Information Delivery**  
  Provide accurate and official travel policy information.

- **Country-specific Guidance**  
  Offer direct MFA advisory links for specific destinations.

- **Weather Awareness**  
  Help travellers plan according to climate data.
"""
)

col2.markdown(
    """
- **Enhanced User Experience**  
  Simple, intuitive conversational interface.

- **Reference Transparency**  
  Always include official clickable URLs when responding.

- **Accessibility & Ease of Use**  
  Clean interface suitable for all users.
"""
)

st.markdown("---")

# -----------------------------------------------------
# Data Sources (Markdown)
# -----------------------------------------------------
st.header("📚 Data Sources")
st.markdown(
    """
TravelPal retrieves information from the following sources:

##### **1. TravelPal RAG Document (extracted from official sites as of 10 Nov 2025)**  
- [Travel tips from MFA](https://www.mfa.gov.sg/Consular-Services/Singapore-Citizens/Travel-Tips)  
- [Help from MFA while overseas](https://www.mfa.gov.sg/Consular-Services/Singapore-Citizens/I-Need-Help-Overseas)  
- [Prohibited, controlled, and dutiable goods](https://www.ica.gov.sg/enter-transit-depart/entering-singapore/what-you-can-bring/prohibited-controlled-dutiable-goods)  
- [Advice for Singapore citizens travelling abroad](https://www.ica.gov.sg/enter-depart/for-singapore-citizens/advice-for-travelling-abroad)  
- [APEC Business Travel Card](https://www.ica.gov.sg/enter-depart/for-singapore-citizens/apec-business-travel-card)

##### **2. MFA Country Pages**  
- [Where Are You Travelling To?](https://www.mfa.gov.sg/Where-Are-You-Travelling-To)  

  This portal contains **country-specific travel advisories from the Ministry of Foreign Affairs (MFA)** for a total of **186 countries**.  

  For each country, the advisory provides information in the following categories:  
  1. Country travel advisories and alerts  
  2. Entry and exit requirements  
  3. Safety and security information  
  4. Local laws and regulations  
  5. General travel advice and precautions
  6. Local emergency contact numbers 
  7. Mission contact details  

##### **3. Weather API**  
- Open-Meteo Climate API
"""
)

st.markdown("---")

# -----------------------------------------------------
# Professional Feature Cards (Interactive)
# -----------------------------------------------------
st.header("✨ Key Features")

# --- Card Style ---
st.markdown("""
<style>
.feature-card {
    background: #f8f9fa;
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    box-shadow: 0 4px 10px rgba(0,0,0,0.08);
    transition: 0.3s ease;
    border: 1px solid #eaeaea;
}
.feature-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 20px rgba(0,0,0,0.15);
}
.feature-icon {
    font-size: 40px;
    margin-bottom: 10px;
}
.feature-title {
    font-size: 20px;
    font-weight: bold;
    margin-bottom: 8px;
}
.feature-text {
    font-size: 16px;
    color: #444;
}
</style>
""", unsafe_allow_html=True)

# --- Display Cards ---
colA, colB, colC = st.columns(3)

with colA:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-icon">🤖</div>
            <div class="feature-title">AI-Powered Chatbot</div>
            <div class="feature-text">
                Answers travel-related queries using official Singapore sources.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with colB:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-icon">🌐</div>
            <div class="feature-title">Country Advisory</div>
            <div class="feature-text">
                Provides MFA travel advisories for specific destinations.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with colC:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-icon">☀️</div>
            <div class="feature-title">Weather Insights</div>
            <div class="feature-text">
                Retrieves monthly average temperatures for trip planning.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("---")

# -----------------------------------------------------
# Disclaimer
# -----------------------------------------------------
st.warning(
    """
### ⚠️ IMPORTANT NOTICE  
This is a prototype demonstration. Always verify travel information via **official government sources**.
"""
)

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
