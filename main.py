import pandas as pd
import numpy as np
import tkinter
from tkinter import filedialog

if __name__ == "__main__":
    tkinter.Tk().withdraw() # prevents an empty tkinter window from appearing
    # file = filedialog.askopenfile(mode='r')
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", ".xlsx .xls")])

    file = open(file_path)

    print(file.read())

# https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html
# https://thinkingneuron.com/add-new-sheet-to-excel-using-pandas/
# https://stackoverflow.com/questions/66663179/how-to-use-windows-file-explorer-to-select-and-return-a-directory-using-python