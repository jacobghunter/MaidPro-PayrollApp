import pandas as pd
import numpy as np
import tkinter
from tkinter import filedialog
from openpyxl import load_workbook

from employee import employee
import math

if __name__ == "__main__":
    EMPLOYEE_CODES = 'Employee Codes'

    tkinter.Tk().withdraw() # prevents an empty tkinter window from appearing
    # file = filedialog.askopenfile(mode='r')
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", ".xlsx .xls")])

    wb = load_workbook(file_path)

    codesFile = pd.read_excel(file_path, sheet_name=EMPLOYEE_CODES)
    dataFile = pd.read_excel(file_path)

    tempCodes = np.asarray(codesFile)
    tempData = np.asarray(dataFile)

    # column by column
    codes = []
    for item in tempCodes:
        tempList = []
        for item2 in item:
            if str(item2) != 'NaT' and str(item2) != 'nan':
                tempList.append(item2)
        if len(tempList) != 0:
            codes.append(tempList)

    print(codes)

    data = []
    for item in tempData:
        tempList = []
        for item2 in item:
            if str(item2) != 'NaT' and str(item2) != 'nan':
                tempList.append(item2)
        if len(tempList) != 0:
            data.append(tempList)

    print(data)

    # 7 = hours of entry

    # writer = pd.ExcelWriter(file_path, engine='openpyxl')

    # 9=tip, 10=adjustment, 11=adjreason, 13=name, 14=category

    employees = {}

    for code in codes:
        if str(code[0]) != 'nan': 
            name = code[0].lower() + ' ' + code[1].lower()
            employees[name] = employee(name, code[2])

    for entry in data:
        # update hours with the category and the hours
        if entry[13].lower() not in employees.keys():
            # tkinter pop up
            pass
            # exit(1)
        else:
            employees[entry[13].lower()].update_hours(entry[14], entry[7])
            employees[entry[13].lower()].update_tip(entry[9])
            employees[entry[13].lower()].update_reimbursement(entry[10])
    
    # print(employees.values())
    for person in employees.values():
        print(person)

# https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html
# https://thinkingneuron.com/add-new-sheet-to-excel-using-pandas/
# https://stackoverflow.com/questions/66663179/how-to-use-windows-file-explorer-to-select-and-return-a-directory-using-python