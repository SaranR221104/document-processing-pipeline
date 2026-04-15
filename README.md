📄 Document Processing Pipeline (Day 2 - RAG Bootcamp)
🚀 Overview

This project is part of Day 2 of the RAG Bootcamp at Nunnari Academy.
It focuses on building a document processing pipeline using LangChain, where PDF files are loaded, split into chunks, enriched with metadata, and filtered for selective retrieval.

🎯 Objectives
Load multiple PDF documents
Split documents into manageable chunks
Attach meaningful metadata to each chunk
Implement filtering based on metadata
Build an interactive UI for processing and filtering
🛠️ Technologies Used
Python
LangChain
PyPDFLoader
RecursiveCharacterTextSplitter
Gradio
📂 Project Structure
documentprocessingpipeline/
│
├── document_loader.py
├── Kalam.pdf
├── Naidu.pdf
└── README.md
⚙️ Features
✅ 1. PDF Loading
Loads multiple PDF files using PyPDFLoader
✅ 2. Text Chunking
Splits documents using:
chunk_size = 1000
chunk_overlap = 200
✅ 3. Metadata Enrichment

Each chunk includes:

filename
page_number
upload_date
source_type
✅ 4. Filtering System

Custom function:

filter_chunks(chunks, **filters)

Supports filtering by:

Filename
Page number
Source type
✅ 5. Interactive UI

Built using Gradio:

Select multiple PDFs
Process documents
Apply filters dynamically
View chunk content and metadata
