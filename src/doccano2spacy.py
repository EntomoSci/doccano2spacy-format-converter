"""
Creation: 2022/10/21
Author: https://github.com/smv7
Description: Format converter from Doccano to Spacy's compatible format of Prodigy."""


from custom_dtypes import DoccanoJsonlEntry, SpacyJsonlEntry


class Doccano2Spacy:
    """
    Format converter from Doccano to Spacy's compatible format of Prodigy."""

    #TODO: Conversion rules as class attributes.

    def __init__(self) -> None:
        pass

    def convert_jsonl(self, data: list[DoccanoJsonlEntry]) -> list[SpacyJsonlEntry]:
        """
        Return converted version of `data` from Doccano's .jsonl format to spaCy's compatible format .jsonl."""

        converted_data: str

        return converted_data


if __name__ == '__main__':
    pass
