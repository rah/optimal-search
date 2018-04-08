#! /usr/env/python
"""
Simple utilities to convert excel files with
multiple sheets into separate csv formats and then
write that format into csv files
"""
import xlrd
import os.path

data_dir = "../data"
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


def convert_to_csv_format(filename):
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


def write_csv_to_file(data, data_dir, file_prefix):
    '''
    Take a dictionary of csv formatted data and write to csv files
    '''
    if file_prefix is None:
        file_prefix = ""

    for key in data.keys():
        csv_file = data_dir + '/' + file_prefix + "-" + key + ".csv"
        if os.path.exists(csv_file):
            continue

        f = open(csv_file, 'w')
        lines = data[key]

        for line in lines:
            f.write(line + '\n')

        f.close()


def test():
    for file in files:
        data = convert_to_csv_format(file)
        write_csv_to_file(data, data_dir, "test")

if __name__ == "__main__":
    test()
