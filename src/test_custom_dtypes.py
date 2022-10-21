"""
Creation: 2022/10/21
Author: https://github.com/smv7
Description: Tests for the custom dtypes at `custom_dtypes.py` module."""


import unittest

from custom_dtypes import (
    DoccanoJsonlEntry, DoccanoJsonlData,
    SpacyJsonlToken, SpacyJsonlSpan, SpacyJsonlEntry, SpacyJsonlData)
from utils.samples import deccano_entry, spacy_entry


class TestCustomDtypes(unittest.TestCase):
    """
    Tests for the custom dtypes at `custom_dtypes.py` module."""

    def setUp(self) -> None:
        doccano_jsonl_entry = DoccanoJsonlEntry()
        doccano_jsonl_data = DoccanoJsonlData()
        spacy_jsonl_token = SpacyJsonlToken()
        spacy_jsonl_span = SpacyJsonlSpan()
        spacy_jsonl_entry = SpacyJsonlEntry()
        spacy_jsonl_data = SpacyJsonlData()

        return None
