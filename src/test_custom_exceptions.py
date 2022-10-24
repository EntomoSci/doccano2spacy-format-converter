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
    bad_doccano_jsonl_label_samples)


class TestCustomExceptions(unittest.TestCase):
    """
    Tests for the custom exceptions at `custom_dtypes.py` module."""

    def setUp(self) -> None:
        self.bad_doccano_jsonl_label_samples = bad_doccano_jsonl_label_samples

        return None

    def test_doccano_jsonl_label_exception(self) -> None:
        """
        Test `custom_dtypes.DoccanoJsonlLabelBadFormat`."""

        samples = self.bad_doccano_jsonl_label_samples
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

        bad_formated_samples: list[DoccanoJsonlEntryTH] = [
            {},
            {"id": 2, "text": "Componentes necesarios para jugar la expansión de La Isla. Por si perdió alguno o todos *guiño guino*","label":[[0,12],[37,57,"BOARDGAME_NAME"]]},
            {"id": 2, "text": "Componentes necesarios para jugar la expansión de La Isla. Por si perdió alguno o todos *guiño guino*","label":[["PRODUCT_TYPE"],[37,57,"BOARDGAME_NAME"]]},
            {"id": 2, "text": "Componentes necesarios para jugar la expansión de La Isla. Por si perdió alguno o todos *guiño guino*","label":[[0,12,"PRODUCT_TYPE"],['37',57,"BOARDGAME_NAME"]]},]
            # {"id": 2, "text": "Componentes necesarios para jugar la expansión de La Isla. Por si perdió alguno o todos *guiño guino*","label":[[0,12, 'PRODUCT_TYPE'],[37,57,"BOARDGAME_NAME"]]}]

        checks: int = 0
        for sample in bad_formated_samples:
            try:
                DoccanoJsonlEntry(sample)
            except DoccanoJsonlEntryBadFormat as e:
                checks += 1

        self.assertTrue(checks == len(bad_formated_samples))

        return None

    def test_doccano_jsonl_data_exception(self) -> None:
        """
        Test `custom_dtypes.DoccanoJsonlDataBadFormat`."""
    
        bad_formated_samples: list[DoccanoJsonlDataTH] = [
            [{},
            {"id": 2, "text": "Componentes necesarios para jugar la expansión de La Isla. Por si perdió alguno o todos *guiño guino*","label":[[0,12],[37,57,"BOARDGAME_NAME"]]},
            {"id": 2, "text": "Componentes necesarios para jugar la expansión de La Isla. Por si perdió alguno o todos *guiño guino*","label":[["PRODUCT_TYPE"],[37,57,"BOARDGAME_NAME"]]}
            ], [
            {"id": 2, "text": "Componentes necesarios para jugar la expansión de La Isla. Por si perdió alguno o todos *guiño guino*","label":[[0,12,"PRODUCT_TYPE"],['37',57,"BOARDGAME_NAME"]]},
            {"text": "Componentes necesarios para jugar la expansión de La Isla. Por si perdió alguno o todos *guiño guino*","label":[[0,[12],"PRODUCT_TYPE"],[37,57,"BOARDGAME_NAME"]]},]]

        checks: int = 0
        for sample in bad_formated_samples:
            try:
                DoccanoJsonlData(sample)
            except DoccanoJsonlDataBadFormat as e:
                # print(type(e), e)
                checks += 1
        self.assertTrue(checks == len(bad_formated_samples))

        return None

    def test_spacy_jsonl_token_exception(self) -> None:
        """
        Test `custom_dtypes.SpacyJsonlTokenBadFormat`."""



        return None


if __name__ == '__main__':
    unittest.main()
