
import subprocess
import sys
from pathlib import Path
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load Gemini API key from .env
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

def gemini_answer(prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    return response.text.strip() if hasattr(response, 'text') else str(response)

def run_data_ingestion():
    print("Running Data Ingestion Pipeline...")
    result = subprocess.run(
        [sys.executable, str(Path("../Data-Ingestion-Pipeline/main_ingest.py"))],
        capture_output=True, text=True
    )
    print(result.stdout)
    if result.returncode != 0:
        print("Data ingestion failed.")
        sys.exit(1)
    print("Data ingestion completed.\n")

def run_rag_query(query):
    print("Running RAG Pipeline with Gemini...")
    # Call RAG pipeline to get context only (not answer)
    from pathlib import Path
    sys.path.append(str(Path(__file__).parent.parent / 'RAG-Pipeline'))
    from rag_query import get_rag_context, build_prompt
    context = get_rag_context(query, k=3)
    final_prompt = build_prompt(query, context)
    answer = gemini_answer(final_prompt)
    print(f"\n🧑‍💻 Query: {query}")
    print(f"\n📚 Retrieved context:\n{context}")
    print(f"\n🤖 Gemini Answer:\n{answer}\n")

def run_llm_direct(query):
    print("Running direct Gemini LLM answer...")
    answer = gemini_answer(query)
    print(f"\n🤖 Gemini LLM Answer:\n{answer}\n")
    print("LLM answer completed.\n")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Agent Pipeline Orchestrator")
    parser.add_argument("--ingest", action="store_true", help="Run data ingestion pipeline")
    parser.add_argument("--rag", type=str, help="Run RAG query with the given question")
    parser.add_argument("--llm", type=str, help="Ask the LLM directly (no retrieval)")
    args = parser.parse_args()

    if args.ingest:
        run_data_ingestion()
    if args.rag:
        run_rag_query(args.rag)
    if args.llm:
        run_llm_direct(args.llm)
    if not args.ingest and not args.rag and not args.llm:
        print("Nothing to do. Use --ingest, --rag, and/or --llm.")
