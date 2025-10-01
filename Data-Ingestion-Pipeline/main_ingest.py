from pathlib import Path
from data_loader import load_transcripts
from text_cleaner import clean_text
from chunker import chunk_text
from embedder import embedding_model
from vector_db import VectorDB

BASE_DIR = Path("./Transcriptions/EMMA_ES-TRANSCRIPTIONS")
KB_DIR = Path("../KB/chroma_db")
COLLECTION_NAME = "transcripts_kb"

# Load transcripts
raw_data = load_transcripts(BASE_DIR)
print(f"Loaded {len(raw_data)} transcripts")

if not raw_data:
    print("No transcripts found. Please check the path and ensure there are .txt files in the directory.")
    exit(1)

# Clean transcripts
for doc in raw_data:
    doc["clean_text"] = clean_text(doc["text"])

# Chunking
docs = []
for doc in raw_data:
    chunks = chunk_text(doc["clean_text"])
    for i, chunk in enumerate(chunks):
        docs.append({
            "id": f"{doc['file']}_chunk{i}",
            "text": chunk,
            "metadata": {"source": doc["file"], "chunk_id": i},
        })
print(f"Generated {len(docs)} chunks from transcripts")

if not docs:
    print("No chunks generated from transcripts. Exiting.")
    exit(1)

# Embedding & Vector DB
vector_db = VectorDB(
    persist_directory=str(KB_DIR),
    collection_name=COLLECTION_NAME,
    embedding_function=embedding_model,
)
texts = [d["text"] for d in docs]
metadatas = [d["metadata"] for d in docs]
ids = [d["id"] for d in docs]
vector_db.add_texts(texts, metadatas, ids)
print("✅ Knowledge Base updated & stored in KB/chroma_db/ with SentenceTransformers")

# Quick Retrieval Test
query = "How does payment system works using Paypal at agency?"
results = vector_db.similarity_search(query, k=5)
for r in results:
    print("----")
    print("Source:", r.metadata["source"])
    print(r.page_content[:])