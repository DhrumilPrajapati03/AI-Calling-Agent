# AI-Calling-Agent

A modular, production-ready Retrieval-Augmented Generation (RAG) and QA bot pipeline for customer transcription data, powered by Google Gemini LLM and ChromaDB.

## Features
- **Data Ingestion Pipeline:**
  - Loads, cleans, and chunks raw transcript files
  - Embeds chunks and stores them in a Chroma vector database
- **RAG Pipeline:**
  - Retrieves relevant context from the knowledge base for any user query
  - Uses Google Gemini LLM for accurate, fast, and context-aware answers
- **Agent Pipeline:**
  - Orchestrates ingestion, RAG, and direct LLM answers
  - CLI and chat mode for interactive QA
- **Main Entry Point:**
  - `main.py` provides a single interface for all functionalities

## Project Structure
```
AI-Calling-Agent/
│
├── Data-Ingestion-Pipeline/
│   ├── chunker.py
│   ├── data_loader.py
│   ├── embedder.py
│   ├── main_ingest.py
│   ├── text_cleaner.py
│   ├── vector_db.py
│   └── __init__.py
│
├── RAG-Pipeline/
│   └── rag_query.py
│
├── Agent-Pipeline/
│   └── agent.py
│
├── KB/
│   └── chroma_db/           # Chroma vector DB files
│
├── Transcriptions/
│   └── EMMA_ES-TRANSCRIPTIONS/  # Raw .txt transcript files
│
├── .env
├── requirements.txt
├── main.py
└── README.md
```

## Setup
1. **Clone the repository:**
   ```sh
   git clone <repo-url>
   cd AI-Calling-Agent
   ```
2. **Create and activate a virtual environment:**
   ```sh
   python -m venv aenv
   aenv\Scripts\activate  # Windows
   # or
   source aenv/bin/activate  # Linux/Mac
   ```
3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Configure environment variables:**
   - Edit `.env` and add your `GEMINI_API_KEY` and other required keys.

5. **Add transcript files:**
   - Place your `.txt` files in `Transcriptions/EMMA_ES-TRANSCRIPTIONS/`.

## Usage
### Data Ingestion
```sh
python main.py --ingest
```

### RAG QA (single question)
```sh
python main.py --rag "Your question here"
```

### Direct LLM QA (no retrieval)
```sh
python main.py --llm "Your open-ended question here"
```

### Interactive Chat Mode
```sh
python main.py --chat
```
Type your questions and get answers from the agent. Type `exit` to quit.

## Customization
- **Switch LLM:** The agent uses Gemini for all answers. You can swap to another LLM by editing `Agent-Pipeline/agent.py`.
- **Add new pipelines:** Extend the modular structure for new data sources or tasks.

## Requirements
- Python 3.9+
- No GPU required (Gemini API runs in the cloud)

## License
MIT

## Credits
- [Google Gemini](https://ai.google.dev/)
- [ChromaDB](https://www.trychroma.com/)
- [LangChain](https://www.langchain.com/)

---

For questions or contributions, open an issue or pull request on GitHub.
