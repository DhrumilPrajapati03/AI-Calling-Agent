import glob
import os
from pathlib import Path

def load_transcripts(path: Path):
    """
    Load all transcript .txt files from folder
    """
    files = glob.glob(str(path / "*.txt"))
    transcripts = []
    for f in files:
        with open(f, "r", encoding="utf-8") as file:
            transcripts.append({"file": os.path.basename(f), "text": file.read()})
    return transcripts
