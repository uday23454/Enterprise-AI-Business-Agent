import streamlit as st

from ai.ui.sidebar import render_sidebar
from ai.ui.uploader import render_uploader
from ai.ui.chat import render_chat
from ai.ui.preview import render_preview

st.set_page_config(
    page_title="Enterprise AI Business Agent",
    page_icon="🤖",
    layout="wide"
)

if "processed_pdf" not in st.session_state:
    st.session_state.processed_pdf = None

if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("🤖 Enterprise AI Business Agent")

render_sidebar()

left, right = st.columns([1, 1.3])

with left:

    render_uploader()

    render_preview()

with right:

    render_chat()