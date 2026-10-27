import os
import streamlit as st
from streamlit_pdf_viewer import pdf_viewer


def render_preview():

    if st.session_state.processed_pdf is None:
        st.info("📄 Upload a PDF to preview.")
        return

    pdf_path = os.path.join(
        "data",
        st.session_state.processed_pdf
    )

    if not os.path.exists(pdf_path):
        st.warning("PDF not found.")
        return

    st.subheader("📄 PDF Preview")

    with open(pdf_path, "rb") as f:
        pdf_bytes = f.read()

    pdf_viewer(
        pdf_bytes,
        width=550,
        height=750
    )