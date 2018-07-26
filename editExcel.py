# Editing excel spreadsheets

import openpyxl

print("Now we'll create a new excel spreadsheet")
print('I need to read the current openpyxl module documentation "http://openpyxl.readthedocs.io/en/stable/tutorial.html"')

wb = openpyxl.Workbook()
wb

print(wb.get_sheet_names())

sheet = wb.get_sheet_by_name('Sheet')

print(sheet)

cellA1 = sheet['A1'].value
print(cellA1)
cellA1 = 42
print(cellA1)

cellA2 = sheet['A2'].value
cellA2 = 'Hello'
print(cellA2)

import os
os.chdir('c:\\users\\drew\\downloads')
cwd = os.getcwd()
print(cwd)
wb.save('editexample.xlsx')

sheet2 = wb.create_sheet()
print(wb.get_sheet_names())

print(sheet2.title)

sheet2.title = "NewName"

print(wb.get_sheet_names())

wb.save('editexample2.xlsx')
