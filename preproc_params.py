#!/bin/env python3
"""
Preprocess output from BookBuddy app into a format which is legible to the
main script
"""

import argparse
import csv
import sys

def main():
    """
    Provide an interface, reading the file provided by that interface,
    calling process on it, and writing it to stdout
    """
    parser = argparse.ArgumentParser(
        description="format into standard expected csv"
                    "for further processing")
    parser.add_argument('infile',
                        nargs='?', default='-',
                        type=argparse.FileType('r'),
                        help="file name of input file")
    args = parser.parse_args()

    with args.infile as infile:
        header_reader = csv.reader(infile)
        header = next(header_reader)
        filereader = csv.DictReader(infile, header)
        filewriter = csv.DictWriter(sys.stdout, header)
        filewriter.writeheader()
        for row in filereader:
            filewriter.writerow(process(row))

if __name__ == "__main__":
    main()

def process(row: dict) -> dict:
    """
    Perform the processing; separate the dimensions column
    """
    return row.copy()
