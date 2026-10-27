import streamlit as st

from ai.rag.chat import ask_pdf


def render_chat():

    # Show old messages
    for message in st.session_state.messages:

        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat input
    question = st.chat_input(
        "Ask anything about your PDF..."
    )

    if not question:
        return

    if st.session_state.processed_pdf is None:

        st.warning(
            "Please upload a PDF first."
        )

        return

    # Save user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    # AI Response
    with st.spinner("🤖 Thinking..."):

        answer, pages = ask_pdf(question)

    answer += (
        "\n\n---\n📄 **Source Page(s):** "
        + ", ".join(map(str, pages))
    )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    with st.chat_message("assistant"):
        st.markdown(answer)

    st.rerun()