"""
Creation: 2022/10/21
Author: https://github.com/smv7
Description: Custom exceptions used by this project."""



class DoccanoJsonlLabelBadFormat(Exception):
    """
    Exception raised when input files don't meet `DoccanoJsonlLabel` format."""


class DoccanoJsonlEntryBadFormat(Exception):
    """
    Exception raised when input files don't meet `DoccanoJsonlEntry` format."""


class DoccanoJsonlDataBadFormat(Exception):
    """
    Exception raised when input files don't meet `DoccanoJsonlData` format."""
