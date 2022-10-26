"""
Creation: 2022/10/21
Author: https://github.com/smv7
Description: Tests for the `Doccano2Spacy` format converter."""


from pathlib import Path
import json
import unittest

from custom_dtypes import DoccanoJsonlData, SpacyJsonlData
from doccano2spacy import Doccano2Spacy


class TestDoccano2Spacy(unittest.TestCase):
    """
    Integration tests for `Doccano2Spacy` class."""

    def setUp(self) -> None:
        path = Path(__file__).parent.joinpath('data/sample.jsonl')
        self.converter = Doccano2Spacy(path)
        # self.to_convert: DoccanoJsonlData = None
        # self.expected_data: SpacyJsonlData = None

        return None

    def test_convert_jsonl(self) -> None:
        """
        Unit test for .jsonl's conversion method between Doccano and spaCy's Prodigy formats."""

        converted_data = self.converter.convert_jsonl()
        self.assertTrue(converted_data == SpacyJsonlData)

        return None


if __name__ == '__main__':
    unittest.main()
