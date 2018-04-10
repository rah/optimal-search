#! /usr/env/python
"""
Simple utilities to convert excel files with
multiple sheets into separate csv formats and then
write that format into csv files
"""
import xlrd
import os
import re


def format_line(values, sep=','):
    '''
    Format an array of values into csv format returning a string
    '''
    line = ""
    cols = len(values)
    col = 0

    for value in values:
        col += 1
        if col != cols:
            line = line + str(value) + sep
        else:
            line = line + str(value)

    return line


def convert_to_csv_format(filename, data_dir):
    '''
    Convert an excel workbook into csv format. For each sheet
    an array of lines will be returned. The result provides a
    dictionary of sheets with csv formatted lines.
    '''
    result = {}

    book = xlrd.open_workbook(data_dir + '/' + filename)
    sheet_names = book.sheet_names()

    for sheet_name in sheet_names:
        sheet = book.sheet_by_name(sheet_name)
        rows = sheet.nrows
        csv = []
        for row in range(rows):
            # remove the second row
            if row == 1:
                continue

            # format the row values array to csv
            csv.append(format_line(sheet.row_values(row)))

        result[sheet_name] = csv

    return result


def filename_from(key):
    '''
    Ensure consistent naming of files:
      - prepend with SNA if not exists
      - remove .1 if exists
    '''
    if 'SNA' not in key:
        key = 'SNA' + key

    if '.1' in key:
        key = re.sub('\.1', '', key)

    return key


def write_csv_to_file(data, data_dir, file_prefix=None):
    '''
    Take a dictionary of csv formatted data and write to csv files
    '''
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    if file_prefix is None:
        file_prefix = ""
    else:
        file_prefix = file_prefix + "-"

    for key in data.keys():
        csv_file = data_dir + '/' + file_prefix + filename_from(key) + ".csv"
        if os.path.exists(csv_file):
            continue

        f = open(csv_file, 'w')
        lines = data[key]

        for line in lines:
            f.write(line + '\n')

        f.close()


def convert_files(input_dir, output_dir, files, prefix=None):
    for file in files:
        data = convert_to_csv_format(file, input_dir)
        write_csv_to_file(data, output_dir, prefix)


if __name__ == "__main__":

    input_dir = "data/ANALYSIS"
    output_dir = "data/tracks"

    files = [
        "84-10-19 tvl.xls",
        "84-10-20 tvl.xls",
        "84-10-22 tvl.xls",
        "84-11-05 lab.xls",
        "84-11-12 lab.xls",
        "84-12-23 mar.xls",
        "85-02-20 lab 2.xls",
        "85-03-06 tvl.xls",
        "85-03-10 lab.xls",
        "85-03-14 lab.xls",
        "85-04-03 tvl.xls",
        "85-05-01 tvl.xls",
        "85-06-12 mar.xls",
        "85-06-17 mar.xls",
        "85-06-28 mar.xls",
        "85-07-16 tvl.xls",
        "85-07-29 tvl.xls",
        "85-08-14 tvl.xls",
        "85-08-26 tvl.xls",
        "85-09-10 tvl.xls",
    ]

    convert_files(input_dir, output_dir, files)
