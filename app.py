import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
import os

st.title("PDF Chatbot (No API Key)")

uploaded_file = st.file_uploader(
    "Upload PDF",
    type="pdf"
)

if uploaded_file:

    with open(uploaded_file.name, "wb") as f:
        f.write(uploaded_file.read())

    loader = PyPDFLoader(uploaded_file.name)
    docs = loader.load()
    st.write("PDF Loaded Successfully")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(docs)
    st.write(f"Created{len(chunks)}chunks")

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    st.write("Embeddings Model loaded")

    db = FAISS.from_documents(
        chunks,
        embeddings
    )
    st.write("FAISS Database created")

    question = st.text_input(
        "Ask a question"
    )

    if question:

        results = db.similarity_search(
            question,
            k=3
        )

        st.subheader("Relevant Answer")

        for doc in results:
            st.write(doc.page_content)
            st.write("----------")