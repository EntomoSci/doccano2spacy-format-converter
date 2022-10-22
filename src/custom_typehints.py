"""
Creation: 2022/10/21
Author: https://github.com/smv7
Description: Custom type hints used by this project."""


from typing import NewType, TypedDict


# Type hints for Doccano's format.
DoccanoJsonlLabelTH = NewType('DoccanoJsonlLabelTH', tuple[int, int, str])
DoccanoJsonlEntryTH = TypedDict('DoccanoJsonlEntryTH', {'id': int, 'text': str, 'labels': list[DoccanoJsonlLabelTH]})
DoccanoJsonlDataTH = NewType('DoccanoJsonlDataTH', list[DoccanoJsonlEntryTH])


# Type hints for spaCy's compatible format.
SpacyJsonlTokenTH = TypedDict('SpacyJsonlTokenTH', {'text': str, 'start': int, 'end': int, 'id': int})
SpacyJsonlSpanTH = TypedDict('SpacyJsonlSpanTH', {'start': int, 'end': int,
                                            'token_start': int, 'token_end': int, 'label': str})
SpacyJsonlEntryTH = TypedDict('SpacyJsonlEntryTH', {'text': str, 'tokens': list[SpacyJsonlTokenTH],
                                               'spans': list[SpacyJsonlSpanTH]})
SpacyJsonlDataTH = NewType('SpacyJsonlDataTH', list[SpacyJsonlEntryTH])
