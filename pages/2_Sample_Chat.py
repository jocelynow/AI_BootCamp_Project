import streamlit as st
import os

# --- Wide layout ---
st.set_page_config(layout="wide")

st.title("🗣️ Sample Chat")
st.markdown("---")

# --- Get image path relative to this script ---
script_dir = os.path.dirname(__file__)  # folder where this script is
image_path = os.path.join(script_dir, "..", "chat_samples1.png")  # move up to root

# --- Display the image ---
if os.path.exists(image_path):
    st.image(image_path, use_column_width=True)
else:
    st.warning(f"Image not found at {image_path}")

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

