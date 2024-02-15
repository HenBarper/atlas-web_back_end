#!/usr/bin/env python3
"""Write a Python script that provides some stats
   about Nginx logs stored in MongoDB:

Database: logs
Collection: nginx
Display (same as the example):
first line: x logs where x is the number of documents in this collection
second line: Methods:
5 lines with the number of documents with the method
    = ["GET", "POST", "PUT", "PATCH", "DELETE"] in this order
    (see example below - warning: it’s a tabulation before each line)
one line with the number of documents with:
method=GET
path=/status
You can use this dump as data sample: dump.zip"""


def log_the_stats():
    """Provides some stats about Nginx logs"""
    pass


if __name__ == "__main__":
    log_the_stats()
