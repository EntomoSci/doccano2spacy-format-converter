"""
Creation: 2022/10/21
Author: https://github.com/smv7
Description: Custom data types used by this project."""


from custom_typehints import (
    DoccanoJsonlEntryTH, DoccanoJsonlLabelTH, DoccanoJsonlDataTH,
    SpacyJsonlTokenTH, SpacyJsonlSpanTH, SpacyJsonlEntryTH, SpacyJsonlDataTH
)


class DoccanoJsonlEntry:
    """
    Doccano's annotated entry in .jsonl format."""

    def __init__(self, id: int, text: str, label: DoccanoJsonlLabelTH) -> None:
        self.id: int = id
        self.text: int = text
        self.label: DoccanoJsonlLabelTH = label

        return None


class DoccanoJsonlData:
    """
    Doccano's annotated data in .jsonl format."""

    def __init__(self, entries: list[DoccanoJsonlEntryTH]) -> None:
        self.entries: list[DoccanoJsonlEntry] = [DoccanoJsonlEntry(entry['id'], entry['text'], entry['label'])
                                                 for entry in entries]

        return None


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

    def __init__(self, text: str, tokens: list[SpacyJsonlTokenTH], spans: list[SpacyJsonlSpanTH]) -> None:
        self.text: str = text
        self.tokens: list[SpacyJsonlToken] = tokens
        self.spans: list[SpacyJsonlSpan] = spans

        return None


class SpacyJsonlData:
    """Spacy's annotated data in .jsonl format."""

    def __init__(self, entries: list[SpacyJsonlEntryTH]) -> None:
        self.entries: list[SpacyJsonlEntry] = entries

        return None
