"""
Creation: 2022/10/21
Author: https://github.com/smv7
Description: Custom type hints used by this project."""


from typing import NewType, TypedDict


# Type hints for Doccano's format.
DoccanoJsonlLabelTH = NewType('DoccanoJsonlLabelTH', tuple[int, int, str])
DoccanoJsonlEntryTH = TypedDict('DoccanoJsonlEntryTH', {'id': int, 'text': str, 'label': DoccanoJsonlLabelTH})
DoccanoJsonlDataTH = NewType('DoccanoJsonlDataTH', list[DoccanoJsonlEntryTH])


# Type hints for spaCy's compatible format.
SpacyJsonlTokenTH = TypedDict('SpacyTokenDictTH', {'text': str, 'start': int, 'end': int, 'id': int})
SpacyJsonlSpanTH = TypedDict('SpacyJsonlSpanTH', {'start': int, 'end': int,
                                            'token_start': int, 'token_end': int, 'label': str})
SpacyJsonlEntryTH = TypedDict('SpacyJsonlDict', {'text': str, 'tokens': list[SpacyJsonlTokenTH],
                                               'spans': list[SpacyJsonlSpanTH]})
SpacyJsonlDataTH = NewType('SpacyJsonlData', list[SpacyJsonlEntryTH])
