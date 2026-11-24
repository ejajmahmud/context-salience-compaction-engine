"""Tests for ContextCompactor."""
import unittest
from context_salience_compaction_engine.core import ContextCompactor

class TestContextCompactor(unittest.TestCase):
    def test_compaction_preserves_salient_sentences(self):
        text = "Hello there. We found a bug in test suite. General chatter here. Another error returned."
        res = ContextCompactor.compact(text, max_sentences=2)
        self.assertTrue(res.compacted_length < res.original_length)
        self.assertIn("bug", res.compacted_text)
        self.assertIn("error", res.compacted_text)
