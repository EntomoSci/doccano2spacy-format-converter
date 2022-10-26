"""
Creation: 2022/10/21
Author: https://github.com/smv7
Description: Main script for Doccano/Spacy format conversions through a CLI."""


import argparse
from json import dumps
import sys
from pathlib import Path

from doccano2spacy import Doccano2Spacy


#TODO: Output file options.
#TODO: Flags to control input/output formats.
def main():
    # Configuring the argument parser to control CLI.
    parser = argparse.ArgumentParser("Doccano to Spacy's compatible format.",
                                     description="Format converter from Doccano to Spacy's compatible format")
    parser.add_argument('-f', '--file', help='File to convert.')
    parser.add_argument('-o', '--out', default='./data/converted.jsonl', help='Converted file destination.')

    # Displaying the help message when no arguments are given.
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()

    # Reading the input file to convert and creating the output converted file.
    destination_file = Path(__file__).parent.joinpath(args.out)
    with destination_file.open('wt', encoding='utf-8') as file2write:
        file2read = Path(args.file)
        converter = Doccano2Spacy(file2read)
        print(f'Converting {file2read}...')
        converted_data = converter.get_converted_jsonl()
        print(f'Writing converted data to {destination_file}...')
        for entry in converted_data.get():
            file2write.write(dumps(entry) + '\n')
        print('File successfully converted!')


if __name__ == '__main__':
    main()
