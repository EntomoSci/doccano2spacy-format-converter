"""
Creation: 2022/10/21
Author: https://github.com/smv7
Description: Tests for the `Doccano2Spacy` format converter."""


from pathlib import Path
import unittest

from custom_dtypes import SpacyJsonlData
from doccano2spacy import Doccano2Spacy
from utils.test_samples import spacy_jsonl_data


class TestDoccano2Spacy(unittest.TestCase):
    """
    Integration tests for `Doccano2Spacy` class."""

    def setUp(self) -> None:
        path = Path(__file__).parent.joinpath('data/sample.jsonl')
        self.converter = Doccano2Spacy(path)
        self.reference_data = spacy_jsonl_data

        return None

    def test_convert_jsonl(self) -> None:
        """
        Test for .jsonl's conversion method between Doccano and spaCy's Prodigy formats."""

        converted_data = self.converter.convert_jsonl()
        self.assertTrue(converted_data == self.reference_data)
        self.assertIsInstance(converted_data, SpacyJsonlData)

        return None


if __name__ == '__main__':
    unittest.main()
