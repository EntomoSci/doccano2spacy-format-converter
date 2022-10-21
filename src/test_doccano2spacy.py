"""
Creation: 2022/10/21
Author: https://github.com/smv7
Description: Tests for the `Doccano2Spacy` format converter."""


import unittest

from custom_dtypes import DoccanoJsonlData, SpacyJsonlData
from doccano2spacy import Doccano2Spacy


class TestDoccano2Spacy(unittest.TestCase):
    """
    Integration tests for `Doccano2Spacy` class."""

    def setUp(self) -> None:
        self.converter = Doccano2Spacy()
        self.to_convert: DoccanoJsonlData = None
        self.expected_data: SpacyJsonlData = None

        return None

    def test_convert_jsonl(self) -> None:
        """
        Unit test for .jsonl's conversion method between Doccano and spaCy's Prodigy formats."""

        converted_data = self.converter.convert_jsonl(self.to_convert)

        return None
