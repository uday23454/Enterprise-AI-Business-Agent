import os
import streamlit as st

from ai.rag.ingest import process_pdf


def render_uploader():

    uploaded_file = st.file_uploader(
        "Upload a PDF",
        type=["pdf"]
    )

    if uploaded_file is None:
        return

    os.makedirs("data", exist_ok=True)

    pdf_path = os.path.join(
        "data",
        uploaded_file.name
    )

    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    if st.session_state.processed_pdf != uploaded_file.name:

        with st.spinner("📄 Processing PDF..."):

            process_pdf(pdf_path)

        st.session_state.processed_pdf = uploaded_file.name

        st.success("✅ PDF Processed Successfully!")