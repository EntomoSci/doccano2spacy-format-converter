"""
Creation: 2022/10/21
Author: https://github.com/smv7
Description: Custom data types used by this project."""


from typing import NewType, TypedDict


# Types for Doccano's format.
DoccanoLabelArray = NewType('DoccanoLabelArray', tuple[int, int, str])
DoccanoJsonlDict = TypedDict('DoccanoJsonlDict', {'id': int, 'text': str, 'label': DoccanoLabelArray})

#TODO: Types for spaCy's compatible format.
