"""
Creation: 2022/10/21
Author: https://github.com/smv7
Description: Main script for Doccano/Spacy format conversions through a CLI."""


import sys
from pathlib import Path
import argparse


#TODO: Output file options.
#TODO: Flags to control input/output formats.
def main():
    # Configuring the argument parser to control CLI.
    parser = argparse.ArgumentParser("Doccano to Spacy's compatible format.",
                                     description="Format converter from Doccano to Spacy's compatible format")
    parser.add_argument('-f', '--file', help='File to convert.')
    parser.add_argument('-o', '--out', default='./converted.jsonl', help='Converted file destination.')

    # Displaying the help message when no arguments are given.
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()


    # Reading the input file to convert and creating the output converted file.
    with Path(__file__).parent.joinpath(args.file).open('rt', encoding='utf-16') as fto_read,\
         Path(__file__).parent.joinpath(args.out).open('wt', encoding='utf-8') as fto_write:
        data = fto_read.read()
        fto_write.write()


if __name__ == '__main__':
    main()
