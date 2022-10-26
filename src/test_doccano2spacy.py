"""
Creation: 2022/10/21
Author: https://github.com/smv7
Description: Tests for the `Doccano2Spacy` format converter."""


from json import loads
from pathlib import Path
import unittest

from custom_dtypes import SpacyJsonlData
from custom_exceptions import SpacyJsonlDataBadFormat
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

    def test_get_converted_jsonl(self) -> None:
        """
        Test for .jsonl's conversion method between Doccano and spaCy's Prodigy formats."""

        converted_data = self.converter._get_converted_jsonl()
        self.assertTrue(converted_data == self.reference_data)
        self.assertIsInstance(converted_data, SpacyJsonlData)

        return None

    def test_loading_converted_file_back(self) -> None:
        """
        Test converted output .jsonl file with `Doccano2Spacy.` by loading it back to a `SpacyJsonlData` object"""

        file2read = Path(__file__).parent.joinpath('./data/sample.jsonl')
        converted_file2load_path = Path(__file__).parent.joinpath('./data/converted.jsonl')
        with (converted_file2load_path.open('wt', encoding='utf-8') as file2write,
              converted_file2load_path.open('rt', encoding='utf-8') as converted_file2load):
            converter = Doccano2Spacy(file2read)
            converter.convert_jsonl_to(file2write)
            convertion_back_fail = False
            try:
                SpacyJsonlData([loads(entry) for entry in converted_file2load.readlines()])
            except SpacyJsonlDataBadFormat:
                convertion_back_fail = True

            self.assertFalse(convertion_back_fail)

        return None


if __name__ == '__main__':
    unittest.main()
