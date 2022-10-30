"""
Creation: 2022/10/21
Author: https://github.com/smv7
Description: Main script for Doccano/Spacy format conversions through a CLI."""


import argparse
import sys
from pathlib import Path

from converter.doccano2spacy import Doccano2Spacy


#TODO: Output file options.
#TODO: Flags to control input/output formats.
def main():
    # Configuring the argument parser to control CLI.
    parser = argparse.ArgumentParser("d2s",
                                     description="Format converter from Doccano to Spacy's compatible format")
    parser.add_argument('file2convert', help='File to convert.')
    parser.add_argument('destination', nargs='?', default='./converted.jsonl',
                        help='Converted file destination. Defaults to "./converted.jsonl".')

    # Displaying the help message when no arguments are given.
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()

    # Reading the input file to convert and creating the output converted file.
    destination_file_path = Path.cwd().joinpath(args.destination)
    with destination_file_path.open('wt', encoding='utf-8') as file2write:
        file2read = Path(args.file2convert)
        converter = Doccano2Spacy(file2read)
        converter.convert_jsonl_to(file2write)

if __name__ == '__main__':
    main()
