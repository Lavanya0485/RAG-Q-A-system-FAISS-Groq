# Document Q&A RAG System using FAISS and Groq

A lightweight **Retrieval-Augmented Generation (RAG)** application that answers questions from uploaded documents.

The system loads documents, splits them into smaller chunks, generates semantic embeddings using **SentenceTransformers**, stores and searches the embeddings using **FAISS**, and uses a **Groq-hosted LLM** to generate answers grounded in the retrieved document context.

## Architecture

```text
Documents
   │
   ▼
Document Loader
   │
   ▼
Text Chunking
   │
   ▼
SentenceTransformer
(all-MiniLM-L6-v2)
   │
   ▼
Embeddings
   │
   ▼
FAISS Vector Store
   │
   │
   └── Metadata / Original Text
   │
   ▼
User Question
   │
   ▼
Query Embedding
   │
   ▼
FAISS Similarity Search
   │
   ▼
Top-K Relevant Chunks
   │
   ▼
Prompt + Retrieved Context
   │
   ▼
Groq LLM
   │
   ▼
Grounded Answer
```

## Features

- Multi-format document loading
- Recursive text chunking with configurable chunk size and overlap
- Semantic embeddings using SentenceTransformers
- FAISS-based vector similarity search
- Persistent FAISS index and document metadata
- Top-K semantic document retrieval
- Groq LLM integration
- Context-grounded question answering
- Environment-based API key management

## Technology Stack

- Python
- LangChain
- SentenceTransformers
- FAISS
- Groq API
- NumPy
- python-dotenv

### Embedding Model

```text
all-MiniLM-L6-v2
```

The embedding model converts document chunks and user queries into dense vector representations for semantic similarity search.

### Generative Model

The application uses a Groq-hosted LLM for response generation.

The model can be configured in `search.py`.

## Project Structure

```text
document-rag-faiss-groq/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   └── sample_document.pdf
│
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── embedding.py
│   ├── vectorstore.py
│   └── search.py
│
└── faiss_store/
    ├── faiss.index
    └── metadata.pkl
```

The `faiss_store` directory contains generated vector-store artifacts and can be excluded from Git because the index can be rebuilt from the source documents.

## Module Overview

### `data_loader.py`

Loads documents from the `data/` directory.

The loader supports document formats such as:

- PDF
- TXT
- CSV
- DOCX
- XLSX
- JSON

### `embedding.py`

Responsible for:

- Splitting documents into chunks
- Generating embeddings using SentenceTransformers

Default configuration:

```python
chunk_size = 1000
chunk_overlap = 200
embedding_model = "all-MiniLM-L6-v2"
```

### `vectorstore.py`

Manages the FAISS vector database.

Responsibilities include:

- Creating the FAISS index
- Adding document embeddings
- Storing associated metadata
- Saving the index to disk
- Loading an existing index
- Performing similarity search
- Retrieving Top-K relevant chunks

### `search.py`

Implements the RAG retrieval and generation pipeline.

The workflow is:

```text
User Question
      ↓
Query Embedding
      ↓
FAISS Search
      ↓
Top-K Chunks
      ↓
Prompt Construction
      ↓
Groq LLM
      ↓
Answer
```

### `app.py`

Entry point for running document Q&A queries.

Multiple questions can be passed to the RAG pipeline.

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd RAG-Q-A-system-FAISS-Groq
```

### 2. Create a virtual environment

Using `uv`:

```bash
uv venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
uv pip install -r requirements.txt
```

## Environment Configuration

Create a `.env` file in the project root:

```text
GROQ_API_KEY=your_groq_api_key
```

The `.env` file should not be committed to GitHub.

It is excluded through `.gitignore`.

## Add Documents

Place documents inside:

```text
data/
```

For example:

```text
data/
├── machine_learning.pdf
├── ai_notes.docx
└── research_notes.txt
```

## Build the Vector Store

The documents are:

1. Loaded
2. Split into chunks
3. Converted into embeddings
4. Stored in FAISS
5. Associated with their original text and metadata

The resulting files are stored under:

```text
faiss_store/
├── faiss.index
└── metadata.pkl
```

If the FAISS index does not exist, the application can build it from the documents in the `data` directory.

## Run the Application

Run:

```bash
python app.py
```

Example questions:

```python
questions = [
    "What is machine learning?",
    "What is supervised learning?"
]
```

The application retrieves relevant document chunks and provides context-grounded answers using the configured Groq LLM.

## RAG Workflow

For a query such as:

```text
What is machine learning?
```

the application performs:

```text
Question
   ↓
SentenceTransformer
   ↓
Query Embedding
   ↓
FAISS Similarity Search
   ↓
Top-K Document Chunks
   ↓
Retrieved Context
   ↓
Groq LLM
   ↓
Final Answer
```

This approach allows the LLM to answer questions using information retrieved from the supplied documents rather than relying only on its pretrained knowledge.

## Prompt Grounding

The LLM is instructed to answer using the retrieved context.

If the requested information is not present in the retrieved documents, the application is designed to indicate that the information could not be found rather than intentionally generating unsupported information.

## Future Improvements

Potential enhancements include:

- Interactive command-line Q&A
- FastAPI REST API
- Streamlit or web-based user interface
- Source citations in generated answers
- Retrieval score thresholding
- Improved chunking strategies
- Hybrid keyword + vector search
- Reranking retrieved chunks
- Support for multiple embedding models
- PostgreSQL + pgvector integration
- Docker deployment
- Conversation history
- Evaluation of retrieval and answer quality

## Learning Objectives

This project was developed as a hands-on implementation to understand the major components of a production-oriented RAG pipeline:

- Document ingestion
- Text preprocessing and chunking
- Embedding generation
- Vector databases
- Semantic similarity search
- Retrieval
- Prompt construction
- LLM integration
- Grounded question answering

## Security

API credentials are loaded through environment variables.

Do not commit the following to the repository:

```text
.env
API keys
credentials
secrets
```

## License

This project is intended for learning, experimentation, and portfolio demonstration.