PDF Chatbot using Retrieval-Augmented Generation (RAG)

Overview

This project is a PDF Question Answering Chatbot that allows users to upload PDF documents and ask questions about their content. The system uses Retrieval-Augmented Generation (RAG) concepts to retrieve the most relevant information from the document and display it to the user.

Features

- Upload PDF documents
- Extract text from PDF files
- Split documents into smaller chunks
- Generate vector embeddings
- Store embeddings using FAISS Vector Database
- Perform semantic similarity search
- Interactive Streamlit web interface
- No API key required

Tech Stack

- Python
- Streamlit
- LangChain
- FAISS
- Sentence Transformers
- PyPDF

Project Workflow

1. User uploads a PDF document.
2. Text is extracted from the PDF.
3. The document is split into chunks.
4. Embeddings are generated using Sentence Transformers.
5. Embeddings are stored in a FAISS vector database.
6. User asks a question.
7. Similarity search retrieves the most relevant chunks.
8. Relevant content is displayed as the answer.

Installation

pip install -r requirements.txt

Run the Project

streamlit run app.py

Future Improvements

- Multi-PDF support
- Chat history
- Source citations
- Advanced LLM integration
- Document summarization

