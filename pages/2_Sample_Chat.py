import os
import streamlit as st

# --- Wide layout ---
st.set_page_config(layout="wide")

st.title("🗣️ Sample Chat")
st.markdown("---")  # Line under title

# Path to image relative to the script
script_dir = os.path.dirname(__file__)
image_path = os.path.join(script_dir, "..", "chat_samples1.png")  # up one level to root

# Convert the path to a URL that the browser can access
# Streamlit allows local paths for HTML <img src>, using "file://"
image_url = f"file://{image_path}"

# Full browser width & height image
st.markdown(f"""
<div style="
    width: 100vw;
    height: 100vh;
    margin: 0;
    padding: 0;
    overflow: hidden;
">
    <img src="{image_url}" style="
        width: 100%;
        height: 100%;
        object-fit: contain;
        display: block;
    ">
</div>
""", unsafe_allow_html=True)

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
