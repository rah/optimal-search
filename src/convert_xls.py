#! /usr/env/python
"""
Simple utilities to convert excel files with
multiple sheets into separate csv formats
"""
import xlrd

data_dir = "../data/SNAILS/ANALYSIS"
files = ["84-10-19 tvl.xls"]


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


def convert_to_csv(filename):
    '''
    Convert an excel workbook into csv format. For each sheet
    an array of lines will be returned. The result provides a
    dictional of sheets with csv formatted lines.
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


if __name__ == "__main__":
    for file in files:
        print convert_to_csv(file)
