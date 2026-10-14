#!/usr/bin/env python3
"""Regression tests for Herald Dictionary retrieval; standard library only."""
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from knowledge_lib import load_entries, search_entries


class KnowledgeSearchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.entries = load_entries(ROOT / "knowledge")

    def test_rag_acronym_finds_retrieval_entry(self):
        results = search_entries(self.entries, "RAG", limit=5)
        self.assertTrue(results)
        self.assertIn("retrieval-augmented-generation", [entry.id for entry, _ in results])

    def test_speech_to_text_alias_finds_speech_entry(self):
        results = search_entries(self.entries, "speech to text", limit=5)
        self.assertTrue(results)
        self.assertIn("speech-recognition-and-synthesis", [entry.id for entry, _ in results])

    def test_ocr_acronym_finds_document_entry(self):
        results = search_entries(self.entries, "OCR", limit=5)
        self.assertTrue(results)
        self.assertIn("document-ocr-and-parsing", [entry.id for entry, _ in results])

    def test_tag_filter_is_respected(self):
        results = search_entries(self.entries, "privacy", limit=10, tag="security")
        self.assertTrue(results)
        self.assertTrue(all("security" in entry.tags for entry, _ in results))

    def test_status_filter_is_respected(self):
        results = search_entries(self.entries, "retrieval", limit=10, status="draft")
        self.assertTrue(results)
        self.assertTrue(all(entry.status == "draft" for entry, _ in results))

    def test_limit_must_be_positive(self):
        with self.assertRaises(ValueError):
            search_entries(self.entries, "retrieval", limit=0)

    def test_unrelated_query_can_return_no_results(self):
        results = search_entries(self.entries, "zzzxqvnonexistentterm", limit=5)
        self.assertEqual(results, [])


if __name__ == "__main__":
    unittest.main()
