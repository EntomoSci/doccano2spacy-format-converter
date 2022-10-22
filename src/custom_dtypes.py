"""
Creation: 2022/10/21
Author: https://github.com/smv7
Description: Custom data types used by this project."""


from custom_typehints import (
    DoccanoJsonlEntryTH, DoccanoJsonlLabelTH, DoccanoJsonlDataTH,
    SpacyJsonlTokenTH, SpacyJsonlSpanTH, SpacyJsonlEntryTH, SpacyJsonlDataTH)


class DoccanoJsonlEntry:
    """
    Doccano's annotated entry in .jsonl format."""

    def __init__(self, entry: DoccanoJsonlEntryTH) -> None:
        self.id: int = entry['id']
        self.text: int = entry['text']
        self.label: DoccanoJsonlLabelTH = entry['label']

        return None


class DoccanoJsonlData:
    """
    Doccano's annotated data in .jsonl format."""

    def __init__(self, entries: list[DoccanoJsonlEntryTH]) -> None:
        self.entries: list[DoccanoJsonlEntry] = [
            DoccanoJsonlEntry(entry['id'], entry['text'], entry['label']) for entry in entries]

        return None


class SpacyJsonlToken:
    """
    Spacy's token in .jsonl format."""

    def __init__(self, token: SpacyJsonlTokenTH) -> None:
        self.text: str = token['text']
        self.start: int = token['start']
        self.end: int = token['end']
        self.id: int = token['id']

        return None

    def __eq__(self, __o: object) -> bool:
        checks: list[bool] = []
        try:
            #NOTE: The check to other compound types is made with its respective __eq__ methods.
            checks.append(isinstance(__o, dict))
            checks.append(isinstance(__o['text'], type(self.text)))
            checks.append(isinstance(__o['start'], type(self.start)))
            checks.append(isinstance(__o['end'], type(self.end)))
            checks.append(isinstance(__o['id'], type(self.id)))
        except KeyError:
            return False

        return all(checks)


class SpacyJsonlSpan:
    """
    Spacy's span in .jsonl format."""

    def __init__(self, span: SpacyJsonlSpanTH) -> None:
        self.start: int = span['start']
        self.end: int = span['end']
        self.token_start: int = span['token_start']
        self.token_end: int = span['token_end']
        self.label: str = span['label']

        return None

    def __eq__(self, __o: object) -> bool:
        checks: list[bool] = []
        try:
            #NOTE: The check to other compound types is made with its respective __eq__ methods.
            checks.append(isinstance(__o, dict))
            checks.append(isinstance(__o['start'], type(self.start)))
            checks.append(isinstance(__o['end'], type(self.end)))
            checks.append(isinstance(__o['token_start'], type(self.token_start)))
            checks.append(isinstance(__o['token_end'], type(self.token_end)))
            checks.append(isinstance(__o['label'], type(self.label)))
        except KeyError:
            return False

        return all(checks)


class SpacyJsonlEntry:
    """
    Spacy's annotated entry in .jsonl format."""

    def __init__(self, entry: SpacyJsonlEntryTH) -> None:
        self.text: str = entry['text']
        self.tokens: list[SpacyJsonlToken] = entry['tokens']
        self.spans: list[SpacyJsonlSpan] = entry['spans']

        return None

    def __eq__(self, __o: object) -> bool:
        checks: list[bool] = []
        try:
            #NOTE: The check to other compound types is made with its respective __eq__ methods.
            checks.append(isinstance(__o, dict))
            checks.append(isinstance(__o['text'], type(self.text)))
            checks.append(isinstance(__o['tokens'], type(self.tokens)))
            checks.append(__o['tokens'][0] == self.tokens[0])
            checks.append(isinstance(__o['spans'], type(self.spans)))
            checks.append(__o['spans'][0] == self.spans[0])
        except KeyError:
            return False

        return all(checks)


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

    def __eq__(self, __o: object) -> bool:
        checks: list[bool] = []
        try:
            #NOTE: The check to other compound types is made with its respective __eq__ methods.
            checks.append(isinstance(__o, list))
            checks.append(__o[0] == self.entries[0])
        except KeyError:
            return False

        return all(checks)
