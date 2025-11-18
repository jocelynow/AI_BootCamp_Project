import streamlit as st
import base64


# --- Wide layout ---
st.set_page_config(layout="wide")


st.title("🗣️ Sample Chat")

st.markdown("---")  # This adds a line under the title

image_path = "images/Chat_Samples1.png"

def img_to_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

img_base64 = img_to_base64(image_path)

# --- Full browser width and height, no gray columns ---
st.markdown(f"""
<div style="
    width: 100vw;
    height: 100vh;
    overflow: auto;
">
    <img src="data:image/png;base64,{img_base64}" style="
        width: 100%;
        height: auto;
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


