"""
Creation: 2022/10/21
Author: https://github.com/smv7
Description: Format converter from Doccano to Spacy's compatible format of Prodigy."""


import json
from pathlib import Path

from custom_dtypes import (
    DoccanoJsonlEntry, DoccanoJsonlData,
    SpacyJsonlEntry, SpacyJsonlData)


class Doccano2Spacy:
    """
    Format converter from Doccano to Spacy's compatible format of Prodigy."""

    #TODO: Conversion rules as class attributes.

    def __init__(self, file2convert: str | Path) -> None:
        # Opening and converting the file to "DoccanoJsonlData" object for internal processing.
        if isinstance(file2convert, str):
            with open(file2convert, 'rt', encoding='utf-8') as f:
                # data = json.loads(f.readlines)
                data = json.load(f)
        elif isinstance(file2convert, Path):
            with file2convert.open('rt', encoding='utf-8') as f:
                data: list = [json.loads(entry) for entry in f.readlines()]
                # data = json.load(f)
        else:
            print(f'Unable to open {file2convert}')
            exit(1)

        print(type(data), data)

        return None

    def convert_jsonl(self, data: list[DoccanoJsonlEntry]) -> list[SpacyJsonlEntry]:
        """
        Return converted version of `data` from Doccano's .jsonl format to spaCy's compatible format .jsonl."""

        converted_data: SpacyJsonlData = list()


        return converted_data


if __name__ == '__main__':
    path = Path(__file__).parent.joinpath('sample.jsonl')
    converter = Doccano2Spacy(path)
