import pandas as pd
import numpy as np
import tkinter
from tkinter import filedialog
from openpyxl import load_workbook

if __name__ == "__main__":
    tkinter.Tk().withdraw() # prevents an empty tkinter window from appearing
    # file = filedialog.askopenfile(mode='r')
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", ".xlsx .xls")])

    wb = load_workbook(file_path)
    
    SHEET_NAME = 'Output_Desired Format'

    # file = pd.read_excel(file_path, sheet_name=SHEET_NAME)
    file = pd.read_excel(file_path)

    fileArr = np.asarray(file)

    # column by column
    fileArr = [[item2 for item2 in item] for item in fileArr]

    # 7 = hours of entry

    # writer = pd.ExcelWriter(file_path, engine='openpyxl')

    # print(fileArr)
    for item in fileArr:
        print(item[7])

# https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html
# https://thinkingneuron.com/add-new-sheet-to-excel-using-pandas/
# https://stackoverflow.com/questions/66663179/how-to-use-windows-file-explorer-to-select-and-return-a-directory-using-python