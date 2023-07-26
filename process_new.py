import sys
# import pickle
import json
import ctypes
from tkinter import *  # get widget classes
# from tkinter import Combobox, Entry, Label, font
# *** path is C:\Users\Owner\AppData\Roaming\JetBrains\PyCharmCE2022.2\scratches
#import ttk
# import logging
# logging.basicConfig(
#     filename = 'app.log',            # Name of the log file (omit to use stderr)
#     filemode = 'w',                  # File mode (use 'a' to append)
#     level    = logging.WARNING,      # Logging level (DEBUG, INFO, WARNING, ERROR, or CRITICAL)
# )
import tkinter as tk
#import numpy as np
#import matplotlib as mpl
#import matplotlib.pyplot as plt
#from scipy import *
#from scipy import constants
# from sqlite3 import *
#from sqlite3 import Error
# import SQL_tables_to_dict_str as sq
# import pdb
# from tkinter import messagebox as mb #*  # get standard dialogs
#from MessageBoxes import *
#from tkinter import messagebox as mb
# from tkinter import font
root = Tk()
# root.config(text="Monster Sudoku Solver")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
print("42 screen_width screen_height", screen_width, screen_height)
root.geometry("1400x1100")
# root.size()
titlefont = ('Ariel', 12, 'bold')
donefont = ('Ariel', 16, 'bold')
labelfont = ('Ariel', 10)
buttonfont = ('Ariel', 10)
entryfont = ('Ariel', 10)
exlanationfont = ('Ariel', 10)
size8font = ('Ariel', 8)
size9font = ('Ariel', 9)
wid = 4
wid6 = 6
hit = 3

currentRow = 0
currentColumn = 0
currentSquare = 0
currentNumber = 0
currentNums = ""
currentSolution = ""
Hints = ""
startingString = "0123456789ABCDEF"
bRemoveANumberFromACell = "False"
bAutoComplete = False
bSolve_singles = False
D = 0
R = 0
NullValue = "Null"

bShowRemainders = False
bInitialShowRemainders = False

r_1_nums = ""
r_2_nums = ""
r_3_nums = ""
r_4_nums = ""
r_5_nums = ""
r_6_nums = ""
r_7_nums = ""
r_8_nums = ""
r_9_nums = ""
r_10_nums = ""
r_11_nums = ""
r_12_nums = ""
r_13_nums = ""
r_14_nums = ""
r_15_nums = ""
r_16_nums = ""
c_1_nums = ""
c_2_nums = ""
c_3_nums = ""
c_4_nums = ""
c_5_nums = ""
c_6_nums = ""
c_7_nums = ""
c_8_nums = ""
c_9_nums = ""
c_10_nums = ""
c_11_nums = ""
c_12_nums = ""
c_13_nums = ""
c_14_nums = ""
c_15_nums = ""
c_16_nums = ""
s_1_nums = ""
s_2_nums = ""
s_3_nums = ""
s_4_nums = ""
s_5_nums = ""
s_6_nums = ""
s_7_nums = ""
s_8_nums = ""
s_9_nums = ""
s_10_nums = ""
s_11_nums = ""
s_12_nums = ""
s_13_nums = ""
s_14_nums = ""
s_15_nums = ""
s_16_nums = ""
row_nums_list = ['r_1_nums', 'r_2_nums', 'r_3_nums', 'r_4_nums', 'r_5_nums', 'r_6_nums', 'r_7_nums', 'r_8_nums',
                 'r_9_nums', 'r_10_nums', 'r_11_nums', 'r_12_nums', 'r_13_nums', 'r_14_nums', 'r_15_nums', 'r_16_nums']
col_nums_list = ['c_1_nums', 'c_2_nums', 'c_3_nums', 'c_4_nums', 'c_5_nums', 'c_6_nums', 'c_7_nums', 'c_8_nums',
                 'c_9_nums', 'c_10_nums', 'c_11_nums', 'c_12_nums', 'c_13_nums', 'c_14_nums', 'c_15_nums', 'c_16_nums']
sq_nums_list = ['s_1_nums', 's_2_nums', 's_3_nums', 's_4_nums', 's_5_nums', 's_6_nums', 's_7_nums', 's_8_nums',
                's_9_nums', 's_10_nums', 's_11_nums', 's_12_nums', 's_13_nums', 's_14_nums', 's_15_nums', 's_16_nums']
delete_singles_row_list = []
delete_singles_col_list = []
delete_singles_sq_list = []

def update_done_arefs_list(aref):
    print("362 Entering update_done_arefs_list aref is ", aref)
    for aref in arrRefs_List:
        if aref['done'] == True:
            not_done_arefs.remove(aref)


btn_ref = {}
# btn_ref = dict(btn='btn_R1C1', aref='arrRef0')

arrStringsRemaining = ""
bShow = False

main_frame = Frame(root)
main_frame.grid(row=0, column=0, columnspan=10)
main_frame.config(highlightbackground="red", highlightthickness=2)
# #Create a Canvas
main_canvas = Canvas(main_frame)
main_canvas.grid(row=0, column=0, columnspan=10)
# Add a Scrollbar to the Canvas
# sb = Scrollbar(main_frame, orient=VERTICAL,command=main_canvas.yview)
# sb.pack(side=RIGHT)
# Configure the Canvas
# main_canvas.configure(yscrollcommand=sb.set)
# main_canvas.bind('<Configure>', lambda e: main_canvas.configure(scrollregion=main_canvas.bbox("all")))
# Create another Frame inside the Canvas
F1_frame = Frame(main_canvas)
F1_frame.grid(row=2, column=0, sticky="nw")
F1_frame.config(highlightbackground="blue", highlightthickness=2)
F2_frame = Frame(main_canvas)
F2_frame.grid(row=2, column=4, sticky="nw")
F2_frame.config(highlightbackground="red", highlightthickness=2)
F3_frame = Frame(main_canvas)
F3_frame.grid(row=2, column=8, sticky="nw")
F3_frame.config(highlightbackground="yellow", highlightthickness=2)
F4_frame = Frame(main_canvas)
F4_frame.grid(row=2, column=12, sticky="nw")
F4_frame.config(highlightbackground="blue", highlightthickness=2)
sn_frame = Frame(main_canvas)
sn_frame.grid(row=2, column=16, sticky="nw") #sn is for select a number
sn_frame.config(highlightbackground="green", highlightthickness=2)
F5_frame = Frame(main_canvas)
F5_frame.grid(row=3, column=0, sticky="nw")
F5_frame.config(highlightbackground="yellow", highlightthickness=2)
F6_frame = Frame(main_canvas)
F6_frame.grid(row=3, column=4, sticky="nw")
F6_frame.config(highlightbackground="green", highlightthickness=2)
F7_frame = Frame(main_canvas)
F7_frame.grid(row=3, column=8, sticky="nw")
F7_frame.config(highlightbackground="blue", highlightthickness=2)
F8_frame = Frame(main_canvas)
F8_frame.grid(row=3, column=12, sticky="nw")
F8_frame.config(highlightbackground="red", highlightthickness=2)
fn_frame = Frame(main_canvas)
fn_frame.grid(row=3, column=16, sticky="nw") #fn is for select a function name
fn_frame.config(highlightbackground="green", highlightthickness=2)
F9_frame = Frame(main_canvas)
F9_frame.grid(row=4, column=0, sticky="nw")
F9_frame.config(highlightbackground="yellow", highlightthickness=2)
F10_frame = Frame(main_canvas)
F10_frame.grid(row=4, column=4, sticky="nw")
F10_frame.config(highlightbackground="green", highlightthickness=2)
F11_frame = Frame(main_canvas)
F11_frame.grid(row=4, column=8, sticky="nw")
F11_frame.config(highlightbackground="blue", highlightthickness=2)
F12_frame = Frame(main_canvas)
F12_frame.grid(row=4, column=12, sticky="nw")
F12_frame.config(highlightbackground="red", highlightthickness=2)
F13_frame = Frame(main_canvas)
F13_frame.grid(row=5, column=0, sticky="nw")
F13_frame.config(highlightbackground="red", highlightthickness=2)
F14_frame = Frame(main_canvas)
F14_frame.grid(row=5, column=4, sticky="nw")
F14_frame.config(highlightbackground="yellow", highlightthickness=2)
F15_frame = Frame(main_canvas)
F15_frame.grid(row=5, column=8, sticky="nw")
F15_frame.config(highlightbackground="green", highlightthickness=2)
F16_frame = Frame(main_canvas)
F16_frame.grid(row=5, column=12, sticky="nw")
F16_frame.config(highlightbackground="blue", highlightthickness=2)
ex_frame = Frame(main_canvas)
ex_frame.grid(row=4, column=16, sticky="nw") #fn is for select a function name
ex_frame.config(highlightbackground="red", highlightthickness=2)
txt_frame = Frame(main_canvas)
txt_frame.grid(row=5, column=16, sticky="nw") #fn is for select a function name
txt_frame.config(highlightbackground="red", highlightthickness=2)


def set_current_num_to_0():
    global currentNumber
    currentNumber = "0"
    print("Current number is ", currentNumber)


def set_current_num_to_1():
    global currentNumber
    currentNumber = "1"
    print("Current number is ", currentNumber)


def set_current_num_to_2():
    global currentNumber
    currentNumber = "2"
    print("Current number is ", currentNumber)


def set_current_num_to_3():
    global currentNumber
    currentNumber = "3"
    print("Current number is ", currentNumber)


def set_current_num_to_4():
    global currentNumber
    currentNumber = "4"
    print("Current number is ", currentNumber)


def set_current_num_to_5():
    global currentNumber
    currentNumber = "5"
    print("Current number is ", currentNumber)

def set_current_num_to_6():
    global currentNumber
    currentNumber = "6"
    print("Current number is ", currentNumber)

def set_current_num_to_7():
    print("button 7 pressed.")
    global currentNumber
    currentNumber = "7"
    print("Current number is ", currentNumber)

def set_current_num_to_8():
    global currentNumber
    currentNumber = "8"
    print("Current number is ", currentNumber)

def set_current_num_to_9():
    global currentNumber
    currentNumber = "9"
    print("Current number is ", currentNumber)

def set_current_num_to_A():
    global currentNumber
    currentNumber = "A"
    print("Current number is ", currentNumber)

def set_current_num_to_B():
    global currentNumber
    currentNumber = "B"
    print("Current number is ", currentNumber)

def set_current_num_to_C():
    global currentNumber
    currentNumber = "C"
    print("Current number is ", currentNumber)

def set_current_num_to_D():
    global currentNumber
    currentNumber = "D"
    print("Current number is ", currentNumber)

def set_current_num_to_E():
    global currentNumber
    currentNumber = "E"
    print("Current number is ", currentNumber)

def set_current_num_to_F():
    global currentNumber
    currentNumber = "F"
    print("Current number is ", currentNumber)

def make_RCS_sets(num):
    print("298 Entered make_RCS_sets", num)
    global r_1_set
    global r_2_set
    global r_3_set
    global r_4_set
    global r_5_set
    global r_6_set
    global r_7_set
    global r_8_set
    global r_9_set
    global r_10_set
    global r_11_set
    global r_12_set
    global r_13_set
    global r_14_set
    global r_15_set
    global r_16_set
    global c_1_set
    global c_2_set
    global c_3_set
    global c_4_set
    global c_5_set
    global c_6_set
    global c_7_set
    global c_8_set
    global c_9_set
    global c_10_set
    global c_11_set
    global c_12_set
    global c_13_set
    global c_14_set
    global c_15_set
    global c_16_set
    global s_1_set
    global s_2_set
    global s_3_set
    global s_4_set
    global s_5_set
    global s_6_set
    global s_7_set
    global s_8_set
    global s_9_set
    global s_10_set
    global s_11_set
    global s_12_set
    global s_13_set
    global s_14_set
    global s_15_set
    global s_16_set
    r_1_set = set()
    r_2_set = set()
    r_3_set = set()
    r_4_set = set()
    r_5_set = set()
    r_6_set = set()
    r_7_set = set()
    r_8_set = set()
    r_9_set = set()
    r_10_set = set()
    r_11_set = set()
    r_12_set = set()
    r_13_set = set()
    r_14_set = set()
    r_15_set = set()
    r_16_set = set()
    c_1_set = set()
    c_2_set = set()
    c_3_set = set()
    c_4_set = set()
    c_5_set = set()
    c_6_set = set()
    c_7_set = set()
    c_8_set = set()
    c_9_set = set()
    c_10_set = set()
    c_11_set = set()
    c_12_set = set()
    c_13_set = set()
    c_14_set = set()
    c_15_set = set()
    c_16_set = set()
    s_1_set = set()
    s_2_set = set()
    s_3_set = set()
    s_4_set = set()
    s_5_set = set()
    s_6_set = set()
    s_7_set = set()
    s_8_set = set()
    s_9_set = set()
    s_10_set = set()
    s_11_set = set()
    s_12_set = set()
    s_13_set = set()
    s_14_set = set()
    s_15_set = set()
    s_16_set = set()
    ex_text = "Empty start\n"
    print("396 len(not_done_arefs) is ", len(not_done_arefs))

    for cell in not_done_arefs:
        if num > len(cell['nums']):
            btn = (cell['btn'])
            row = (cell['row'])
            col = (cell['col'])
            sq = (cell['sq'])
            print("400 cell ", cell)
            if cell['row'] == 1 and len(cell['nums']) < 4:
                r_1_set.add(cell['nums'])
            elif cell['row'] == 2 and len(cell['nums']) < 4:
                r_2_set.add(cell['nums'])
            elif cell['row'] == 3 and len(cell['nums']) < 4:
                r_3_set.add(cell['nums'])
            elif cell['row'] == 4 and len(cell['nums']) < 4:
                r_4_set.add(cell['nums'])
            elif cell['row'] == 5 and len(cell['nums']) < 4:
                r_5_set.add(cell['nums'])
            elif cell['row'] == 6 and len(cell['nums']) < 4:
                r_6_set.add(cell['nums'])
            elif cell['row'] == 7 and len(cell['nums']) < 4:
                r_7_set.add(cell['nums'])
            elif cell['row'] == 8 and len(cell['nums']) < 4:
                r_8_set.add(cell['nums'])
            elif cell['row'] == 9 and len(cell['nums']) < 4:
                r_9_set.add(cell['nums'])
            elif cell['row'] == 10 and len(cell['nums']) < 4:
                r_10_set.add(cell['nums'])
            elif cell['row'] == 11 and len(cell['nums']) < 4:
                r_11_set.add(cell['nums'])
            elif cell['row'] == 12 and len(cell['nums']) < 4:
                r_12_set.add(cell['nums'])
            elif cell['row'] == 13 and len(cell['nums']) < 4:
                r_13_set.add(cell['nums'])
            elif cell['row'] == 14 and len(cell['nums']) < 4:
                r_14_set.add(cell['nums'])
            elif cell['row'] == 15 and len(cell['nums']) < 4:
                r_15_set.add(cell['nums'])
            elif cell['row'] == 16 and len(cell['nums']) < 4:
                r_16_set.add(cell['nums'])
    print("409 r_X_set are ", r_1_set, r_2_set, r_3_set, r_4_set, r_5_set, r_6_set, r_7_set, r_8_set,
          r_9_set, r_10_set, r_11_set, r_12_set, r_13_set, r_14_set, r_15_set, r_16_set)

def CheckForOnlyOneNumber():
    print("296 Entered CheckForOnlyOneNumber")
    global r_1_nums
    global r_2_nums
    global r_3_nums
    global r_4_nums
    global r_5_nums
    global r_6_nums
    global r_7_nums
    global r_8_nums
    global r_9_nums
    global r_10_nums
    global r_11_nums
    global r_12_nums
    global r_13_nums
    global r_14_nums
    global r_15_nums
    global r_16_nums
    global c_1_nums
    global c_2_nums
    global c_3_nums
    global c_4_nums
    global c_5_nums
    global c_6_nums
    global c_7_nums
    global c_8_nums
    global c_9_nums
    global c_10_nums
    global c_11_nums
    global c_12_nums
    global c_13_nums
    global c_14_nums
    global c_15_nums
    global c_16_nums
    global s_1_nums
    global s_2_nums
    global s_3_nums
    global s_4_nums
    global s_5_nums
    global s_6_nums
    global s_7_nums
    global s_8_nums
    global s_9_nums
    global s_10_nums
    global s_11_nums
    global s_12_nums
    global s_13_nums
    global s_14_nums
    global s_15_nums
    global s_16_nums
    r_1_nums = ""
    r_2_nums = ""
    r_3_nums = ""
    r_4_nums = ""
    r_5_nums = ""
    r_6_nums = ""
    r_7_nums = ""
    r_8_nums = ""
    r_9_nums = ""
    r_10_nums = ""
    r_11_nums = ""
    r_12_nums = ""
    r_13_nums = ""
    r_14_nums = ""
    r_15_nums = ""
    r_16_nums = ""
    c_1_nums = ""
    c_2_nums = ""
    c_3_nums = ""
    c_4_nums = ""
    c_5_nums = ""
    c_6_nums = ""
    c_7_nums = ""
    c_8_nums = ""
    c_9_nums = ""
    c_10_nums = ""
    c_11_nums = ""
    c_12_nums = ""
    c_13_nums = ""
    c_14_nums = ""
    c_15_nums = ""
    c_16_nums = ""
    s_1_nums = ""
    s_2_nums = ""
    s_3_nums = ""
    s_4_nums = ""
    s_5_nums = ""
    s_6_nums = ""
    s_7_nums = ""
    s_8_nums = ""
    s_9_nums = ""
    s_10_nums = ""
    s_11_nums = ""
    s_12_nums = ""
    s_13_nums = ""
    s_14_nums = ""
    s_15_nums = ""
    s_16_nums = ""
    ex_text = "Empty start\n"
    print("396 len(not_done_arefs) is ", len(not_done_arefs))

    for cell in not_done_arefs:
        current_button = cell['btn']
        print(current_button)
        # print("400 btn is ", eval(cell['btn']))
        if cell['row'] == 1:
            r_1_nums += cell['nums']
        elif cell['row'] == 2:
            r_2_nums += cell['nums']
        elif cell['row'] == 3:
            r_3_nums += cell['nums']
        elif cell['row'] == 4:
            r_4_nums += cell['nums']
        elif cell['row'] == 5:
            r_5_nums += cell['nums']
        elif cell['row'] == 6:
            r_6_nums += cell['nums']
        elif cell['row'] == 7:
            r_7_nums += cell['nums']
        elif cell['row'] == 8:
            r_8_nums += cell['nums']
        elif cell['row'] == 9:
            r_9_nums += cell['nums']
        elif cell['row'] == 10:
            r_10_nums += cell['nums']
        elif cell['row'] == 11:
            r_11_nums += cell['nums']
        elif cell['row'] == 12:
            r_12_nums += cell['nums']
        elif cell['row'] == 13:
            r_13_nums += cell['nums']
        elif cell['row'] == 14:
            r_14_nums += cell['nums']
        elif cell['row'] == 15:
            r_15_nums += cell['nums']
        elif cell['row'] == 16:
            r_16_nums += cell['nums']
        if cell['col'] == 1:
            c_1_nums += cell['nums']
        elif cell['col'] == 2:
            c_2_nums += cell['nums']
        elif cell['col'] == 3:
            c_3_nums += cell['nums']
        elif cell['col'] == 4:
            c_4_nums += cell['nums']
        elif cell['col'] == 5:
            c_5_nums += cell['nums']
        elif cell['col'] == 6:
            c_6_nums += cell['nums']
        elif cell['col'] == 7:
            c_7_nums += cell['nums']
        elif cell['col'] == 8:
            c_8_nums += cell['nums']
        elif cell['col'] == 9:
            c_9_nums += cell['nums']
        elif cell['col'] == 10:
            c_10_nums += cell['nums']
        elif cell['col'] == 11:
            c_11_nums += cell['nums']
        elif cell['col'] == 12:
            c_12_nums += cell['nums']
        elif cell['col'] == 13:
            c_13_nums += cell['nums']
        elif cell['col'] == 14:
            c_14_nums += cell['nums']
        elif cell['col'] == 15:
            c_15_nums += cell['nums']
        elif cell['col'] == 16:
            c_16_nums += cell['nums']
        if cell['sq'] == 1:
            s_1_nums += cell['nums']
        elif cell['sq'] == 2:
            s_2_nums += cell['nums']
        elif cell['sq'] == 3:
            s_3_nums += cell['nums']
        elif cell['sq'] == 4:
            s_4_nums += cell['nums']
        elif cell['sq'] == 5:
            s_5_nums += cell['nums']
        elif cell['sq'] == 6:
            s_6_nums += cell['nums']
        elif cell['sq'] == 7:
            s_7_nums += cell['nums']
        elif cell['sq'] == 8:
            s_8_nums += cell['nums']
        elif cell['sq'] == 9:
            s_9_nums += cell['nums']
        elif cell['sq'] == 10:
            s_10_nums += cell['nums']
        elif cell['sq'] == 11:
            s_11_nums += cell['nums']
        elif cell['sq'] == 12:
            s_12_nums += cell['nums']
        elif cell['sq'] == 13:
            s_13_nums += cell['nums']
        elif cell['sq'] == 14:
            s_14_nums += cell['nums']
        elif cell['sq'] == 15:
            s_15_nums += cell['nums']
        elif cell['sq'] == 16:
            s_16_nums += cell['nums']
    # print("495 row_1_nums are ", r_1_nums)
    # print("497 btn is ", cell['btn'])
    temp_list = []
    for row in row_nums_list:
        row_nums = eval(row)
        for char in startingString:
            if char in row_nums:
                if row_nums.count(char) == 1:
                    row_num = row.strip('r_')
                    row_num = row_num.strip('_nums')
                    temp_list = [row_num, char]
                    delete_singles_row_list.append(temp_list)
                    # deletedelete_singles_row_list_singles_list.append(list(row_num))
                    ex_text = char + " only occurs once in row " + row_num + "\n"
                    txt_Explain.insert(END, ex_text)
                    if bSolve_singles == True:
                        print("514 bSolve_singles == True")
                        currentNumber = char
                        btn = cell['btn']
                        # aref = btn_dict[btn]
                        update_cell(btn, cell)

    for col in col_nums_list:
        col_nums = eval(col)
        # print("761 row_nums are ", row_nums)
        for char in startingString:
            # print("763 char is ", char)
            if char in col_nums:
                if col_nums.count(char) == 1:
                    col_num = col.strip('c_')
                    col_num = col_num.strip('_nums')
                    temp_list = [col_num, char]
                    delete_singles_col_list.append(temp_list)
                    ex_text = char + " only occurs once in col " + col_num + "\n"
                    txt_Explain.insert(END, ex_text)
                    if bSolve_singles == True:
                        # print("514 bSolve_singles == True")
                        currentNumber = char
                        btn = cell['btn']
                        # aref = btn_dict[btn]
                        update_cell(btn, cell)
    for sq in sq_nums_list:
        sq_nums = eval(sq)
        # print("749 row_nums are ", row_nums)
        for char in startingString:
            # print("751 char is ", char)
            if char in sq_nums:
                if sq_nums.count(char) == 1:
                    sq_num = sq.strip('r_')
                    sq_num = sq_num.strip('_nums')
                    temp_list = [sq_num, char]
                    delete_singles_sq_list.append(temp_list)
                    ex_text = char + " only occurs once in square " + sq_num + "\n"
                    txt_Explain.insert(END, ex_text)
                    if bSolve_singles == True:
                        # print("514 bSolve_singles == True")
                        currentNumber = char
                        btn = cell['btn']
                        # aref = btn_dict[btn]
                        update_cell(btn, cell)
    cells_done()
    cells_remaining()
    print("550 delete_singles_row_list is ", delete_singles_row_list)

def solve_row_singles():
    print("564 Entering solve_singles")
    # global bSolve_singles
    bSolve_singles = True
    # print("567 bSolve_singles == ", bSolve_singles)
    # CheckForOnlyOneNumber()

    for cell in not_done_arefs:
        # print("559 cell is ", cell)
        # current_button = cell['btn']
        nums = cell['nums']
        row = cell['row']
        col = cell['col']
        sq = cell['sq']
        for item in delete_singles_row_list:
            # print("578 row item ", row, type(row), item[0], type(int(item[0])), item[1])
            if row == int(item[0]) and item[1] in nums:
                # print("580 item ", row, type(row), item[0], type(int(item[0])), item[1])
                currentNumber = item[1]
                current_button = cell['btn']
                # print("572 cell and type are ", type(current_button), current_button, type(cell), cell)
                # reset_cell_values(current_button, cell) # function doesn't work, but lines work
                cell['done'] = True
                cell['nums'] = currentNumber
                cell['font'] = donefont
                cell['width'] = wid6
                cell['height'] = 4
                cell['fg'] = "red"
                current_button['width'] = cell['width']
                current_button['width'] = cell['width']
                current_button['text'] = cell['nums']
                current_button['fg'] = cell['fg']
                # print("583 cell and type are ", type(cell), cell)
                remove_aref_from_not_done_arefs(cell)
                # update_puzzle(cell['row'], cell['col'], cell['sq'])
                for aref in not_done_arefs:
                    current_button = aref['btn']
                    if row == aref['row'] and col == aref['col'] and sq == aref['sq']:
                        aref['font'] = donefont
                        if aref in not_done_arefs and aref['done'] == True:
                            not_done_arefs.remove(aref)
                            continue
                    elif row == aref['row'] or col == aref['col'] or sq == aref['sq']:
                        if currentNumber in aref['nums']:
                            new_nums = aref['nums'].replace(currentNumber, "")
                            aref['nums'] = new_nums
                            current_button['text'] = aref['nums']

    for cell in not_done_arefs:
        # print("619 cell is ", cell)
        # current_button = cell['btn']
        nums = cell['nums']
        row = cell['row']
        col = cell['col']
        sq = cell['sq']
        for item in delete_singles_col_list:
            # print("619 col item ", col, type(col), item[0], type(int(item[0])), item[1])
            if col == int(item[0]) and item[1] in nums:
                print("521 col item ", col, type(row), item[0], type(int(item[0])), item[1])
                currentNumber = item[1]
                current_button = cell['btn']
                print("572 cell and type are ", type(current_button), current_button, type(cell), cell)
                # reset_cell_values(current_button, cell) # function doesn't work, but lines work
                cell['done'] = True
                cell['nums'] = currentNumber
                cell['font'] = donefont
                cell['width'] = wid6
                cell['height'] = 4
                cell['fg'] = "red"
                current_button['width'] = cell['width']
                current_button['width'] = cell['width']
                current_button['text'] = cell['nums']
                current_button['fg'] = cell['fg']
                # print("583 cell and type are ", type(cell), cell)
                remove_aref_from_not_done_arefs(cell)
                # update_puzzle(cell['row'], cell['col'], cell['sq'])
                for aref in not_done_arefs:
                    current_button = aref['btn']
                    if row == aref['row'] and col == aref['col'] and sq == aref['sq']:
                        aref['font'] = donefont
                        if aref in not_done_arefs and aref['done'] == True:
                            not_done_arefs.remove(aref)
                            continue
                    elif row == aref['row'] or col == aref['col'] or sq == aref['sq']:
                        if currentNumber in aref['nums']:
                            new_nums = aref['nums'].replace(currentNumber, "")
                            aref['nums'] = new_nums
                            current_button['text'] = aref['nums']
    for cell in not_done_arefs:
        # print("652 cell is ", cell)
        # current_button = cell['btn']
        nums = cell['nums']
        row = cell['row']
        col = cell['col']
        sq = cell['sq']
        for item in delete_singles_sq_list:
            # print("659 sq item ", sq, type(sq), item[0], type(int(item[0])), item[1])
            if sq == int(item[0]) and item[1] in nums:
                # print("568 item ", col, type(row), item[0], type(int(item[0])), item[1])
                currentNumber = item[1]
                current_button = cell['btn']
                # print("572 cell and type are ", type(current_button), current_button, type(cell), cell)
                # reset_cell_values(current_button, cell) # function doesn't work, but lines work
                cell['done'] = True
                cell['nums'] = currentNumber
                cell['font'] = donefont
                cell['width'] = wid6
                cell['height'] = 4
                cell['fg'] = "red"
                current_button['width'] = cell['width']
                current_button['width'] = cell['width']
                current_button['text'] = cell['nums']
                current_button['fg'] = cell['fg']
                # print("583 cell and type are ", type(cell), cell)
                remove_aref_from_not_done_arefs(cell)
                # update_puzzle(cell['row'], cell['col'], cell['sq'])
                for aref in not_done_arefs:
                    current_button = aref['btn']
                    if row == aref['row'] and col == aref['col'] and sq == aref['sq']:
                        aref['font'] = donefont
                        if aref in not_done_arefs and aref['done'] == True:
                            not_done_arefs.remove(aref)
                            continue
                    elif row == aref['row'] or col == aref['col'] or sq == aref['sq']:
                        if currentNumber in aref['nums']:
                            new_nums = aref['nums'].replace(currentNumber, "")
                            aref['nums'] = new_nums
                            current_button['text'] = aref['nums']


def find_Duple():
    print("525 Entering find_Duple")
    # print("343 len(not_done_arefs) is ", len(not_done_arefs))
    ex_text = ""
    temp_list = []
    temp_list_1 = []
    duple_list = []
    for cell in not_done_arefs:
        if len(cell['nums']) == 2:
            print("530 potential duple ", cell, cell['nums'])
            ex_text = str(cell['row']) + ", " + str(cell['col']) + ", " + str(cell['sq']) + ", " + str(cell['nums']) + "\n "
            row = cell['row']
            col = cell['col']
            sq = cell['sq']
            nums = cell['nums']
            temp_list.append(row)
            temp_list.append(col)
            temp_list.append(sq)
            temp_list.append(nums)
            txt_Explain.insert(END, ex_text)
            duple_list.append(list(temp_list))
            temp_list = []
            # *** The duple_list now has a list of all the lists of duple row, col, sq, and nums
    # print("706 potential duple ", duple_list) #str(cell['row']), , cell['nums']
    # ex_text = ""
    for item in duple_list:
        if item:
        # print("716 item nums are ", item[0], item[1], item[2], item[3])
            i_row = int(item[0])
            i_col = int(item[1])
            i_sq = int(item[2])
            i_pair = item[3]
        try:
            for item in duple_list:
                # if item[0] and item[1] and item[2] and item[3]:
                c_row = int(item[0])
                c_col = int(item[1])
                c_sq = int(item[2])
                c_pair = item[3]
                if i_pair == c_pair and i_row == c_row and i_col == c_col and i_sq == c_sq:
                    pass
                # print("727 pairs are the same.")
                elif i_pair == c_pair and (i_row == c_row or i_col == c_col or i_sq == c_sq):
                    ex_text = f"{i_row}, {i_col}, {i_sq}, {i_pair}, {c_row}, {c_col}, {c_sq}, {c_pair}"
                    print("741 pairs are ", i_row, i_col, i_sq, i_pair, c_row, c_col, c_sq, c_pair, c_pair[0], c_pair[1])
                    # duple_first = {i_row}, {i_col}, {i_sq}, {i_pair}
                    duple_first = f"{i_row}, {i_col}, {i_sq}, {i_pair}"
                    duple_first = duple_first.split(',')
                    duple_second = f"{c_row}, {c_col}, {c_sq}, {c_pair}"
                    duple_second = duple_second.split(',')
                    print("747 duple_first is ", duple_first, duple_second)
                    print("748 duple_list is ", duple_first[0], duple_first[1])
                    # txt_Explain.delete(0, END)
                    txt_Explain.insert(END, ex_text)
                    txt_Explain.insert(END, "\n")
                    # duple_list_1 = duple_first.split(',')
                    print("755 duple_list is ", duple_first, duple_first[0], duple_first[1])
                    # duple_list_2 = duple_second.split(',')
                    duple_list = [duple_first, duple_second]
                    print("754 duple_list is ", duple_list)
                    if duple_list != []:
                        process_duple_list(duple_first, duple_second)

        except Exception as e:
            pass
            # print(e)

        # start with item 1 duple e.g. item[3]
        # if item item[3] == item[3] in any item in the rest of the list,
        # it is a potential duple, so check to see if it is in the same RCS

def process_duple_list(duple_first, duple_second):
    global not_done_arefs
    global currentNumber
    # print("772 duple list is ", duple_first)
    # print("773 duple list is ", duple_first[0], duple_first[1], duple_first[2], duple_first[3])
    first_row = int(duple_first[0])
    first_col = int(duple_first[1])
    first_sq = int(duple_first[2])
    first_nums = duple_first[3]
    first_chr_1 = first_nums[1]
    second_chr_1 = first_nums[2]
    second_row = int(duple_second[0])
    second_col = int(duple_second[1])
    second_sq = int(duple_second[2])
    duple_row = 0
    duple_col = 0
    duple_sq = 0
    if first_row == second_row:
        duple_row = first_row
        # print("791 duple row is ", first_row, second_row, duple_row)
    if first_col == second_col:
        duple_col = first_col
        # print("794 duple col is ", first_col, second_col, duple_col)
    if first_sq == second_sq:
        duple_sq = first_sq
        # print("797 duple sq is ", first_sq, second_sq, duple_sq) #first_row, first_col, first_sq,
    # print("798 first duple is ", type(first_nums), first_nums, first_chr_1, second_chr_1)
    # if the rows, or col, or sq are the same,
    # delete each number from the other cells in the row
    for aref in not_done_arefs:
        current_btn = aref['btn']
        a_row = aref['row']
        a_col = aref['col']
        a_sq = aref['sq']
        a_nums = aref['nums']
        # print("812 first cell is ", a_row, a_col, a_sq, a_nums)
        # aref = eval(btn_dict[current_btn])
        if (a_row == first_row and a_col == first_col and a_sq == first_sq) or \
                (a_row == second_row and a_col == second_col and a_sq == second_sq):
            pass
        elif duple_row != 0 and first_row == a_row:
            print("818 partial match in aref", duple_row, duple_col, duple_sq, first_row, a_row, first_chr_1, a_nums)
            if first_chr_1 in a_nums:
                new_nums = aref['nums'].replace(first_chr_1, "")
                # print("723 new_nums ", new_nums)
                aref['nums'] = new_nums
                current_btn['text'] = aref['nums']
            if second_chr_1 in a_nums:
                new_nums = aref['nums'].replace(second_chr_1, "")
                print("723 new_nums ", new_nums)
                aref['nums'] = new_nums
                current_btn['text'] = aref['nums']
        elif duple_col != 0 and first_col == a_col:
            print("823 partial match in aref", duple_row, duple_col, duple_sq, first_row, a_row, first_chr_1, a_nums)
            if first_chr_1 in a_nums:
                new_nums = aref['nums'].replace(first_chr_1, "")
                print("723 new_nums ", new_nums)
                aref['nums'] = new_nums
                current_btn['text'] = aref['nums']
            if second_chr_1 in a_nums:
                new_nums = aref['nums'].replace(second_chr_1, "")
                print("723 new_nums ", new_nums)
                aref['nums'] = new_nums
                current_btn['text'] = aref['nums']
        elif duple_sq != 0 and first_sq == a_sq:
            print("828 partial match in aref", duple_row, duple_col, duple_sq, first_row, a_row, first_chr_1, a_nums)
            if first_chr_1 in a_nums:
                new_nums = aref['nums'].replace(first_chr_1, "")
                print("723 new_nums ", new_nums)
                aref['nums'] = new_nums
                current_btn['text'] = aref['nums']
            if second_chr_1 in a_nums:
                new_nums = aref['nums'].replace(second_chr_1, "")
                print("723 new_nums ", new_nums)
                aref['nums'] = new_nums
                current_btn['text'] = aref['nums']

def find_Triple():
    print("953 Entering find_Triple")
    # number passed is the length sought plus 1
    make_RCS_sets(4)

def find_Quad():
    print("525 Entering find_Quad")

def update_RCS(current_button, aref): #Row, Column, Square):
    current_button['text'] = aref['nums']
    # current_btn['text'] = aref['nums']

# def update_not_done_arefs(aref):
#     print("542 Entered update_not_done_arefs(aref)", aref['done'])
#     if aref['done'] == True and aref in not_done_arefs:
#         not_done_arefs.remove(aref)
#     print("545 update_not_done_arefs ", len(not_done_arefs))

def update_puzzle(row, column, square):
    # print("529 update_puzzle row, column, square ", row, column, square, currentNumber)
    for aref in not_done_arefs:
        current_button = aref['btn']
        # aref = eval(btn_dict[current_button])
        if row == aref['row'] and column == aref['col'] and square == aref['sq']:
            aref['font'] = donefont
            if aref in not_done_arefs:
                aref['done'] == True

                print("550 In update_puzzle if aref['done']")
                not_done_arefs.remove(aref)
                print("557 len(not_done_arefs)", len(not_done_arefs))
                continue
            #     print("532 row, column and square are same. ", row, column, square)
        elif row == aref['row'] or column == aref['col'] or square == aref['sq']:
            # print("562 row, column or square are same. ", row, column, square, aref['nums'])
            if currentNumber in aref['nums']:
                # print("564 row, column and square are same. ", row, column, square, aref['nums'])
                # current_button = cell['btn']
                # aref = eval(btn_dict[current_button])
                # current_button = eval(current_button)
                # print("525", current_button, type(current_button), aref)
                new_nums = aref['nums'].replace(currentNumber, "")
                # print("655 current_button and new_nums ", current_button, new_nums)
                aref['nums'] = new_nums
                current_button['text'] = aref['nums']
                # print("658 ", current_button, aref['nums'], aref['done'])
                # if aref['done'] == True:
                #     not_done_arefs.remove(aref)
                # print("569 len(not_done_arefs) ", len(not_done_arefs))


def reset_cell_values(current_btn, aref):
    print("710 Entered reset_cell_values", type(current_btn), current_btn, type(aref), aref)
    '''A single number has been selected, so reset the cell values.'''
    aref['done'] = True
    aref['nums'] = currentNumber
    aref['font'] = donefont
    aref['width'] = wid6
    aref['height'] = 4
    aref['fg'] = "red"
    current_btn['width'] = aref['width']
    current_btn['width'] = aref['width']
    current_btn['text'] = aref['nums']
    current_btn['fg'] = aref['fg']
    # print("722 aref values", aref['done'], aref['nums'], aref)
    # print("723 Entered reset_cell_values", current_btn, aref)
    # current_btn['font'] = aref['font']
    # current_btn['height'] = aref['height']
    # aref['height'] = 2


def refresh_display(current_btn, aref):
    print("565 Entered refresh_display", current_btn, aref)
    aref['nums'] = currentNumber
    current_btn['text'] = aref['nums']
    # arrRef0['nums'] = currentNumber
    # arrRef0['font'] = buttonfont
    # arrRef0['fg'] = "red"

def set_bRemoveANumberFromACell():
    global bRemoveANumberFromACell
    if bRemoveANumberFromACell == "False":
        bRemoveANumberFromACell = "True"
        btn_del_num['text'] = "Del\nnum\nact\nive"

    else:
        bRemoveANumberFromACell = "False"
        btn_del_num['text'] = 'Del\nnum\nfrom\ncell'
    print("695 bRemoveANumberFromACell is ", bRemoveANumberFromACell)

def remove_num_from_cell(current_btn, aref):
    print("701 Entered remove_num_from_cell.")
    global currentNumber
    new_nums = aref['nums'].replace(currentNumber, "")
    print("723 new_nums ", new_nums)
    aref['nums'] = new_nums
    current_btn['text'] = aref['nums']

def remove_aref_from_not_done_arefs(aref):
    print("709 Entered remove_aref_from_not_done_arefs.")
    if aref in not_done_arefs:
        not_done_arefs.remove(aref)

# def update_cell(btn, aref, row, col, sq):
def update_cell(btn, aref):
    print("705 Entered update_cell.", type(btn), btn, type(aref), aref)
    # print("705 Entered update_cell.", btn, aref)
    # arrRef0 = dict(btn='btn_R1C1', row=1, col=1, sq=1,
    global bRemoveANumberFromACell
    # btn1 = aref["btn"]
    # print("720 ", btn1, type(btn1))
    row = aref["row"]
    col = aref["col"]
    sq = aref["sq"]
    # print("724 ", btn, row, col, sq)
    # reset_cell_values(current_btn, aref)
    if bRemoveANumberFromACell == "False":
        # print("707 Entered bRemoveANumberFromACell.")
        reset_cell_values(btn, aref)
        remove_aref_from_not_done_arefs(aref)
        update_puzzle(row, col, sq)
        # print(f"currentNumber = '{currentNumber}'")
        # print(f"update_cell'{btn}, {aref}")
    elif bRemoveANumberFromACell == "True":
        # print("712 Entered bRemoveANumberFromACell.")
        remove_num_from_cell(btn, aref)
        set_bRemoveANumberFromACell()
        # print(f"currentNumber = '{currentNumber}'")
        # print(f"update_cell'{btn}, {aref}")

def update_R1C1():
    print("691 R1C1 button pressed.")
    ''' A number has been set by a number button, 
        either set that number as the value of the cell in aref['nums'],
        or, if bRemoveANumberFromACell == True, 
        remove the number from the current numbers.'''
    update_cell(btn_R1C1, arrRef0)
    # update_cell(btn_R1C1, arrRef0, 1, 1, 1)

def update_R1C2():
    print("R1C2 button pressed.")
    update_cell(btn_R1C2, arrRef1)

def update_R1C3():
    print("R1C3 button pressed.")
    update_cell(btn_R1C3, arrRef2)

def update_R1C4():
    print("R1C4 button pressed.")
    update_cell(btn_R1C4, arrRef3)

def update_R1C5():
    print("R1C5 button pressed.")
    update_cell(btn_R1C5, arrRef4)

def update_R1C6():
    print("R1C6 button pressed.")
    update_cell(btn_R1C6, arrRef5)

def update_R1C7():
    print("R1C7 button pressed.")
    update_cell(btn_R1C7, arrRef6)

def update_R1C8():
    print("R1C8 button pressed.")
    update_cell(btn_R1C8, arrRef7)

def update_R1C9():
    print("R1C9 button pressed.")
    update_cell(btn_R1C9, arrRef8)

def update_R1C10():
    print("R1C10 button pressed.")
    update_cell(btn_R1C10, arrRef9)

def update_R1C11():
    print("R1C11 button pressed.")
    update_cell(btn_R1C11, arrRef10)

def update_R1C12():
    print("R1C12 button pressed.")
    update_cell(btn_R1C12, arrRef11)

def update_R1C13():
    print("R1C13 button pressed.")
    update_cell(btn_R1C13, arrRef12)

def update_R1C14():
    print("R1C14 button pressed.")
    update_cell(btn_R1C14, arrRef13)

def update_R1C15():
    print("R1C15 button pressed.")
    update_cell(btn_R1C15, arrRef14)

def update_R1C16():
    print("R2C16 button pressed.")
    update_cell(btn_R1C16, arrRef15)

def update_R2C1():
    print("R2C1 button pressed.")
    update_cell(btn_R2C1, arrRef16)

def update_R2C2():
    print("R2C2 button pressed.")
    update_cell(btn_R2C2, arrRef17)

def update_R2C3():
    print("R2C3 button pressed.")
    update_cell(btn_R2C3, arrRef18)

def update_R2C4():
    print("R2C4 button pressed.")
    update_cell(btn_R2C4, arrRef19)

def update_R2C5():
    print("R2C5 button pressed.")
    update_cell(btn_R2C5, arrRef20)

def update_R2C6():
    print("R2C6 button pressed.")
    update_cell(btn_R2C6, arrRef21)

def update_R2C7():
    print("R2C7 button pressed.")
    update_cell(btn_R2C7, arrRef22)

def update_R2C8():
    print("R2C8 button pressed.")
    update_cell(btn_R2C8, arrRef23)

def update_R2C9():
    print("R2C9 button pressed.")
    update_cell(btn_R2C9, arrRef24)

def update_R2C10():
    print("R2C10 button pressed.")
    update_cell(btn_R2C10, arrRef25)

def update_R2C11():
    print("R2C11 button pressed.")
    update_cell(btn_R2C11, arrRef26)

def update_R2C12():
    print("R2C12 button pressed.")
    update_cell(btn_R2C12, arrRef27)

def update_R2C13():
    print("R2C13 button pressed.")
    update_cell(btn_R2C13, arrRef28)

def update_R2C14():
    print("R2C14 button pressed.")
    update_cell(btn_R2C14, arrRef29)

def update_R2C15():
    print("R2C15 button pressed.")
    update_cell(btn_R2C15, arrRef30)

def update_R2C16():
    print("R2C16 button pressed.")
    update_cell(btn_R2C16, arrRef31)

def update_R3C1():
    print("R3C1 button pressed.")
    update_cell(btn_R3C1, arrRef32)

def update_R3C2():
    print("R3C2 button pressed.")
    update_cell(btn_R3C2, arrRef33)

def update_R3C3():
    print("R3C3 button pressed.")
    update_cell(btn_R3C3, arrRef34)

def update_R3C4():
    print("R3C4 button pressed.")
    update_cell(btn_R3C4, arrRef35)

def update_R3C5():
    print("R3C5 button pressed.")
    update_cell(btn_R3C5, arrRef36)

def update_R3C6():
    print("R3C6 button pressed.")
    update_cell(btn_R3C6, arrRef37)

def update_R3C7():
    print("R3C7 button pressed.")
    update_cell(btn_R3C7, arrRef38)

def update_R3C8():
    print("R3C8 button pressed.")
    update_cell(btn_R3C8, arrRef39)

def update_R3C9():
    print("R3C9 button pressed.")
    update_cell(btn_R3C9, arrRef40)

def update_R3C10():
    print("R3C10 button pressed.")
    update_cell(btn_R3C10, arrRef41)

def update_R3C11():
    print("R3C11 button pressed.")
    update_cell(btn_R3C11, arrRef42)

def update_R3C12():
    print("R3C12 button pressed.")
    update_cell(btn_R3C12, arrRef43)

def update_R3C13():
    print("R3C13 button pressed.")
    update_cell(btn_R3C13, arrRef44)

def update_R3C14():
    print("R3C14 button pressed.")
    update_cell(btn_R3C14, arrRef45)

def update_R3C15():
    print("R3C15 button pressed.")
    update_cell(btn_R3C15, arrRef46)

def update_R3C16():
    print("R3C16 button pressed.")
    update_cell(btn_R3C16, arrRef47)

def update_R4C1():
    print("R4C1 button pressed.")
    update_cell(btn_R4C1, arrRef48)

def update_R4C2():
    print("R4C2 button pressed.")
    update_cell(btn_R4C2, arrRef49)

def update_R4C3():
    print("R4C3 button pressed.")
    update_cell(btn_R4C3, arrRef50)

def update_R4C4():
    print("R4C4 button pressed.")
    update_cell(btn_R4C4, arrRef51)

def update_R4C5():
    print("R4C5 button pressed.")
    update_cell(btn_R4C5, arrRef52)

def update_R4C6():
    print("R4C6 button pressed.")
    update_cell(btn_R4C6, arrRef53)

def update_R4C7():
    print("R4C7 button pressed.")
    update_cell(btn_R4C7, arrRef54)

def update_R4C8():
    print("R4C8 button pressed.")
    update_cell(btn_R4C8, arrRef55)

def update_R4C9():
    print("R4C9 button pressed.")
    update_cell(btn_R4C9, arrRef56)

def update_R4C10():
    print("R4C10 button pressed.")
    update_cell(btn_R4C10, arrRef57)

def update_R4C11():
    print("R4C11 button pressed.")
    update_cell(btn_R4C11, arrRef58)

def update_R4C12():
    print("R4C12 button pressed.")
    update_cell(btn_R4C12, arrRef59)

def update_R4C13():
    print("R4C13 button pressed.")
    update_cell(btn_R4C13, arrRef60)

def update_R4C14():
    print("R4C14 button pressed.")
    update_cell(btn_R4C14, arrRef61)

def update_R4C15():
    print("R4C15 button pressed.")
    update_cell(btn_R4C15, arrRef62)

def update_R4C16():
    print("R4C16 button pressed.")
    update_cell(btn_R4C16, arrRef63)

def update_R5C1():
    print("R5C1 button pressed.")
    update_cell(btn_R5C1, arrRef64)

def update_R5C2():
    print("R5C2 button pressed.")
    update_cell(btn_R5C2, arrRef65)

def update_R5C3():
    print("R5C3 button pressed.")
    update_cell(btn_R5C3, arrRef66)

def update_R5C4():
    print("R5C4 button pressed.")
    update_cell(btn_R5C4, arrRef67)

def update_R5C5():
    print("R5C5 button pressed.")
    update_cell(btn_R5C5, arrRef68)

def update_R5C6():
    print("R5C6 button pressed.")
    update_cell(btn_R5C6, arrRef69)

def update_R5C7():
    print("R5C7 button pressed.")
    update_cell(btn_R5C7, arrRef70)

def update_R5C8():
    print("R5C8 button pressed.")
    update_cell(btn_R5C8, arrRef71)

def update_R5C9():
    print("R5C9 button pressed.")
    update_cell(btn_R5C9, arrRef72)

def update_R5C10():
    print("R5C10 button pressed.")
    update_cell(btn_R5C10, arrRef73)

def update_R5C11():
    print("R5C11 button pressed.")
    update_cell(btn_R5C11, arrRef74)

def update_R5C12():
    print("R5C12 button pressed.")
    update_cell(btn_R5C12, arrRef75)

def update_R5C13():
    print("R5C13 button pressed.")
    update_cell(btn_R5C13, arrRef76)

def update_R5C14():
    print("R5C14 button pressed.")
    update_cell(btn_R5C14, arrRef77)

def update_R5C15():
    print("R5C15 button pressed.")
    update_cell(btn_R5C15, arrRef78)

def update_R5C16():
    print("R5C16 button pressed.")
    update_cell(btn_R5C16, arrRef79)

def update_R6C1():
    print("R6C1 button pressed.")
    update_cell(btn_R6C1, arrRef80)

def update_R6C2():
    print("R6C2 button pressed.")
    update_cell(btn_R6C2, arrRef81)

def update_R6C3():
    print("R6C3 button pressed.")
    update_cell(btn_R6C3, arrRef82)

def update_R6C4():
    print("R6C4 button pressed.")
    update_cell(btn_R6C4, arrRef83)

def update_R6C5():
    print("R6C5 button pressed.")
    update_cell(btn_R6C5, arrRef84)

def update_R6C6():
    print("R6C6 button pressed.")
    update_cell(btn_R6C6, arrRef85)

def update_R6C7():
    print("R6C7 button pressed.")
    update_cell(btn_R6C7, arrRef86)

def update_R6C8():
    print("R6C8 button pressed.")
    update_cell(btn_R6C8, arrRef87)

def update_R6C9():
    print("R6C9 button pressed.")
    update_cell(btn_R6C9, arrRef88)

def update_R6C10():
    print("R6C10 button pressed.")
    update_cell(btn_R6C10, arrRef89)

def update_R6C11():
    print("R6C11 button pressed.")
    update_cell(btn_R6C11, arrRef90)

def update_R6C12():
    print("R6C12 button pressed.")
    update_cell(btn_R6C12, arrRef91)

def update_R6C13():
    print("R6C13 button pressed.")
    update_cell(btn_R6C13, arrRef92)

def update_R6C14():
    print("R6C14 button pressed.")
    update_cell(btn_R6C14, arrRef93)

def update_R6C15():
    print("R6C15 button pressed.")
    update_cell(btn_R6C15, arrRef94)

def update_R6C16():
    print("R6C16 button pressed.")
    update_cell(btn_R6C16, arrRef95)

def update_R7C1():
    print("R7C1 button pressed.")
    update_cell(btn_R7C1, arrRef96)

def update_R7C2():
    print("R7C2 button pressed.")
    update_cell(btn_R7C2, arrRef97)

def update_R7C3():
    print("R7C3 button pressed.")
    update_cell(btn_R7C3, arrRef98)

def update_R7C4():
    print("R7C4 button pressed.")
    update_cell(btn_R7C4, arrRef99)

def update_R7C5():
    print("R7C5 button pressed.")
    update_cell(btn_R7C5, arrRef100)

def update_R7C6():
    print("R7C6 button pressed.")
    update_cell(btn_R7C6, arrRef101)

def update_R7C7():
    print("R7C7 button pressed.")
    update_cell(btn_R7C7, arrRef102)

def update_R7C8():
    print("R7C8 button pressed.")
    update_cell(btn_R7C8, arrRef103)

def update_R7C9():
    print("R7C9 button pressed.")
    update_cell(btn_R7C9, arrRef104)

def update_R7C10():
    print("R7C10 button pressed.")
    update_cell(btn_R7C10, arrRef105)

def update_R7C11():
    print("R7C11 button pressed.")
    update_cell(btn_R7C11, arrRef106)

def update_R7C12():
    print("R7C12 button pressed.")
    update_cell(btn_R7C12, arrRef107)

def update_R7C13():
    print("R7C13 button pressed.")
    update_cell(btn_R7C13, arrRef108)

def update_R7C14():
    print("R7C14 button pressed.")
    update_cell(btn_R7C14, arrRef109)

def update_R7C15():
    print("R7C15 button pressed.")
    update_cell(btn_R7C15, arrRef110)

def update_R7C16():
    print("R7C16 button pressed.")
    update_cell(btn_R7C16, arrRef111)

def update_R8C1():
    print("R8C1 button pressed.")
    update_cell(btn_R8C1, arrRef112)

def update_R8C2():
    print("R8C2 button pressed.")
    update_cell(btn_R8C2, arrRef113)

def update_R8C3():
    print("R8C3 button pressed.")
    update_cell(btn_R8C3, arrRef114)

def update_R8C4():
    print("R8C4 button pressed.")
    update_cell(btn_R8C4, arrRef115)

def update_R8C5():
    print("R8C5 button pressed.")
    update_cell(btn_R8C5, arrRef116)

def update_R8C6():
    print("R8C6 button pressed.")
    update_cell(btn_R8C6, arrRef117)

def update_R8C7():
    print("R8C7 button pressed.")
    update_cell(btn_R8C7, arrRef118)

def update_R8C8():
    print("R8C8 button pressed.")
    update_cell(btn_R8C8, arrRef119)

def update_R8C9():
    print("R8C9 button pressed.")
    update_cell(btn_R8C9, arrRef120)

def update_R8C10():
    print("R8C10 button pressed.")
    update_cell(btn_R8C10, arrRef121)

def update_R8C11():
    print("R8C11 button pressed.")
    update_cell(btn_R8C11, arrRef122)

def update_R8C12():
    print("R8C12 button pressed.")
    update_cell(btn_R8C12, arrRef123)

def update_R8C13():
    print("R7C13 button pressed.")
    update_cell(btn_R8C13, arrRef124)

def update_R8C14():
    print("R8C14 button pressed.")
    update_cell(btn_R8C14, arrRef125)

def update_R8C15():
    print("R8C15 button pressed.")
    update_cell(btn_R8C15, arrRef126)

def update_R8C16():
    print("R8C16 button pressed.")
    update_cell(btn_R8C16, arrRef127)

def update_R9C1():
    print("R9C1 button pressed.")
    update_cell(btn_R9C1, arrRef128)

def update_R9C2():
    print("R9C2 button pressed.")
    update_cell(btn_R9C2, arrRef129)

def update_R9C3():
    print("R9C3 button pressed.")
    update_cell(btn_R9C3, arrRef130)

def update_R9C4():
    print("R9C4 button pressed.")
    update_cell(btn_R9C4, arrRef131)

def update_R9C5():
    print("R9C5 button pressed.")
    update_cell(btn_R9C5, arrRef132)

def update_R9C6():
    print("R9C6 button pressed.")
    update_cell(btn_R9C6, arrRef133)

def update_R9C7():
    print("R9C7 button pressed.")
    update_cell(btn_R9C7, arrRef134)

def update_R9C8():
    print("R9C8 button pressed.")
    update_cell(btn_R9C8, arrRef135)

def update_R9C9():
    print("R9C9 button pressed.")
    update_cell(btn_R9C9, arrRef136)

def update_R9C10():
    print("R9C10 button pressed.")
    update_cell(btn_R9C10, arrRef137)

def update_R9C11():
    print("R9C11 button pressed.")
    update_cell(btn_R9C11, arrRef138)

def update_R9C12():
    print("R9C12 button pressed.")
    update_cell(btn_R9C12, arrRef139)

def update_R9C13():
    print("R9C13 button pressed.")
    update_cell(btn_R9C13, arrRef140)

def update_R9C14():
    print("R9C14 button pressed.")
    update_cell(btn_R9C14, arrRef141)

def update_R9C15():
    print("R9C15 button pressed.")
    update_cell(btn_R9C15, arrRef142)

def update_R9C16():
    print("R7C16 button pressed.")
    update_cell(btn_R9C16, arrRef143)

def update_R10C1():
    print("R10C1 button pressed.")
    update_cell(btn_R10C1, arrRef144)

def update_R10C2():
    print("R10C2 button pressed.")
    update_cell(btn_R10C2, arrRef145)

def update_R10C3():
    print("R10C3 button pressed.")
    update_cell(btn_R10C3, arrRef146)

def update_R10C4():
    print("R10C4 button pressed.")
    update_cell(btn_R10C4, arrRef147)

def update_R10C5():
    print("R10C5 button pressed.")
    update_cell(btn_R10C5, arrRef148)

def update_R10C6():
    print("R10C6 button pressed.")
    update_cell(btn_R10C6, arrRef149)

def update_R10C7():
    print("R10C7 button pressed.")
    update_cell(btn_R10C7, arrRef150)

def update_R10C8():
    print("R10C8 button pressed.")
    update_cell(btn_R10C8, arrRef151)

def update_R10C9():
    print("R10C9 button pressed.")
    update_cell(btn_R10C9, arrRef152)

def update_R10C10():
    print("R10C10 button pressed.")
    update_cell(btn_R10C10, arrRef153)

def update_R10C11():
    print("R10C11 button pressed.")
    update_cell(btn_R10C11, arrRef154)

def update_R10C12():
    print("R10C12 button pressed.")
    update_cell(btn_R10C12, arrRef155)


def update_R10C13():
    print("R10C13 button pressed.")
    update_cell(btn_R10C13, arrRef156)

def update_R10C14():
    print("R10C14 button pressed.")
    update_cell(btn_R10C14, arrRef157)

def update_R10C15():
    print("R10C15 button pressed.")
    update_cell(btn_R10C15, arrRef158)

def update_R10C16():
    print("R10C16 button pressed.")
    update_cell(btn_R10C16, arrRef159)

def update_R11C1():
    print("R11C1 button pressed.")
    update_cell(btn_R11C1, arrRef160)

def update_R11C2():
    print("R11C2 button pressed.")
    update_cell(btn_R11C2, arrRef161)

def update_R11C3():
    print("R11C3 button pressed.")
    update_cell(btn_R11C3, arrRef162)

def update_R11C4():
    update_cell(btn_R11C4, arrRef163)

def update_R11C5():
    print("R11C5 button pressed.")
    update_cell(btn_R11C5, arrRef164)

def update_R11C6():
    print("R11C6 button pressed.")
    update_cell(btn_R11C6, arrRef165)

def update_R11C7():
    print("R11C7 button pressed.")
    update_cell(btn_R11C7, arrRef166)

def update_R11C8():
    print("R11C8 button pressed.")
    update_cell(btn_R11C8, arrRef167)

def update_R11C9():
    print("R11C9 button pressed.")
    update_cell(btn_R11C9, arrRef168)

def update_R11C10():
    print("R11C10 button pressed.")
    update_cell(btn_R11C10, arrRef169)

def update_R11C11():
    print("R11C11 button pressed.")
    update_cell(btn_R11C11, arrRef170)

def update_R11C12():
    print("R11C12 button pressed.")
    update_cell(btn_R11C12, arrRef171)

def update_R11C13():
    print("R11C13 button pressed.")
    update_cell(btn_R11C13, arrRef172)

def update_R11C14():
    print("R11C14 button pressed.")
    update_cell(btn_R11C14, arrRef173)

def update_R11C15():
    print("R11C15 button pressed.")
    update_cell(btn_R11C15, arrRef174)

def update_R11C16():
    print("R11C16 button pressed.")
    update_cell(btn_R11C16, arrRef175)

def update_R12C1():
    print("R12C1 button pressed.")
    update_cell(btn_R12C1, arrRef176)

def update_R12C2():
    print("R12C2 button pressed.")
    update_cell(btn_R12C2, arrRef177)

def update_R12C3():
    print("R12C3 button pressed.")
    update_cell(btn_R12C3, arrRef178)

def update_R12C4():
    print("R12C4 button pressed.")
    update_cell(btn_R12C4, arrRef179)

def update_R12C5():
    print("R12C5 button pressed.")
    update_cell(btn_R12C5, arrRef180)

def update_R12C6():
    print("R12C6 button pressed.")
    update_cell(btn_R12C6, arrRef181)

def update_R12C7():
    print("R12C7 button pressed.")
    update_cell(btn_R12C7, arrRef182)

def update_R12C8():
    print("R12C8 button pressed.")
    update_cell(btn_R12C8, arrRef183)

def update_R12C9():
    print("R12C9 button pressed.")
    update_cell(btn_R12C9, arrRef184)

def update_R12C10():
    print("R11C10 button pressed.")
    update_cell(btn_R12C10, arrRef185)

def update_R12C11():
    print("R12C11 button pressed.")
    update_cell(btn_R12C11, arrRef186)

def update_R12C12():
    print("R12C12 button pressed.")
    update_cell(btn_R12C12, arrRef187)

def update_R12C13():
    print("R12C13 button pressed.")
    update_cell(btn_R12C13, arrRef188)

def update_R12C14():
    print("R12C14 button pressed.")
    update_cell(btn_R12C14, arrRef189)

def update_R12C15():
    print("R12C15 button pressed.")
    update_cell(btn_R12C15, arrRef190)

def update_R12C16():
    print("R12C16 button pressed.")
    update_cell(btn_R12C16, arrRef191)

def update_R13C1():
    print("R13C1 button pressed.")
    update_cell(btn_R13C1, arrRef192)

def update_R13C2():
    print("R13C2 button pressed.")
    update_cell(btn_R13C2, arrRef193)

def update_R13C3():
    print("R13C3 button pressed.")
    update_cell(btn_R13C3, arrRef194)

def update_R13C4():
    print("R13C4 button pressed.")
    update_cell(btn_R13C4, arrRef195)

def update_R13C5():
    print("R13C5 button pressed.")
    update_cell(btn_R13C5, arrRef196)

def update_R13C6():
    print("R13C6 button pressed.")
    update_cell(btn_R13C6, arrRef197)

def update_R13C7():
    print("R13C7 button pressed.")
    update_cell(btn_R13C7, arrRef198)

def update_R13C8():
    print("R13C8 button pressed.")
    update_cell(btn_R13C8, arrRef199)

def update_R13C9():
    print("R13C9 button pressed.")
    update_cell(btn_R13C9, arrRef200)

def update_R13C10():
    print("R13C10 button pressed.")
    update_cell(btn_R13C10, arrRef201)

def update_R13C11():
    print("R13C11 button pressed.")
    update_cell(btn_R13C11, arrRef202)

def update_R13C12():
    print("R13C12 button pressed.")
    update_cell(btn_R13C12, arrRef203)

def update_R13C13():
    print("R13C13 button pressed.")
    update_cell(btn_R13C13, arrRef204)

def update_R13C14():
    print("R13C14 button pressed.")
    update_cell(btn_R13C14, arrRef205)

def update_R13C15():
    print("R13C15 button pressed.")
    update_cell(btn_R13C15, arrRef206)

def update_R13C16():
    print("R13C16 button pressed.")
    update_cell(btn_R13C16, arrRef207)

def update_R14C1():
    print("R14C1 button pressed.")
    update_cell(btn_R14C1, arrRef208)

def update_R14C2():
    print("R14C2 button pressed.")
    update_cell(btn_R14C2, arrRef209)

def update_R14C3():
    print("R14C3 button pressed.")
    update_cell(btn_R14C3, arrRef210)

def update_R14C4():
    print("R14C4 button pressed.")
    update_cell(btn_R14C4, arrRef211)

def update_R14C5():
    print("R14C5 button pressed.")
    update_cell(btn_R14C5, arrRef212)

def update_R14C6():
    print("R14C6 button pressed.")
    update_cell(btn_R14C6, arrRef213)

def update_R14C7():
    print("R14C7 button pressed.")
    update_cell(btn_R14C7, arrRef214)

def update_R14C8():
    print("R14C8 button pressed.")
    update_cell(btn_R14C8, arrRef215)

def update_R14C9():
    print("R14C9 button pressed.")
    update_cell(btn_R14C9, arrRef216)

def update_R14C10():
    print("R14C10 button pressed.")
    update_cell(btn_R14C10, arrRef217)

def update_R14C11():
    print("R14C11 button pressed.")
    update_cell(btn_R14C11, arrRef218)

def update_R14C12():
    print("R14C12 button pressed.")
    update_cell(btn_R14C12, arrRef219)

def update_R14C13():
    print("R14C13 button pressed.")
    update_cell(btn_R14C13, arrRef220)

def update_R14C14():
    print("R14C14 button pressed.")
    update_cell(btn_R14C14, arrRef221)

def update_R14C15():
    print("R14C15 button pressed.")
    update_cell(btn_R14C15, arrRef222)

def update_R14C16():
    print("R14C16 button pressed.")
    update_cell(btn_R14C16, arrRef223)

def update_R15C1():
    print("R15C1 button pressed.")
    update_cell(btn_R15C1, arrRef224)

def update_R15C2():
    print("R15C2 button pressed.")
    update_cell(btn_R15C2, arrRef225)

def update_R15C3():
    print("R15C3 button pressed.")
    update_cell(btn_R15C3, arrRef226)

def update_R15C4():
    print("R15C4 button pressed.")
    update_cell(btn_R15C4, arrRef227)

def update_R15C5():
    print("R15C5 button pressed.")
    update_cell(btn_R15C5, arrRef228)

def update_R15C6():
    print("R15C6 button pressed.")
    update_cell(btn_R15C6, arrRef229)

def update_R15C7():
    print("R15C7 button pressed.")
    update_cell(btn_R15C7, arrRef230)

def update_R15C8():
    print("R15C8 button pressed.")
    update_cell(btn_R15C8, arrRef231)

def update_R15C9():
    print("R15C9 button pressed.")
    update_cell(btn_R15C9, arrRef232)

def update_R15C10():
    print("R15C10 button pressed.")
    update_cell(btn_R15C10, arrRef233)

def update_R15C11():
    print("R15C11 button pressed.")
    update_cell(btn_R15C11, arrRef234)

def update_R15C12():
    print("R15C12 button pressed.")
    update_cell(btn_R15C12, arrRef235)

def update_R15C13():
    print("R15C13 button pressed.")
    update_cell(btn_R15C13, arrRef236)

def update_R15C14():
    print("R15C14 button pressed.")
    update_cell(btn_R15C14, arrRef237)

def update_R15C15():
    print("R15C15 button pressed.")
    update_cell(btn_R15C15, arrRef238)

def update_R15C16():
    print("R15C16 button pressed.")
    update_cell(btn_R15C16, arrRef239)

def update_R16C1():
    print("R16C1 button pressed.")
    update_cell(btn_R16C1, arrRef240)

def update_R16C2():
    print("R16C2 button pressed.")
    update_cell(btn_R16C2, arrRef241)

def update_R16C3():
    print("R16C3 button pressed.")
    update_cell(btn_R16C3, arrRef242)

def update_R16C4():
    print("R16C4 button pressed.")
    update_cell(btn_R16C4, arrRef243)

def update_R16C5():
    print("R16C5 button pressed.")
    update_cell(btn_R16C5, arrRef244)

def update_R16C6():
    print("R16C6 button pressed.")
    update_cell(btn_R16C6, arrRef245)

def update_R16C7():
    print("R16C7 button pressed.")
    update_cell(btn_R16C7, arrRef246)

def update_R16C8():
    print("R16C8 button pressed.")
    update_cell(btn_R16C8, arrRef247)

def update_R16C9():
    print("R16C9 button pressed.")
    update_cell(btn_R16C9, arrRef248)

def update_R16C10():
    print("R16C10 button pressed.")
    update_cell(btn_R16C10, arrRef249)

def update_R16C11():
    print("R16C11 button pressed.")
    update_cell(btn_R16C11, arrRef250)

def update_R16C12():
    print("R16C12 button pressed.")
    update_cell(btn_R16C12, arrRef251)

def update_R16C13():
    print("R16C13 button pressed.")
    update_cell(btn_R16C13, arrRef252)

def update_R16C14():
    print("R16C14 button pressed.")
    update_cell(btn_R16C14, arrRef253)

def update_R16C15():
    print("R16C15 button pressed.")
    update_cell(btn_R16C15, arrRef254)

def update_R16C16():
    print("R16C16 button pressed.")
    update_cell(btn_R16C16, arrRef255)

def ButtonRemoveANumber(): #sender As Object, e As EventArgs) Handles ButtonRemoveANumber.Click
        bRemoveANumberFromACell = True

def cells_done():
    cells_done = 256 - len(not_done_arefs)
    btn_done['text'] = f"Cells\nDone\n  {cells_done}"


def cells_remaining():
    cells_remaining = len(not_done_arefs)
    btn_remaining['text'] = f"Cells\nTo do\n {cells_remaining}"
# def build_RCS_strings():
#     print("2388 Entering CheckForOnlyOneNumber.")
#     for aref in not_done_arefs:
#         if aref['row'] == 1:
#             print("2797 row 1 nums", aref['row'])


# def CheckForOnlyOneNumber():
#     print("1733 Entering CheckForOnlyOneNumber.")
#     for aref in arrRefs_List:
#         if not aref['done']:
#             for row in range(1, 16):
#                 strTemp = ""
#             for chr in startingString:
#                 # do rows, then columns, then squares
#                 strTemp = ""    #arrValues(i)
#                 char_Count = 0
#             if len(aref['nums']) > 2 and aref['row'] == 1:
#                print("aref info ", aref['btn'], len(aref['nums']), aref['nums'])
            # if "5" in aref['nums']:
            #     # if "secret" in raw_file_content:
            #     print("aref info ", aref['nums'])
        #     if item == arrRef0:
        #         current_btn = item['btn']
        #         print(item['text'])  # , item[3], item[4], item[5]
        # print("2394 aref ", item)
    #     Me.TextBox1.Text = Me.TextBox1.Text & "Entering CheckForOnlyOneNumber " & vbCrLf
    #     Dim i As Int16
    #     'Dim j As Int16
    #     Dim strTemp As String
    #
    #     'If there is only one number in a cell, mark it done, update its value, and refresh the puzzle
    #     'Also, if a cell causes an update, run through the puzzle again looking for another cell. Thus, reset the counter "j"
    #     'CheckForOnlyOneNumber()
    #     'For j = 0 To 1
    #     For i = 0 To 255
    #         If arrDone(i) = False Then
    #             strTemp = arrValues(i)
    #             If Len(strTemp) = 1 Then
    #                 If i = 74 Then
    #                     Me.TextBox1.Text = TextBox1.Text & "Only number is " & CurrentRow & ", " & CurrentColumn & ", " & CurrentNumber & vbCrLf
    #                 End If
    #                 CurrentRow = arrReferences(i, 0)
    #                 CurrentColumn = arrReferences(i, 1)
    #                 CurrentSquare = arrReferences(i, 2)
    #                 CurrentNumber = strTemp
    #                 Me.TextBox1.Text = TextBox1.Text & "Only number is " & CurrentRow & ", " & CurrentColumn & ", " & CurrentNumber & vbCrLf
    #
    #                 arrDone(i) = True
    #                 arrValues(i) = CurrentNumber
    #                 UpdatePuzzle()
    #                 RefreshPuzzle()
    #                 Exit Sub
    #             End If
    #         End If
    #     Next
    # End Sub

def CheckForOnlyNumberInARow():
    pass

def create_record():
    pass

def temp_Test():
    global currentNumber
    currentNumber = 'D'
    # update_cell(btn_R1C2, arrRef1)
    for aref in not_done_arefs:
        temp_btn = aref['btn'] # ''' This works '''
        temp_aref = eval(aref['aref']) # ''' This works when aref is a string'''
        update_cell(temp_btn, temp_aref)
        # temp_btn = arrRef0['btn']  # ''' This works when aref is a string'''
        # temp_btn = eval(arrRef0['btn']) # TypeError: eval() arg 1 must be a string, bytes or code object

        # temp_aref = aref['aref']
        print("1900 aref ", aref)
        print("1901 temp_aref ", temp_aref)
        print("1902 temp_aref ", type(temp_btn), temp_btn)


        break

def btn_ShowAref():
    aref_text ='aref=arrRef0, btn=btn_R1C1, \n' \
    'row=1, col=1, sq=1, done=False,\n' \
    'nums=0123456789ABCDEF,\n' \
    'width=6, height=hit, font=labelfont, \n' \
    'fg=black'
    txt_Other.insert(END, aref_text)

solution_1 = {}

def save_currentSolution():
    print("2764 Entered save_currentSolution")
    global currentNumber
    global currentSolution
    currentSolution = ""
    for cell in arrRefs_List:
        if cell['done'] == True:
            currentNumber = cell['nums']
            print(f"2255 currentNumber = '{currentNumber}'")
            # btn = cell['btn']
            # aref = eval(btn_dict[cell['btn']])
            aref = cell['aref']
            btn = cell['btn']
            # update_cell(btn_R1C2, arrRef1)
            currentSolution += f"currentNumber = '{currentNumber}'"
            # currentSolution += str(cell['nums']) + "\n"
            print(f"2263 update_cell({btn} , {aref})")
            currentSolution += f"update_cell({btn} , {aref})"
            # btn = cell['btn']
            # aref = eval(btn_dict[cell['btn']])
            # aref = btn_dict[cell['btn']]
            # num = cell['nums']
            # print("1908 ", num)
            # # btn_dict = {'btn_R1C1': 'arrRef0')
            # print("1902 aref, btn ", aref, btn) # print(f"Hello, {name}")
            # currentSolution += f"currentNumber = '{num}'\n"
            # currentSolution += f"update_cell({btn}, {aref})\n"

    # print("1912 currentSolution is")
    # print(currentSolution)
        # currentNumber = 'B'
        # update_cell(btn_R1C2, arrRef1)
        # # print("2766 cell is ", cell, cell['done'])
        # current_btn = cell['btn']
        # aref = eval(btn_dict[current_btn])
        # arefID = "aref" + str(i)
        # solution_1 = dict(aref=arefID, btn=aref['btn'], done=aref['done'], nums=aref['nums'], fg=aref['fg'])
        # if cell['done'] == True:
        #     print("2900 solution 1", solution_1)
        #     # print("2768 aref0['btn'] ", arefID,  aref['btn'], aref['done'], aref['nums'], aref['fg'])
        # i += 1


                 # [aref1[btn='btn_R1C2', done=False, nums="0123\n4567\n89AB\nCDEF", fg="black"]]
    # print("2766 solution 1 ", solution_1)

    # arrRef0 = dict(btn='btn_R1C1', row=1, col=1, sq=1, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit,
    #                font=labelfont, fg="black")
    # with open('data.json', 'w') as f:
    #     json.dump(data, f)
    # aref0('done') = aref0('done')
    # aref0('nums') = aref0('nums')

def load_currentSolution():
    arc = dict{}
    # arrRef0 = dict(aref='arrRef0', btn=btn_R1C1, row=1, col=1, sq=1, done=False, nums=startingString, width=6,
    #                height=hit, font=labelfont, fg="black")

    print("2301 Entered load_solution_1")
    global currentNumber
    print(currentSolution)
    # for item in currentSolution:
    #     print("2304 load item ", item)
    #     item
    # currentNumber = 'A'
    # update_cell(btn_R1C1, arrRef0)
    # currentNumber = 'B'
    # update_cell(btn_R1C2, arrRef1)
    # currentNumber = '9'
    # update_cell(btn_R1C3, arrRef2)
    # currentNumber = '8'
    # update_cell(btn_R1C4, arrRef3)
    # currentNumber = '6'
    # update_cell(btn_R1C8, arrRef7)
    # currentNumber = '5'
    # update_cell(btn_R1C12, arrRef11)
    # currentNumber = '3'
    # update_cell(btn_R1C16, arrRef15)
    # currentNumber = '6'
    # update_cell(btn_R2C1, arrRef16)
    # currentNumber = 'D'
    # update_cell(btn_R1C1, arrRef0)
    # currentNumber = '2'
    # update_cell(btn_R1C3, arrRef2)
    # currentNumber = '1'
    # update_cell(btn_R1C4, arrRef3)
    # currentNumber = '3'
    # update_cell(btn_R1C12, arrRef11)
    # currentNumber = '7'
    # update_cell(btn_R1C16, arrRef15)
    # currentNumber = 'F'
    # update_cell(btn_R2C1, arrRef16)


def load_solution_1(btn_R1C1=None):
    print("1945 Entered load_solution_1")
    global currentNumber
    currentNumber = 'B'
    update_cell(btn_R1C2, arrRef1)
    currentNumber = '2'
    update_cell(btn_R1C3, arrRef2)
    currentNumber = '1'
    update_cell(btn_R1C4, arrRef3)
    currentNumber = '3'
    update_cell(btn_R1C8, arrRef7)
    currentNumber = '9'
    update_cell(btn_R1C11, arrRef10)
    currentNumber = '0'
    update_cell(btn_R1C15, arrRef14)
    currentNumber = '7'
    update_cell(btn_R1C16, arrRef15)
    currentNumber = 'F'
    update_cell(btn_R2C1, arrRef16)
    currentNumber = '5'
    update_cell(btn_R2C3, arrRef18)
    currentNumber = 'D'
    update_cell(btn_R2C5, arrRef20)
    currentNumber = '4'
    update_cell(btn_R2C11, arrRef26)
    currentNumber = 'B'
    update_cell(btn_R2C13, arrRef28)
    currentNumber = 'C'
    update_cell(btn_R2C14, arrRef29)
    currentNumber = 'B'
    update_cell(btn_R3C6, arrRef37)
    currentNumber = '6'
    update_cell(btn_R3C7, arrRef38)
    currentNumber = '5'
    update_cell(btn_R3C9, arrRef40)
    currentNumber = '1'
    update_cell(btn_R3C10, arrRef41)
    currentNumber = 'D'
    update_cell(btn_R3C14, arrRef45)
    currentNumber = '0'
    update_cell(btn_R4C3, arrRef50)
    currentNumber = '0'
    update_cell(btn_R4C3, arrRef50)
    currentNumber = '1'
    update_cell(btn_R4C7, arrRef54)
    currentNumber = '5'
    update_cell(btn_R4C8, arrRef55)
    currentNumber = 'C'
    update_cell(btn_R4C9, arrRef56)
    currentNumber = 'D'
    update_cell(btn_R4C10, arrRef57)
    currentNumber = 'F'
    update_cell(btn_R4C12, arrRef59)
    currentNumber = 'E'
    update_cell(btn_R4C14, arrRef61)
    currentNumber = 'A'
    update_cell(btn_R4C16, arrRef63)
    currentNumber = 'A'
    update_cell(btn_R5C5, arrRef68)
    currentNumber = 'D'
    update_cell(btn_R5C7, arrRef70)
    currentNumber = '4'
    update_cell(btn_R5C10, arrRef73)
    currentNumber = '3'
    update_cell(btn_R5C16, arrRef79)
    currentNumber = 'B'
    update_cell(btn_R6C1, arrRef80)
    currentNumber = '8'
    update_cell(btn_R6C2, arrRef81)
    currentNumber = 'F'
    update_cell(btn_R6C3, arrRef82)
    currentNumber = '4'
    update_cell(btn_R6C4, arrRef83)
    currentNumber = '6'
    update_cell(btn_R6C6, arrRef85)
    currentNumber = '9'
    update_cell(btn_R6C8, arrRef87)
    currentNumber = '2'
    update_cell(btn_R6C11, arrRef90)
    currentNumber = 'D'
    update_cell(btn_R6C13, arrRef92)
    currentNumber = '7'
    update_cell(btn_R6C14, arrRef93)
    currentNumber = 'E'
    update_cell(btn_R7C1, arrRef96)
    currentNumber = '9'
    update_cell(btn_R7C4, arrRef99)
    currentNumber = '6'
    update_cell(btn_R7C11, arrRef106)
    currentNumber = '0'
    update_cell(btn_R7C12, arrRef107)
    currentNumber = '1'
    update_cell(btn_R7C13, arrRef108)
    currentNumber = '2'
    update_cell(btn_R7C15, arrRef110)
    currentNumber = '0'
    update_cell(btn_R8C1, arrRef112)
    currentNumber = '6'
    update_cell(btn_R8C4, arrRef115)
    currentNumber = '7'
    update_cell(btn_R8C6, arrRef117)
    currentNumber = '5'
    update_cell(btn_R8C7, arrRef118)
    currentNumber = 'E'
    update_cell(btn_R8C10, arrRef121)
    currentNumber = 'A'
    update_cell(btn_R8C11, arrRef122)
    currentNumber = '4'
    update_cell(btn_R8C14, arrRef125)
    currentNumber = '8'
    update_cell(btn_R8C15, arrRef126)
    currentNumber = '6'
    update_cell(btn_R9C2, arrRef129)
    currentNumber = 'B'
    update_cell(btn_R9C3, arrRef130)
    currentNumber = '5'
    update_cell(btn_R9C6, arrRef133)
    currentNumber = 'C'
    update_cell(btn_R9C7, arrRef134)
    currentNumber = '2'
    update_cell(btn_R9C10, arrRef137)
    currentNumber = 'D'
    update_cell(btn_R9C11, arrRef138)
    currentNumber = '0'
    update_cell(btn_R9C13, arrRef140)
    currentNumber = 'F'
    update_cell(btn_R9C16, arrRef143)
    currentNumber = 'C'
    update_cell(btn_R10C2, arrRef145)
    currentNumber = 'F'
    update_cell(btn_R10C4, arrRef147)
    currentNumber = '9'
    update_cell(btn_R10C5, arrRef148)
    currentNumber = 'E'
    update_cell(btn_R10C6, arrRef149)
    currentNumber = '7'
    update_cell(btn_R10C13, arrRef156)
    currentNumber = 'B'
    update_cell(btn_R10C16, arrRef159)
    currentNumber = '4'
    update_cell(btn_R11C3, arrRef162)
    currentNumber = '2'
    update_cell(btn_R11C4, arrRef163)
    currentNumber = 'F'
    update_cell(btn_R11C6, arrRef165)
    currentNumber = '9'
    update_cell(btn_R11C9, arrRef168)
    currentNumber = 'C'
    update_cell(btn_R11C11, arrRef170)
    currentNumber = '3'
    update_cell(btn_R11C13, arrRef172)
    currentNumber = 'A'
    update_cell(btn_R11C14, arrRef173)
    currentNumber = 'E'
    update_cell(btn_R11C15, arrRef174)
    currentNumber = 'D'
    update_cell(btn_R11C16, arrRef175)
    currentNumber = '5'
    update_cell(btn_R12C1, arrRef176)
    currentNumber = '7'
    update_cell(btn_R12C7, arrRef182)
    currentNumber = 'F'
    update_cell(btn_R12C10, arrRef185)
    currentNumber = '6'
    update_cell(btn_R12C12, arrRef187)
    currentNumber = '2'
    update_cell(btn_R13C1, arrRef192)
    currentNumber = 'E'
    update_cell(btn_R13C3, arrRef194)
    currentNumber = '6'
    update_cell(btn_R13C5, arrRef196)
    currentNumber = '0'
    update_cell(btn_R13C7, arrRef198)
    currentNumber = '8'
    update_cell(btn_R13C8, arrRef199)
    currentNumber = '4'
    update_cell(btn_R13C9, arrRef200)
    currentNumber = 'B'
    update_cell(btn_R13C10, arrRef201)
    currentNumber = '1'
    update_cell(btn_R13C14, arrRef205)
    currentNumber = '9'
    update_cell(btn_R14C3, arrRef210)
    currentNumber = 'F'
    update_cell(btn_R14C7, arrRef214)
    currentNumber = 'E'
    update_cell(btn_R14C8, arrRef215)
    currentNumber = '8'
    update_cell(btn_R14C10, arrRef217)
    currentNumber = '7'
    update_cell(btn_R14C11, arrRef218)
    currentNumber = '8'
    update_cell(btn_R15C3, arrRef226)
    currentNumber = 'B'
    update_cell(btn_R15C4, arrRef227)
    currentNumber = '4'
    update_cell(btn_R15C6, arrRef229)
    currentNumber = '2'
    update_cell(btn_R15C12, arrRef235)
    currentNumber = '0'
    update_cell(btn_R15C14, arrRef237)
    currentNumber = 'E'
    update_cell(btn_R15C16, arrRef239)
    currentNumber = 'C'
    update_cell(btn_R16C1, arrRef240)
    currentNumber = '7'
    update_cell(btn_R16C2, arrRef241)
    currentNumber = '1'
    update_cell(btn_R16C6, arrRef245)
    currentNumber = '0'
    update_cell(btn_R16C9, arrRef248)
    currentNumber = '8'
    update_cell(btn_R16C13, arrRef252)
    currentNumber = '2'
    update_cell(btn_R16C14, arrRef253)
    currentNumber = 'B'
    update_cell(btn_R16C15, arrRef254)
    cells_done()
    cells_remaining()
    # aref['nums'] = currentNumber
    # btn_R1C1['text'] = D
    # current_btn = btn_R1C1
    # update_R1C1()
    # reset_cell_values(current_btn, aref)

    # print("2919 solution_1", currentNumber)
    #
    # print("2921 solution_1", arrRef0['done'])
    # aref['nums'] = D
    # print("2923 solution_1", arrRef0['nums'])
    # aref['fg'] = 'red'
    # print("2925 solution_1", arrRef0['fg'])
    # # btn_R1C1['text'] = arrRef0['nums']
    # current_btn['text'] = aref['nums']
    # print("2919 solution_1 finished")
    # update_R1C1()
    # current_btn = btn_R1C1
    # aref = arrRef0
    # reset_cell_values(current_btn, aref)

    # not_done_arefs.remove(aref)
    # aref['nums'] = currentNumber
    # update_puzzle(1, 1, 1)
    # arrRef0['done'] = True
    # arrRef0['nums'] = D
    # arrRef0['fg'] = 'red'
    # btn_R1C1['text'] = arrRef0['nums']


    # for cell in not_done_arefs:
    #     current_button = cell['btn']
    #     aref = eval(btn_dict[current_button])
        # aref0('done') = False


lbl_Title = Label(main_canvas, text="Monster Sudoku Solver")
lbl_Title.grid(row=0, sticky='n')
lbl_Title.config(font=titlefont)
# lbl_LineSpace = Label(main_canvas, text="")
# lbl_LineSpace.grid(row=1, sticky='n')
# lbl_LineSpace.config(font=titlefont)

btn_R1C1 = tk.Button(F1_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R1C1, width=6, height=hit)
btn_R1C1.grid(row=1, column=0, sticky='w')
btn_R1C1.config(font=labelfont)
# btn_R1C1.bind("<<ButtonPress>>", update_R1C1())
btn_R1C2 = Button(F1_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R1C2, width=6, height=hit)
btn_R1C2.grid(row=1, column=1, sticky='w')
btn_R1C2.config(font=labelfont)
# btn_R1C2.bind("<<ComboboxSelected>>", create_record())
btn_R1C3 = Button(F1_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R1C3, width=6, height=hit)
btn_R1C3.grid(row=1, column=2, sticky='w')
btn_R1C3.config(font=labelfont)
# btn_R1C3.bind("<<ComboboxSelected>>", create_record())
btn_R1C4 = Button(F1_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R1C4, width=6, height=hit)
btn_R1C4.grid(row=1, column=3, sticky='w')
btn_R1C4.config(font=labelfont)
btn_R1C4.bind("<<ComboboxSelected>>", create_record())

btn_R1C5 = Button(F2_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R1C5, width=6, height=hit)
btn_R1C5.grid(row=1, column=0, sticky='w')
btn_R1C5.config(font=labelfont)
# btn_R1C5.bind("<<ComboboxSelected>>", create_record())
btn_R1C6 = Button(F2_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R1C6, width=6, height=hit)
btn_R1C6.grid(row=1, column=1, sticky='w')
btn_R1C6.config(font=labelfont)
btn_R1C6.bind("<<ComboboxSelected>>", create_record())
btn_R1C7 = Button(F2_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R1C7, width=6, height=hit)
btn_R1C7.grid(row=1, column=2, sticky='w')
btn_R1C7.config(font=labelfont)
# btn_R1C7.bind("<<ComboboxSelected>>", create_record())
btn_R1C8 = Button(F2_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R1C8, width=6, height=hit)
btn_R1C8.grid(row=1, column=3, sticky='w')
btn_R1C8.config(font=labelfont)
# btn_R1C8.bind("<<ComboboxSelected>>", create_record())

btn_R1C9 = Button(F3_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R1C9, width=6, height=hit)
btn_R1C9.grid(row=1, column=0, sticky='w')
btn_R1C9.config(font=labelfont)
# btn_R1C9.bind("<<ComboboxSelected>>", create_record())
btn_R1C10 = Button(F3_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R1C10, width=6, height=hit)
btn_R1C10.grid(row=1, column=1, sticky='w')
btn_R1C10.config(font=labelfont)
# btn_R1C10.bind("<<ComboboxSelected>>", create_record())
btn_R1C11 = Button(F3_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R1C11, width=6, height=hit)
btn_R1C11.grid(row=1, column=2, sticky='w')
btn_R1C11.config(font=labelfont)
btn_R1C12 = Button(F3_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R1C12, width=6, height=hit)
btn_R1C12.grid(row=1, column=3, sticky='w')
btn_R1C12.config(font=labelfont)
# btn_R1C12.bind("<<ComboboxSelected>>", create_record())
btn_R1C13 = Button(F4_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R1C13, width=6, height=hit)
btn_R1C13.grid(row=1, column=0, sticky='w')
btn_R1C13.config(font=labelfont)
# btn_R1C13.bind("<<ComboboxSelected>>", create_record())
btn_R1C14 = Button(F4_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R1C14, width=6, height=hit)
btn_R1C14.grid(row=1, column=1, sticky='w')
btn_R1C14.config(font=labelfont)
# btn_R1C14.bind("<<ComboboxSelected>>", create_record())
btn_R1C15 = Button(F4_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R1C15, width=6, height=hit)
btn_R1C15.grid(row=1, column=2, sticky='w')
btn_R1C15.config(font=labelfont)
btn_R1C16 = Button(F4_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R1C16, width=6, height=hit)
btn_R1C16.grid(row=1, column=3, sticky='w')
btn_R1C16.config(font=labelfont)
# btn_R1C16.bind("<<ComboboxSelected>>", create_record())
btn_0 = Button(sn_frame, wraplength=40, justify=LEFT, text='0',
            command=set_current_num_to_0, width=6, height=hit)
btn_0.grid(row=2, column=0, sticky='nw')
btn_0.config(font=entryfont)
btn_1 = Button(sn_frame, wraplength=40, justify=LEFT, text='1',
            command=set_current_num_to_1, width=6, height=hit)
btn_1.grid(row=2, column=1, sticky='nw')
btn_1.config(font=labelfont)
btn_2 = Button(sn_frame, wraplength=40, justify=LEFT, text='2',
            command=set_current_num_to_2, width=6, height=hit)
btn_2.grid(row=2, column=2, sticky='nw')
btn_2.config(font=labelfont)
btn_3 = Button(sn_frame, wraplength=40, justify=LEFT, text='3',
            command=set_current_num_to_3, width=6, height=hit)
btn_3.grid(row=2, column=3, sticky='nw')
btn_3.config(font=labelfont)
# ***********
btn_R2C1 = Button(F1_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R2C1, width=6, height=hit)
btn_R2C1.grid(row=2, column=0, sticky='w')
btn_R2C1.config(font=labelfont)
btn_R2C1.bind("<<ComboboxSelected>>", create_record())
btn_R2C2 = Button(F1_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R2C2, width=6, height=hit)
btn_R2C2.grid(row=2, column=1, sticky='w')
btn_R2C2.config(font=labelfont)
btn_R2C2.bind("<<ComboboxSelected>>", create_record())
btn_R2C3 = Button(F1_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R2C3, width=6, height=hit)
btn_R2C3.grid(row=2, column=2, sticky='w')
btn_R2C3.config(font=labelfont)
btn_R2C3.bind("<<ComboboxSelected>>", create_record())
btn_R2C4 = Button(F1_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R2C4, width=6, height=hit)
btn_R2C4.grid(row=2, column=3, sticky='w')
btn_R2C4.config(font=labelfont)
btn_R2C4.bind("<<ComboboxSelected>>", create_record())

btn_R2C5 = Button(F2_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R2C5, width=6, height=hit)
btn_R2C5.grid(row=2, column=0, sticky='w')
btn_R2C5.config(font=labelfont)
btn_R2C5.bind("<<ComboboxSelected>>", create_record())
btn_R2C6 = Button(F2_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R2C6, width=6, height=hit)
btn_R2C6.grid(row=2, column=1, sticky='w')
btn_R2C6.config(font=labelfont)
btn_R2C6.bind("<<ComboboxSelected>>", create_record())
btn_R2C7 = Button(F2_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R2C7, width=6, height=hit)
btn_R2C7.grid(row=2, column=2, sticky='w')
btn_R2C7.config(font=labelfont)
btn_R2C7.bind("<<ComboboxSelected>>", create_record())
btn_R2C8 = Button(F2_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R2C8, width=6, height=hit)
btn_R2C8.grid(row=2, column=3, sticky='w')
btn_R2C8.config(font=labelfont)
btn_R2C8.bind("<<ComboboxSelected>>", create_record())

btn_R2C9 = Button(F3_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R2C9, width=6, height=hit)
btn_R2C9.grid(row=2, column=0, sticky='w')
btn_R2C9.config(font=labelfont)
btn_R2C9.bind("<<ComboboxSelected>>", create_record())
btn_R2C10 = Button(F3_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R2C10, width=6, height=hit)
btn_R2C10.grid(row=2, column=1, sticky='w')
btn_R2C10.config(font=labelfont)
btn_R2C11 = Button(F3_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R2C11, width=6, height=hit)
btn_R2C11.grid(row=2, column=2, sticky='w')
btn_R2C11.config(font=labelfont)
btn_R2C12 = Button(F3_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R2C12, width=6, height=hit)
btn_R2C12.grid(row=2, column=3, sticky='w')
btn_R2C12.config(font=labelfont)
# btn_R2C12.bind("<<ComboboxSelected>>", create_record())
btn_R2C13 = Button(F4_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R2C13, width=6, height=hit)
btn_R2C13.grid(row=2, column=0, sticky='w')
btn_R2C13.config(font=labelfont)
# btn_R2C13.bind("<<ComboboxSelected>>", create_record())
btn_R2C14 = Button(F4_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R2C14, width=6, height=hit)
btn_R2C14.grid(row=2, column=1, sticky='w')
btn_R2C14.config(font=labelfont)
btn_R2C14.bind("<<ComboboxSelected>>", create_record())
btn_R2C15 = Button(F4_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R2C15, width=6, height=hit)
btn_R2C15.grid(row=2, column=2, sticky='w')
btn_R2C15.config(font=labelfont)
btn_R2C16 = Button(F4_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R2C16, width=6, height=hit)
btn_R2C16.grid(row=2, column=3, sticky='w')
btn_R2C16.config(font=labelfont)
# btn_R2C16.bind("<<ComboboxSelected>>", create_record())
btn_4 = Button(sn_frame, wraplength=40, justify=LEFT, text='4',
            command=set_current_num_to_4, width=6, height=hit)
btn_4.grid(row=3, column=0, sticky='nw')
btn_4.config(font=entryfont)
btn_5 = Button(sn_frame, wraplength=40, justify=LEFT, text='5',
            command=set_current_num_to_5, width=6, height=hit)
btn_5.grid(row=3, column=1, sticky='nw')
btn_5.config(font=entryfont)
btn_6 = Button(sn_frame, wraplength=40, justify=LEFT, text='6',
            command=set_current_num_to_6, width=6, height=hit)
btn_6.grid(row=3, column=2, sticky='nw')
btn_6.config(font=entryfont)
btn_7 = Button(sn_frame, wraplength=48, justify=LEFT, text='7',
            command=set_current_num_to_7, width=6, height=hit)
btn_7.grid(row=3, column=3, sticky='nw')
btn_7.config(font=entryfont)
btn_7.bind("<<ButtonPress>>", set_current_num_to_7)   # <<ButtonPress>>
######
btn_R3C1 = Button(F1_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R3C1, width=6, height=hit)
btn_R3C1.grid(row=3, column=0, sticky='w')
btn_R3C1.config(font=labelfont)
btn_R3C1.bind("<<ComboboxSelected>>", create_record())
btn_R3C2 = Button(F1_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R3C2, width=6, height=hit)
btn_R3C2.grid(row=3, column=1, sticky='w')
btn_R3C2.config(font=labelfont)
btn_R3C2.bind("<<ComboboxSelected>>", create_record())
btn_R3C3 = Button(F1_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R3C3, width=6, height=hit)
btn_R3C3.grid(row=3, column=2, sticky='w')
btn_R3C3.config(font=labelfont)
# btn_R3C3.bind("<<ComboboxSelected>>", create_record())
btn_R3C4 = Button(F1_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R3C4, width=6, height=hit)
btn_R3C4.grid(row=3, column=3, sticky='w')
btn_R3C4.config(font=labelfont)
# btn_R3C4.bind("<<ComboboxSelected>>", create_record())

btn_R3C5 = Button(F2_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R3C5, width=6, height=hit)
btn_R3C5.grid(row=3, column=0, sticky='w')
btn_R3C5.config(font=labelfont)
# btn_R3C5.bind("<<ComboboxSelected>>", create_record())
btn_R3C6 = Button(F2_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R3C6, width=6, height=hit)
btn_R3C6.grid(row=3, column=1, sticky='w')
btn_R3C6.config(font=labelfont)
# btn_R3C6.bind("<<ComboboxSelected>>", create_record())
btn_R3C7 = Button(F2_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R3C7, width=6, height=hit)
btn_R3C7.grid(row=3, column=2, sticky='w')
btn_R3C7.config(font=labelfont)
btn_R3C7.bind("<<ComboboxSelected>>", create_record())
btn_R3C8 = Button(F2_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R3C8, width=6, height=hit)
btn_R3C8.grid(row=3, column=3, sticky='w')
btn_R3C8.config(font=labelfont)
btn_R3C8.bind("<<ComboboxSelected>>", create_record())

btn_R3C9 = Button(F3_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R3C9, width=6, height=hit)
btn_R3C9.grid(row=3, column=0, sticky='w')
btn_R3C9.config(font=labelfont)
btn_R3C9.bind("<<ComboboxSelected>>", create_record())
btn_R3C10 = Button(F3_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R3C10, width=6, height=hit)
btn_R3C10.grid(row=3, column=1, sticky='w')
btn_R3C10.config(font=labelfont)
btn_R3C10.bind("<<ComboboxSelected>>", create_record())
btn_R3C11 = Button(F3_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R3C11, width=6, height=hit)
btn_R3C11.grid(row=3, column=2, sticky='w')
btn_R3C11.config(font=labelfont)
btn_R3C12 = Button(F3_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R3C12, width=6, height=hit)
btn_R3C12.grid(row=3, column=3, sticky='w')
btn_R3C12.config(font=labelfont)
btn_R3C12.bind("<<ComboboxSelected>>", create_record())
btn_R3C13 = Button(F4_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R3C13, width=6, height=hit)
btn_R3C13.grid(row=3, column=0, sticky='w')
btn_R3C13.config(font=labelfont)
btn_R3C13.bind("<<ComboboxSelected>>", create_record())
btn_R3C14 = Button(F4_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R3C14, width=6, height=hit)
btn_R3C14.grid(row=3, column=1, sticky='w')
btn_R3C14.config(font=labelfont)
btn_R3C14.bind("<<ComboboxSelected>>", create_record())
btn_R3C15 = Button(F4_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R3C15, width=6, height=hit)
btn_R3C15.grid(row=3, column=2, sticky='w')
btn_R3C15.config(font=labelfont)
btn_R3C16 = Button(F4_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R3C16, width=6, height=hit)
btn_R3C16.grid(row=3, column=3, sticky='w')
btn_R3C16.config(font=labelfont)
btn_8 = Button(sn_frame, wraplength=40, justify=LEFT, text='8',
            command=set_current_num_to_8, width=6, height=hit)
btn_8.grid(row=4, column=0, sticky='nw')
btn_8.config(font=entryfont)
btn_9 = Button(sn_frame, wraplength=40, justify=LEFT, text='9',
            command=set_current_num_to_9, width=6, height=hit)
btn_9.grid(row=4, column=1, sticky='nw')
btn_9.config(font=entryfont)
btn_A = Button(sn_frame, wraplength=40, justify=LEFT, text='A',
            command=set_current_num_to_A, width=6, height=hit)
btn_A.grid(row=4, column=2, sticky='nw')
btn_A.config(font=entryfont)
btn_B = Button(sn_frame, wraplength=40, justify=LEFT, text='B',
            command=set_current_num_to_B, width=6, height=hit)
btn_B.grid(row=4, column=3, sticky='nw')
btn_B.config(font=entryfont)
# ***********
btn_R4C1 = Button(F1_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R4C1, width=6, height=hit)
btn_R4C1.grid(row=4, column=0, sticky='nw')
btn_R4C1.config(font=labelfont)
btn_R4C1.bind("<<ComboboxSelected>>", create_record())
btn_R4C2 = Button(F1_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R4C2, width=6, height=hit)
btn_R4C2.grid(row=4, column=1, sticky='w')
btn_R4C2.config(font=labelfont)
btn_R4C2.bind("<<ComboboxSelected>>", create_record())
btn_R4C3 = Button(F1_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R4C3, width=6, height=hit)
btn_R4C3.grid(row=4, column=2, sticky='w')
btn_R4C3.config(font=labelfont)
btn_R4C3.bind("<<ComboboxSelected>>", create_record())
btn_R4C4 = Button(F1_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R4C4, width=6, height=hit)
btn_R4C4.grid(row=4, column=3, sticky='w')
btn_R4C4.config(font=labelfont)
btn_R4C4.bind("<<ComboboxSelected>>", create_record())

btn_R4C5 = Button(F2_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R4C5, width=6, height=hit)
btn_R4C5.grid(row=4, column=0, sticky='w')
btn_R4C5.config(font=labelfont)
btn_R4C5.bind("<<ComboboxSelected>>", create_record())
btn_R4C6 = Button(F2_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R4C6, width=6, height=hit)
btn_R4C6.grid(row=4, column=1, sticky='w')
btn_R4C6.config(font=labelfont)
btn_R4C7 = Button(F2_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R4C7, width=6, height=hit)
btn_R4C7.grid(row=4, column=2, sticky='w')
btn_R4C7.config(font=labelfont)
btn_R4C8 = Button(F2_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R4C8, width=6, height=hit)
btn_R4C8.grid(row=4, column=3, sticky='w')
btn_R4C8.config(font=labelfont)
btn_R4C9 = Button(F3_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R4C9, width=6, height=hit)
btn_R4C9.grid(row=4, column=0, sticky='w')
btn_R4C9.config(font=labelfont)
btn_R4C10 = Button(F3_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R4C10, width=6, height=hit)
btn_R4C10.grid(row=4, column=1, sticky='w')
btn_R4C10.config(font=labelfont)
btn_R4C11 = Button(F3_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R4C11, width=6, height=hit)
btn_R4C11.grid(row=4, column=2, sticky='w')
btn_R4C11.config(font=labelfont)
btn_R4C12 = Button(F3_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R4C12, width=6, height=hit)
btn_R4C12.grid(row=4, column=3, sticky='w')
btn_R4C12.config(font=labelfont)
btn_R4C13 = Button(F4_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R4C13, width=6, height=hit)
btn_R4C13.grid(row=4, column=0, sticky='w')
btn_R4C13.config(font=labelfont)
btn_R4C14 = Button(F4_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R4C14, width=6, height=hit)
btn_R4C14.grid(row=4, column=1, sticky='w')
btn_R4C14.config(font=labelfont)
btn_R4C15 = Button(F4_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R4C15, width=6, height=hit)
btn_R4C15.grid(row=4, column=2, sticky='w')
btn_R4C15.config(font=labelfont)
btn_R4C16 = Button(F4_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R4C16, width=6, height=hit)
btn_R4C16.grid(row=4, column=3, sticky='w')
btn_R4C16.config(font=labelfont)
btn_C = Button(sn_frame, wraplength=40, justify=LEFT, text='C',
            command=set_current_num_to_C, width=6, height=hit)
btn_C.grid(row=5, column=0, sticky='nw')
btn_C.config(font=entryfont)
btn_D = Button(sn_frame, wraplength=40, justify=LEFT, text='D',
            command=set_current_num_to_D, width=6, height=hit)
btn_D.grid(row=5, column=1, sticky='nw')
btn_D.config(font=entryfont)
btn_E = Button(sn_frame, wraplength=40, justify=LEFT, text='E',
            command=set_current_num_to_E, width=6, height=hit)
btn_E.grid(row=5, column=2, sticky='nw')
btn_E.config(font=entryfont)
btn_F = Button(sn_frame, wraplength=40, justify=LEFT, text='F',
            command=set_current_num_to_F, width=6, height=hit)
btn_F.grid(row=5, column=3, sticky='nw')
btn_F.config(font=entryfont)
# ########3333
btn_R5C1 = tk.Button(F5_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R5C1, width=6, height=hit)
btn_R5C1.grid(row=1, column=0, sticky='w')
btn_R5C1.config(font=labelfont)
# btn_R1C1.bind("<<ButtonPress>>", update_R1C1())
btn_R5C2 = Button(F5_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R5C2, width=6, height=hit)
btn_R5C2.grid(row=1, column=1, sticky='w')
btn_R5C2.config(font=labelfont)
btn_R5C2.bind("<<ComboboxSelected>>", create_record())
btn_R5C3 = Button(F5_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R5C3, width=6, height=hit)
btn_R5C3.grid(row=1, column=2, sticky='w')
btn_R5C3.config(font=labelfont)
btn_R5C3.bind("<<ComboboxSelected>>", create_record())
btn_R5C4 = Button(F5_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R5C4, width=6, height=hit)
btn_R5C4.grid(row=1, column=3, sticky='w')
btn_R5C4.config(font=labelfont)
btn_R5C4.bind("<<ComboboxSelected>>", create_record())

btn_R5C5 = Button(F6_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R5C5, width=6, height=hit)
btn_R5C5.grid(row=1, column=0, sticky='w')
btn_R5C5.config(font=labelfont)
btn_R5C5.bind("<<ComboboxSelected>>", create_record())
btn_R5C6 = Button(F6_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R5C6, width=6, height=hit)
btn_R5C6.grid(row=1, column=1, sticky='w')
btn_R5C6.config(font=labelfont)
btn_R5C6.bind("<<ComboboxSelected>>", create_record())
btn_R5C7 = Button(F6_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R5C7, width=6, height=hit)
btn_R5C7.grid(row=1, column=2, sticky='w')
btn_R5C7.config(font=labelfont)
btn_R5C7.bind("<<ComboboxSelected>>", create_record())
btn_R5C8 = Button(F6_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R5C8, width=6, height=hit)
btn_R5C8.grid(row=1, column=3, sticky='w')
btn_R5C8.config(font=labelfont)
btn_R5C8.bind("<<ComboboxSelected>>", create_record())

btn_R5C9 = Button(F7_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R5C9, width=6, height=hit)
btn_R5C9.grid(row=1, column=0, sticky='w')
btn_R5C9.config(font=labelfont)
btn_R5C9.bind("<<ComboboxSelected>>", create_record())
btn_R5C10 = Button(F7_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R5C10, width=6, height=hit)
btn_R5C10.grid(row=1, column=1, sticky='w')
btn_R5C10.config(font=labelfont)
btn_R5C10.bind("<<ComboboxSelected>>", create_record())
btn_R5C11 = Button(F7_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R5C11, width=6, height=hit)
btn_R5C11.grid(row=1, column=2, sticky='w')
btn_R5C11.config(font=labelfont)
btn_R5C12 = Button(F7_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R5C12, width=6, height=hit)
btn_R5C12.grid(row=1, column=3, sticky='w')
btn_R5C12.config(font=labelfont)
btn_R5C12.bind("<<ComboboxSelected>>", create_record())
btn_R5C13 = Button(F8_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R5C13, width=6, height=hit)
btn_R5C13.grid(row=1, column=0, sticky='w')
btn_R5C13.config(font=labelfont)
btn_R5C13.bind("<<ComboboxSelected>>", create_record())
btn_R5C14 = Button(F8_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R5C14, width=6, height=hit)
btn_R5C14.grid(row=1, column=1, sticky='w')
btn_R5C14.config(font=labelfont)
btn_R5C14.bind("<<ComboboxSelected>>", create_record())
btn_R5C15 = Button(F8_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R5C15, width=6, height=hit)
btn_R5C15.grid(row=1, column=2, sticky='w')
btn_R5C15.config(font=labelfont)
btn_R5C16 = Button(F8_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R5C16, width=6, height=hit)
btn_R5C16.grid(row=1, column=3, sticky='w')
btn_R5C16.config(font=labelfont)
# btn_R1C16.bind("<<ComboboxSelected>>", create_record())
# btn_x = Button(fn_frame, wraplength=40, justify=LEFT, text='0',
#             command=set_current_num_to_0, width=6, height=hit)
# btn_x.grid(row=1, column=0, sticky='nw')
# btn_x.config(font=entryfont)

# btn_z = Button(fn_frame, wraplength=40, justify=LEFT, text='2',
#             command=set_current_num_to_2, width=6, height=hit)
# btn_z.grid(row=1, column=2, sticky='n')
# btn_z.config(font=entryfont)
# btn_z = Button(fn_frame, wraplength=40, justify=LEFT, text='3',
#             command=set_current_num_to_3, width=6, height=hit)
# btn_z.grid(row=1, column=3, sticky='n')
# btn_z.config(font=entryfont)
btn_R6C1 = tk.Button(F5_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R6C1, width=6, height=hit)
btn_R6C1.grid(row=2, column=0, sticky='w')
btn_R6C1.config(font=labelfont)
# btn_R6C1.bind("<<ButtonPress>>", update_R1C1())
btn_R6C2 = Button(F5_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R6C2, width=6, height=hit)
btn_R6C2.grid(row=2, column=1, sticky='w')
btn_R6C2.config(font=labelfont)
btn_R6C2.bind("<<ComboboxSelected>>", create_record())
btn_R6C3 = Button(F5_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R6C3, width=6, height=hit)
btn_R6C3.grid(row=2, column=2, sticky='w')
btn_R6C3.config(font=labelfont)
btn_R6C3.bind("<<ComboboxSelected>>", create_record())
btn_R6C4 = Button(F5_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R6C4, width=6, height=hit)
btn_R6C4.grid(row=2, column=3, sticky='w')
btn_R6C4.config(font=labelfont)
btn_R6C4.bind("<<ComboboxSelected>>", create_record())

btn_R6C5 = Button(F6_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R6C5, width=6, height=hit)
btn_R6C5.grid(row=2, column=0, sticky='w')
btn_R6C5.config(font=labelfont)
btn_R6C5.bind("<<ComboboxSelected>>", create_record())
btn_R6C6 = Button(F6_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R6C6, width=6, height=hit)
btn_R6C6.grid(row=2, column=1, sticky='w')
btn_R6C6.config(font=labelfont)
btn_R6C6.bind("<<ComboboxSelected>>", create_record())
btn_R6C7 = Button(F6_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R6C7, width=6, height=hit)
btn_R6C7.grid(row=2, column=2, sticky='w')
btn_R6C7.config(font=labelfont)
btn_R6C7.bind("<<ComboboxSelected>>", create_record())
btn_R6C8 = Button(F6_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R6C8, width=6, height=hit)
btn_R6C8.grid(row=2, column=3, sticky='w')
btn_R6C8.config(font=labelfont)
btn_R6C8.bind("<<ComboboxSelected>>", create_record())

btn_R6C9 = Button(F7_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R6C9, width=6, height=hit)
btn_R6C9.grid(row=2, column=0, sticky='w')
btn_R6C9.config(font=labelfont)
btn_R6C9.bind("<<ComboboxSelected>>", create_record())
btn_R6C10 = Button(F7_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R6C10, width=6, height=hit)
btn_R6C10.grid(row=2, column=1, sticky='w')
btn_R6C10.config(font=labelfont)
btn_R6C10.bind("<<ComboboxSelected>>", create_record())
btn_R6C11 = Button(F7_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R6C11, width=6, height=hit)
btn_R6C11.grid(row=2, column=2, sticky='w')
btn_R6C11.config(font=labelfont)
btn_R6C12 = Button(F7_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R6C12, width=6, height=hit)
btn_R6C12.grid(row=2, column=3, sticky='w')
btn_R6C12.config(font=labelfont)
btn_R6C12.bind("<<ComboboxSelected>>", create_record())
btn_R6C13 = Button(F8_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R6C13, width=6, height=hit)
btn_R6C13.grid(row=2, column=0, sticky='w')
btn_R6C13.config(font=labelfont)
btn_R6C13.bind("<<ComboboxSelected>>", create_record())
btn_R6C14 = Button(F8_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R6C14, width=6, height=hit)
btn_R6C14.grid(row=2, column=1, sticky='w')
btn_R6C14.config(font=labelfont)
btn_R6C14.bind("<<ComboboxSelected>>", create_record())
btn_R6C15 = Button(F8_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R6C15, width=6, height=hit)
btn_R6C15.grid(row=2, column=2, sticky='w')
btn_R6C15.config(font=labelfont)
btn_R6C16 = Button(F8_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R6C16, width=6, height=hit)
btn_R6C16.grid(row=2, column=3, sticky='w')
btn_R6C16.config(font=labelfont)
# ***********
btn_R7C1 = tk.Button(F5_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R7C1, width=6, height=hit)
btn_R7C1.grid(row=3, column=0, sticky='w')
btn_R7C1.config(font=labelfont)
btn_R7C2 = Button(F5_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R7C2, width=6, height=hit)
btn_R7C2.grid(row=3, column=1, sticky='w')
btn_R7C2.config(font=labelfont)
btn_R7C2.bind("<<ComboboxSelected>>", create_record())
btn_R7C3 = Button(F5_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R7C3, width=6, height=hit)
btn_R7C3.grid(row=3, column=2, sticky='w')
btn_R7C3.config(font=labelfont)
btn_R7C3.bind("<<ComboboxSelected>>", create_record())
btn_R7C4 = Button(F5_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R7C4, width=6, height=hit)
btn_R7C4.grid(row=3, column=3, sticky='w')
btn_R7C4.config(font=labelfont)
btn_R7C4.bind("<<ComboboxSelected>>", create_record())

btn_R7C5 = Button(F6_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R7C5, width=6, height=hit)
btn_R7C5.grid(row=3, column=0, sticky='w')
btn_R7C5.config(font=labelfont)
btn_R7C5.bind("<<ComboboxSelected>>", create_record())
btn_R7C6 = Button(F6_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R7C6, width=6, height=hit)
btn_R7C6.grid(row=3, column=1, sticky='w')
btn_R7C6.config(font=labelfont)
btn_R7C6.bind("<<ComboboxSelected>>", create_record())
btn_R7C7 = Button(F6_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R7C7, width=6, height=hit)
btn_R7C7.grid(row=3, column=2, sticky='w')
btn_R7C7.config(font=labelfont)
btn_R7C7.bind("<<ComboboxSelected>>", create_record())
btn_R7C8 = Button(F6_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R7C8, width=6, height=hit)
btn_R7C8.grid(row=3, column=3, sticky='w')
btn_R7C8.config(font=labelfont)
btn_R7C8.bind("<<ComboboxSelected>>", create_record())

btn_R7C9 = Button(F7_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R7C9, width=6, height=hit)
btn_R7C9.grid(row=3, column=0, sticky='w')
btn_R7C9.config(font=labelfont)
btn_R7C9.bind("<<ComboboxSelected>>", create_record())
btn_R7C10 = Button(F7_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R7C10, width=6, height=hit)
btn_R7C10.grid(row=3, column=1, sticky='w')
btn_R7C10.config(font=labelfont)
btn_R7C10.bind("<<ComboboxSelected>>", create_record())
btn_R7C11 = Button(F7_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R7C11, width=6, height=hit)
btn_R7C11.grid(row=3, column=2, sticky='w')
btn_R7C11.config(font=labelfont)
btn_R7C12 = Button(F7_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R7C12, width=6, height=hit)
btn_R7C12.grid(row=3, column=3, sticky='w')
btn_R7C12.config(font=labelfont)
btn_R7C12.bind("<<ComboboxSelected>>", create_record())
btn_R7C13 = Button(F8_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R7C13, width=6, height=hit)
btn_R7C13.grid(row=3, column=0, sticky='w')
btn_R7C13.config(font=labelfont)
btn_R7C13.bind("<<ComboboxSelected>>", create_record())
btn_R7C14 = Button(F8_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R7C14, width=6, height=hit)
btn_R7C14.grid(row=3, column=1, sticky='w')
btn_R7C14.config(font=labelfont)
btn_R7C14.bind("<<ComboboxSelected>>", create_record())
btn_R7C15 = Button(F8_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R7C15, width=6, height=hit)
btn_R7C15.grid(row=3, column=2, sticky='w')
btn_R7C15.config(font=labelfont)
btn_R7C16 = Button(F8_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R7C16, width=6, height=hit)
btn_R7C16.grid(row=3, column=3, sticky='w')
btn_R7C16.config(font=labelfont)
# btn_R1C16.bind("<<ComboboxSelected>>", create_record())
btn_only_one_num = Button(fn_frame, wraplength=40, justify=LEFT, text='Find\nSingle',
            command=CheckForOnlyOneNumber, width=6, height=3)
btn_only_one_num.grid(row=0, column=0, sticky='nw')
btn_only_one_num.config(font=labelfont)
btn_find_duple = Button(fn_frame, wraplength=40, justify=LEFT, text='Find\nDuple',
            command=find_Duple, width=6, height=hit)
btn_find_duple.grid(row=0, column=1, sticky='nw')
btn_find_duple.config(font=entryfont)
btn_find_triple = Button(fn_frame, wraplength=40, justify=LEFT, text='Find\nTriple',
            command=find_Triple, width=6, height=hit)
btn_find_triple.grid(row=0, column=2, sticky='nw')
btn_find_triple.config(font=entryfont)
btn_find_quad = Button(fn_frame, wraplength=40, justify=LEFT, text='Find\nQuad',
            command=find_Quad, width=6, height=hit)
btn_find_quad.grid(row=0, column=3, sticky='nw')
btn_find_quad.config(font=entryfont)
btn_R8C1 = tk.Button(F5_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R8C1, width=6, height=hit)
btn_R8C1.grid(row=4, column=0, sticky='w')
btn_R8C1.config(font=labelfont)
btn_R8C2 = Button(F5_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R8C2, width=6, height=hit)
btn_R8C2.grid(row=4, column=1, sticky='w')
btn_R8C2.config(font=labelfont)
btn_R8C2.bind("<<ComboboxSelected>>", create_record())
btn_R8C3 = Button(F5_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R8C3, width=6, height=hit)
btn_R8C3.grid(row=4, column=2, sticky='w')
btn_R8C3.config(font=labelfont)
btn_R8C3.bind("<<ComboboxSelected>>", create_record())
btn_R8C4 = Button(F5_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R8C4, width=6, height=hit)
btn_R8C4.grid(row=4, column=3, sticky='w')
btn_R8C4.config(font=labelfont)
btn_R8C4.bind("<<ComboboxSelected>>", create_record())

btn_R8C5 = Button(F6_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R8C5, width=6, height=hit)
btn_R8C5.grid(row=4, column=0, sticky='w')
btn_R8C5.config(font=labelfont)
btn_R8C5.bind("<<ComboboxSelected>>", create_record())
btn_R8C6 = Button(F6_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R8C6, width=6, height=hit)
btn_R8C6.grid(row=4, column=1, sticky='w')
btn_R8C6.config(font=labelfont)
btn_R8C6.bind("<<ComboboxSelected>>", create_record())
btn_R8C7 = Button(F6_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R8C7, width=6, height=hit)
btn_R8C7.grid(row=4, column=2, sticky='w')
btn_R8C7.config(font=labelfont)
btn_R8C7.bind("<<ComboboxSelected>>", create_record())
btn_R8C8 = Button(F6_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R8C8, width=6, height=hit)
btn_R8C8.grid(row=4, column=3, sticky='w')
btn_R8C8.config(font=labelfont)
btn_R8C8.bind("<<ComboboxSelected>>", create_record())

btn_R8C9 = Button(F7_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R8C9, width=6, height=hit)
btn_R8C9.grid(row=4, column=0, sticky='w')
btn_R8C9.config(font=labelfont)
btn_R8C9.bind("<<ComboboxSelected>>", create_record())
btn_R8C10 = Button(F7_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R8C10, width=6, height=hit)
btn_R8C10.grid(row=4, column=1, sticky='w')
btn_R8C10.config(font=labelfont)
btn_R8C10.bind("<<ComboboxSelected>>", create_record())
btn_R8C11 = Button(F7_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R8C11, width=6, height=hit)
btn_R8C11.grid(row=4, column=2, sticky='w')
btn_R8C11.config(font=labelfont)
btn_R8C12 = Button(F7_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R8C12, width=6, height=hit)
btn_R8C12.grid(row=4, column=3, sticky='w')
btn_R8C12.config(font=labelfont)
btn_R8C12.bind("<<ComboboxSelected>>", create_record())
btn_R8C13 = Button(F8_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R8C13, width=6, height=hit)
btn_R8C13.grid(row=4, column=0, sticky='w')
btn_R8C13.config(font=labelfont)
btn_R8C13.bind("<<ComboboxSelected>>", create_record())
btn_R8C14 = Button(F8_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R8C14, width=6, height=hit)
btn_R8C14.grid(row=4, column=1, sticky='w')
btn_R8C14.config(font=labelfont)
btn_R8C14.bind("<<ComboboxSelected>>", create_record())
btn_R8C15 = Button(F8_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R8C15, width=6, height=hit)
btn_R8C15.grid(row=4, column=2, sticky='w')
btn_R8C15.config(font=labelfont)
btn_R8C16 = Button(F8_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R8C16, width=6, height=hit)
btn_R8C16.grid(row=4, column=3, sticky='w')
btn_R8C16.config(font=labelfont)

################

btn_R9C1 = Button(F9_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R9C1, width=6, height=hit)
btn_R9C1.grid(row=1, column=0, sticky='w')
btn_R9C1.config(font=labelfont)
btn_R9C1.bind("<<ComboboxSelected>>", create_record())
btn_R9C2 = Button(F9_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R9C2, width=6, height=hit)
btn_R9C2.grid(row=1, column=1, sticky='w')
btn_R9C2.config(font=labelfont)
btn_R9C2.bind("<<ComboboxSelected>>", create_record())
btn_R9C3 = Button(F9_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R9C3, width=6, height=hit)
btn_R9C3.grid(row=1, column=2, sticky='w')
btn_R9C3.config(font=labelfont)
btn_R9C3.bind("<<ComboboxSelected>>", create_record())
btn_R9C4 = Button(F9_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R9C4, width=6, height=hit)
btn_R9C4.grid(row=1, column=3, sticky='w')
btn_R9C4.config(font=labelfont)
btn_R9C4.bind("<<ComboboxSelected>>", create_record())

btn_R9C5 = Button(F10_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R9C5, width=6, height=hit)
btn_R9C5.grid(row=1, column=0, sticky='w')
btn_R9C5.config(font=labelfont)
btn_R9C5.bind("<<ComboboxSelected>>", create_record())
btn_R9C6 = Button(F10_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R9C6, width=6, height=hit)
btn_R9C6.grid(row=1, column=1, sticky='w')
btn_R9C6.config(font=labelfont)
btn_R9C6.bind("<<ComboboxSelected>>", create_record())
btn_R9C7 = Button(F10_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R9C7, width=6, height=hit)
btn_R9C7.grid(row=1, column=2, sticky='w')
btn_R9C7.config(font=labelfont)
btn_R9C7.bind("<<ComboboxSelected>>", create_record())
btn_R9C8 = Button(F10_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R9C8, width=6, height=hit)
btn_R9C8.grid(row=1, column=3, sticky='w')
btn_R9C8.config(font=labelfont)
btn_R9C8.bind("<<ComboboxSelected>>", create_record())

btn_R9C9 = Button(F11_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R9C9, width=6, height=hit)
btn_R9C9.grid(row=1, column=0, sticky='w')
btn_R9C9.config(font=labelfont)
btn_R9C10 = Button(F11_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R9C10, width=6, height=hit)
btn_R9C10.grid(row=1, column=1, sticky='w')
btn_R9C10.config(font=labelfont)
btn_R9C10.bind("<<ComboboxSelected>>", create_record())
btn_R9C11 = Button(F11_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R9C11, width=6, height=hit)
btn_R9C11.grid(row=1, column=2, sticky='w')
btn_R9C11.config(font=labelfont)
btn_R9C12 = Button(F11_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R9C12, width=6, height=hit)
btn_R9C12.grid(row=1, column=3, sticky='w')
btn_R9C12.config(font=labelfont)
btn_R9C12.bind("<<ComboboxSelected>>", create_record())
btn_R9C13 = Button(F12_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R9C13, width=6, height=hit)
btn_R9C13.grid(row=1, column=0, sticky='w')
btn_R9C13.config(font=labelfont)
btn_R9C13.bind("<<ComboboxSelected>>", create_record())
btn_R9C14 = Button(F12_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R9C14, width=6, height=hit)
btn_R9C14.grid(row=1, column=1, sticky='w')
btn_R9C14.config(font=labelfont)
btn_R9C14.bind("<<ComboboxSelected>>", create_record())
btn_R9C15 = Button(F12_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R9C15, width=6, height=hit)
btn_R9C15.grid(row=1, column=2, sticky='w')
btn_R9C15.config(font=labelfont)
btn_R9C16 = Button(F12_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R9C16, width=6, height=hit)
btn_R9C16.grid(row=1, column=3, sticky='w')
btn_R9C16.config(font=labelfont)
# btn_R2C16.bind("<<ComboboxSelected>>", create_record())
btn_solve_singles = Button(fn_frame, wraplength=40, justify=LEFT, text='Solve\nRow Col Square',
            command=solve_row_singles, width=6, height=hit)
btn_solve_singles.grid(row=2, column=0, sticky='nw')
btn_solve_singles.config(font=entryfont)
btn_Save = Button(fn_frame, wraplength=40, justify=LEFT, text='Save\ncurr\nsoln',
            command=save_currentSolution, width=6, height=hit)
btn_Save.grid(row=2, column=1, sticky='nw')
btn_Save.config(font=entryfont)
btn_load_current = Button(fn_frame, wraplength=40, justify=LEFT, text='Load\ncurr\nsoln',
            command=load_currentSolution, width=6, height=hit)
btn_load_current.grid(row=2, column=2, sticky='nw')
btn_load_current.config(font=entryfont)
# btn_y = Button(fn_frame, wraplength=40, justify=LEFT, text='y',
#             command=set_current_num_to_6, width=6, height=hit)
# btn_y.grid(row=2, column=2, sticky='nw')
# btn_y.config(font=entryfont)
btn_z = Button(fn_frame, wraplength=48, justify=LEFT, text='z',
            command=set_current_num_to_7, width=6, height=hit)
btn_z.grid(row=2, column=3, sticky='nw')
btn_z.config(font=entryfont)
btn_z.bind("<<ButtonPress>>", set_current_num_to_7)
###
btn_del_num = Button(fn_frame, wraplength=40, justify=LEFT, text='Del\nnum\nfrom\ncell',
            command=set_bRemoveANumberFromACell, width=6, height=hit)
btn_del_num.grid(row=3, column=0, sticky='nw')
btn_del_num.config(font=entryfont)
# btn_a = Button(fn_frame, wraplength=40, justify=LEFT, text='a',
#             command=set_current_num_to_4, width=6, height=hit)
# btn_a.grid(row=3, column=0, sticky='nw')
# btn_a.config(font=entryfont)
btn_ShowAref = Button(fn_frame, wraplength=40, justify=LEFT, text='Show\nData\nStruct',
            command=btn_ShowAref, width=6, height=hit)
btn_ShowAref.grid(row=3, column=1, sticky='nw')
btn_ShowAref.config(font=entryfont)
btn_done = Button(fn_frame, wraplength=40, justify=LEFT, text='Cells\nDone',
            command=cells_done, width=6, height=hit)
btn_done.grid(row=3, column=2, sticky='nw')
btn_done.config(font=entryfont)
btn_remaining = Button(fn_frame, wraplength=48, justify=LEFT, text='Cells\nRemaining',
            command=cells_remaining, width=6, height=hit)
btn_remaining.grid(row=3, column=3, sticky='nw')
btn_remaining.config(font=entryfont)

btn_e = Button(fn_frame, wraplength=40, justify=LEFT, text='Temp\ntest',
            command=temp_Test, width=6, height=hit)
btn_e.grid(row=4, column=0, sticky='nw')
btn_e.config(font=entryfont)
btn_load = Button(fn_frame, wraplength=40, justify=LEFT, text='Load\nsoln',
            command=load_solution_1, width=6, height=hit)
btn_load.grid(row=4, column=1, sticky='nw')
btn_load.config(font=entryfont)
btn_g = Button(fn_frame, wraplength=40, justify=LEFT, text='Make\nRCS\nSets',
            command=find_Triple, width=6, height=hit)
btn_g.grid(row=4, column=2, sticky='nw')
btn_g.config(font=entryfont)
btn_h = Button(fn_frame, wraplength=48, justify=LEFT, text='save\nsol\n1',
            command=save_currentSolution, width=6, height=hit)
btn_h.grid(row=4, column=3, sticky='nw')
btn_h.config(font=entryfont)


btn_R10C1 = Button(F9_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R10C1, width=6, height=hit)
btn_R10C1.grid(row=2, column=0, sticky='w')
btn_R10C1.config(font=labelfont)
btn_R10C2 = Button(F9_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R10C2, width=6, height=hit)
btn_R10C2.grid(row=2, column=1, sticky='w')
btn_R10C2.config(font=labelfont)
btn_R10C3 = Button(F9_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R10C3, width=6, height=hit)
btn_R10C3.grid(row=2, column=2, sticky='w')
btn_R10C3.config(font=labelfont)
btn_R10C4 = Button(F9_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R10C4, width=6, height=hit)
btn_R10C4.grid(row=2, column=3, sticky='w')
btn_R10C4.config(font=labelfont)
btn_R10C5 = Button(F10_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R10C5, width=6, height=hit)
btn_R10C5.grid(row=2, column=0, sticky='w')
btn_R10C5.config(font=labelfont)
btn_R10C6 = Button(F10_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R10C6, width=6, height=hit)
btn_R10C6.grid(row=2, column=1, sticky='w')
btn_R10C6.config(font=labelfont)
btn_R10C7 = Button(F10_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R10C7, width=6, height=hit)
btn_R10C7.grid(row=2, column=2, sticky='w')
btn_R10C7.config(font=labelfont)
btn_R10C8 = Button(F10_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R10C8, width=6, height=hit)
btn_R10C8.grid(row=2, column=3, sticky='w')
btn_R10C8.config(font=labelfont)
btn_R10C9 = Button(F11_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R10C9, width=6, height=hit)
btn_R10C9.grid(row=2, column=0, sticky='w')
btn_R10C9.config(font=labelfont)
btn_R10C10 = Button(F11_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R10C10, width=6, height=hit)
btn_R10C10.grid(row=2, column=1, sticky='w')
btn_R10C10.config(font=labelfont)
btn_R10C11 = Button(F11_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R10C11, width=6, height=hit)
btn_R10C11.grid(row=2, column=2, sticky='w')
btn_R10C11.config(font=labelfont)
btn_R10C12 = Button(F11_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R10C12, width=6, height=hit)
btn_R10C12.grid(row=2, column=3, sticky='w')
btn_R10C12.config(font=labelfont)
btn_R10C13 = Button(F12_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R10C13, width=6, height=hit)
btn_R10C13.grid(row=2, column=0, sticky='w')
btn_R10C13.config(font=labelfont)
btn_R10C14 = Button(F12_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R10C14, width=6, height=hit)
btn_R10C14.grid(row=2, column=1, sticky='w')
btn_R10C14.config(font=labelfont)
btn_R10C15 = Button(F12_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R10C15, width=6, height=hit)
btn_R10C15.grid(row=2, column=2, sticky='w')
btn_R10C15.config(font=labelfont)
btn_R10C16 = Button(F12_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R10C16, width=6, height=hit)
btn_R10C16.grid(row=2, column=3, sticky='w')
btn_R10C16.config(font=labelfont)

btn_R11C1 = Button(F9_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R11C1, width=6, height=hit)
btn_R11C1.grid(row=3, column=0, sticky='w')
btn_R11C1.config(font=labelfont)
btn_R11C2 = Button(F9_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R11C2, width=6, height=hit)
btn_R11C2.grid(row=3, column=1, sticky='w')
btn_R11C2.config(font=labelfont)
btn_R11C3 = Button(F9_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R11C3, width=6, height=hit)
btn_R11C3.grid(row=3, column=2, sticky='w')
btn_R11C3.config(font=labelfont)
btn_R11C4 = Button(F9_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R11C4, width=6, height=hit)
btn_R11C4.grid(row=3, column=3, sticky='w')
btn_R11C4.config(font=labelfont)
btn_R11C5 = Button(F10_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R11C5, width=6, height=hit)
btn_R11C5.grid(row=3, column=0, sticky='w')
btn_R11C5.config(font=labelfont)
btn_R11C6 = Button(F10_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R11C6, width=6, height=hit)
btn_R11C6.grid(row=3, column=1, sticky='w')
btn_R11C6.config(font=labelfont)
btn_R11C7 = Button(F10_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R11C7, width=6, height=hit)
btn_R11C7.grid(row=3, column=2, sticky='w')
btn_R11C7.config(font=labelfont)
btn_R11C8 = Button(F10_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R11C8, width=6, height=hit)
btn_R11C8.grid(row=3, column=3, sticky='w')
btn_R11C8.config(font=labelfont)
btn_R11C9 = Button(F11_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R11C9, width=6, height=hit)
btn_R11C9.grid(row=3, column=0, sticky='w')
btn_R11C9.config(font=labelfont)
btn_R11C10 = Button(F11_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R11C10, width=6, height=hit)
btn_R11C10.grid(row=3, column=1, sticky='w')
btn_R11C10.config(font=labelfont)
btn_R11C11 = Button(F11_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R11C11, width=6, height=hit)
btn_R11C11.grid(row=3, column=2, sticky='w')
btn_R11C11.config(font=labelfont)
btn_R11C12 = Button(F11_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R11C12, width=6, height=hit)
btn_R11C12.grid(row=3, column=3, sticky='w')
btn_R11C12.config(font=labelfont)
btn_R11C13 = Button(F12_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R11C13, width=6, height=hit)
btn_R11C13.grid(row=3, column=0, sticky='w')
btn_R11C13.config(font=labelfont)
btn_R11C14 = Button(F12_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R11C14, width=6, height=hit)
btn_R11C14.grid(row=3, column=1, sticky='w')
btn_R11C14.config(font=labelfont)
btn_R11C15 = Button(F12_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R11C15, width=6, height=hit)
btn_R11C15.grid(row=3, column=2, sticky='w')
btn_R11C15.config(font=labelfont)
btn_R11C16 = Button(F12_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R11C16, width=6, height=hit)
btn_R11C16.grid(row=3, column=3, sticky='w')
btn_R11C16.config(font=labelfont)
btn_R12C1 = Button(F9_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R12C1, width=6, height=hit)
btn_R12C1.grid(row=4, column=0, sticky='w')
btn_R12C1.config(font=labelfont)
btn_R12C2 = Button(F9_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R12C2, width=6, height=hit)
btn_R12C2.grid(row=4, column=1, sticky='w')
btn_R12C2.config(font=labelfont)
btn_R12C3 = Button(F9_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R12C3, width=6, height=hit)
btn_R12C3.grid(row=4, column=2, sticky='w')
btn_R12C3.config(font=labelfont)
btn_R12C4 = Button(F9_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R12C4, width=6, height=hit)
btn_R12C4.grid(row=4, column=3, sticky='w')
btn_R12C4.config(font=labelfont)
btn_R12C5 = Button(F10_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R12C5, width=6, height=hit)
btn_R12C5.grid(row=4, column=0, sticky='w')
btn_R12C5.config(font=labelfont)
btn_R12C6 = Button(F10_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R12C6, width=6, height=hit)
btn_R12C6.grid(row=4, column=1, sticky='w')
btn_R12C6.config(font=labelfont)
btn_R12C7 = Button(F10_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R12C7, width=6, height=hit)
btn_R12C7.grid(row=4, column=2, sticky='w')
btn_R12C7.config(font=labelfont)
btn_R12C8 = Button(F10_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R12C8, width=6, height=hit)
btn_R12C8.grid(row=4, column=3, sticky='w')
btn_R12C8.config(font=labelfont)
btn_R12C9 = Button(F11_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R12C9, width=6, height=hit)
btn_R12C9.grid(row=4, column=0, sticky='w')
btn_R12C9.config(font=labelfont)
btn_R12C10 = Button(F11_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R12C10, width=6, height=hit)
btn_R12C10.grid(row=4, column=1, sticky='w')
btn_R12C10.config(font=labelfont)
btn_R12C11 = Button(F11_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R12C11, width=6, height=hit)
btn_R12C11.grid(row=4, column=2, sticky='w')
btn_R12C11.config(font=labelfont)
btn_R12C12 = Button(F11_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R12C12, width=6, height=hit)
btn_R12C12.grid(row=4, column=3, sticky='w')
btn_R12C12.config(font=labelfont)
btn_R12C13 = Button(F12_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R12C13, width=6, height=hit)
btn_R12C13.grid(row=4, column=0, sticky='w')
btn_R12C13.config(font=labelfont)
btn_R12C14 = Button(F12_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R12C14, width=6, height=hit)
btn_R12C14.grid(row=4, column=1, sticky='w')
btn_R12C14.config(font=labelfont)
btn_R12C15 = Button(F12_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R12C15, width=6, height=hit)
btn_R12C15.grid(row=4, column=2, sticky='w')
btn_R12C15.config(font=labelfont)
btn_R12C16 = Button(F12_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R12C16, width=6, height=hit)
btn_R12C16.grid(row=4, column=3, sticky='w')
btn_R12C16.config(font=labelfont)
btn_R13C1 = Button(F13_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R13C1, width=6, height=hit)
btn_R13C1.grid(row=0, column=0, sticky='w')
btn_R13C1.config(font=labelfont)
btn_R13C2 = Button(F13_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R13C2, width=6, height=hit)
btn_R13C2.grid(row=0, column=1, sticky='w')
btn_R13C2.config(font=labelfont)
btn_R13C3 = Button(F13_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R13C3, width=6, height=hit)
btn_R13C3.grid(row=0, column=2, sticky='w')
btn_R13C3.config(font=labelfont)
btn_R13C4 = Button(F13_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R13C4, width=6, height=hit)
btn_R13C4.grid(row=0, column=3, sticky='w')
btn_R13C4.config(font=labelfont)
btn_R13C5 = Button(F14_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R13C5, width=6, height=hit)
btn_R13C5.grid(row=0, column=0, sticky='w')
btn_R13C5.config(font=labelfont)
btn_R13C6 = Button(F14_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R13C6, width=6, height=hit)
btn_R13C6.grid(row=0, column=1, sticky='w')
btn_R13C6.config(font=labelfont)
btn_R13C7 = Button(F14_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R13C7, width=6, height=hit)
btn_R13C7.grid(row=0, column=2, sticky='w')
btn_R13C7.config(font=labelfont)
btn_R13C8 = Button(F14_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R13C8, width=6, height=hit)
btn_R13C8.grid(row=0, column=3, sticky='w')
btn_R13C8.config(font=labelfont)
btn_R13C9 = Button(F15_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R13C9, width=6, height=hit)
btn_R13C9.grid(row=0, column=0, sticky='w')
btn_R13C9.config(font=labelfont)
btn_R13C10 = Button(F15_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R13C10, width=6, height=hit)
btn_R13C10.grid(row=0, column=1, sticky='w')
btn_R13C10.config(font=labelfont)
btn_R13C11 = Button(F15_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R13C11, width=6, height=hit)
btn_R13C11.grid(row=0, column=2, sticky='w')
btn_R13C11.config(font=labelfont)
btn_R13C12 = Button(F15_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R13C12, width=6, height=hit)
btn_R13C12.grid(row=0, column=3, sticky='w')
btn_R13C12.config(font=labelfont)
btn_R13C13 = Button(F16_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R13C13, width=6, height=hit)
btn_R13C13.grid(row=0, column=0, sticky='w')
btn_R13C13.config(font=labelfont)
btn_R13C14 = Button(F16_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R13C14, width=6, height=hit)
btn_R13C14.grid(row=0, column=1, sticky='w')
btn_R13C14.config(font=labelfont)
btn_R13C15 = Button(F16_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R13C15, width=6, height=hit)
btn_R13C15.grid(row=0, column=2, sticky='w')
btn_R13C15.config(font=labelfont)
btn_R13C16 = Button(F16_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R13C16, width=6, height=hit)
btn_R13C16.grid(row=0, column=3, sticky='w')
btn_R13C16.config(font=labelfont)

btn_R14C1 = Button(F13_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R14C1, width=6, height=hit)
btn_R14C1.grid(row=1, column=0, sticky='w')
btn_R14C1.config(font=labelfont)
btn_R14C2 = Button(F13_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R14C2, width=6, height=hit)
btn_R14C2.grid(row=1, column=1, sticky='w')
btn_R14C2.config(font=labelfont)
btn_R14C3 = Button(F13_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R14C3, width=6, height=hit)
btn_R14C3.grid(row=1, column=2, sticky='w')
btn_R14C3.config(font=labelfont)
btn_R14C4 = Button(F13_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R14C4, width=6, height=hit)
btn_R14C4.grid(row=1, column=3, sticky='w')
btn_R14C4.config(font=labelfont)
btn_R14C5 = Button(F14_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R14C5, width=6, height=hit)
btn_R14C5.grid(row=1, column=0, sticky='w')
btn_R14C5.config(font=labelfont)
btn_R14C6 = Button(F14_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R14C6, width=6, height=hit)
btn_R14C6.grid(row=1, column=1, sticky='w')
btn_R14C6.config(font=labelfont)
btn_R14C7 = Button(F14_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R14C7, width=6, height=hit)
btn_R14C7.grid(row=1, column=2, sticky='w')
btn_R14C7.config(font=labelfont)
btn_R14C8 = Button(F14_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R14C8, width=6, height=hit)
btn_R14C8.grid(row=1, column=3, sticky='w')
btn_R14C8.config(font=labelfont)
btn_R14C9 = Button(F15_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R14C9, width=6, height=hit)
btn_R14C9.grid(row=1, column=0, sticky='w')
btn_R14C9.config(font=labelfont)
btn_R14C10 = Button(F15_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R14C10, width=6, height=hit)
btn_R14C10.grid(row=1, column=1, sticky='w')
btn_R14C10.config(font=labelfont)
btn_R14C11 = Button(F15_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R14C11, width=6, height=hit)
btn_R14C11.grid(row=1, column=2, sticky='w')
btn_R14C11.config(font=labelfont)
btn_R14C12 = Button(F15_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R14C12, width=6, height=hit)
btn_R14C12.grid(row=1, column=3, sticky='w')
btn_R14C12.config(font=labelfont)
btn_R14C13 = Button(F16_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R14C13, width=6, height=hit)
btn_R14C13.grid(row=1, column=0, sticky='w')
btn_R14C13.config(font=labelfont)
btn_R14C14 = Button(F16_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R14C14, width=6, height=hit)
btn_R14C14.grid(row=1, column=1, sticky='w')
btn_R14C14.config(font=labelfont)
btn_R14C15 = Button(F16_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R14C15, width=6, height=hit)
btn_R14C15.grid(row=1, column=2, sticky='w')
btn_R14C15.config(font=labelfont)
btn_R14C16 = Button(F16_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R14C16, width=6, height=hit)
btn_R14C16.grid(row=1, column=3, sticky='w')
btn_R14C16.config(font=labelfont)
btn_R15C1 = Button(F13_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R15C1, width=6, height=hit)
btn_R15C1.grid(row=2, column=0, sticky='w')
btn_R15C1.config(font=labelfont)
btn_R15C2 = Button(F13_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R15C2, width=6, height=hit)
btn_R15C2.grid(row=2, column=1, sticky='w')
btn_R15C2.config(font=labelfont)
btn_R15C3 = Button(F13_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R15C3, width=6, height=hit)
btn_R15C3.grid(row=2, column=2, sticky='w')
btn_R15C3.config(font=labelfont)
btn_R15C4 = Button(F13_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R15C4, width=6, height=hit)
btn_R15C4.grid(row=2, column=3, sticky='w')
btn_R15C4.config(font=labelfont)
btn_R15C5 = Button(F14_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R15C5, width=6, height=hit)
btn_R15C5.grid(row=2, column=0, sticky='w')
btn_R15C5.config(font=labelfont)
btn_R15C6 = Button(F14_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R15C6, width=6, height=hit)
btn_R15C6.grid(row=2, column=1, sticky='w')
btn_R15C6.config(font=labelfont)
btn_R15C7 = Button(F14_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R15C7, width=6, height=hit)
btn_R15C7.grid(row=2, column=2, sticky='w')
btn_R15C7.config(font=labelfont)
btn_R15C8 = Button(F14_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R15C8, width=6, height=hit)
btn_R15C8.grid(row=2, column=3, sticky='w')
btn_R15C8.config(font=labelfont)
btn_R15C9 = Button(F15_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R15C9, width=6, height=hit)
btn_R15C9.grid(row=2, column=0, sticky='w')
btn_R15C9.config(font=labelfont)
btn_R15C10 = Button(F15_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R15C10, width=6, height=hit)
btn_R15C10.grid(row=2, column=1, sticky='w')
btn_R15C10.config(font=labelfont)
btn_R15C11 = Button(F15_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R15C11, width=6, height=hit)
btn_R15C11.grid(row=2, column=2, sticky='w')
btn_R15C11.config(font=labelfont)
btn_R15C12 = Button(F15_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R15C12, width=6, height=hit)
btn_R15C12.grid(row=2, column=3, sticky='w')
btn_R15C12.config(font=labelfont)
btn_R15C13 = Button(F16_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R15C13, width=6, height=hit)
btn_R15C13.grid(row=2, column=0, sticky='w')
btn_R15C13.config(font=labelfont)
btn_R15C14 = Button(F16_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R15C14, width=6, height=hit)
btn_R15C14.grid(row=2, column=1, sticky='w')
btn_R15C14.config(font=labelfont)
btn_R15C15 = Button(F16_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R15C15, width=6, height=hit)
btn_R15C15.grid(row=2, column=2, sticky='w')
btn_R15C15.config(font=labelfont)
btn_R15C16 = Button(F16_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R15C16, width=6, height=hit)
btn_R15C16.grid(row=2, column=3, sticky='w')
btn_R15C16.config(font=labelfont)

btn_R16C1 = Button(F13_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R16C1, width=6, height=hit)
btn_R16C1.grid(row=3, column=0, sticky='w')
btn_R16C1.config(font=labelfont)
btn_R16C2 = Button(F13_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R16C2, width=6, height=hit)
btn_R16C2.grid(row=3, column=1, sticky='w')
btn_R16C2.config(font=labelfont)
btn_R16C3 = Button(F13_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R16C3, width=6, height=hit)
btn_R16C3.grid(row=3, column=2, sticky='w')
btn_R16C3.config(font=labelfont)
btn_R16C4 = Button(F13_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R16C4, width=6, height=hit)
btn_R16C4.grid(row=3, column=3, sticky='w')
btn_R16C4.config(font=labelfont)
btn_R16C5 = Button(F14_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R16C5, width=6, height=hit)
btn_R16C5.grid(row=3, column=0, sticky='w')
btn_R16C5.config(font=labelfont)
btn_R16C6 = Button(F14_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R16C6, width=6, height=hit)
btn_R16C6.grid(row=3, column=1, sticky='w')
btn_R16C6.config(font=labelfont)
btn_R16C7 = Button(F14_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R16C7, width=6, height=hit)
btn_R16C7.grid(row=3, column=2, sticky='w')
btn_R16C7.config(font=labelfont)
btn_R16C8 = Button(F14_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R16C8, width=6, height=hit)
btn_R16C8.grid(row=3, column=3, sticky='w')
btn_R16C8.config(font=labelfont)
btn_R16C9 = Button(F15_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R16C9, width=6, height=hit)
btn_R16C9.grid(row=3, column=0, sticky='w')
btn_R16C9.config(font=labelfont)
btn_R16C10 = Button(F15_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R16C10, width=6, height=hit)
btn_R16C10.grid(row=3, column=1, sticky='w')
btn_R16C10.config(font=labelfont)
btn_R16C11 = Button(F15_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R16C11, width=6, height=hit)
btn_R16C11.grid(row=3, column=2, sticky='w')
btn_R16C11.config(font=labelfont)
btn_R16C12 = Button(F15_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R16C12, width=6, height=hit)
btn_R16C12.grid(row=3, column=3, sticky='w')
btn_R16C12.config(font=labelfont)
btn_R16C13 = Button(F16_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R16C13, width=6, height=hit)
btn_R16C13.grid(row=3, column=0, sticky='w')
btn_R16C13.config(font=labelfont)
btn_R16C14 = Button(F16_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R16C14, width=6, height=hit)
btn_R16C14.grid(row=3, column=1, sticky='w')
btn_R16C14.config(font=labelfont)
btn_R16C15 = Button(F16_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R16C15, width=6, height=hit)
btn_R16C15.grid(row=3, column=2, sticky='w')
btn_R16C15.config(font=labelfont)
btn_R16C16 = Button(F16_frame, wraplength=48, justify=LEFT, text=startingString,
            command=update_R16C16, width=6, height=hit)
btn_R16C16.grid(row=3, column=3, sticky='w')
btn_R16C16.config(font=labelfont)
txt_Explain = Text(ex_frame, width=30, height=15)
txt_Explain.grid(row=0, column=0, rowspan=4, sticky='w')  #, columnspan=4, sticky='nw'
txt_Explain.config(font=labelfont)
txt_Explain.insert(END, 'Explanatory text goes below.\n')
# txt_Explain.insert(END, startingString)

txt_Other = Text(txt_frame, width=32, height=15)
txt_Other.grid(row=0, column=0, rowspan=4, sticky='w')  #, columnspan=4, sticky='nw'
txt_Other.config(font=labelfont)
txt_Other.insert(END, 'Other text goes below.\n')

# EventText=tk.Text(root, height=10, width=50)
EventScrollBar = tk.Scrollbar(ex_frame, command=txt_Explain.yview, orient="vertical")
EventScrollBar.grid(row=0, column=1, sticky="ns")
# txt_Explain.grid(row=0,column=0)
txt_Explain.configure(yscrollcommand=EventScrollBar.set)
# Quote=("""Suck\ne\ne\ne\ne\ne\ne\ne\ne\ne\nee\ne\ne\ne\ne\ne\ne\ne\nee\ned\ne\ne\nde\nd\ne\nded\nc\nc\nx\nc\nx\nc\nzc\ns\nds\nx\nwd\ns\nd\nwd""")
# txt_Explain.insert(tk.END, Quote)



# arrRef0 = dict(btn=btn_R1C1)

btn_dict = {}
arrRef0 = dict(aref='arrRef0', btn=btn_R1C1, row=1, col=1, sq=1, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef1 = dict(aref='arrRef1', btn=btn_R1C2, row=1, col=2, sq=1, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef2 = dict(aref='arrRef2', btn=btn_R1C3, row=1, col=3, sq=1, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef3 = dict(aref='arrRef3', btn=btn_R1C4, row=1, col=4, sq=1, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef4 = dict(aref='arrRef4', btn=btn_R1C5, row=1, col=5, sq=2, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef5 = dict(aref='arrRef5', btn=btn_R1C6, row=1, col=6, sq=2, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef6 = dict(aref='arrRef6', btn=btn_R1C7, row=1, col=7, sq=2, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef7 = dict(aref='arrRef7', btn=btn_R1C8, row=1, col=8, sq=2, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef8 = dict(aref='arrRef8', btn=btn_R1C9, row=1, col=9, sq=3, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef9 = dict(aref='arrRef9', btn=btn_R1C10, row=1, col=10, sq=3, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef10 = dict(aref='arrRef10', btn=btn_R1C11, row=1, col=11, sq=3, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef11 = dict(aref='arrRef11', btn=btn_R1C12, row=1, col=12, sq=3, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef12 = dict(aref='arrRef12', btn=btn_R1C13, row=1, col=13, sq=4, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef13 = dict(aref='arrRef13', btn=btn_R1C14, row=1, col=14, sq=4, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef14 = dict(aref='arrRef14', btn=btn_R1C15, row=1, col=15, sq=4, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef15 = dict(aref='arrRef15', btn=btn_R1C16, row=1, col=16, sq=4, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef16 = dict(aref='arrRef16', btn=btn_R2C1, row=2, col=1, sq=1, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef17 = dict(aref='arrRef17', btn=btn_R2C2, row=2, col=2, sq=1, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef18 = dict(aref='arrRef18', btn=btn_R2C3, row=2, col=3, sq=1, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef19 = dict(aref='arrRef19', btn=btn_R2C4, row=2, col=4, sq=1, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef20 = dict(aref='arrRef20', btn=btn_R2C5, row=2, col=5, sq=2, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef21 = dict(aref='arrRef21', btn=btn_R2C6, row=2, col=6, sq=2, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef22 = dict(aref='arrRef22', btn=btn_R2C7, row=2, col=7, sq=2, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef23 = dict(aref='arrRef23', btn=btn_R2C8, row=2, col=8, sq=2, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef24 = dict(aref='arrRef24', btn=btn_R2C9, row=2, col=9, sq=3, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef25 = dict(aref='arrRef25', btn=btn_R2C10, row=2, col=10, sq=3, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef26 = dict(aref='arrRef26', btn=btn_R2C11, row=2, col=11, sq=3, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef27 = dict(aref='arrRef27', btn=btn_R2C12, row=2, col=12, sq=3, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef28 = dict(aref='arrRef28', btn=btn_R2C13, row=2, col=13, sq=4, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef29 = dict(aref='arrRef29', btn=btn_R2C14, row=2, col=14, sq=4, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef30 = dict(aref='arrRef30', btn=btn_R2C15, row=2, col=15, sq=4, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef31 = dict(aref='arrRef31', btn=btn_R2C16, row=2, col=16, sq=4, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef32 = dict(aref='arrRef32', btn=btn_R3C1, row=3, col=1, sq=1, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef33 = dict(aref='arrRef33', btn=btn_R3C2, row=3, col=2, sq=1, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef34 = dict(aref='arrRef34', btn=btn_R3C3, row=3, col=3, sq=1, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef35 = dict(aref='arrRef35', btn=btn_R3C4, row=3, col=4, sq=1, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef36 = dict(aref='arrRef36', btn=btn_R3C5, row=3, col=5, sq=2, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef37 = dict(aref='arrRef37', btn=btn_R3C6, row=3, col=6, sq=2, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef38 = dict(aref='arrRef38', btn=btn_R3C7, row=3, col=7, sq=2, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef39 = dict(aref='arrRef39', btn=btn_R3C8, row=3, col=8, sq=2, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef40 = dict(aref='arrRef40', btn=btn_R3C9, row=3, col=9, sq=3, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef41 = dict(aref='arrRef41', btn=btn_R3C10, row=3, col=10, sq=3, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef42 = dict(aref='arrRef41', btn=btn_R3C11, row=3, col=11, sq=3, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef43 = dict(aref='arrRef43', btn=btn_R3C12, row=3, col=12, sq=3, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef44 = dict(aref='arrRef44', btn=btn_R3C13, row=3, col=13, sq=4, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef45 = dict(aref='arrRef45', btn=btn_R3C14, row=3, col=14, sq=4, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef46 = dict(aref='arrRef46', btn=btn_R3C15, row=3, col=15, sq=4, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef47 = dict(aref='arrRef47', btn=btn_R3C16, row=3, col=16, sq=4, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef48 = dict(aref='arrRef48', btn=btn_R4C1, row=4, col=1, sq=1, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef49 = dict(aref='arrRef49', btn=btn_R4C2, row=4, col=2, sq=1, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef50 = dict(aref='arrRef50', btn=btn_R4C3, row=4, col=3, sq=1, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef51 = dict(aref='arrRef51', btn=btn_R4C4, row=4, col=4, sq=1, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef52 = dict(aref='arrRef52', btn=btn_R4C5, row=4, col=5, sq=2, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef53 = dict(aref='arrRef53', btn=btn_R4C6, row=4, col=6, sq=2, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef54 = dict(aref='arrRef54', btn=btn_R4C7, row=4, col=7, sq=2, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef55 = dict(aref='arrRef55', btn=btn_R4C8, row=4, col=8, sq=2, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef56 = dict(aref='arrRef56', btn=btn_R4C9, row=4, col=9, sq=3, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef57 = dict(aref='arrRef57', btn=btn_R4C10, row=4, col=10, sq=3, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef58 = dict(aref='arrRef58', btn=btn_R4C11, row=4, col=11, sq=3, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef59 = dict(aref='arrRef59', btn=btn_R4C12, row=4, col=12, sq=3, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef60 = dict(aref='arrRef60', btn=btn_R4C13, row=4, col=13, sq=4, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef61 = dict(aref='arrRef61', btn=btn_R4C14, row=4, col=14, sq=4, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef62 = dict(aref='arrRef62', btn=btn_R4C15, row=4, col=15, sq=4, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef63 = dict(aref='arrRef63', btn=btn_R4C16, row=4, col=16, sq=4, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef64 = dict(aref='arrRef64', btn=btn_R5C1, row=5, col=1, sq=5, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef65 = dict(aref='arrRef65', btn=btn_R5C2, row=5, col=2, sq=5, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef66 = dict(aref='arrRef66', btn=btn_R5C3, row=5, col=3, sq=5, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef67 = dict(aref='arrRef67', btn=btn_R5C4, row=5, col=4, sq=5, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef68 = dict(aref='arrRef68', btn=btn_R5C5, row=5, col=5, sq=6, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef69 = dict(aref='arrRef69', btn=btn_R5C6, row=5, col=6, sq=6, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef70 = dict(aref='arrRef70', btn=btn_R5C7, row=5, col=7, sq=6, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef71 = dict(aref='arrRef71', btn=btn_R5C8, row=5, col=8, sq=6, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef72 = dict(aref='arrRef72', btn=btn_R5C9, row=5, col=9, sq=7, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef73 = dict(aref='arrRef73', btn=btn_R5C10, row=5, col=10, sq=7, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef74 = dict(aref='arrRef74', btn=btn_R5C11, row=5, col=11, sq=7, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef75 = dict(aref='arrRef75', btn=btn_R5C12, row=5, col=12, sq=7, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef76 = dict(aref='arrRef76', btn=btn_R5C13, row=5, col=13, sq=8, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef77 = dict(aref='arrRef77', btn=btn_R5C14, row=5, col=14, sq=8, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef78 = dict(aref='arrRef78', btn=btn_R5C15, row=5, col=15, sq=8, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef79 = dict(aref='arrRef79', btn=btn_R5C16, row=5, col=16, sq=8, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef80 = dict(aref='arrRef80', btn=btn_R6C1, row=6, col=1, sq=5, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef81 = dict(aref='arrRef81', btn=btn_R6C2, row=6, col=2, sq=5, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef82 = dict(aref='arrRef82', btn=btn_R6C3, row=6, col=3, sq=5, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef83 = dict(aref='arrRef83', btn=btn_R6C4, row=6, col=4, sq=5, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef84 = dict(aref='arrRef84', btn=btn_R6C5, row=6, col=5, sq=6, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef85 = dict(aref='arrRef85', btn=btn_R6C6, row=6, col=6, sq=6, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef86 = dict(aref='arrRef86', btn=btn_R6C7, row=6, col=7, sq=6, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef87 = dict(aref='arrRef87', btn=btn_R6C8, row=6, col=8, sq=6, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef88 = dict(aref='arrRef88', btn=btn_R6C9, row=6, col=9, sq=7, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef89 = dict(aref='arrRef89', btn=btn_R6C10, row=6, col=10, sq=7, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef90 = dict(aref='arrRef90', btn=btn_R6C11, row=6, col=11, sq=7, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef91 = dict(aref='arrRef91', btn=btn_R6C12, row=6, col=12, sq=7, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef92 = dict(aref='arrRef92', btn=btn_R6C13, row=6, col=13, sq=8, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef93 = dict(aref='arrRef93', btn=btn_R6C14, row=6, col=14, sq=8, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef94 = dict(aref='arrRef94', btn=btn_R6C15, row=6, col=15, sq=8, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef95 = dict(aref='arrRef95', btn=btn_R6C16, row=6, col=16, sq=8, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef96 = dict(aref='arrRef96', btn=btn_R7C1, row=7, col=1, sq=5, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef97 = dict(aref='arrRef97', btn=btn_R7C2, row=7, col=2, sq=5, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef98 = dict(aref='arrRef98', btn=btn_R7C3, row=7, col=3, sq=5, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef99 = dict(aref='arrRef99', btn=btn_R7C4, row=7, col=4, sq=5, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef100 = dict(aref='arrRef100', btn=btn_R7C5, row=7, col=5, sq=6, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef101 = dict(aref='arrRef101', btn=btn_R7C6, row=7, col=6, sq=6, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef102 = dict(aref='arrRef102', btn=btn_R7C7, row=7, col=7, sq=6, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef103 = dict(aref='arrRef103', btn=btn_R7C8, row=7, col=8, sq=6, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef104 = dict(aref='arrRef104', btn=btn_R7C9, row=7, col=9, sq=7, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef105 = dict(aref='arrRef105', btn=btn_R7C10, row=7, col=10, sq=7, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef106 = dict(aref='arrRef106', btn=btn_R7C11, row=7, col=11, sq=7, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef107 = dict(aref='arrRef107', btn=btn_R7C12, row=7, col=12, sq=7, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef108 = dict(aref='arrRef108', btn=btn_R7C13, row=7, col=13, sq=8, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef109 = dict(aref='arrRef109', btn=btn_R7C14, row=7, col=14, sq=8, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef110 = dict(aref='arrRef110', btn=btn_R7C15, row=7, col=15, sq=8, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef111 = dict(aref='arrRef111', btn=btn_R7C16, row=7, col=16, sq=8, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef112 = dict(aref='arrRef112', btn=btn_R8C1, row=8, col=1, sq=5, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef113 = dict(aref='arrRef113', btn=btn_R8C2, row=8, col=2, sq=5, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef114 = dict(aref='arrRef114', btn=btn_R8C3, row=8, col=3, sq=5, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef115 = dict(aref='arrRef115', btn=btn_R8C4, row=8, col=4, sq=5, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef116 = dict(aref='arrRef116', btn=btn_R8C5, row=8, col=5, sq=6, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef117 = dict(aref='arrRef117', btn=btn_R8C6, row=8, col=6, sq=6, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef118 = dict(aref='arrRef118', btn=btn_R8C7, row=8, col=7, sq=6, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef119 = dict(aref='arrRef119', btn=btn_R8C8, row=8, col=8, sq=6, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef120 = dict(aref='arrRef120', btn=btn_R8C9, row=8, col=9, sq=7, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef121 = dict(aref='arrRef121', btn=btn_R8C10, row=8, col=10, sq=7, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef122 = dict(aref='arrRef122', btn=btn_R8C11, row=8, col=11, sq=7, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef123 = dict(aref='arrRef123', btn=btn_R8C12, row=8, col=12, sq=7, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef124 = dict(aref='arrRef124', btn=btn_R8C13, row=8, col=13, sq=8, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef125 = dict(aref='arrRef125', btn=btn_R8C14, row=8, col=14, sq=8, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef126 = dict(aref='arrRef126', btn=btn_R8C15, row=8, col=15, sq=8, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef127 = dict(aref='arrRef127', btn=btn_R8C16, row=8, col=16, sq=8, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef128 = dict(aref='arrRef128', btn=btn_R9C1, row=9, col=1, sq=9, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef129 = dict(aref='arrRef129', btn=btn_R9C2, row=9, col=2, sq=9, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef130 = dict(aref='arrRef130', btn=btn_R9C3, row=9, col=3, sq=9, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef131 = dict(aref='arrRef131', btn=btn_R9C4, row=9, col=4, sq=9, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef132 = dict(aref='arrRef132', btn=btn_R9C5, row=9, col=5, sq=10, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef133 = dict(aref='arrRef133', btn=btn_R9C6, row=9, col=6, sq=10, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef134 = dict(aref='arrRef134', btn=btn_R9C7, row=9, col=7, sq=10, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef135 = dict(aref='arrRef135', btn=btn_R9C8, row=9, col=8, sq=10, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef136 = dict(aref='arrRef136', btn=btn_R9C9, row=9, col=9, sq=11, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef137 = dict(aref='arrRef137', btn=btn_R9C10, row=9, col=10, sq=11, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef138 = dict(aref='arrRef138', btn=btn_R9C11, row=9, col=11, sq=11, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef139 = dict(aref='arrRef139', btn=btn_R9C12, row=9, col=12, sq=11, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef140 = dict(aref='arrRef140', btn=btn_R9C13, row=9, col=13, sq=12, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef141 = dict(aref='arrRef141', btn=btn_R9C14, row=9, col=14, sq=12, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef142 = dict(aref='arrRef142', btn=btn_R9C15, row=9, col=15, sq=12, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef143 = dict(aref='arrRef143', btn=btn_R9C16, row=9, col=16, sq=12, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef144 = dict(aref='arrRef144', btn=btn_R10C1, row=10, col=1, sq=9, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef145 = dict(aref='arrRef145', btn=btn_R10C2, row=10, col=2, sq=9, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef146 = dict(aref='arrRef146', btn=btn_R10C3, row=10, col=3, sq=9, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef147 = dict(aref='arrRef147', btn=btn_R10C4, row=10, col=4, sq=9, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef148 = dict(aref='arrRef148', btn=btn_R10C5, row=10, col=5, sq=10, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef149 = dict(aref='arrRef149', btn=btn_R10C6, row=10, col=6, sq=10, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef150 = dict(aref='arrRef150', btn=btn_R10C7, row=10, col=7, sq=10, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef151 = dict(aref='arrRef151', btn=btn_R10C8, row=10, col=8, sq=10, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef152 = dict(aref='arrRef152', btn=btn_R10C9, row=10, col=9, sq=11, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef153 = dict(aref='arrRef153', btn=btn_R10C10, row=10, col=10, sq=11, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef154 = dict(aref='arrRef154', btn=btn_R10C11, row=10, col=11, sq=11, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef155 = dict(aref='arrRef155', btn=btn_R10C12, row=10, col=12, sq=11, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef156 = dict(aref='arrRef156', btn=btn_R10C13, row=10, col=13, sq=12, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef157 = dict(aref='arrRef157', btn=btn_R10C14, row=10, col=14, sq=12, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef158 = dict(aref='arrRef158', btn=btn_R10C15, row=10, col=15, sq=12, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef159 = dict(aref='arrRef159', btn=btn_R10C16, row=10, col=16, sq=12, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef160 = dict(aref='arrRef160', btn=btn_R11C1, row=11, col=1, sq=9, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef161 = dict(aref='arrRef161', btn=btn_R11C2, row=11, col=2, sq=9, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef162 = dict(aref='arrRef162', btn=btn_R11C3, row=11, col=3, sq=9, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef163 = dict(aref='arrRef163', btn=btn_R11C4, row=11, col=4, sq=9, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef164 = dict(aref='arrRef164', btn=btn_R11C5, row=11, col=5, sq=10, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef165 = dict(aref='arrRef165', btn=btn_R11C6, row=11, col=6, sq=10, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef166 = dict(aref='arrRef166', btn=btn_R11C7, row=11, col=7, sq=10, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef167 = dict(aref='arrRef167', btn=btn_R11C8, row=11, col=8, sq=10, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef168 = dict(aref='arrRef168', btn=btn_R11C9, row=11, col=9, sq=11, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef169 = dict(aref='arrRef169', btn=btn_R11C10, row=11, col=10, sq=11, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef170 = dict(aref='arrRef170', btn=btn_R11C11, row=11, col=11, sq=11, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef171 = dict(aref='arrRef171', btn=btn_R11C12, row=11, col=12, sq=11, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef172 = dict(aref='arrRef172', btn=btn_R11C13, row=11, col=13, sq=12, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef173 = dict(aref='arrRef173', btn=btn_R11C14, row=11, col=14, sq=12, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef174 = dict(aref='arrRef174', btn=btn_R11C15, row=11, col=15, sq=12, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef175 = dict(aref='arrRef175', btn=btn_R11C16, row=11, col=16, sq=12, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef176 = dict(aref='arrRef176', btn=btn_R12C1, row=12, col=1, sq=9, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef177 = dict(aref='arrRef177', btn=btn_R12C2, row=12, col=2, sq=9, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef178 = dict(aref='arrRef178', btn=btn_R12C3, row=12, col=3, sq=9, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef179 = dict(aref='arrRef179', btn=btn_R12C4, row=12, col=4, sq=9, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef180 = dict(aref='arrRef180', btn=btn_R12C5, row=12, col=5, sq=10, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef181 = dict(aref='arrRef181', btn=btn_R12C6, row=12, col=6, sq=10, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef182 = dict(aref='arrRef182', btn=btn_R12C7, row=12, col=7, sq=10, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef183 = dict(aref='arrRef183', btn=btn_R12C8, row=12, col=8, sq=10, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef184 = dict(aref='arrRef184', btn=btn_R12C9, row=12, col=9, sq=11, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef185 = dict(aref='arrRef185', btn=btn_R12C10, row=12, col=10, sq=11, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef186 = dict(aref='arrRef186', btn=btn_R12C11, row=12, col=11, sq=11, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef187 = dict(aref='arrRef187', btn=btn_R12C12, row=12, col=12, sq=11, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef188 = dict(aref='arrRef188', btn=btn_R12C13, row=12, col=13, sq=12, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef189 = dict(aref='arrRef189', btn=btn_R12C14, row=12, col=14, sq=12, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef190 = dict(aref='arrRef190', btn=btn_R12C15, row=12, col=15, sq=12, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef191 = dict(aref='arrRef191', btn=btn_R12C16, row=12, col=16, sq=12, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef192 = dict(aref='arrRef192', btn=btn_R13C1, row=13, col=1, sq=13, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef193 = dict(aref='arrRef193', btn=btn_R13C2, row=13, col=2, sq=13, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef194 = dict(aref='arrRef194', btn=btn_R13C3, row=13, col=3, sq=13, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef195 = dict(aref='arrRef195', btn=btn_R13C4, row=13, col=4, sq=13, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef196 = dict(aref='arrRef196', btn=btn_R13C5, row=13, col=5, sq=14, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef197 = dict(aref='arrRef197', btn=btn_R13C6, row=13, col=6, sq=14, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef198 = dict(aref='arrRef198', btn=btn_R13C7, row=13, col=7, sq=14, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef199 = dict(aref='arrRef199', btn=btn_R13C8, row=13, col=8, sq=14, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef200 = dict(aref='arrRef200', btn=btn_R13C9, row=13, col=9, sq=15, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef201 = dict(aref='arrRef201', btn=btn_R13C10, row=13, col=10, sq=15, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef202 = dict(aref='arrRef202', btn=btn_R13C11, row=13, col=11, sq=15, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef203 = dict(aref='arrRef203', btn=btn_R13C12, row=13, col=12, sq=15, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef204 = dict(aref='arrRef204', btn=btn_R13C13, row=13, col=13, sq=16, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef205 = dict(aref='arrRef205', btn=btn_R13C14, row=13, col=14, sq=16, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef206 = dict(aref='arrRef206', btn=btn_R13C15, row=13, col=15, sq=16, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef207 = dict(aref='arrRef207', btn=btn_R13C16, row=13, col=16, sq=16, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef208 = dict(aref='arrRef208', btn=btn_R14C1, row=14, col=1, sq=13, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef209 = dict(aref='arrRef209', btn=btn_R14C2, row=14, col=2, sq=13, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef210 = dict(aref='arrRef210', btn=btn_R14C3, row=14, col=3, sq=13, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef211 = dict(aref='arrRef211', btn=btn_R14C4, row=14, col=4, sq=13, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef212 = dict(aref='arrRef212', btn=btn_R14C5, row=14, col=5, sq=14, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef213 = dict(aref='arrRef213', btn=btn_R14C6, row=14, col=6, sq=14, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef214 = dict(aref='arrRef214', btn=btn_R14C7, row=14, col=7, sq=14, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef215 = dict(aref='arrRef215', btn=btn_R14C8, row=14, col=8, sq=14, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef216 = dict(aref='arrRef216', btn=btn_R14C9, row=14, col=9, sq=15, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef217 = dict(aref='arrRef217', btn=btn_R14C10, row=14, col=10, sq=15, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef218 = dict(aref='arrRef218', btn=btn_R14C11, row=14, col=11, sq=15, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef219 = dict(aref='arrRef219', btn=btn_R14C12, row=14, col=12, sq=15, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef220 = dict(aref='arrRef220', btn=btn_R14C13, row=14, col=13, sq=16, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef221 = dict(aref='arrRef221', btn=btn_R14C14, row=14, col=14, sq=16, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef222 = dict(aref='arrRef222', btn=btn_R14C15, row=14, col=15, sq=16, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef223 = dict(aref='arrRef223', btn=btn_R14C16, row=14, col=16, sq=16, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef224 = dict(aref='arrRef224', btn=btn_R15C1, row=15, col=1, sq=13, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef225 = dict(aref='arrRef225', btn=btn_R15C2, row=15, col=2, sq=13, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef226 = dict(aref='arrRef226', btn=btn_R15C3, row=15, col=3, sq=13, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef227 = dict(aref='arrRef227', btn=btn_R15C4, row=15, col=4, sq=13, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef228 = dict(aref='arrRef228', btn=btn_R15C5, row=15, col=5, sq=14, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef229 = dict(aref='arrRef229', btn=btn_R15C6, row=15, col=6, sq=14, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef230 = dict(aref='arrRef230', btn=btn_R15C7, row=15, col=7, sq=14, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef231 = dict(aref='arrRef231', btn=btn_R15C8, row=15, col=8, sq=14, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef232 = dict(aref='arrRef232', btn=btn_R15C9, row=15, col=9, sq=15, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef233 = dict(aref='arrRef233', btn=btn_R15C10, row=15, col=10, sq=15, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef234 = dict(aref='arrRef234', btn=btn_R15C11, row=15, col=11, sq=15, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef235 = dict(aref='arrRef235', btn=btn_R15C12, row=15, col=12, sq=15, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef236 = dict(aref='arrRef236', btn=btn_R15C13, row=15, col=13, sq=16, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef237 = dict(aref='arrRef237', btn=btn_R15C14, row=15, col=14, sq=16, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef238 = dict(aref='arrRef238', btn=btn_R15C15, row=15, col=15, sq=16, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef239 = dict(aref='arrRef239', btn=btn_R15C16, row=15, col=16, sq=16, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef240 = dict(aref='arrRef240', btn=btn_R16C1, row=16, col=1, sq=13, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef241 = dict(aref='arrRef241', btn=btn_R16C2, row=16, col=2, sq=13, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef242 = dict(aref='arrRef242', btn=btn_R16C3, row=16, col=3, sq=13, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef243 = dict(aref='arrRef243', btn=btn_R16C4, row=16, col=4, sq=13, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef244 = dict(aref='arrRef244', btn=btn_R16C5, row=16, col=5, sq=14, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef245 = dict(aref='arrRef245', btn=btn_R16C6, row=16, col=6, sq=14, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef246 = dict(aref='arrRef246', btn=btn_R16C7, row=16, col=7, sq=14, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef247 = dict(aref='arrRef247', btn=btn_R16C8, row=16, col=8, sq=14, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef248 = dict(aref='arrRef248', btn=btn_R16C9, row=16, col=9, sq=15, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef249 = dict(aref='arrRef249', btn=btn_R16C10, row=16, col=10, sq=15, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef250 = dict(aref='arrRef250', btn=btn_R16C11, row=16, col=11, sq=15, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef251 = dict(aref='arrRef251', btn=btn_R16C12, row=16, col=12, sq=15, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef252 = dict(aref='arrRef252', btn=btn_R16C13, row=16, col=13, sq=16, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef253 = dict(aref='arrRef253', btn=btn_R16C14, row=16, col=14, sq=16, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef254 = dict(aref='arrRef254', btn=btn_R16C15, row=16, col=15, sq=16, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef255 = dict(aref='arrRef255', btn=btn_R16C16, row=16, col=16, sq=16, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")

arrRefs_List = [arrRef0, arrRef1, arrRef2, arrRef3, arrRef4, arrRef5, arrRef6, arrRef7,
                arrRef8, arrRef9, arrRef10, arrRef11, arrRef12, arrRef13, arrRef14,
                arrRef15, arrRef16, arrRef17, arrRef18, arrRef19, arrRef20, arrRef21,
                arrRef22, arrRef23, arrRef24, arrRef25, arrRef26, arrRef27, arrRef28,
                arrRef29, arrRef30, arrRef31, arrRef32, arrRef33, arrRef34, arrRef35,
                arrRef36, arrRef37, arrRef38, arrRef39, arrRef40, arrRef41, arrRef42,
                arrRef43, arrRef44, arrRef45, arrRef46, arrRef47, arrRef48, arrRef49,
                arrRef50, arrRef51, arrRef52, arrRef53, arrRef54, arrRef55, arrRef56,
                arrRef57, arrRef58, arrRef59, arrRef60, arrRef61, arrRef62, arrRef63,
                arrRef64, arrRef65, arrRef66, arrRef67, arrRef68, arrRef69, arrRef70,
                arrRef71, arrRef72, arrRef73, arrRef74, arrRef75, arrRef76, arrRef77,
                arrRef78, arrRef79, arrRef80, arrRef81, arrRef82, arrRef83, arrRef84,
                arrRef85, arrRef86, arrRef87, arrRef88, arrRef89, arrRef90, arrRef91,
                arrRef92, arrRef93, arrRef94, arrRef95, arrRef96, arrRef97, arrRef98,
                arrRef99, arrRef100, arrRef101, arrRef102, arrRef103, arrRef104, arrRef105,
                arrRef106, arrRef107, arrRef108, arrRef109, arrRef110, arrRef111, arrRef112,
                arrRef113, arrRef114, arrRef115, arrRef116, arrRef117, arrRef118, arrRef119,
                arrRef120, arrRef121, arrRef122, arrRef123, arrRef124, arrRef125, arrRef126,
                arrRef127, arrRef128, arrRef129, arrRef130, arrRef131, arrRef132, arrRef133,
                arrRef134, arrRef135, arrRef136, arrRef137, arrRef138, arrRef139, arrRef140,
                arrRef141, arrRef142, arrRef143, arrRef144, arrRef145, arrRef146, arrRef147,
                arrRef148, arrRef149, arrRef150, arrRef151, arrRef152, arrRef153, arrRef154,
                arrRef155, arrRef156, arrRef157, arrRef158, arrRef159, arrRef160, arrRef161,
                arrRef162, arrRef163, arrRef164, arrRef165, arrRef166, arrRef167, arrRef168,
                arrRef169, arrRef170, arrRef171, arrRef172, arrRef173, arrRef174, arrRef175,
                arrRef176, arrRef177, arrRef178, arrRef179, arrRef180, arrRef181, arrRef182,
                arrRef183, arrRef184, arrRef185, arrRef186, arrRef187, arrRef188, arrRef189,
                arrRef190, arrRef191, arrRef192, arrRef193, arrRef194, arrRef195, arrRef196,
                arrRef197, arrRef198, arrRef199, arrRef200, arrRef201, arrRef202, arrRef203,
                arrRef204, arrRef205, arrRef206, arrRef207, arrRef208, arrRef209, arrRef210,
                arrRef211, arrRef212, arrRef213, arrRef214, arrRef215, arrRef216, arrRef217,
                arrRef218, arrRef219, arrRef220, arrRef221, arrRef222, arrRef223, arrRef224,
                arrRef225, arrRef226, arrRef227, arrRef228, arrRef229, arrRef230, arrRef231,
                arrRef232, arrRef233, arrRef234, arrRef235, arrRef236, arrRef237, arrRef238,
                arrRef239, arrRef240, arrRef241, arrRef242, arrRef243, arrRef244, arrRef245,
                arrRef246, arrRef247, arrRef248, arrRef249, arrRef250, arrRef251, arrRef252,
                arrRef253, arrRef254, arrRef255]

btn_dict = {'btn_R1C1': 'arrRef0', 'btn_R1C2': 'arrRef1', 'btn_R1C3': 'arrRef2', 'btn_R1C4': 'arrRef3',
            'btn_R1C5': 'arrRef4', 'btn_R1C6': 'arrRef5', 'btn_R1C7': 'arrRef6', 'btn_R1C8': 'arrRef7',
            'btn_R1C9': 'arrRef8', 'btn_R1C10': 'arrRef9', 'btn_R1C11': 'arrRef10', 'btn_R1C12': 'arrRef11',
            'btn_R1C13': 'arrRef12', 'btn_R1C14': 'arrRef13', 'btn_R1C15': 'arrRef14', 'btn_R1C16': 'arrRef15',
            'btn_R2C1': 'arrRef16', 'btn_R2C2': 'arrRef17', 'btn_R2C3': 'arrRef18', 'btn_R2C4': 'arrRef19',
            'btn_R2C5': 'arrRef20', 'btn_R2C6': 'arrRef21', 'btn_R2C7': 'arrRef22', 'btn_R2C8': 'arrRef23',
            'btn_R2C9': 'arrRef24', 'btn_R2C10': 'arrRef25', 'btn_R2C11': 'arrRef26', 'btn_R2C12': 'arrRef27',
            'btn_R2C13': 'arrRef28', 'btn_R2C14': 'arrRef29', 'btn_R2C15': 'arrRef30', 'btn_R2C16': 'arrRef31',
            'btn_R3C1': 'arrRef32', 'btn_R3C2': 'arrRef33', 'btn_R3C3': 'arrRef34', 'btn_R3C4': 'arrRef35',
            'btn_R3C5': 'arrRef36', 'btn_R3C6': 'arrRef37', 'btn_R3C7': 'arrRef38', 'btn_R3C8': 'arrRef39',
            'btn_R3C9': 'arrRef40', 'btn_R3C10': 'arrRef41', 'btn_R3C11': 'arrRef42', 'btn_R3C12': 'arrRef43',
            'btn_R3C13': 'arrRef44', 'btn_R3C14': 'arrRef45', 'btn_R3C15': 'arrRef46', 'btn_R3C16': 'arrRef47',
            'btn_R4C1': 'arrRef48', 'btn_R4C2': 'arrRef49', 'btn_R4C3': 'arrRef50', 'btn_R4C4': 'arrRef51',
            'btn_R4C5': 'arrRef52', 'btn_R4C6': 'arrRef53', 'btn_R4C7': 'arrRef54', 'btn_R4C8': 'arrRef55',
            'btn_R4C9': 'arrRef56', 'btn_R4C10': 'arrRef57', 'btn_R4C11': 'arrRef58', 'btn_R4C12': 'arrRef59',
            'btn_R4C13': 'arrRef60', 'btn_R4C14': 'arrRef61', 'btn_R4C15': 'arrRef62', 'btn_R4C16': 'arrRef63',
            'btn_R5C1': 'arrRef64', 'btn_R5C2': 'arrRef65', 'btn_R5C3': 'arrRef66', 'btn_R5C4': 'arrRef67',
            'btn_R5C5': 'arrRef68', 'btn_R5C6': 'arrRef69', 'btn_R5C7': 'arrRef70', 'btn_R5C8': 'arrRef71',
            'btn_R5C9': 'arrRef72', 'btn_R5C10': 'arrRef73', 'btn_R5C11': 'arrRef74', 'btn_R5C12': 'arrRef75',
            'btn_R5C13': 'arrRef76', 'btn_R5C14': 'arrRef77', 'btn_R5C15': 'arrRef78', 'btn_R5C16': 'arrRef79',
            'btn_R6C1': 'arrRef80', 'btn_R6C2': 'arrRef81', 'btn_R6C3': 'arrRef82', 'btn_R6C4': 'arrRef83',
            'btn_R6C5': 'arrRef84', 'btn_R6C6': 'arrRef85', 'btn_R6C7': 'arrRef86', 'btn_R6C8': 'arrRef87',
            'btn_R6C9': 'arrRef88', 'btn_R6C10': 'arrRef89', 'btn_R6C11': 'arrRef90', 'btn_R6C12': 'arrRef91',
            'btn_R6C13': 'arrRef92', 'btn_R6C14': 'arrRef93', 'btn_R6C15': 'arrRef94', 'btn_R6C16': 'arrRef95',
            'btn_R7C1': 'arrRef96', 'btn_R7C2': 'arrRef97', 'btn_R7C3': 'arrRef98', 'btn_R7C4': 'arrRef99',
            'btn_R7C5': 'arrRef100', 'btn_R7C6': 'arrRef101', 'btn_R7C7': 'arrRef102', 'btn_R7C8': 'arrRef103',
            'btn_R7C9': 'arrRef104', 'btn_R7C10': 'arrRef105', 'btn_R7C11': 'arrRef106', 'btn_R7C12': 'arrRef107',
            'btn_R7C13': 'arrRef108', 'btn_R7C14': 'arrRef109', 'btn_R7C15': 'arrRef110', 'btn_R7C16': 'arrRef111',
            'btn_R8C1': 'arrRef112', 'btn_R8C2': 'arrRef113', 'btn_R8C3': 'arrRef114', 'btn_R8C4': 'arrRef115',
            'btn_R8C5': 'arrRef116', 'btn_R8C6': 'arrRef117', 'btn_R8C7': 'arrRef118', 'btn_R8C8': 'arrRef119',
            'btn_R8C9': 'arrRef120', 'btn_R8C10': 'arrRef121', 'btn_R8C11': 'arrRef122', 'btn_R8C12': 'arrRef123',
            'btn_R8C13': 'arrRef124', 'btn_R8C14': 'arrRef125', 'btn_R8C15': 'arrRef126', 'btn_R8C16': 'arrRef127',
            'btn_R9C1': 'arrRef128', 'btn_R9C2': 'arrRef129', 'btn_R9C3': 'arrRef130', 'btn_R9C4': 'arrRef131',
            'btn_R9C5': 'arrRef132', 'btn_R9C6': 'arrRef133', 'btn_R9C7': 'arrRef134', 'btn_R9C8': 'arrRef135',
            'btn_R9C9': 'arrRef136', 'btn_R9C10': 'arrRef137', 'btn_R9C11': 'arrRef138', 'btn_R9C12': 'arrRef139',
            'btn_R9C13': 'arrRef140', 'btn_R9C14': 'arrRef141', 'btn_R9C15': 'arrRef142', 'btn_R9C16': 'arrRef143',
            'btn_R10C1': 'arrRef144', 'btn_R10C2': 'arrRef145', 'btn_R10C3': 'arrRef146', 'btn_R10C4': 'arrRef147',
            'btn_R10C5': 'arrRef148', 'btn_R10C6': 'arrRef149', 'btn_R10C7': 'arrRef150', 'btn_R10C8': 'arrRef151',
            'btn_R10C9': 'arrRef152', 'btn_R10C10': 'arrRef153', 'btn_R10C11': 'arrRef154', 'btn_R10C12': 'arrRef155',
            'btn_R10C13': 'arrRef156', 'btn_R10C14': 'arrRef157', 'btn_R10C15': 'arrRef158', 'btn_R10C16': 'arrRef159',
            'btn_R11C1': 'arrRef160', 'btn_R11C2': 'arrRef161', 'btn_R11C3': 'arrRef162', 'btn_R11C4': 'arrRef163',
            'btn_R11C5': 'arrRef164', 'btn_R11C6': 'arrRef165', 'btn_R11C7': 'arrRef166', 'btn_R11C8': 'arrRef167',
            'btn_R11C9': 'arrRef168', 'btn_R11C10': 'arrRef169', 'btn_R11C11': 'arrRef170', 'btn_R11C12': 'arrRef171',
            'btn_R11C13': 'arrRef172', 'btn_R11C14': 'arrRef173', 'btn_R11C15': 'arrRef174', 'btn_R11C16': 'arrRef175',
            'btn_R12C1': 'arrRef176', 'btn_R12C2': 'arrRef177', 'btn_R12C3': 'arrRef178', 'btn_R12C4': 'arrRef179',
            'btn_R12C5': 'arrRef180', 'btn_R12C6': 'arrRef181', 'btn_R12C7': 'arrRef182', 'btn_R12C8': 'arrRef183',
            'btn_R12C9': 'arrRef184', 'btn_R12C10': 'arrRef185', 'btn_R12C11': 'arrRef186', 'btn_R12C12': 'arrRef187',
            'btn_R12C13': 'arrRef188', 'btn_R12C14': 'arrRef189', 'btn_R12C15': 'arrRef190', 'btn_R12C16': 'arrRef191',
            'btn_R13C1': 'arrRef192', 'btn_R13C2': 'arrRef193', 'btn_R13C3': 'arrRef194', 'btn_R13C4': 'arrRef195',
            'btn_R13C5': 'arrRef196', 'btn_R13C6': 'arrRef197', 'btn_R13C7': 'arrRef198', 'btn_R13C8': 'arrRef199',
            'btn_R13C9': 'arrRef200', 'btn_R13C10': 'arrRef201', 'btn_R13C11': 'arrRef202', 'btn_R13C12': 'arrRef203',
            'btn_R13C13': 'arrRef204', 'btn_R13C14': 'arrRef205', 'btn_R13C15': 'arrRef206', 'btn_R13C16': 'arrRef207',
            'btn_R14C1': 'arrRef208', 'btn_R14C2': 'arrRef209', 'btn_R14C3': 'arrRef210', 'btn_R14C4': 'arrRef211',
            'btn_R14C5': 'arrRef212', 'btn_R14C6': 'arrRef213', 'btn_R14C7': 'arrRef214', 'btn_R14C8': 'arrRef215',
            'btn_R14C9': 'arrRef216', 'btn_R14C10': 'arrRef217', 'btn_R14C11': 'arrRef218', 'btn_R14C12': 'arrRef219',
            'btn_R14C13': 'arrRef220', 'btn_R14C14': 'arrRef221', 'btn_R14C15': 'arrRef222', 'btn_R14C16': 'arrRef223',
            'btn_R15C1': 'arrRef224', 'btn_R15C2': 'arrRef225', 'btn_R15C3': 'arrRef226', 'btn_R15C4': 'arrRef227',
            'btn_R15C5': 'arrRef228', 'btn_R15C6': 'arrRef229', 'btn_R15C7': 'arrRef230', 'btn_R15C8': 'arrRef231',
            'btn_R15C9': 'arrRef232', 'btn_R15C10': 'arrRef233', 'btn_R15C11': 'arrRef234', 'btn_R15C12': 'arrRef235',
            'btn_R15C13': 'arrRef236', 'btn_R15C14': 'arrRef237', 'btn_R15C15': 'arrRef238', 'btn_R15C16': 'arrRef239',
            'btn_R16C1': 'arrRef240', 'btn_R16C2': 'arrRef241', 'btn_R16C3': 'arrRef242', 'btn_R16C4': 'arrRef243',
            'btn_R16C5': 'arrRef244', 'btn_R16C6': 'arrRef245', 'btn_R16C7': 'arrRef246', 'btn_R16C8': 'arrRef247',
            'btn_R16C9': 'arrRef248', 'btn_R16C10': 'arrRef249', 'btn_R16C11': 'arrRef250', 'btn_R16C12': 'arrRef251',
            'btn_R16C13': 'arrRef252', 'btn_R16C14': 'arrRef253', 'btn_R16C15': 'arrRef254', 'btn_R16C16': 'arrRef255',
            }
not_done_arefs = arrRefs_List.copy()

# new_list = lis.copy()
# "eci_1_d=dict(eci='eci_1', formula= ""
# eci_1_d=dict(eci='eci_1'
# "compound_names_dict={'aluminum_carbide': 'Al4C3', 'aluminum_chloride': 'AlCl3', 'air': 'Ar2He2Kr2Ne2Xe2Rn2',
if __name__ == '__main__':
    root.mainloop()
