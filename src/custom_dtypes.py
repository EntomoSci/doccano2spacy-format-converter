"""
Creation: 2022/10/21
Author: https://github.com/smv7
Description: Custom data types used by this project."""


from typing import NewType, TypedDict


# Types for Doccano's format.
DoccanoLabelArray = NewType('DoccanoLabelArray', tuple[int, int, str])
DoccanoJsonlEntry = TypedDict('DoccanoJsonlEntry', {'id': int, 'text': str, 'label': DoccanoLabelArray})

# Types for spaCy's compatible format.
SpacyTokenDict = TypedDict('SpacyTokenDict', {'text': str, 'start': int, 'end': int, 'id': int})
SpacySpanDict = TypedDict('SpacySpanDict', {'start': int, 'end': int,
                                            'token_start': int, 'token_end': int, 'label': str})
SpacyJsonlEntry = TypedDict('SpacyJsonlDict', {'text': str, 'tokens': list[SpacyTokenDict],
                                               'spans': list[SpacySpanDict]})
