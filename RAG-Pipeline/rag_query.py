import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / 'Data-Ingestion-Pipeline'))
from vector_db import VectorDB
from embedder import embedding_model

# Settings
KB_DIR = Path("../KB/chroma_db")
COLLECTION_NAME = "transcripts_kb"

def build_prompt(user_query, context):
    return f"Context:\n{context}\n\nQuestion: {user_query}\nAnswer:"

def get_rag_context(user_query, k=3):
    """Return only the retrieved context for a user query."""
    vector_db = VectorDB(
        persist_directory=str(KB_DIR),
        collection_name=COLLECTION_NAME,
        embedding_function=embedding_model,
    )
    results = vector_db.similarity_search(user_query, k=k)
    retrieved_texts = [r.page_content for r in results]
    return "\n".join(retrieved_texts)

def query_rag(user_query, k=3):
    context = get_rag_context(user_query, k)
    final_prompt = build_prompt(user_query, context)
    print("\n🧑‍💻 Query:", user_query)
    print("\n📚 Retrieved context:\n", context)
    print("\nPrompt for LLM:\n", final_prompt)

if __name__ == "__main__":
    query_rag("Summarize the customer concerns about pricing.")
