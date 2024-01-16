#!/usr/bin/env python3
"""Write a function called filter_datum
that returns the log message obfuscated"""
import re
import typing


def filter_datum(fields: typing.List[str], redaction: str,
                 message: str, separator: str) -> str:
    """The function should use a regex to replace
    occurrences of certain field values"""
    for field in fields:
        pattern = r'({})([^{}]+)'.format(field + '=', separator)
        message = re.sub(pattern, r"\1{}".format(redaction), message)
    return message
