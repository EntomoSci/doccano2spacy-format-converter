"""
Creation: 2022/10/21
Author: https://github.com/smv7
Description: Custom data types used by this project."""


from custom_typehints import (
    DoccanoJsonlLabelTH, DoccanoJsonlEntryTH, DoccanoJsonlDataTH,
    SpacyJsonlTokenTH, SpacyJsonlSpanTH, SpacyJsonlEntryTH, SpacyJsonlDataTH)

from custom_exceptions import (
    DoccanoJsonlLabelBadFormat, DoccanoJsonlEntryBadFormat, DoccanoJsonlDataBadFormat)


#NOTE: The __eq__ methods are used for object comparison using the compound custom type hints that defines the structure
# of the objects. For the comparison of inner compound types like "DoccanoJsonlLabel" inside "DoccanoJsonlEntry" objects
# its respetive __eq__ methods are used iteratively.


class DoccanoJsonlLabel:
    """
    Doccano's annotated label in .jsonl format."""

    def __init__(self, label_: DoccanoJsonlLabelTH) -> None:
        err_msg: str = f'Label "{label_}" don\'t meet format required. ' +\
                       f'Must be non-empty {DoccanoJsonlLabelTH.__supertype__}.'
        err = DoccanoJsonlLabelBadFormat(err_msg)
        try:
            start, end, label = label_[0], label_[1], label_[2]
            if not all([isinstance(x, type_) for x, type_ in zip((start, end, label), (int, int, str))]):
                raise err
        except IndexError:
            raise err
        else:
            self.start: int = start
            self.end: int = end
            self.label: str = label

        return None

    def __eq__(self, __o: object) -> bool:
        checks: list[bool] = []
        try:
            checks.append(isinstance(__o, tuple | list))  #NOTE: Labels format can be passed as in/mutable sequences.
            checks.append(isinstance(__o[0], type(self.start)))
            checks.append(isinstance(__o[1], type(self.end)))
            checks.append(isinstance(__o[2], type(self.label)))
        except IndexError as e:
            print(e)
            return False

        return all(checks)


class DoccanoJsonlEntry:
    """
    Doccano's annotated entry in .jsonl format."""

    def __init__(self, entry: DoccanoJsonlEntryTH) -> None:
        err_msg: str = f'Entry "{entry}" don\'t meet format required. ' +\
                       f'Must be non-empty {DoccanoJsonlEntryTH.__annotations__}.'
        err = DoccanoJsonlEntryBadFormat(err_msg)
        try:
            id_, text, label = entry['id'], entry['text'], [DoccanoJsonlLabel(label) for label in entry['label']]
            if not isinstance(entry, dict) or\
               not all([isinstance(x, type_) for x, type_ in zip((id_, text, label), (int, int, list))]) or\
               not isinstance(label[0], DoccanoJsonlEntryTH):
                raise err
        except (KeyError, IndexError, TypeError, DoccanoJsonlLabelBadFormat):
            raise err
        else:
            self.id: int = id_
            self.text: int = text
            self.label: list[DoccanoJsonlLabelTH] = label

        return None

    def __eq__(self, __o: object) -> bool:
        checks: list[bool] = []
        try:
            checks.append(isinstance(__o, dict))
            checks.append(isinstance(__o['id'], type(self.id)))
            checks.append(isinstance(__o['text'], type(self.text)))
            checks.append(isinstance(__o['label'], type(self.label)))
            checks.append(self.label[0] == __o['label'][0])
        except KeyError as e:
            print(e)
            return False

        return all(checks)


class DoccanoJsonlData:
    """
    Doccano's annotated data in .jsonl format."""

    def __init__(self, entries: list[DoccanoJsonlEntryTH]) -> None:
        err_msg: str = f'Entries "{entries}" don\'t meet format required. ' +\
                       f'Must be non-empty {DoccanoJsonlDataTH.__supertype__}.'
        err = DoccanoJsonlDataBadFormat(err_msg)
        try:
            entries: list[DoccanoJsonlEntry] = [DoccanoJsonlEntry(entry) for entry in entries]
        except (DoccanoJsonlLabelBadFormat, DoccanoJsonlEntryBadFormat, TypeError) as e:
            raise err
        else:
            self.entries = entries

        return None

    def __eq__(self, __o: object) -> bool:
        checks: list[bool] = []
        try:
            checks.append(isinstance(__o, list))
            checks.append(self.entries[0] == __o[0])
        except KeyError as e:
            print(e)
            return False

        return all(checks)


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
        self.tokens: list[SpacyJsonlToken] = [SpacyJsonlToken(token) for token in entry['tokens']]
        self.spans: list[SpacyJsonlSpan] = [SpacyJsonlSpan(span) for span in entry['spans']]

        return None

    def __eq__(self, __o: object) -> bool:
        checks: list[bool] = []
        try:
            checks.append(isinstance(__o, dict))
            checks.append(isinstance(__o['text'], type(self.text)))
            checks.append(isinstance(__o['tokens'], type(self.tokens)))
            checks.append(self.tokens[0] == __o['tokens'][0])
            checks.append(isinstance(__o['spans'], type(self.spans)))
            checks.append(self.spans[0] == __o['spans'][0])
        except KeyError:
            return False

        return all(checks)


class SpacyJsonlData:
    """Spacy's annotated data in .jsonl format."""

    def __init__(self, entries: list[SpacyJsonlEntryTH]) -> None:
        self.entries: list[SpacyJsonlEntry] = [SpacyJsonlEntry(entry) for entry in entries]

        return None

    def __eq__(self, __o: object) -> bool:
        checks: list[bool] = []
        try:
            checks.append(isinstance(__o, list))
            checks.append(self.entries[0] == __o[0])
        except KeyError:
            return False

        return all(checks)

if __name__ == '__main__':
    a = DoccanoJsonlLabel((1, 1, ['label']))
    print(type(a), a)
    print(DoccanoJsonlLabelTH.__supertype__)
