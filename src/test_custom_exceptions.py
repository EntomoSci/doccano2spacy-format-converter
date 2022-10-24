"""
Creation: 2022/10/21
Author: https://github.com/smv7
Description: Tests for the custom exceptions at `custom_exceptions.py` module."""


import unittest

from custom_dtypes import (
    DoccanoJsonlLabel, DoccanoJsonlEntry, DoccanoJsonlData,
    SpacyJsonlToken, SpacyJsonlSpan, SpacyJsonlEntry, SpacyJsonlData)
from custom_exceptions import (
    DoccanoJsonlLabelBadFormat, DoccanoJsonlEntryBadFormat, DoccanoJsonlDataBadFormat)
from custom_typehints import (
    DoccanoJsonlLabelTH, DoccanoJsonlEntryTH, DoccanoJsonlDataTH,
    SpacyJsonlTokenTH, SpacyJsonlSpanTH, SpacyJsonlEntryTH, SpacyJsonlDataTH)


class TestCustomExceptions(unittest.TestCase):
    """
    Tests for the custom exceptions at `custom_dtypes.py` module."""

    def test_doccano_jsonl_label_exception(self) -> None:
        """
        Test `custom_dtypes.DoccanoJsonlLabelBadFormat`."""

        bad_formated_samples: list[DoccanoJsonlLabelTH] = [
            ('label', 1, 1),
            (1, 1, 1),
            (1, 'label', 1),
            ('1', '1', 'label'),
            ('1', 1, 'label'),
            (1, 1, ['label'])]

        checks: int = 0
        for sample in bad_formated_samples:
            try:
                DoccanoJsonlLabel(sample)
            except DoccanoJsonlLabelBadFormat as e:
                checks += 1

        self.assertTrue(checks == len(bad_formated_samples))

        return None


if __name__ == '__main__':
    unittest.main()
