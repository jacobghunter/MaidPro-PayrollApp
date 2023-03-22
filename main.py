import os
import pandas as pd
import numpy as np
import tkinter
from tkinter import filedialog
from tkinter import messagebox
from openpyxl import load_workbook

import datetime

from employee import employee
import math

if __name__ == "__main__":
    EMPLOYEE_CODES = 'Employee Codes'

    tkinter.Tk().withdraw() # prevents an empty tkinter window from appearing
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", ".xlsx .xls")])
    if not file_path:
        messagebox.showerror("PayrollApp Error", f"Error in opening file, check spreadsheet and try again")
        exit(1)

    try:
        wb = load_workbook(file_path)
    except:
        messagebox.showerror("PayrollApp Error", f"Make sure the excel file is not corrupted")
        exit(1)

    try:
        codesFile = pd.read_excel(file_path, sheet_name=EMPLOYEE_CODES)
    except ValueError:
        messagebox.showerror("PayrollApp Error", f"Missing employee codes sheet")
        exit(1)

    tempCodes = np.asarray(codesFile)

    # reading in employee codes
    codes = []
    for item in tempCodes:
        tempList = []
        if str(item[0]) != 'NaT' and str(item[0]) != 'nan':
            for item2 in item:
                tempList.append(item2)
        if len(tempList) != 0:
            codes.append(tempList)


    # data file has to be first one
    dataFile = pd.read_excel(file_path)
    tempData = np.asarray(dataFile)

    # reading in data
    data = []
    for item in tempData:
        tempList = []
        # hinges on column 1 being a date
        if isinstance(item[0], datetime.date) and str(item[0]) != 'NaT':
            for item2 in item:
                # converting to int to avoid weird errors
                if isinstance(item2, float) and str(item2) != 'nan':
                    tempList.append(round(item2 * 100))
                else:
                    tempList.append(item2)
        if len(tempList) != 0:
            data.append(tempList)


    # employee creation
    employees = {}
    for code in codes:
        if str(code[0]) != 'nan': 
            name = code[0].lower() + ' ' + code[1].lower()
            employees[name] = employee(name, code[2])

    missing_names = set()

    # updating employees with data
    for entry in data:
        # update hours with the category and the hours
        if entry[13].lower() not in employees.keys():
            # add missing names to set
            missing_names.add(entry[13])
        else:
            employees[entry[13].lower()].update_hours(entry[14], entry[7])
            employees[entry[13].lower()].update_tip(entry[9])
            employees[entry[13].lower()].update_reimbursement(entry[10])

    # add pop up for all missing names
    if len(missing_names) > 0:
        messagebox.showerror("PayrollApp Error", f"Missing employee code for {missing_names}")
        exit(1)

    # performing final calculation and outputting
    final_output = []
    for person in employees.values():
        final_output.append(person.final_hours())
    
    np.savetxt("payroll_output.csv", final_output, delimiter=", ",fmt='% s')
    messagebox.showinfo("PayrollApp", f"Output file went to: { os.path.dirname(os.path.realpath(__file__)) }")