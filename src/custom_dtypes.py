"""
Creation: 2022/10/21
Author: https://github.com/smv7
Description: Custom data types used by this project."""


from typing import NewType, TypedDict


# Types and classes for Doccano's format.
DoccanoJsonlLabel = NewType('DoccanoLabelArray', tuple[int, int, str])

#TODO: Consider the replacement of classes instead of custom type hints.
# DoccanoJsonlEntry = TypedDict('DoccanoJsonlEntry', {'id': int, 'text': str, 'label': DoccanoLabelArray})
# DoccanoJsonlData = NewType('DoccanoJsonlData', list[DoccanoJsonlEntry])

class DoccanoJsonlEntry:
    """
    Doccano's annotated entry in .jsonl format."""

    def __init__(self, id: int, text: str, label: DoccanoJsonlLabel) -> None:
        self.id: int = id
        self.text: int = text
        self.label: DoccanoJsonlLabel = label

        return None


class DoccanoJsonlData:
    """
    Doccano's annotated data in .jsonl format."""

    def __init__(self, entries: list[DoccanoJsonlEntry]) -> None:
        self.entries: list[DoccanoJsonlEntry] = entries

        return None


# Types for spaCy's compatible format.
SpacyTokenDict = TypedDict('SpacyTokenDict', {'text': str, 'start': int, 'end': int, 'id': int})
SpacySpanDict = TypedDict('SpacySpanDict', {'start': int, 'end': int,
                                            'token_start': int, 'token_end': int, 'label': str})
SpacyJsonlEntry = TypedDict('SpacyJsonlDict', {'text': str, 'tokens': list[SpacyTokenDict],
                                               'spans': list[SpacySpanDict]})
SpacyJsonlData = NewType('SpacyJsonlData', list[SpacyJsonlEntry])


class SpacyJsonlToken:
    """
    Spacy's token in .jsonl format."""

    def __init__(self, text: str, start: int, end: int, id: int) -> None:
        self.text: str = text
        self.start: int = start
        self.end: int = end
        self.id: int = id

        return None


class SpacyJsonlSpan:
    """
    Spacy's span in .jsonl format."""

    def __init__(self, start: int, end: int, token_start: int, token_end: int, label: str) -> None:
        self.start: int = start
        self.end: int = end
        self.token_start: int = token_start
        self.token_end: int = token_end
        self.label: str = label

        return None


class SpacyJsonlEntry:
    """
    Spacy's annotated entry in .jsonl format."""

    def __init__(self, text: str, tokens: list[SpacyJsonlToken], spans: list[SpacyJsonlSpan]) -> None:
        self.text: str = text
        self.tokens: list[SpacyJsonlToken] = tokens
        self.spans: list[SpacyJsonlSpan] = spans

        return None


class SpacyJsonlData:
    """Spacy's annotated data in .jsonl format."""

    def __init__(self, entries: list[SpacyJsonlEntry]) -> None:
        self.entries: list[SpacyJsonlEntry] = entries

        return None
