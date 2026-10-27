from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pickle
import os

model = SentenceTransformer("all-MiniLM-L6-v2")


def store_embeddings(chunks):

    embeddings = model.encode(chunks)

    embeddings = np.array(embeddings).astype("float32")

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(embeddings)

    os.makedirs("faiss_index", exist_ok=True)

    faiss.write_index(index, "faiss_index/index.faiss")

    with open("faiss_index/chunks.pkl", "wb") as f:
        pickle.dump(chunks, f)

    print("Embeddings Stored Successfully!")