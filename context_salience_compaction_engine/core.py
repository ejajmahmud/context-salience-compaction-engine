"""Core Context Salience Compaction Engine implementation."""
import re
from typing import Dict, List, Tuple

class CompactionResult:
    def __init__(self, compacted_text: str, original_length: int, compacted_length: int, ratio: float):
        self.compacted_text = compacted_text
        self.original_length = original_length
        self.compacted_length = compacted_length
        self.ratio = ratio

class ContextCompactor:
    IMPORTANT_KEYWORDS = {"error", "bug", "fix", "patch", "test", "fail", "pass", "file", "line", "return", "class", "def"}

    @classmethod
    def _score_sentence(cls, sentence: str) -> float:
        words = set(re.findall(r"\w+", sentence.lower()))
        score = len(words)
        for w in words:
            if w in cls.IMPORTANT_KEYWORDS:
                score += 5.0
        return score

    @classmethod
    def compact(cls, text: str, max_sentences: int = 3) -> CompactionResult:
        sentences = [s.strip() for s in re.split(r"[.!?]+", text) if s.strip()]
        if len(sentences) <= max_sentences:
            return CompactionResult(text, len(text), len(text), 1.0)

        # Score and keep top sentences in original order
        scored = [(i, s, cls._score_sentence(s)) for i, s in enumerate(sentences)]
        scored.sort(key=lambda x: x[2], reverse=True)
        top = sorted(scored[:max_sentences], key=lambda x: x[0])

        compacted = ". ".join(s for _, s, _ in top) + "."
        orig_len = len(text)
        comp_len = len(compacted)
        ratio = round(comp_len / max(1, orig_len), 3)

        return CompactionResult(compacted, orig_len, comp_len, ratio)
