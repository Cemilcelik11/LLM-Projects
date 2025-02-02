import streamlit as st
from chains import Chain

def streamlit_app():
    st.title("📄 PDF Chat Assistant")
    chain = Chain()

    uploaded_file = st.file_uploader(
        "Upload a PDF file", 
        type="pdf",
        accept_multiple_files=False
        )

    if uploaded_file:
        chain.upload_pdf(uploaded_file)
        documents = chain.load_pdf(uploaded_file.name)
        chunked_documents = chain.split_text(documents)
        chain.index_docs(chunked_documents)

        question = st.chat_input("Ask a question about the PDF:")

        if question:
            st.chat_message("user").write(question)
            related_documents = chain.retrieve_docs(question)
            answer = chain.answer_question(question, related_documents)
            st.chat_message("assistant").write(answer)

if __name__ == "__main__":
    st.set_page_config(
        layout="wide", 
        page_title="PDF Chat Assistant", 
        page_icon="📄"
        )
    streamlit_app()

