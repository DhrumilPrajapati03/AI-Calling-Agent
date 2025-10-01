import sys
from pathlib import Path
import subprocess

# Paths to pipelines
AGENT_PIPELINE = Path("Agent-Pipeline/agent.py")


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Main entry point for the AI-Calling-Agent project.")
    parser.add_argument("--ingest", action="store_true", help="Run data ingestion pipeline")
    parser.add_argument("--rag", type=str, help="Run RAG query with the given question")
    parser.add_argument("--llm", type=str, help="Ask the LLM directly (no retrieval)")
    parser.add_argument("--chat", action="store_true", help="Start interactive QA chat bot mode")
    args = parser.parse_args()

    if args.chat:
        print("\nAI-Calling-Agent Chat Mode (type 'exit' to quit)\n")
        while True:
            user_input = input("You: ").strip()
            if user_input.lower() in {"exit", "quit"}:
                print("Goodbye!")
                break
            # Default to RAG, fallback to LLM if needed
            cmd = [sys.executable, str(AGENT_PIPELINE), "--rag", user_input]
            result = subprocess.run(cmd, capture_output=True, text=True)
            print(result.stdout)
    elif args.ingest or args.rag or args.llm:
        cmd = [sys.executable, str(AGENT_PIPELINE)]
        if args.ingest:
            cmd.append("--ingest")
        if args.rag:
            cmd.extend(["--rag", args.rag])
        if args.llm:
            cmd.extend(["--llm", args.llm])
        result = subprocess.run(cmd)
        sys.exit(result.returncode)
    else:
        print("Nothing to do. Use --ingest, --rag, --llm, and/or --chat.")

if __name__ == "__main__":
    main()
