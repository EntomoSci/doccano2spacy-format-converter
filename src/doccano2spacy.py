"""
Creation: 2022/10/21
Author: https://github.com/smv7
Description: Format converter from Doccano to Spacy's compatible format of Prodigy."""


from io import TextIOWrapper
import re
import json
from pathlib import Path

from spacy.tokenizer import Tokenizer
from spacy.pipeline import Sentencizer
from spacy.tokens import Token, Span, Doc
from spacy.lang.es import Spanish

from custom_dtypes import SpacyJsonlData
from custom_typehints import (
    DoccanoJsonlLabelTH, DoccanoJsonlEntryTH, DoccanoJsonlDataTH,
    SpacyJsonlTokenTH, SpacyJsonlSpanTH, SpacyJsonlEntryTH, SpacyJsonlDataTH)


class Doccano2Spacy:
    """
    Format converter from Doccano to Spacy's compatible format of Prodigy."""

    def __init__(self, file2read: str | Path) -> None:
        self.file2read = file2read 
        # Opening and converting the file to "DoccanoJsonlData" object for internal processing.
        if isinstance(file2read, str):
            with open(file2read, 'rt', encoding='utf-8') as f:
                self.loaded_data: DoccanoJsonlDataTH = [json.loads(entry) for entry in f.readlines()]
        elif isinstance(file2read, Path):
            with file2read.open('rt', encoding='utf-8') as f:
                self.loaded_data: DoccanoJsonlDataTH = [json.loads(entry) for entry in f.readlines()]
        else:
            print(f'Unable to open {file2read}')
            exit(1)

        # Creating a blank tokenizer to segment text and a blank sentencizer to detect sentences.
        # NOTE: The tokenizer needs a custom suffix rule to consider  also as tokens ".", "," and consecutive numbers
        # that can be appended to text. The no differentiation of those tokens causes issues with start/end indices set
        # by Doccano in the .jsonl file.
        self.tokenizer = Tokenizer(Spanish().vocab,
                                   suffix_search=re.compile(r'[.,]$|\d+').search)
        self.sentencizer = Sentencizer()

        return None

    def _get_converted_jsonl(self) -> SpacyJsonlData:
        """
        Return initialized document from Doccano's .jsonl format converted to spaCy's compatible .jsonl format."""

        converted_data: SpacyJsonlDataTH = []
        for entry in self.loaded_data:
            entry: DoccanoJsonlEntryTH
            tokenized_text: Doc = self.tokenizer(entry['text'])

            # Create list of SpacyJsonlToken using DoccanoJsonlEntry's text key.
            tokens: list[SpacyJsonlTokenTH] = []
            for token in tokenized_text:
                token: Token
                token_dict = {'text': token.text, 'start': token.idx, 'end': token.idx + len(token), 'id': token.i}
                tokens.append(token_dict)

            # Create list of SpacyJsonlSpan using DoccanoJsonlEntry's label key.
            # NOTE: To get the token's start/end ids relative to the full text, a spaCy's Span object with convenient
            # attributes had to be used, created by slicing the text's Doc object by its chars instead of tokens,
            # because Doccano's .jsonl format only had available the chars' start/end indices.
            spans: list[SpacyJsonlSpanTH] = []
            doc: Doc = self.sentencizer(tokenized_text)
            for label in entry['label']:
                label: DoccanoJsonlLabelTH
                st_slice, end_slice = label[0], label[1]
                # NOTE: The "Doc.char_span" method using its default "alignment_mode='strict'" consider the punctuation
                # as part of the last sentence's token, so the start/end indices MUST consider them as tokens; only
                # whitespace separates tokens with the configuration used here.
                span_slice: Span = doc.char_span(st_slice, end_slice)
                token_start, token_end = span_slice.start, span_slice.end - 1
                label_dict = {'start': label[0], 'end': label[1],
                              'token_start': token_start, 'token_end': token_end, 'label': label[2]}
                spans.append(label_dict)

            # Create the converted entry as a SpacyJsonlEntry object with the builded tokens and spans.
            converted_entry: SpacyJsonlEntryTH = {'text': entry['text'],'tokens': tokens, 'spans': spans}
            converted_data.append(converted_entry)

        return SpacyJsonlData(converted_data)

    def convert_jsonl_to(self, file2write: TextIOWrapper) -> None:
        """
        Convert `file2read` from Doccano's .jsonl format to Spacy's compatible .jsonl format at `file2write`."""

        print(f'Converting {self.file2read}...')
        converted_data = self._get_converted_jsonl()
        print(f'Writing converted data to {file2write.name}...')
        for entry in converted_data.get():
            file2write.write(json.dumps(entry) + '\n')
        print('File successfully converted!')

        return None


if __name__ == '__main__':
    path = Path(__file__).parent.joinpath('data/sample.jsonl')
    converter = Doccano2Spacy(path)
    converter.convert_jsonl()
