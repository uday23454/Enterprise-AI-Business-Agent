import pickle
import faiss
import numpy as np

from sentence_transformers import SentenceTransformer

from ai.documents.pdf_processor import extract_pages, chunk_pages

model = SentenceTransformer("all-MiniLM-L6-v2")


def process_pdf(pdf_path):

    pages = extract_pages(pdf_path)

    chunks, metadata = chunk_pages(pages)

    embeddings = model.encode(chunks).astype("float32")

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(embeddings)

    faiss.write_index(index, "faiss_index/index.faiss")

    with open("faiss_index/chunks.pkl", "wb") as f:
        pickle.dump(chunks, f)

    with open("faiss_index/metadata.pkl", "wb") as f:
        pickle.dump(metadata, f)

    print("PDF Processed Successfully!")