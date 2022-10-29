"""
Creation: 2022/10/21
Author: https://github.com/smv7
Description: Custom data types used by this project."""


from converter.custom_typehints import (
    DoccanoJsonlLabelTH, DoccanoJsonlEntryTH, DoccanoJsonlDataTH,
    SpacyJsonlTokenTH, SpacyJsonlSpanTH, SpacyJsonlEntryTH, SpacyJsonlDataTH)

from converter.custom_exceptions import (
    DoccanoJsonlLabelBadFormat, DoccanoJsonlEntryBadFormat, DoccanoJsonlDataBadFormat,
    SpacyJsonlTokenBadFormat, SpacyJsonlSpanBadFormat, SpacyJsonlEntryBadFormat, SpacyJsonlDataBadFormat)


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
        try:
            id_, text, label = entry['id'], entry['text'], [DoccanoJsonlLabel(label) for label in entry['label']]
        except (KeyError, IndexError, TypeError, DoccanoJsonlLabelBadFormat):
            err_msg: str = f'Entry "{entry}" don\'t meet format required. ' +\
                        f'Must be non-empty {DoccanoJsonlEntryTH.__annotations__}.'
            raise DoccanoJsonlEntryBadFormat(err_msg)
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
        try:
            entries: list[DoccanoJsonlEntry] = [DoccanoJsonlEntry(entry) for entry in entries]
        except (DoccanoJsonlEntryBadFormat, TypeError) as e:
            err_msg: str = f'Entries "{entries}" don\'t meet format required. ' +\
                        f'Must be non-empty {DoccanoJsonlDataTH.__supertype__}.'
            raise DoccanoJsonlDataBadFormat(err_msg)
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
        err_msg: str = f'Token "{token}" don\'t meet format required. ' +\
                        f'Must be non-empty {SpacyJsonlTokenTH.__annotations__}.'
        err = SpacyJsonlTokenBadFormat(err_msg)
        try:
            text, start, end, id_ = token['text'], token['start'], token['end'], token['id']
            if not all([isinstance(x, type_) for x, type_ in zip((text, start, end, id_), (str, int, int, int))]):
                raise err
        except (TypeError, KeyError) as e:
            raise err
        else:
            self.text: str = text
            self.start: int = start
            self.end: int = end
            self.id: int = id_

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

    def get(self) -> SpacyJsonlTokenTH:
        """
        Return spaCy's jsonl token representation with python build-in dtypes."""

        return {'text': self.text, 'start': self.start, 'end': self.end, 'id': self.id}


class SpacyJsonlSpan:
    """
    Spacy's span in .jsonl format."""

    def __init__(self, span: SpacyJsonlSpanTH) -> None:
        err_msg: str = f'Span "{span}" don\'t meet format required. ' +\
                        f'Must be non-empty {SpacyJsonlSpanTH.__annotations__}.'
        err = SpacyJsonlSpanBadFormat(err_msg)
        try:
            start: int = span['start']
            end: int = span['end']
            token_start: int = span['token_start']
            token_end: int = span['token_end']
            label: str = span['label']
            if not all([isinstance(x, type_)
                        for x, type_ in zip((start, end, token_start, token_end, label),
                                             (int, int, int, int, str))]):
                raise err
        except (KeyError, TypeError) as e:
            raise err
        else:
            self.start: int = start
            self.end: int = end
            self.token_start: int = token_start
            self.token_end: int = token_end
            self.label: str = label

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

    def get(self) -> SpacyJsonlSpanTH:
        """
        Return spaCy's jsonl span representation with python build-in dtypes."""

        return {
            'start': self.start, 'end': self.end,
            'token_start': self.token_start, 'token_end': self.token_end, 'label': self.label}


class SpacyJsonlEntry:
    """
    Spacy's annotated entry in .jsonl format."""

    def __init__(self, entry: SpacyJsonlEntryTH) -> None:
        try:
            text: str = entry['text']
            tokens: list[SpacyJsonlToken] = [SpacyJsonlToken(token) for token in entry['tokens']]
            spans: list[SpacyJsonlSpan] = [SpacyJsonlSpan(span) for span in entry['spans']]
        except (KeyError, IndexError, TypeError, SpacyJsonlTokenBadFormat, SpacyJsonlSpanBadFormat):
            err_msg: str = f'Entry "{entry}" don\'t meet format required. ' +\
                        f'Must be non-empty {SpacyJsonlEntryTH.__annotations__}.'
            raise SpacyJsonlEntryBadFormat(err_msg)
        else:
            self.text: str = text
            self.tokens: list[SpacyJsonlToken] = tokens
            self.spans: list[SpacyJsonlSpan] = spans

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

    def get(self) -> SpacyJsonlEntryTH:
        """
        Return spaCy's jsonl entry representation with python build-in dtypes."""

        return {
            'text': self.text,
            'tokens': [token.get() for token in self.tokens],
            'spans': [span.get() for span in self.spans]}


class SpacyJsonlData:
    """Spacy's annotated data in .jsonl format."""

    def __init__(self, entries: SpacyJsonlDataTH) -> None:
        try:
            entries: SpacyJsonlDataTH = [SpacyJsonlEntry(entry) for entry in entries]
        except (SpacyJsonlEntryBadFormat, TypeError) as e:
            err_msg: str = f'Entries "{entries}" don\'t meet format required. ' +\
                           f'Must be non-empty {SpacyJsonlDataTH.__supertype__}.'
            raise SpacyJsonlDataBadFormat(err_msg)
        else:
            self.entries: list[SpacyJsonlEntry] = entries

        return None

    def __eq__(self, __o: object) -> bool:
        checks: list[bool] = []
        try:
            checks.append(isinstance(__o, list))
            checks.append(self.entries[0] == __o[0])
        except KeyError:
            return False

        return all(checks)

    def get(self) -> SpacyJsonlDataTH:
        """
        Return spaCy's jsonl data representation with python build-in dtypes."""

        for entry in self.entries:
            yield entry.get()
