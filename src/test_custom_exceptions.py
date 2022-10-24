"""
Creation: 2022/10/21
Author: https://github.com/smv7
Description: Tests for the custom exceptions at `custom_exceptions.py` module."""


import unittest

from custom_dtypes import (
    DoccanoJsonlLabel, DoccanoJsonlEntry, DoccanoJsonlData,
    SpacyJsonlToken, SpacyJsonlSpan, SpacyJsonlEntry, SpacyJsonlData)
from custom_exceptions import (
    DoccanoJsonlLabelBadFormat, DoccanoJsonlEntryBadFormat, DoccanoJsonlDataBadFormat,
    SpacyJsonlTokenBadFormat, SpacyJsonlSpanBadFormat, SpacyJsonlEntryBadFormat, SpacyJsonlDataBadFormat)
from custom_typehints import (
    DoccanoJsonlLabelTH, DoccanoJsonlEntryTH, DoccanoJsonlDataTH,
    SpacyJsonlTokenTH, SpacyJsonlSpanTH, SpacyJsonlEntryTH, SpacyJsonlDataTH)
from utils.test_samples import (
    bad_doccano_jsonl_label_samples, bad_doccano_jsonl_entry_samples, bad_doccano_jsonl_data_samples,
    bad_spacy_jsonl_token_samples, bad_spacy_jsonl_span_samples, bad_spacy_jsonl_entry_samples)


class TestCustomExceptions(unittest.TestCase):
    """
    Tests for the custom exceptions at `custom_dtypes.py` module."""

    def setUp(self) -> None:
        self.bad_doccano_jsonl_label_samples = bad_doccano_jsonl_label_samples
        self.bad_doccano_jsonl_entry_samples = bad_doccano_jsonl_entry_samples
        self.bad_doccano_jsonl_data_samples = bad_doccano_jsonl_data_samples
        self.bad_spacy_jsonl_token_samples = bad_spacy_jsonl_token_samples
        self.bad_spacy_jsonl_span_samples = bad_spacy_jsonl_span_samples
        self.bad_spacy_jsonl_entry_samples = bad_spacy_jsonl_entry_samples

        return None

    def test_doccano_jsonl_label_exception(self) -> None:
        """
        Test `custom_dtypes.DoccanoJsonlLabelBadFormat`."""

        samples: DoccanoJsonlLabelTH = self.bad_doccano_jsonl_label_samples
        checks: int = 0
        for sample in samples:
            try:
                DoccanoJsonlLabel(sample)
            except DoccanoJsonlLabelBadFormat as e:
                checks += 1

        self.assertTrue(checks == len(samples))

        return None

    def test_doccano_jsonl_entry_exception(self) -> None:
        """
        Test `custom_dtypes.DoccanoJsonlEntryBadFormat`."""

        samples: DoccanoJsonlEntryTH = self.bad_doccano_jsonl_entry_samples
        checks: int = 0
        for sample in samples:
            try:
                DoccanoJsonlEntry(sample)
            except DoccanoJsonlEntryBadFormat as e:
                checks += 1

        self.assertTrue(checks == len(samples))

        return None

    def test_doccano_jsonl_data_exception(self) -> None:
        """
        Test `custom_dtypes.DoccanoJsonlDataBadFormat`."""
    
        samples: DoccanoJsonlDataTH = self.bad_doccano_jsonl_data_samples
        checks: int = 0
        for sample in samples:
            try:
                DoccanoJsonlData(sample)
            except DoccanoJsonlDataBadFormat as e:
                # print(type(e), e)
                checks += 1
        self.assertTrue(checks == len(samples))

        return None

    def test_spacy_jsonl_token_exception(self) -> None:
        """
        Test `custom_dtypes.SpacyJsonlTokenBadFormat`."""

        samples: list[SpacyJsonlTokenTH] = self.bad_spacy_jsonl_token_samples
        checks: int = 0
        for sample in samples:
            try:
                SpacyJsonlToken(sample)
            except SpacyJsonlTokenBadFormat as e:
                # print(type(e), e)
                checks += 1
        self.assertTrue(checks == len(samples))

        return None

    def test_spacy_jsonl_span_exception(self) -> None:
        """
        Test `custom_dtypes.SpacyJsonlSpanBadFormat`."""

        samples: list[SpacyJsonlSpanTH] = self.bad_spacy_jsonl_span_samples
        checks: int = 0
        for sample in samples:
            try:
                SpacyJsonlSpan(sample)
            except SpacyJsonlSpanBadFormat as e:
                # print(type(e), e)
                checks += 1
        self.assertTrue(checks == len(samples))

        return None

    def test_spacy_jsonl_entry_exception(self) -> None:
        """
        Test `custom_dtypes.SpacyJsonlEntryBadFormat`."""

        samples: list[SpacyJsonlEntryTH] = self.bad_spacy_jsonl_entry_samples
        checks: int = 0
        for sample in samples:
            try:
                SpacyJsonlEntry(sample)
            except SpacyJsonlEntryBadFormat as e:
                # print(type(e), e)
                checks += 1
        self.assertTrue(checks == len(samples))

        return None


if __name__ == '__main__':
    unittest.main()
