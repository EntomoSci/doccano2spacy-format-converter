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

        # Building and storing the Doccano's .jsonl entries passed as they custom dtypes.
        self.entries = list[SpacyJsonlEntry] = []
        for e in entries:

            # Building and storing the entry tokens as its custom dtype.
            tokens: list[SpacyJsonlToken] = []
            for t in e['tokens']:
                token = SpacyJsonlToken(t['text'], t['start'], t['end'], t['id'])
                tokens.append(token)

            # Building and storing the entry spans as its custom dtype.
            spans: list[SpacyJsonlSpan] = []
            for s in e['spans']:
                span = SpacyJsonlSpan(s['start'], s['end'], s['token_start'], s['token_end'], s['label'])
                spans.append(span)

            # Building and storing the annotated entry as they custom dtypes.
            entry = SpacyJsonlEntry(e['text'], tokens, spans)
            self.entries.append(entry)

        return None
