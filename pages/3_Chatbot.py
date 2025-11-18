import streamlit as st
from logics.llm import agent
import re


# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="TravelPal Chatbot",
    page_icon="🌍",
    layout="wide"
)


# -----------------------------
# Title
# -----------------------------
st.markdown(
    """
    <h1 style="font-size:36px; font-weight:700;">🤖 TravelPal Chatbot</h1>
    <p style="font-size:16px; color:#555; max-width:750px;">
        Your smart assistant for official travel information from <b>MFA</b>, <b>ICA</b>, and reliable weather services.
    </p>
    <hr>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# Chat Styling
# -----------------------------
st.markdown("""
<style>
.user-bubble {
    background-color: #d1e7ff;
    padding: 12px 16px;
    border-radius: 12px;
    margin: 5px 0;
    max-width: 70%;
    display: inline-block;
}
.assistant-bubble {
    background-color: #f1f1f1;
    padding: 12px 16px;
    border-radius: 12px;
    margin: 5px 0;
    max-width: 70%;
    display: inline-block;
}
.chat-row {
    display: flex;
    gap: 10px;
    align-items: flex-start;
}
.user-icon, .bot-icon {
    font-size: 24px;
}
input:focus {
    outline: none;
    border: 1px solid #aaa;
    box-shadow: none;
}
a {
    color: #0645ad;
    text-decoration: underline;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Helper Function
# -----------------------------
def make_links_clickable(text: str) -> str:
    """
    Converts Markdown-style links [text](url) to HTML clickable links.
    """
    # Remove duplicate links first
    seen = set()
    def dedup(match):
        full_match = match.group(0)
        if full_match in seen:
            return match.group(1)  # Just keep the text, no link
        seen.add(full_match)
        return f'<a href="{match.group(2)}" target="_blank">{match.group(1)}</a>'

    pattern = re.compile(r'\[([^\]]+)\]\((https?://[^\)]+)\)')
    return pattern.sub(dedup, text)

# -----------------------------
# Session State for Messages
# -----------------------------
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# -----------------------------
# Display Chat
# -----------------------------
for msg in st.session_state["messages"]:
    if msg["role"] == "user":
        st.markdown(f"""
        <div class="chat-row">
            <div class="user-icon">🙋‍♂️</div>
            <div class="user-bubble">{msg['content']}</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        # Convert Markdown links to clickable HTML
        assistant_text = make_links_clickable(msg['content'])
        st.markdown(f"""
        <div class="chat-row">
            <div class="bot-icon">🤖</div>
            <div class="assistant-bubble">{assistant_text}</div>
        </div>
        """, unsafe_allow_html=True)

# -----------------------------
# Centered Input Bar
# -----------------------------
def submit_message():
    user_input = st.session_state["input_text"]
    if not user_input:
        return

    # Append user message
    st.session_state["messages"].append({"role": "user", "content": user_input})

    # Call your agent
    response = agent.run(user_input)

    # Append MFA/ICA disclaimer if relevant
    disclaimer_keywords = ["prohibited", "ica", "apec"]
    skip_keywords= ["temperature", "climate", "weather"]
    if any(k in response.lower() for k in disclaimer_keywords) and not any(k in response.lower() for k in skip_keywords):
        response += "\n\n_This information is based on official MFA/ICA sources (retrieved Nov 2025)._"

    # Append assistant message
    st.session_state["messages"].append({"role": "assistant", "content": response})

    # Clear input
    st.session_state["input_text"] = ""

st.text_input(
    label="",
    key="input_text",
    placeholder="Ask about MFA advisories, ICA rules, or weather...",
    on_change=submit_message
)

st.markdown(
    """
    <style>
    div.stTextInput > div > div > input {
        padding-right: 40px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# Disclaimer & Footer
# -----------------------------
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

# st.markdown("---")
# st.markdown(
#     """
# <p style="text-align:center; color:#777; font-size:14px;">
# © 2025 TravelPal | Demo Application | Developed by Jocelyn Ow
# </p>
# """,
#     unsafe_allow_html=True
# )
