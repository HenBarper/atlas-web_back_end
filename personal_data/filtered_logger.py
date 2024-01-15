#!/usr/bin/env python3
""""""
import re


def filter_datum(fields, redaction, message, separator):
    """"""
    for field in fields:
        pattern = r'({})([^;]+)'.format(field + '=')
        message = re.sub(pattern, r"\1{}".format(redaction), message)
    return message
