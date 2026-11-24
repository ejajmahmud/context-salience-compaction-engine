"""CLI for Context Salience Compaction Engine."""
import argparse
from .core import ContextCompactor

def main():
    parser = argparse.ArgumentParser(description="Context Salience Compaction Engine CLI")
    parser.add_argument("--demo", action="store_true", help="Run compaction demo")
    args = parser.parse_args()

    sample = "The agent began task execution. We found a critical bug in parser.py on line 42. It was raining today. The test failed abruptly. The weather was nice."
    res = ContextCompactor.compact(sample, max_sentences=2)
    print(f"Original: {res.original_length} chars -> Compacted: {res.compacted_length} chars (Ratio: {res.ratio})")
    print("Compacted text:", res.compacted_text)

if __name__ == "__main__":
    main()
