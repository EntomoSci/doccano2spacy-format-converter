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


class SpacyJsonlTokenBadFormat(Exception):
    """
    Exception raised when input files don't meet `SpacyJsonlToken` format."""
    

class SpacyJsonlSpanBadFormat(Exception):
    """
    Exception raised when input files don't meet `SpacyJsonlSpan` format."""


class SpacyJsonlEntryBadFormat:
    """
    Exception raised when input files don't meet `SpacyJsonlEntry` format."""


class SpacyJsonlDataBadFormat:
    """
    Exception raised when input files don't meet `SpacyJsonlData` format."""
