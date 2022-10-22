"""
Creation: 2022/10/21
Author: https://github.com/smv7
Description: Tests for the custom dtypes at `custom_dtypes.py` module."""


import unittest

from custom_dtypes import (
    DoccanoJsonlLabel, DoccanoJsonlEntry, DoccanoJsonlData,
    SpacyJsonlToken, SpacyJsonlSpan, SpacyJsonlEntry, SpacyJsonlData)
from custom_typehints import (
    DoccanoJsonlEntryTH, DoccanoJsonlLabelTH, DoccanoJsonlDataTH,
    SpacyJsonlTokenTH, SpacyJsonlSpanTH, SpacyJsonlEntryTH, SpacyJsonlDataTH)
from utils.test_samples import doccano_jsonl_data, spacy_jsonl_data


class TestCustomDtypes(unittest.TestCase):
    """
    Tests for the custom dtypes at `custom_dtypes.py` module."""

    def setUp(self) -> None:
        # doccano_jsonl_label = DoccanoJsonlLabel()
        # doccano_jsonl_entry = DoccanoJsonlEntry()
        # doccano_jsonl_data = DoccanoJsonlData()
        # spacy_jsonl_token = SpacyJsonlToken()
        # spacy_jsonl_span = SpacyJsonlSpan()
        # spacy_jsonl_entry = SpacyJsonlEntry()
        # spacy_jsonl_data = SpacyJsonlData()

        return None

    def test_doccano_jsonl_label(self) -> None:
        """
        Test `custom_dtypes.DoccanoJsonlLabel`."""

        checks: list[bool] = []
        for entry in doccano_jsonl_data:
            entry: DoccanoJsonlEntryTH
            for label in entry['labels']:
                label: DoccanoJsonlLabelTH
                checks.append(DoccanoJsonlLabel(label) == label)
        self.assertTrue(all(checks))

        return None

    def test_doccano_jsonl_entry(self) -> None:
        """
        Test `custom_dtypes.DoccanoJsonlEntry`."""

        checks: list[bool] = []
        for entry in doccano_jsonl_data:
            entry: DoccanoJsonlEntryTH
            checks.append(DoccanoJsonlEntry(entry) == entry)
        self.assertTrue(all(checks))

        return None

    def test_doccano_jsonl_data(self) -> None:
        """
        Test `custom_dtypes.DoccanoJsonlData`."""

        doccano_jsonl_data: DoccanoJsonlDataTH
        self.assertTrue(DoccanoJsonlEntry(doccano_jsonl_data) == doccano_jsonl_data)

        return None

    def test_spacy_jsonl_token(self) -> None:
        """
        Test `custom_dtypes.SpacyJsonlToken`."""

        checks: list[bool] = []
        for entry in spacy_jsonl_data:
            entry: SpacyJsonlEntryTH
            for token in entry['tokens']:
                token: SpacyJsonlTokenTH
                checks.append(SpacyJsonlToken(token) == token)
        self.assertTrue(all(checks))

        return None

    def test_spacy_jsonl_span(self) -> None:
        """
        Test `custom_dtypes.SpacyJsonlSpan`."""

        checks: list[bool] = []
        for entry in spacy_jsonl_data:
            entry: SpacyJsonlEntryTH
            for span in entry['spans']:
                span: SpacyJsonlSpanTH
                checks.append(SpacyJsonlSpan(span) == span)
        self.assertTrue(all(checks))

        return None

    def test_spacy_jsonl_entry(self) -> None:
        """
        Test `custom_dtypes.SpacyJsonlEntry`."""

        checks: list[bool] = []
        for entry in spacy_jsonl_data:
            entry: SpacyJsonlEntryTH
            checks.append(SpacyJsonlEntry(entry) == entry)
        self.assertTrue(all(checks))

        return None

    def test_spacy_jsonl_data(self) -> None:
        """
        Test `custom_dtypes.SpacyJsonlData`."""

        spacy_jsonl_data: SpacyJsonlDataTH
        self.assertTrue(SpacyJsonlData(spacy_jsonl_data) == spacy_jsonl_data)

        return None
