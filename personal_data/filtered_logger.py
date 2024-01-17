#!/usr/bin/env python3
"""Write a function called filter_datum
that returns the log message obfuscated"""
import re
import typing
import logging
import os
import mysql.connector


PII_FIELDS: tuple = ("name", "email", "phone", "ssn", "password")


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: typing.List[str]):
        """Init method for redacting formatter"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Format method for redacting formatter"""
        record.msg = filter_datum(self.fields, self.REDACTION,
                                  record.msg, self.SEPARATOR)
        return super(RedactingFormatter, self).format(record)


def filter_datum(fields: typing.List[str], redaction: str,
                 message: str, separator: str) -> str:
    """The function should use a regex to replace
    occurrences of certain field values"""
    for field in fields:
        pattern = r'({})([^{}]+)'.format(field + '=', separator)
        message = re.sub(pattern, r"\1{}".format(redaction), message)
    return message


def get_logger() -> logging.Logger:
    """Get logger method for the filtered logger"""
    user_data = logging.getLogger("user_data")
    user_data.setLevel(logging.INFO)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(fields=PII_FIELDS))
    user_data.addHandler(stream_handler)
    user_data.propagate = False

    return user_data


def get_db() -> mysql.connector.connection.MySQLConnection:
    """Return a connector to the secure database"""
    return mysql.connector.connect(
        user=os.getenv('PERSONAL_DATA_DB_USERNAME', 'root'),
        password=os.getenv("PERSONAL_DATA_DB_PASSWORD", ""),
        host=os.getenv("PERSONAL_DATA_DB_HOST", "localhost"),
        database=os.getenv("PERSONAL_DATA_DB_NAME", "")
    )
