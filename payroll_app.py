import os
import pandas as pd
import numpy as np
import tkinter
import datetime
from tkinter import filedialog
from tkinter import messagebox
from openpyxl import load_workbook

from employee import employee

if __name__ == "__main__":
    EMPLOYEE_CODES = 'Employee Codes'
    VACATION_HOURS = 'Vacation Hours'

    tkinter.Tk().withdraw() # prevents an empty tkinter window from appearing
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", ".xlsx .xls")])
    if not file_path:
        messagebox.showerror("PayrollApp Error", f"Error in opening file, check spreadsheet and try again")
        exit(1)

    # check for if file exists
    try:
        wb = load_workbook(file_path, read_only=True)
    except:
        messagebox.showerror("PayrollApp Error", f"Make sure the excel file is not corrupted")
        exit(1)

    try:
        codesFile = pd.read_excel(file_path, sheet_name=EMPLOYEE_CODES)
    except ValueError:
        messagebox.showerror("PayrollApp Error", f"Missing 'Employee Codes' sheet")
        exit(1)



    tempCodes = np.asarray(codesFile)
    # reading in employee codes
    codes = []
    for item in tempCodes:
        tempList = []
        if str(item[0]) != 'NaT' and str(item[0]) != 'nan':
            if type(item[2]) == type(1) or type(item[2]) == type(1.0) or '-' in str(item[2]):
                for item2 in item:
                    tempList.append(item2)
        if len(tempList) != 0:
            codes.append(tempList)



    vacationSheet = False
    try:
        vacationFile = pd.read_excel(file_path, sheet_name=VACATION_HOURS)
        vacationSheet = True
    except ValueError:
        vacationSheet = False

    if vacationSheet:
        tempVacation = np.asarray(vacationFile)
        vacationHours = []
        for item in tempVacation:
            tempList = []
            if str(item[0]) != 'NaT' and str(item[0]) != 'nan' and str(item[7]) != 'NaT' and str(item[7]) != 'nan':
                tempList.append(item[0])
                tempList.append(item[1])
                tempList.append(round(item[7] * 100))
            if len(tempList) != 0:
                vacationHours.append(tempList)



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
            try:
                name = code[0].lower().strip() + ' ' + code[1].lower().strip()
            except AttributeError:
                messagebox.showerror("PayrollApp Error", f"Please remove the last line in the codes file")
                exit(1)
            if type(code[2]) == type('str'):
                employees[name] = employee(name, str(code[2]).replace("-",""))
            else:
                employees[name] = employee(name, str(int(code[2])))

    

    # updating employees with data
    missing_names = set()
    for entry in data:
        # update hours with the category and the hours
        if entry[13].lower() not in employees.keys():
            # add missing names to set
            missing_names.add(entry[13])
        else:
            employees[entry[13].lower()].update_hours(entry[14], entry[7])
            employees[entry[13].lower()].update_tip(entry[9])
            employees[entry[13].lower()].update_reimbursement(entry[10])

    # updating employees with vacation hours
    if vacationSheet:
        for entry in vacationHours:
            name = entry[0] + ' ' + entry[1]
            if name.lower() not in employees.keys():
                missing_names.add(name)
            else:
                employees[name.lower()].update_hours("vacation", entry[2])



    # add pop up for all missing names
    if len(missing_names) > 0:
        messagebox.showerror("PayrollApp Error", f"Missing employee code for {missing_names}")
        exit(1)



    # performing final calculation and outputting
    final_output = employees.values()
    final_output = [output.final_hours() for output in final_output if output != employee()]
    

    
    try:
        np.savetxt(os.path.join(os.path.split(file_path)[0], "payroll_output.csv"), final_output, delimiter=", ",fmt='% s')
    except:
        messagebox.showerror("PayrollApp", f"Please close the previous output file")
        exit(1)

    tkinter.Tk().withdraw()
    messagebox.showinfo("PayrollApp", f"Output file went to: { os.path.split(file_path)[0] }")
    exit(0)