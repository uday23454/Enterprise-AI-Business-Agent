import os
import pickle
import faiss

from dotenv import load_dotenv
from google import genai
from sentence_transformers import SentenceTransformer

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

model = SentenceTransformer("all-MiniLM-L6-v2")


def ask_pdf(question):

    index = faiss.read_index("faiss_index/index.faiss")

    with open("faiss_index/chunks.pkl", "rb") as f:
        chunks = pickle.load(f)

    with open("faiss_index/metadata.pkl", "rb") as f:
        metadata = pickle.load(f)

    question_embedding = model.encode([question]).astype("float32")

    distances, indices = index.search(question_embedding, 3)

    selected_chunks = []
    pages = []

    for i in indices[0]:

        if i != -1:
            selected_chunks.append(chunks[i])
            pages.append(metadata[i]["page"])

    context = "\n\n".join(selected_chunks)

    prompt = f"""
You are an AI assistant.

Answer ONLY using the context below.

If the answer is not available reply:

I don't know.

Context:
{context}

Question:
{question}
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    return response.text, sorted(set(pages))