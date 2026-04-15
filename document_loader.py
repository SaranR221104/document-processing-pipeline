from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from datetime import date
import os
import gradio as gr



pdf_files = {
    "Kalam.pdf": r"C:\Users\Saran\OneDrive\Documents\Desktop\nunnari workshop\documentprocessingpipeline\Kalam.pdf",
    "Naidu.pdf": r"C:\Users\Saran\OneDrive\Documents\Desktop\nunnari workshop\documentprocessingpipeline\Naidu.pdf"
}



def process_pdfs(selected_files):
    all_pages = []

    for name in selected_files:
        loader = PyPDFLoader(pdf_files[name])
        pages = loader.load()
        all_pages.extend(pages)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(all_pages)

    # Metadata
    today = str(date.today())

    for chunk in chunks:
        source_path = chunk.metadata.get("source", "")
        filename = os.path.basename(source_path)

        chunk.metadata["filename"] = filename
        chunk.metadata["page_number"] = chunk.metadata.get("page", 0)
        chunk.metadata["upload_date"] = today
        chunk.metadata["source_type"] = "pdf"

    return chunks

def filter_chunks(chunks, filename=None, page_number=None):
    results = []

    for chunk in chunks:
        if filename and chunk.metadata.get("filename") != filename:
            continue
        if page_number is not None and str(chunk.metadata.get("page_number")) != str(page_number):
            continue
        results.append(chunk)

    return results

def run_pipeline(selected_files, filter_file, page_number):
    if not selected_files:
        return "❌ Please select at least one file"

    chunks = process_pdfs(selected_files)

    filtered = filter_chunks(
        chunks,
        filename=filter_file if filter_file else None,
        page_number=page_number if page_number else None
    )

    output = f"✅ Total Chunks: {len(chunks)}\n"
    output += f"✅ Filtered Chunks: {len(filtered)}\n\n"

    for i, chunk in enumerate(filtered[:3]):
        output += f"--- Chunk {i+1} ---\n"
        output += chunk.page_content[:300] + "\n"
        output += str(chunk.metadata) + "\n\n"

    return output



with gr.Blocks() as app:
    gr.Markdown("# 📄 Document Processing Pipeline (Gradio)")

    file_selector = gr.CheckboxGroup(
        choices=list(pdf_files.keys()),
        label="Select PDF Files"
    )

    filter_file = gr.Dropdown(
        choices=["", "Kalam.pdf", "Naidu.pdf"],
        label="Filter by Filename"
    )

    page_number = gr.Textbox(label="Page Number (optional)")

    run_btn = gr.Button("🚀 Process")

    output = gr.Textbox(label="Output", lines=20)

    run_btn.click(
        fn=run_pipeline,
        inputs=[file_selector, filter_file, page_number],
        outputs=output
    )

app.launch()
