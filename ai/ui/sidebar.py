import streamlit as st

from ai.utils.chat_history import (
    load_history,
    save_chat,
    delete_chat
)


def render_sidebar():

    with st.sidebar:

        st.title("🤖 Enterprise AI")

        st.markdown("---")

        st.subheader("📄 Current PDF")

        if st.session_state.processed_pdf:
            st.success(st.session_state.processed_pdf)
        else:
            st.info("No PDF Uploaded")

        st.markdown("---")

        if st.button("➕ New Chat"):

            if st.session_state.messages:

                save_chat(
                    st.session_state.processed_pdf,
                    st.session_state.messages
                )

            st.session_state.messages = []
            st.session_state.processed_pdf = None

            st.rerun()

        st.markdown("---")

        st.subheader("💬 Previous Chats")

        history = load_history()

        search = st.text_input(
            "🔍 Search Chats",
            placeholder="Search..."
        )

        if search:
            history = [
                chat
                for chat in history
                if search.lower() in chat["title"].lower()
            ]

        if not history:

            st.caption("No previous chats")

        else:

            for chat in history:

                col1, col2 = st.columns([5, 1])

                with col1:

                    if st.button(
                        f"📄 {chat['title']}",
                        key=f"open_{chat['id']}"
                    ):

                        st.session_state.messages = chat["messages"]
                        st.session_state.processed_pdf = chat["pdf"]

                        st.rerun()

                with col2:

                    if st.button(
                        "🗑",
                        key=f"delete_{chat['id']}"
                    ):

                        delete_chat(chat["id"])

                        st.rerun()

        st.markdown("---")

        st.subheader("ℹ About")

        st.info(
            """
Enterprise AI Business Agent

✅ PDF Chat

✅ FAISS

✅ Gemini

✅ Chat History
"""
        )