import sys
# import pickle
import json
import ctypes
from tkinter import *  # get widget classes
# from tkinter import Combobox, Entry, Label, font
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
root.geometry("1200x800")
titlefont = ('Ariel', 12, 'bold')
labelfont = ('Ariel', 7)  # , 'bold')
buttonfont = ('Ariel', 10)  # , 'bold')
entryfont = ('Ariel', 7)  # , 'bold')
wid = 4
wid6 = 6
hit = 3

currentRow = 0
currentColumn = 0
currentSquare = 0
currentNumber = 0
currentNums = ""
Hints = ""
StartingString = "0123456789ABCDEF"
bRemoveANumberFromACell = "False"
bAutoComplete = False
D = 0
R = 0
NullValue = "Null"
arrDone = dict(d0=0, d1=0, d2=0)
arrDone0 = dict(d0=0, d1=0, d2=0)
arrDone1 = dict(d0=0, d1=0, d2=0)
arrDone2 = dict(d0=0, d1=0, d2=0)
bShowRemainders = False
bInitialShowRemainders = False
arrValues = dict(d0=0, d1=0, d2=0)
arrValues0 = dict(d0=0, d1=0, d2=0)
arrValues1 = dict(d0=0, d1=0, d2=0)
arrValues2 = dict(d0=0, d1=0, d2=0)

# arrRef00 = 1 # refs are for row, col, square
# btn_R1C1.config(font=buttonfont, width=wid4, height=hit, fg="red")
# numbers = StartingString.fill(nums, width=4)
arrRef0 = dict(btn='btn_R1C1', row=1, col=1, sq=1, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef1 = dict(btn='btn_R1C2', row=1, col=2, sq=1, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef2 = dict(btn='btn_R1C3', row=1, col=3, sq=1, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef3 = dict(btn='btn_R1C4', row=1, col=4, sq=1, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef4 = dict(btn='btn_R1C5', row=1, col=5, sq=2, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef5 = dict(btn='btn_R1C6', row=1, col=6, sq=2, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef6 = dict(btn='btn_R1C7', row=1, col=7, sq=2, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef7 = dict(btn='btn_R1C8', row=1, col=8, sq=2, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef8 = dict(btn='btn_R1C9', row=1, col=9, sq=3, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef9 = dict(btn='btn_R1C10', row=1, col=10, sq=3, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef10 = dict(btn='btn_R1C11', row=1, col=11, sq=3, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef11 = dict(btn='btn_R1C12', row=1, col=12, sq=3, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef12 = dict(btn='btn_R1C13', row=1, col=13, sq=4, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef13 = dict(btn='btn_R1C14', row=1, col=14, sq=4, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef14 = dict(btn='btn_R1C15', row=1, col=15, sq=4, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef15 = dict(btn='btn_R1C16', row=1, col=16, sq=4, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef16 = dict(btn='btn_R2C1', row=2, col=1, sq=1, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef17 = dict(btn='btn_R2C2', row=2, col=2, sq=1, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef18 = dict(btn='btn_R2C3', row=2, col=3, sq=1, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef19 = dict(btn='btn_R2C4', row=2, col=4, sq=1, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef20 = dict(btn='btn_R2C5', row=2, col=5, sq=2, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef21 = dict(btn='btn_R2C6', row=2, col=6, sq=2, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef22 = dict(btn='btn_R2C7', row=2, col=7, sq=2, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef23 = dict(btn='btn_R2C8', row=2, col=8, sq=2, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef24 = dict(btn='btn_R2C9', row=2, col=9, sq=3, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef25 = dict(btn='btn_R2C10', row=2, col=10, sq=3, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef26 = dict(btn='btn_R2C11', row=2, col=11, sq=3, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef27 = dict(btn='btn_R2C12', row=2, col=12, sq=3, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef28 = dict(btn='btn_R2C13', row=2, col=13, sq=4, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef29 = dict(btn='btn_R2C14', row=2, col=14, sq=4, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef30 = dict(btn='btn_R2C15', row=2, col=15, sq=4, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef31 = dict(btn='btn_R2C16', row=2, col=16, sq=4, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef32 = dict(btn='btn_R3C1', row=3, col=1, sq=1, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef33 = dict(btn='btn_R3C2', row=3, col=2, sq=1, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef34 = dict(btn='btn_R3C3', row=3, col=3, sq=1, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef35 = dict(btn='btn_R3C4', row=3, col=4, sq=1, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef36 = dict(btn='btn_R3C5', row=3, col=5, sq=2, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef37 = dict(btn='btn_R3C6', row=3, col=6, sq=2, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef38 = dict(btn='btn_R3C7', row=3, col=7, sq=2, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef39 = dict(btn='btn_R3C8', row=3, col=8, sq=2, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef40 = dict(btn='btn_R3C9', row=3, col=9, sq=3, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef41 = dict(btn='btn_R3C10', row=3, col=10, sq=3, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef42 = dict(btn='btn_R3C11', row=3, col=11, sq=3, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef43 = dict(btn='btn_R3C12', row=3, col=12, sq=3, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef44 = dict(btn='btn_R3C13', row=3, col=13, sq=4, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef45 = dict(btn='btn_R3C14', row=3, col=14, sq=4, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef46 = dict(btn='btn_R3C15', row=3, col=15, sq=4, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef47 = dict(btn='btn_R3C16', row=3, col=16, sq=4, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef48 = dict(btn='btn_R4C1', row=4, col=1, sq=1, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef49 = dict(btn='btn_R4C2', row=4, col=2, sq=1, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef50 = dict(btn='btn_R4C3', row=4, col=3, sq=1, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef51 = dict(btn='btn_R4C4', row=4, col=4, sq=1, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef52 = dict(btn='btn_R4C5', row=4, col=5, sq=2, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef53 = dict(btn='btn_R4C6', row=4, col=6, sq=2, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef54 = dict(btn='btn_R4C7', row=4, col=7, sq=2, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef55 = dict(btn='btn_R4C8', row=4, col=8, sq=2, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef56 = dict(btn='btn_R4C9', row=4, col=9, sq=3, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef57 = dict(btn='btn_R4C10', row=4, col=10, sq=3, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef58 = dict(btn='btn_R4C11', row=4, col=11, sq=3, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef59 = dict(btn='btn_R4C12', row=4, col=12, sq=3, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef60 = dict(btn='btn_R4C13', row=4, col=13, sq=4, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef61 = dict(btn='btn_R4C14', row=4, col=14, sq=4, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef62 = dict(btn='btn_R4C15', row=4, col=15, sq=4, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef63 = dict(btn='btn_R4C16', row=4, col=16, sq=4, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef64 = dict(btn='btn_R5C1', row=5, col=1, sq=5, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef65 = dict(btn='btn_R5C2', row=5, col=2, sq=5, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef66 = dict(btn='btn_R5C3', row=5, col=3, sq=5, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef67 = dict(btn='btn_R5C4', row=5, col=4, sq=5, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef68 = dict(btn='btn_R5C5', row=5, col=5, sq=6, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef69 = dict(btn='btn_R5C6', row=5, col=6, sq=6, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef70 = dict(btn='btn_R5C7', row=5, col=7, sq=6, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef71 = dict(btn='btn_R5C8', row=5, col=8, sq=6, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef72 = dict(btn='btn_R5C9', row=5, col=9, sq=7, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef73 = dict(btn='btn_R5C10', row=5, col=10, sq=7, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef74 = dict(btn='btn_R5C11', row=5, col=11, sq=7, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef75 = dict(btn='btn_R5C12', row=5, col=12, sq=7, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef76 = dict(btn='btn_R5C13', row=5, col=13, sq=8, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef77 = dict(btn='btn_R5C14', row=5, col=14, sq=8, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef78 = dict(btn='btn_R5C15', row=5, col=15, sq=8, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef79 = dict(btn='btn_R5C16', row=5, col=16, sq=8, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef80 = dict(btn='btn_R6C1', row=6, col=1, sq=5, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef81 = dict(btn='btn_R6C2', row=6, col=2, sq=5, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef82 = dict(btn='btn_R6C3', row=6, col=3, sq=5, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef83 = dict(btn='btn_R6C4', row=6, col=4, sq=5, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef84 = dict(btn='btn_R6C5', row=6, col=5, sq=6, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef85 = dict(btn='btn_R6C6', row=6, col=6, sq=6, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef86 = dict(btn='btn_R6C7', row=6, col=7, sq=6, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef87 = dict(btn='btn_R6C8', row=6, col=8, sq=6, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef88 = dict(btn='btn_R6C9', row=6, col=9, sq=7, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef89 = dict(btn='btn_R6C10', row=6, col=10, sq=7, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef90 = dict(btn='btn_R6C11', row=6, col=11, sq=7, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef91 = dict(btn='btn_R6C12', row=6, col=12, sq=7, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef92 = dict(btn='btn_R6C13', row=6, col=13, sq=8, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef93 = dict(btn='btn_R6C14', row=6, col=14, sq=8, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef94 = dict(btn='btn_R6C15', row=6, col=15, sq=8, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef95 = dict(btn='btn_R6C16', row=6, col=16, sq=8, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef96 = dict(btn='btn_R7C1', row=7, col=1, sq=5, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef97 = dict(btn='btn_R7C2', row=7, col=2, sq=5, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef98 = dict(btn='btn_R7C3', row=7, col=3, sq=5, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef99 = dict(btn='btn_R7C4', row=7, col=4, sq=5, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef100 = dict(btn='btn_R7C5', row=7, col=5, sq=6, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef101 = dict(btn='btn_R7C6', row=7, col=6, sq=6, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef102 = dict(btn='btn_R7C7', row=7, col=7, sq=6, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef103 = dict(btn='btn_R7C8', row=7, col=8, sq=6, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef104 = dict(btn='btn_R7C9', row=7, col=9, sq=7, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef105 = dict(btn='btn_R7C10', row=7, col=10, sq=7, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef106 = dict(btn='btn_R7C11', row=7, col=11, sq=7, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef107 = dict(btn='btn_R7C12', row=7, col=12, sq=7, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef108 = dict(btn='btn_R7C13', row=7, col=13, sq=8, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef109 = dict(btn='btn_R7C14', row=7, col=14, sq=8, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef110 = dict(btn='btn_R7C15', row=7, col=15, sq=8, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef111 = dict(btn='btn_R7C16', row=7, col=16, sq=8, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef112 = dict(btn='btn_R8C1', row=8, col=1, sq=5, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef113 = dict(btn='btn_R8C2', row=8, col=2, sq=5, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef114 = dict(btn='btn_R8C3', row=8, col=3, sq=5, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef115 = dict(btn='btn_R8C4', row=8, col=4, sq=5, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef116 = dict(btn='btn_R8C5', row=8, col=5, sq=6, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef117 = dict(btn='btn_R8C6', row=8, col=6, sq=6, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef118 = dict(btn='btn_R8C7', row=8, col=7, sq=6, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef119 = dict(btn='btn_R8C8', row=8, col=8, sq=6, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef120 = dict(btn='btn_R8C9', row=8, col=9, sq=7, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef121 = dict(btn='btn_R8C10', row=8, col=10, sq=7, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef122 = dict(btn='btn_R8C11', row=8, col=11, sq=7, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef123 = dict(btn='btn_R8C12', row=8, col=12, sq=7, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef124 = dict(btn='btn_R8C13', row=8, col=13, sq=8, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef125 = dict(btn='btn_R8C14', row=8, col=14, sq=8, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef126 = dict(btn='btn_R8C15', row=8, col=15, sq=8, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef127 = dict(btn='btn_R8C16', row=8, col=16, sq=8, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef128 = dict(btn='btn_R9C1', row=9, col=1, sq=9, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef129 = dict(btn='btn_R9C2', row=9, col=2, sq=9, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef130 = dict(btn='btn_R9C3', row=9, col=3, sq=9, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef131 = dict(btn='btn_R9C4', row=9, col=4, sq=9, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef132 = dict(btn='btn_R9C5', row=9, col=5, sq=10, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef133 = dict(btn='btn_R9C6', row=9, col=6, sq=10, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef134 = dict(btn='btn_R9C7', row=9, col=7, sq=10, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef135 = dict(btn='btn_R9C8', row=9, col=8, sq=10, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef136 = dict(btn='btn_R9C9', row=9, col=9, sq=11, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef137 = dict(btn='btn_R9C10', row=9, col=10, sq=11, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef138 = dict(btn='btn_R9C11', row=9, col=11, sq=11, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef139 = dict(btn='btn_R9C12', row=9, col=12, sq=11, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef140 = dict(btn='btn_R9C13', row=9, col=13, sq=12, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef141 = dict(btn='btn_R9C14', row=9, col=14, sq=12, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef142 = dict(btn='btn_R9C15', row=9, col=15, sq=12, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef143 = dict(btn='btn_R9C16', row=9, col=16, sq=12, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef144 = dict(btn='btn_R10C1', row=10, col=1, sq=9, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef145 = dict(btn='btn_R10C2', row=10, col=2, sq=9, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef146 = dict(btn='btn_R10C3', row=10, col=3, sq=9, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef147 = dict(btn='btn_R10C4', row=10, col=4, sq=9, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef148 = dict(btn='btn_R10C5', row=10, col=5, sq=10, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef149 = dict(btn='btn_R10C6', row=10, col=6, sq=10, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef150 = dict(btn='btn_R10C7', row=10, col=7, sq=10, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef151 = dict(btn='btn_R10C8', row=10, col=8, sq=10, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef152 = dict(btn='btn_R10C9', row=10, col=9, sq=11, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef153 = dict(btn='btn_R10C10', row=10, col=10, sq=11, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef154 = dict(btn='btn_R10C11', row=10, col=11, sq=11, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef155 = dict(btn='btn_R10C12', row=10, col=12, sq=11, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef156 = dict(btn='btn_R10C13', row=10, col=13, sq=12, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef157 = dict(btn='btn_R10C14', row=10, col=14, sq=12, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef158 = dict(btn='btn_R10C15', row=10, col=15, sq=12, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef159 = dict(btn='btn_R10C16', row=10, col=16, sq=12, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef160 = dict(btn='btn_R11C1', row=11, col=1, sq=9, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef161 = dict(btn='btn_R11C2', row=11, col=2, sq=9, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef162 = dict(btn='btn_R11C3', row=11, col=3, sq=9, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef163 = dict(btn='btn_R11C4', row=11, col=4, sq=9, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef164 = dict(btn='btn_R11C5', row=11, col=5, sq=10, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef165 = dict(btn='btn_R11C6', row=11, col=6, sq=10, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef166 = dict(btn='btn_R11C7', row=11, col=7, sq=10, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef167 = dict(btn='btn_R11C8', row=11, col=8, sq=10, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef168 = dict(btn='btn_R11C9', row=11, col=9, sq=11, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef169 = dict(btn='btn_R11C10', row=11, col=10, sq=11, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef170 = dict(btn='btn_R11C11', row=11, col=11, sq=11, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef171 = dict(btn='btn_R11C12', row=11, col=12, sq=11, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef172 = dict(btn='btn_R11C13', row=11, col=13, sq=12, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef173 = dict(btn='btn_R11C14', row=11, col=14, sq=12, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef174 = dict(btn='btn_R11C15', row=11, col=15, sq=12, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef175 = dict(btn='btn_R11C16', row=11, col=16, sq=12, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef176 = dict(btn='btn_R12C1', row=12, col=1, sq=9, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef177 = dict(btn='btn_R12C2', row=12, col=2, sq=9, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef178 = dict(btn='btn_R12C3', row=12, col=3, sq=9, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef179 = dict(btn='btn_R12C4', row=12, col=4, sq=9, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef180 = dict(btn='btn_R12C5', row=12, col=5, sq=10, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef181 = dict(btn='btn_R12C6', row=12, col=6, sq=10, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef182 = dict(btn='btn_R12C7', row=12, col=7, sq=10, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef183 = dict(btn='btn_R12C8', row=12, col=8, sq=10, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef184 = dict(btn='btn_R12C9', row=12, col=9, sq=11, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef185 = dict(btn='btn_R12C10', row=12, col=10, sq=11, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef186 = dict(btn='btn_R12C11', row=12, col=11, sq=11, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef187 = dict(btn='btn_R12C12', row=12, col=12, sq=11, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef188 = dict(btn='btn_R12C13', row=12, col=13, sq=12, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef189 = dict(btn='btn_R12C14', row=12, col=14, sq=12, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef190 = dict(btn='btn_R12C15', row=12, col=15, sq=12, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef191 = dict(btn='btn_R12C16', row=12, col=16, sq=12, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef192 = dict(btn='btn_R13C1', row=13, col=1, sq=13, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef193 = dict(btn='btn_R13C2', row=13, col=2, sq=13, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef194 = dict(btn='btn_R13C3', row=13, col=3, sq=13, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef195 = dict(btn='btn_R13C4', row=13, col=4, sq=13, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef196 = dict(btn='btn_R13C5', row=13, col=5, sq=14, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef197 = dict(btn='btn_R13C6', row=13, col=6, sq=14, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef198 = dict(btn='btn_R13C7', row=13, col=7, sq=14, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef199 = dict(btn='btn_R13C8', row=13, col=8, sq=14, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef200 = dict(btn='btn_R13C9', row=13, col=9, sq=15, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef201 = dict(btn='btn_R13C10', row=13, col=10, sq=15, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef202 = dict(btn='btn_R13C11', row=13, col=11, sq=15, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef203 = dict(btn='btn_R13C12', row=13, col=12, sq=15, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef204 = dict(btn='btn_R13C13', row=13, col=13, sq=16, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef205 = dict(btn='btn_R13C14', row=13, col=14, sq=16, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef206 = dict(btn='btn_R13C15', row=13, col=15, sq=16, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef207 = dict(btn='btn_R13C16', row=13, col=16, sq=16, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef208 = dict(btn='btn_R14C1', row=14, col=1, sq=13, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef209 = dict(btn='btn_R14C2', row=14, col=2, sq=13, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef210 = dict(btn='btn_R14C3', row=14, col=3, sq=13, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef211 = dict(btn='btn_R14C4', row=14, col=4, sq=13, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef212 = dict(btn='btn_R14C5', row=14, col=5, sq=14, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef213 = dict(btn='btn_R14C6', row=14, col=6, sq=14, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef214 = dict(btn='btn_R14C7', row=14, col=7, sq=14, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef215 = dict(btn='btn_R14C8', row=14, col=8, sq=14, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef216 = dict(btn='btn_R14C9', row=14, col=9, sq=15, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef217 = dict(btn='btn_R14C10', row=14, col=10, sq=15, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef218 = dict(btn='btn_R14C11', row=14, col=11, sq=15, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef219 = dict(btn='btn_R14C12', row=14, col=12, sq=15, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef220 = dict(btn='btn_R14C13', row=14, col=13, sq=16, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef221 = dict(btn='btn_R14C14', row=14, col=14, sq=16, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef222 = dict(btn='btn_R14C15', row=14, col=15, sq=16, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef223 = dict(btn='btn_R14C16', row=14, col=16, sq=16, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef224 = dict(btn='btn_R15C1', row=15, col=1, sq=13, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef225 = dict(btn='btn_R15C2', row=15, col=2, sq=13, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef226 = dict(btn='btn_R15C3', row=15, col=3, sq=13, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef227 = dict(btn='btn_R15C4', row=15, col=4, sq=13, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef228 = dict(btn='btn_R15C5', row=15, col=5, sq=14, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef229 = dict(btn='btn_R15C6', row=15, col=6, sq=14, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef230 = dict(btn='btn_R15C7', row=15, col=7, sq=14, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef231 = dict(btn='btn_R15C8', row=15, col=8, sq=14, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef232 = dict(btn='btn_R15C9', row=15, col=9, sq=15, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef233 = dict(btn='btn_R15C10', row=15, col=10, sq=15, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef234 = dict(btn='btn_R15C11', row=15, col=11, sq=15, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef235 = dict(btn='btn_R15C12', row=15, col=12, sq=15, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef236 = dict(btn='btn_R15C13', row=15, col=13, sq=16, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef237 = dict(btn='btn_R15C14', row=15, col=14, sq=16, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef238 = dict(btn='btn_R15C15', row=15, col=15, sq=16, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef239 = dict(btn='btn_R15C16', row=15, col=16, sq=16, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef240 = dict(btn='btn_R16C1', row=16, col=1, sq=13, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef241 = dict(btn='btn_R16C2', row=16, col=2, sq=13, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef242 = dict(btn='btn_R16C3', row=16, col=3, sq=13, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef243 = dict(btn='btn_R16C4', row=16, col=4, sq=13, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef244 = dict(btn='btn_R16C5', row=16, col=5, sq=14, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef245 = dict(btn='btn_R16C6', row=16, col=6, sq=14, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef246 = dict(btn='btn_R16C7', row=16, col=7, sq=14, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef247 = dict(btn='btn_R16C8', row=16, col=8, sq=14, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef248 = dict(btn='btn_R16C9', row=16, col=9, sq=15, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef249 = dict(btn='btn_R16C10', row=16, col=10, sq=15, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef250 = dict(btn='btn_R16C11', row=16, col=11, sq=15, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef251 = dict(btn='btn_R16C12', row=16, col=12, sq=15, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef252 = dict(btn='btn_R16C13', row=16, col=13, sq=16, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef253 = dict(btn='btn_R16C14', row=16, col=14, sq=16, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef254 = dict(btn='btn_R16C15', row=16, col=15, sq=16, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")
arrRef255 = dict(btn='btn_R16C16', row=16, col=16, sq=16, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit, font=labelfont, fg="black")

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
                arrRef183, arrRef184, arrRef184, arrRef186, arrRef187, arrRef188, arrRef189,
                arrRef190, arrRef191, arrRef192, arrRef193, arrRef194, arrRef195, arrRef196,
                arrRef197, arrRef198, arrRef199, arrRef200, arrRef201, arrRef202, arrRef203,
                arrRef204, arrRef205, arrRef206, arrRef207, arrRef208, arrRef209, arrRef210,
                arrRef211, arrRef212, arrRef213, arrRef214, arrRef215, arrRef216, arrRef217,
                arrRef218, arrRef219, arrRef220, arrRef221, arrRef222, arrRef223, arrRef224,
                arrRef225, arrRef226, arrRef227, arrRef228, arrRef229, arrRef230, arrRef231,
                arrRef232, arrRef233, arrRef234, arrRef235, arrRef236, arrRef237, arrRef236,
                arrRef239, arrRef240, arrRef241, arrRef242, arrRef243, arrRef244, arrRef245,
                arrRef246, arrRef247, arrRef248, arrRef249, arrRef250, arrRef251, arrRef252,
                arrRef253, arrRef254, arrRef255]

r_1_nums = []
r_2_nums = []
r_3_nums = []
r_4_nums = []
r_5_nums = []
r_6_nums = []
r_7_nums = []
r_8_nums = []
r_9_nums = []
r_10_nums = []
r_11_nums = []
r_12_nums = []
r_13_nums = []
r_14_nums = []
r_15_nums = []
r_16_nums = []
c_1_nums = []
c_2_nums = []
c_3_nums = []
c_4_nums = []
c_5_nums = []
c_6_nums = []
c_7_nums = []
c_8_nums = []
c_9_nums = []
c_10_nums = []
c_11_nums = []
c_12_nums = []
c_13_nums = []
c_14_nums = []
c_15_nums = []
c_16_nums = []
s_1_nums = []
s_2_nums = []
s_3_nums = []
s_4_nums = []
s_5_nums = []
s_6_nums = []
s_7_nums = []
s_8_nums = []
s_9_nums = []
s_10_nums = []
s_11_nums = []
s_12_nums = []
s_13_nums = []
s_14_nums = []
s_15_nums = []
s_16_nums = []

not_done_arefs = arrRefs_List.copy()
# new_list = lis.copy()

def update_done_arefs_list(aref):
    print("362 Entering update_done_arefs_list aref is ", aref)
    for aref in arrRefs_List:
        if aref['done'] == True:
            not_done_arefs.remove(aref)


btn_ref = {}
# btn_ref = dict(btn='btn_R1C1', aref='arrRef0')

arrStringsRemaining = ""
bShow = False;

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
F1_frame.grid(row=2, column=0)
F1_frame.config(highlightbackground="blue", highlightthickness=2)
F2_frame = Frame(main_canvas)
F2_frame.grid(row=2, column=4)
F2_frame.config(highlightbackground="red", highlightthickness=2)
F3_frame = Frame(main_canvas)
F3_frame.grid(row=2, column=8)
F3_frame.config(highlightbackground="yellow", highlightthickness=2)
F4_frame = Frame(main_canvas)
F4_frame.grid(row=2, column=12)
F4_frame.config(highlightbackground="blue", highlightthickness=2)
sn_frame = Frame(main_canvas)
sn_frame.grid(row=2, column=16) #sn is for select a number
sn_frame.config(highlightbackground="green", highlightthickness=2)
F5_frame = Frame(main_canvas)
F5_frame.grid(row=3, column=0)
F5_frame.config(highlightbackground="yellow", highlightthickness=2)
F6_frame = Frame(main_canvas)
F6_frame.grid(row=3, column=4)
F6_frame.config(highlightbackground="green", highlightthickness=2)
F7_frame = Frame(main_canvas)
F7_frame.grid(row=3, column=8)
F7_frame.config(highlightbackground="blue", highlightthickness=2)
F8_frame = Frame(main_canvas)
F8_frame.grid(row=3, column=12)
F8_frame.config(highlightbackground="red", highlightthickness=2)
fn_frame = Frame(main_canvas)
fn_frame.grid(row=3, column=16) #fn is for select a function name
fn_frame.config(highlightbackground="green", highlightthickness=2)
#############
F9_frame = Frame(main_canvas)
F9_frame.grid(row=4, column=0)
F9_frame.config(highlightbackground="yellow", highlightthickness=2)
F10_frame = Frame(main_canvas)
F10_frame.grid(row=4, column=4)
F10_frame.config(highlightbackground="green", highlightthickness=2)
F11_frame = Frame(main_canvas)
F11_frame.grid(row=4, column=8)
F11_frame.config(highlightbackground="blue", highlightthickness=2)
F12_frame = Frame(main_canvas)
F12_frame.grid(row=4, column=12)
F12_frame.config(highlightbackground="red", highlightthickness=2)
F13_frame = Frame(main_canvas)
F13_frame.grid(row=5, column=0)
F13_frame.config(highlightbackground="red", highlightthickness=2)
F14_frame = Frame(main_canvas)
F14_frame.grid(row=5, column=4)
F14_frame.config(highlightbackground="yellow", highlightthickness=2)
F15_frame = Frame(main_canvas)
F15_frame.grid(row=5, column=8)
F15_frame.config(highlightbackground="green", highlightthickness=2)
F16_frame = Frame(main_canvas)
F16_frame.grid(row=5, column=12)
F16_frame.config(highlightbackground="blue", highlightthickness=2)
# fm_frame = Frame(main_canvas)
# fm_frame.grid(row=2, column=16) #fn is for select a function name
# fm_frame.config(highlightbackground="green", highlightthickness=2)



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

def make_RCS_nums():
    for cell in not_done_arefs:
        if cell['row'] == 1:
            r_1_nums.append(cell['nums'])
        elif cell['row'] == 2:
            r_2_nums.append(cell['nums'])
        elif cell['row'] == 3:
            r_3_nums.append(cell['nums'])
        elif cell['row'] == 4:
            r_4_nums.append(cell['nums'])
        elif cell['row'] == 5:
            r_5_nums.append(cell['nums'])
        elif cell['row'] == 6:
            r_6_nums.append(cell['nums'])
        elif cell['row'] == 7:
            r_7_nums.append(cell['nums'])
        elif cell['row'] == 8:
            r_8_nums.append(cell['nums'])
        elif cell['row'] == 9:
            r_9_nums.append(cell['nums'])
        elif cell['row'] == 10:
            r_10_nums.append(cell['nums'])
        elif cell['row'] == 11:
            r_11_nums.append(cell['nums'])
        elif cell['row'] == 12:
            r_12_nums.append(cell['nums'])
        elif cell['row'] == 13:
            r_13_nums.append(cell['nums'])
        elif cell['row'] == 14:
            r_14_nums.append(cell['nums'])
        elif cell['row'] == 15:
            r_15_nums.append(cell['nums'])
        elif cell['row'] == 16:
            r_16_nums.append(cell['nums'])

    print("591 row nums ", r_1_nums, r_2_nums, r_3_nums, r_4_nums, r_5_nums)

def update_RCS(current_button, aref): #Row, Column, Square):
    current_button['text'] = aref['nums']
    # current_btn['text'] = aref['nums']

# def update_not_done_arefs(aref):
#     print("542 Entered update_not_done_arefs(aref)", aref['done'])
#     if aref['done'] == True and aref in not_done_arefs:
#         not_done_arefs.remove(aref)
#     print("545 update_not_done_arefs ", len(not_done_arefs))

def update_puzzle(row, column, square):
    print("529 update_puzzle row, column, square ", row, column, square, currentNumber)
    for cell in not_done_arefs:
        current_button = cell['btn']
        aref = eval(btn_dict[current_button])
        if row == cell['row'] and column == cell['col'] and square == cell['sq']:
            if aref in not_done_arefs:
                aref['done'] == True
                print("550 In update_puzzle if aref['done']")
                not_done_arefs.remove(aref)
                print("557 len(not_done_arefs)", len(not_done_arefs))
                continue
            #     print("532 row, column and square are same. ", row, column, square)
        elif row == cell['row'] or column == cell['col'] or square == cell['sq']:
            print("562 row, column and square are same. ", row, column, square, cell['nums'])
            if currentNumber in cell['nums']:
                print("564 row, column and square are same. ", row, column, square, cell['nums'])
                # current_button = cell['btn']
                # aref = eval(btn_dict[current_button])
                current_button = eval(current_button)
                # print("525", current_button, type(current_button), aref)
                new_nums = cell['nums'].replace(currentNumber, "")
                print("570 new_nums ", new_nums)
                aref['nums'] = new_nums
                current_button['text'] = aref['nums']
                # print("560", aref, aref['done'])
                # if aref['done'] == True:
                #     not_done_arefs.remove(aref)
                # print("569 len(not_done_arefs) ", len(not_done_arefs))


def refresh_display_aux(current_btn, aref):
    print("551 Entered refresh_display_aux", current_btn, aref)
    aref['done'] = True
    aref['nums'] = currentNumber
    aref['font'] = buttonfont
    aref['width'] = 6
    # aref['height'] = 2
    aref['fg'] = "red"
    current_btn['text'] = aref['nums']
    # current_btn['font'] = aref['font']
    current_btn['width'] = aref['width']
    # current_btn['height'] = aref['height']
    current_btn['fg'] = aref['fg']

def refresh_display(current_btn, aref):
    print("565 Entered refresh_display", current_btn, aref)
    aref['nums'] = currentNumber
    current_btn['text'] = aref['nums']
    # arrRef0['nums'] = currentNumber
    # arrRef0['font'] = buttonfont
    # arrRef0['fg'] = "red"


def update_R1C1():
    print("R1C1 button pressed.")
    if bRemoveANumberFromACell == "False":
        # btn_R1C1.config(font=buttonfont, width=wid4, height=hit, fg="red")
        current_btn = btn_R1C1
        aref = arrRef0
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        not_done_arefs.remove(aref)
        # aref['nums'] = currentNumber
        update_puzzle(1, 1, 1)

def update_R1C2():
    print("R1C2 button pressed.")
    if bRemoveANumberFromACell == "False":
        # btn_R1C2.config(font=buttonfont, width=wid4, height=hit, fg="red")
        current_btn = btn_R1C2
        aref = arrRef1
        refresh_display_aux(current_btn, aref)
        # print("607 update_R1C2", aref, aref['done'], len(not_done_arefs))
        aref['done'] = True
        not_done_arefs.remove(aref)
        print("609 update_R1C2", aref, aref['done'])
        update_puzzle(1, 2, 1)

def update_R1C3():
    print("R1C3 button pressed.")
    if bRemoveANumberFromACell == "False":
        # btn_R1C3.config(font=buttonfont, width=wid4, height=hit, fg="red")
        # btn_R1C3['text'] = currentNumber
        current_btn = btn_R1C3
        aref = arrRef2
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        not_done_arefs.remove(aref)
        update_puzzle(1, 3, 1)


def update_R1C4():
    print("R1C4 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R1C4
        aref = arrRef3
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        not_done_arefs.remove(aref)
        update_puzzle(1, 4, 1)


def update_R1C5():
    print("R1C5 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R1C5
        aref = arrRef4
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        not_done_arefs.remove(aref)
        update_puzzle(1, 5, 2)

def update_R1C6():
    print("R1C6 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R1C6
        aref = arrRef5
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        not_done_arefs.remove(aref)
        update_puzzle(1, 6, 2)

def update_R1C7():
    print("R1C7 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R1C7
        aref = arrRef6
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        not_done_arefs.remove(aref)
        update_puzzle(1, 7, 2)

def update_R1C8():
    print("R1C8 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R1C8
        aref = arrRef7
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        not_done_arefs.remove(aref)
        update_puzzle(1, 8, 2)

def update_R1C9():
    print("R1C9 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R1C9
        aref = arrRef8
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        not_done_arefs.remove(aref)
        update_puzzle(1, 9, 3)

def update_R1C10():
    print("R1C10 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R1C10
        aref = arrRef9
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        not_done_arefs.remove(aref)
        update_puzzle(1, 10, 3)

def update_R1C11():
    print("R1C11 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R1C11
        aref = arrRef10
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        not_done_arefs.remove(aref)
        update_puzzle(1, 11, 3)


def update_R1C12():
    print("R1C12 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R1C12
        aref = arrRef11
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        not_done_arefs.remove(aref)
        update_puzzle(1, 12, 3)

def update_R1C13():
    print("R1C13 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R1C13
        aref = arrRef12
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        not_done_arefs.remove(aref)
        update_puzzle(1, 13, 4)

def update_R1C14():
    print("R1C14 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R1C14
        aref = arrRef13
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        not_done_arefs.remove(aref)
        update_puzzle(1, 14, 4)

def update_R1C15():
    print("R1C15 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R1C15
        aref = arrRef14
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        not_done_arefs.remove(aref)
        update_puzzle(1, 15, 4)

def update_R1C16():
    print("R2C16 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R1C16
        aref = arrRef15
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        not_done_arefs.remove(aref)
        update_puzzle(1, 16, 4)

def update_R2C1():
    print("R2C1 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R2C1
        aref = arrRef16
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        not_done_arefs.remove(aref)
        update_puzzle(2, 1, 1)

def update_R2C2():
    print("R2C2 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R2C2
        aref = arrRef17
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        not_done_arefs.remove(aref)
        update_puzzle(2, 2, 1)

def update_R2C3():
    print("R2C3 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R2C3
        aref = arrRef18
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        not_done_arefs.remove(aref)
        update_puzzle(2, 3, 1)

def update_R2C4():
    print("R2C4 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R2C4
        aref = arrRef19
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        not_done_arefs.remove(aref)
        update_puzzle(2, 4, 1)

def update_R2C5():
    print("R2C5 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R2C5
        aref = arrRef20
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        not_done_arefs.remove(aref)
        update_puzzle(2, 5, 2)

def update_R2C6():
    print("R2C6 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R2C6
        aref = arrRef21
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        not_done_arefs.remove(aref)
        update_puzzle(2, 6, 2)

def update_R2C7():
    print("R2C7 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R2C7
        aref = arrRef22
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        not_done_arefs.remove(aref)
        update_puzzle(2, 7, 2)

def update_R2C8():
    print("R2C8 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R2C8
        aref = arrRef23
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        not_done_arefs.remove(aref)
        update_puzzle(2, 8, 2)

def update_R2C9():
    print("R2C9 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R2C9
        aref = arrRef24
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        not_done_arefs.remove(aref)
        update_puzzle(2, 9, 3)

def update_R2C10():
    print("R2C10 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R2C10
        aref = arrRef25
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        not_done_arefs.remove(aref)
        update_puzzle(2, 10, 3)

def update_R2C11():
    print("R2C11 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R2C11
        aref = arrRef26
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        not_done_arefs.remove(aref)
        update_puzzle(2, 11, 3)

def update_R2C12():
    print("R2C12 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R2C12
        aref = arrRef27
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        not_done_arefs.remove(aref)
        update_puzzle(2, 12, 3)

def update_R2C13():
    print("R2C13 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R2C13
        aref = arrRef28
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        not_done_arefs.remove(aref)
        update_puzzle(2, 13, 4)

def update_R2C14():
    print("R2C14 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R2C14
        aref = arrRef29
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        not_done_arefs.remove(aref)
        update_puzzle(2, 14, 4)


def update_R2C15():
    print("R2C15 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R2C15
        aref = arrRef30
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        not_done_arefs.remove(aref)
        update_puzzle(2, 15, 4)

def update_R2C16():
    print("R2C16 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R2C16
        aref = arrRef31
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        not_done_arefs.remove(aref)
        update_puzzle(2, 16, 4)

def update_R3C1():
    print("R3C1 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R3C1
        aref = arrRef32
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(3, 1, 1)

def update_R3C2():
    print("R3C2 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R3C2
        aref = arrRef33
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(3, 2, 1)
def update_R3C3():
    print("R3C3 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R3C3
        aref = arrRef34
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(3, 3, 1)
def update_R3C4():
    print("R3C4 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R3C4
        aref = arrRef35
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(3, 4, 1)
def update_R3C5():
    print("R3C5 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R3C5
        aref = arrRef36
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(3, 5, 2)
def update_R3C6():
    print("R3C6 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R3C6
        aref = arrRef37
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(3, 6, 2)
def update_R3C7():
    print("R3C7 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R3C7
        aref = arrRef38
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(3, 7, 2)
def update_R3C8():
    print("R3C8 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R3C8
        aref = arrRef39
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(3, 8, 2)
def update_R3C9():
    print("R3C9 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R3C9
        aref = arrRef40
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(3, 9, 3)
def update_R3C10():
    print("R3C10 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R3C10
        aref = arrRef41
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(3, 10, 3)
def update_R3C11():
    print("R3C11 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R3C11
        aref = arrRef42
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(3, 11, 3)
def update_R3C12():
    print("R3C12 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R3C12
        aref = arrRef43
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(3, 12, 3)
def update_R3C13():
    print("R3C13 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R3C13
        aref = arrRef44
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(3, 13, 4)
def update_R3C14():
    print("R3C14 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R3C14
        aref = arrRef45
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(3, 14, 4)
def update_R3C15():
    print("R3C15 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R3C15
        aref = arrRef46
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(3, 15, 4)
def update_R3C16():
    print("R3C16 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R3C16
        aref = arrRef47
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(3, 16, 4)
def update_R4C1():
    print("R4C1 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R4C1
        aref = arrRef48
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(4, 1, 1)
def update_R4C2():
    print("R4C2 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R4C2
        aref = arrRef49
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(4, 2, 1)
def update_R4C3():
    print("R4C3 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R4C3
        aref = arrRef50
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(4, 3, 1)
def update_R4C4():
    print("R4C4 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R4C4
        aref = arrRef51
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(4, 4, 1)
def update_R4C5():
    print("R4C5 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R4C5
        aref = arrRef52
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(4, 5, 2)
def update_R4C6():
    print("R4C6 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R4C6
        aref = arrRef53
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(4, 6, 2)
def update_R4C7():
    print("R4C7 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R4C7
        aref = arrRef54
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(4, 7, 2)
def update_R4C8():
    print("R4C8 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R4C8
        aref = arrRef55
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(4, 8, 2)
def update_R4C9():
    print("R4C9 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R4C9
        aref = arrRef56
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(4, 9, 3)
def update_R4C10():
    print("R4C10 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R4C10
        aref = arrRef57
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        not_done_arefs.remove(aref)
        update_puzzle(4, 10, 3)
def update_R4C11():
    print("R4C11 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R4C11
        aref = arrRef58
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(4, 11, 3)
def update_R4C12():
    print("R4C12 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R4C12
        aref = arrRef59
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(4, 12, 3)
def update_R4C13():
    print("R4C13 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R4C13
        aref = arrRef60
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(4, 13, 4)
def update_R4C14():
    print("R4C14 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R4C14
        aref = arrRef61
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(4, 14, 4)
def update_R4C15():
    print("R4C15 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R4C15
        aref = arrRef62
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(4, 15, 4)
def update_R4C16():
    print("R4C16 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R4C16
        aref = arrRef63
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(4, 16, 4)
######################1234
def update_R5C1():
    print("R5C1 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R5C1
        aref = arrRef64
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(5, 1, 5)
def update_R5C2():
    print("R5C2 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R5C2
        aref = arrRef65
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(5, 2, 5)
def update_R5C3():
    print("R5C3 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R5C3
        aref = arrRef66
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(5, 3, 5)
def update_R5C4():
    print("R5C4 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R5C4
        aref = arrRef67
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(5, 4, 5)
def update_R5C5():
    print("R5C5 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R5C5
        aref = arrRef68
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(5, 5, 6)
def update_R5C6():
    print("R5C6 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R5C6
        aref = arrRef69
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(5, 6, 6)
def update_R5C7():
    print("R5C7 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R5C7
        aref = arrRef70
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(5, 7, 6)
def update_R5C8():
    print("R5C8 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R5C8
        aref = arrRef71
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(5, 8, 6)
def update_R5C9():
    print("R5C9 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R5C9
        aref = arrRef72
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(5, 9, 7)
def update_R5C10():
    print("R5C10 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R5C10
        aref = arrRef73
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(5, 10, 7)
def update_R5C11():
    print("R5C11 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R5C11
        aref = arrRef74
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(5, 11, 7)
def update_R5C12():
    print("R5C12 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R5C12
        aref = arrRef75
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(5, 12, 7)
def update_R5C13():
    print("R5C13 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R5C13
        aref = arrRef76
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(5, 13, 8)
def update_R5C14():
    print("R5C14 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R5C14
        aref = arrRef77
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(5, 14, 8)
def update_R5C15():
    print("R5C15 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R5C15
        aref = arrRef78
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(5, 15, 8)
def update_R5C16():
    print("R5C16 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R5C16
        aref = arrRef79
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(5, 16, 8)
def update_R6C1():
    print("R6C1 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R6C1
        aref = arrRef80
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(6, 1, 5)
def update_R6C2():
    print("R6C2 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R6C2
        aref = arrRef81
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(6, 2, 5)
def update_R6C3():
    print("R6C3 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R6C3
        aref = arrRef82
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(6, 3, 5)
def update_R6C4():
    print("R6C4 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R6C4
        aref = arrRef83
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(6, 4, 5)
def update_R6C5():
    print("R6C5 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R6C5
        aref = arrRef84
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(6, 5, 6)
def update_R6C6():
    print("R6C6 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R6C6
        aref = arrRef85
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(6, 6, 6)
def update_R6C7():
    print("R6C7 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R6C7
        aref = arrRef86
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(6, 7, 6)
def update_R6C8():
    print("R6C8 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R6C8
        aref = arrRef87
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(6, 8, 6)
def update_R6C9():
    print("R6C9 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R6C9
        aref = arrRef88
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(6, 9, 7)
def update_R6C10():
    print("R6C10 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R6C10
        aref = arrRef89
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(6, 10, 7)
def update_R6C11():
    print("R6C11 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R6C11
        aref = arrRef90
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(6, 11, 7)
def update_R6C12():
    print("R6C12 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R6C12
        aref = arrRef91
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(6, 12, 7)
def update_R6C13():
    print("R6C13 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R6C13
        aref = arrRef92
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(6, 13, 8)
def update_R6C14():
    print("R6C14 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R6C14
        aref = arrRef93
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(6, 14, 8)
def update_R6C15():
    print("R6C15 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R6C15
        aref = arrRef94
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(6, 15, 8)
def update_R6C16():
    print("R6C16 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R6C16
        aref = arrRef95
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(6, 16, 8)
def update_R7C1():
    print("R7C1 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R7C1
        aref = arrRef96
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(7, 1, 5)
def update_R7C2():
    print("R7C2 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R7C2
        aref = arrRef97
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(7, 2, 5)
def update_R7C3():
    print("R7C3 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R7C3
        aref = arrRef98
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(7, 3, 5)
def update_R7C4():
    print("R7C4 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R7C4
        aref = arrRef99
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(7, 4, 5)
def update_R7C5():
    print("R7C5 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R7C5
        aref = arrRef100
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(7, 5, 6)
def update_R7C6():
    print("R7C6 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R7C6
        aref = arrRef101
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(7, 6, 6)
def update_R7C7():
    print("R7C7 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R7C7
        aref = arrRef102
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(7, 7, 6)
def update_R7C8():
    print("R7C8 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R7C8
        aref = arrRef103
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(7, 8, 6)
def update_R7C9():
    print("R7C9 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R7C9
        aref = arrRef104
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(7, 9, 7)
def update_R7C10():
    print("R7C10 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R7C10
        aref = arrRef105
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(7, 10, 7)
def update_R7C11():
    print("R7C11 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R7C11
        aref = arrRef106
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(7, 11, 7)
def update_R7C12():
    print("R7C12 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R7C12
        aref = arrRef107
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(7, 12, 7)
def update_R7C13():
    print("R7C13 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R7C13
        aref = arrRef108
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(7, 13, 8)
def update_R7C14():
    print("R7C14 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R7C14
        aref = arrRef109
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(7, 14, 8)
def update_R7C15():
    print("R7C15 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R7C15
        aref = arrRef110
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(7, 15, 8)
def update_R7C16():
    print("R7C16 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R7C16
        aref = arrRef111
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(7, 16, 8)

def update_R8C1():
    print("R8C1 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R8C1
        aref = arrRef112
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(8, 1, 5)
def update_R8C2():
    print("R8C2 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R8C2
        aref = arrRef113
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(8, 2, 5)
def update_R8C3():
    print("R8C3 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R8C3
        aref = arrRef114
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(8, 3, 5)
def update_R8C4():
    print("R8C4 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R8C4
        aref = arrRef115
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(8, 4, 5)
def update_R8C5():
    print("R8C5 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R8C5
        aref = arrRef116
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(8, 5, 6)
def update_R8C6():
    print("R8C6 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R8C6
        aref = arrRef117
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(8, 6, 6)
def update_R8C7():
    print("R8C7 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R8C7
        aref = arrRef118
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(8, 7, 6)
def update_R8C8():
    print("R8C8 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R8C8
        aref = arrRef119
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(8, 8, 6)
def update_R8C9():
    print("R8C9 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R8C9
        aref = arrRef120
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(8, 9, 7)
def update_R8C10():
    print("R8C10 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R8C10
        aref = arrRef121
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(8, 10, 7)
def update_R8C11():
    print("R8C11 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R8C11
        aref = arrRef122
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(8, 11, 7)
def update_R8C12():
    print("R8C12 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R8C12
        aref = arrRef123
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(8, 12, 7)
def update_R8C13():
    print("R7C13 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R8C13
        aref = arrRef124
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(8, 13, 8)
def update_R8C14():
    print("R8C14 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R8C14
        aref = arrRef125
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(8, 14, 8)
def update_R8C15():
    print("R8C15 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R8C15
        aref = arrRef126
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(8, 15, 8)
def update_R8C16():
    print("R8C16 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R8C16
        aref = arrRef127
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(8, 16, 8)
def update_R9C1():
    print("R9C1 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R9C1
        aref = arrRef128
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(9, 1, 9)
def update_R9C2():
    print("R9C2 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R9C2
        aref = arrRef129
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(9, 2, 9)
def update_R9C3():
    print("R9C3 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R9C3
        aref = arrRef130
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(9, 3, 9)
def update_R9C4():
    print("R9C4 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R9C4
        aref = arrRef131
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(9, 4, 9)
def update_R9C5():
    print("R9C5 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R9C5
        aref = arrRef132
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(9, 5, 10)
def update_R9C6():
    print("R9C6 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R9C6
        aref = arrRef133
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(9, 6, 10)
def update_R9C7():
    print("R9C7 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R9C7
        aref = arrRef134
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(9, 7, 10)
def update_R9C8():
    print("R9C8 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R9C8
        aref = arrRef135
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(9, 8, 10)
def update_R9C9():
    print("R9C9 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R9C9
        aref = arrRef136
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(9, 9, 11)
def update_R9C10():
    print("R9C10 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R9C10
        aref = arrRef137
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(9, 10, 11)
def update_R9C11():
    print("R9C11 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R9C11
        aref = arrRef138
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(9, 11, 11)
def update_R9C12():
    print("R9C12 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R9C12
        aref = arrRef139
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(9, 12, 11)
def update_R9C13():
    print("R9C13 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R9C13
        aref = arrRef140
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(9, 13, 12)
def update_R9C14():
    print("R9C14 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R9C14
        aref = arrRef141
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(9, 14, 12)
def update_R9C15():
    print("R9C15 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R9C15
        aref = arrRef142
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(9, 15, 12)
def update_R9C16():
    print("R7C16 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R9C16
        aref = arrRef143
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(9, 16, 12)
def update_R10C1():
    print("R10C1 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R10C1
        aref = arrRef144
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(10, 1, 9)
def update_R10C2():
    print("R10C2 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R10C2
        aref = arrRef145
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(10, 2, 9)
def update_R10C3():
    print("R10C3 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R10C3
        aref = arrRef146
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(10, 3, 9)
def update_R10C4():
    print("R10C4 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R10C4
        aref = arrRef147
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(10, 4, 9)
def update_R10C5():
    print("R10C5 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R10C5
        aref = arrRef148
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(10, 5, 10)
def update_R10C6():
    print("R10C6 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R10C6
        aref = arrRef149
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(10, 6, 10)
def update_R10C7():
    print("R10C7 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R10C7
        aref = arrRef150
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(10, 7, 10)
def update_R10C8():
    print("R10C8 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R10C8
        aref = arrRef151
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(10, 8, 10)
def update_R10C9():
    print("R10C9 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R10C9
        aref = arrRef152
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(10, 9, 11)
def update_R10C10():
    print("R10C10 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R10C10
        aref = arrRef153
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(10, 10, 11)
def update_R10C11():
    print("R10C11 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R10C11
        aref = arrRef154
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(10, 11, 11)
def update_R10C12():
    print("R10C12 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R10C12
        aref = arrRef155
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(10, 12, 11)
def update_R10C13():
    print("R10C13 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R10C13
        aref = arrRef156
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(10, 13, 12)
def update_R10C14():
    print("R10C14 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R10C14
        aref = arrRef157
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(10, 14, 12)
def update_R10C15():
    print("R10C15 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R10C15
        aref = arrRef158
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(10, 15, 16)
def update_R10C16():
    print("R10C16 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R10C16
        aref = arrRef159
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(10, 16, 12)

def update_R11C1():
    print("R11C1 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R11C1
        aref = arrRef160
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(11, 1, 9)
def update_R11C2():
    print("R11C2 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R11C2
        aref = arrRef161
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(11, 2, 9)
def update_R11C3():
    print("R11C3 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R11C3
        aref = arrRef162
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(11, 3, 9)
def update_R11C4():
    print("R11C4 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R11C4
        aref = arrRef163
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(11, 4, 9)
def update_R11C5():
    print("R11C5 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R11C5
        aref = arrRef164
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(11, 5, 10)
def update_R11C6():
    print("R11C6 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R11C6
        aref = arrRef165
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(11, 6, 10)
def update_R11C7():
    print("R11C7 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R11C7
        aref = arrRef166
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(11, 7, 10)
def update_R11C8():
    print("R11C8 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R11C8
        aref = arrRef167
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(11, 8, 10)
def update_R11C9():
    print("R11C9 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R11C9
        aref = arrRef168
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(11, 9, 11)
def update_R11C10():
    print("R11C10 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R11C10
        aref = arrRef169
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(11, 10, 11)
def update_R11C11():
    print("R11C11 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R11C11
        aref = arrRef170
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(11, 11, 11)
def update_R11C12():
    print("R11C12 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R11C12
        aref = arrRef171
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(11, 12, 11)
def update_R11C13():
    print("R11C13 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R11C13
        aref = arrRef172
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(11, 13, 12)
def update_R11C14():
    print("R11C14 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R11C14
        aref = arrRef173
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(11, 14, 12)
def update_R11C15():
    print("R11C15 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R11C15
        aref = arrRef174
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(11, 15, 12)
def update_R11C16():
    print("R11C16 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R11C16
        aref = arrRef175
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(11, 16, 12)

def update_R12C1():
    print("R12C1 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R12C1
        aref = arrRef176
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(12, 1, 9)
def update_R12C2():
    print("R12C2 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R12C2
        aref = arrRef177
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(12, 2, 9)
def update_R12C3():
    print("R12C3 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R12C3
        aref = arrRef178
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(12, 3, 9)
def update_R12C4():
    print("R12C4 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R12C4
        aref = arrRef179
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(12, 4, 9)
def update_R12C5():
    print("R12C5 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R12C5
        aref = arrRef180
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(12, 5, 10)
def update_R12C6():
    print("R12C6 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R12C6
        aref = arrRef181
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(12, 6, 10)
def update_R12C7():
    print("R12C7 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R12C7
        aref = arrRef182
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(12, 7, 10)
def update_R12C8():
    print("R12C8 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R12C8
        aref = arrRef183
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(12, 8, 10)
def update_R12C9():
    print("R12C9 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R12C9
        aref = arrRef184
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(12, 9, 11)
def update_R12C10():
    print("R11C10 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R12C10
        aref = arrRef185
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(12, 10, 11)
def update_R12C11():
    print("R12C11 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R12C11
        aref = arrRef186
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(12, 11, 11)
def update_R12C12():
    print("R12C12 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R12C12
        aref = arrRef187
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(12, 12, 11)
def update_R12C13():
    print("R12C13 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R12C13
        aref = arrRef188
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(12, 13, 12)
def update_R12C14():
    print("R12C14 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R12C14
        aref = arrRef189
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(12, 14, 12)
def update_R12C15():
    print("R12C15 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R12C15
        aref = arrRef190
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(12, 15, 12)
def update_R12C16():
    print("R12C16 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R12C16
        aref = arrRef191
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(12, 16, 12)
def update_R13C1():
    print("R13C1 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R13C1
        aref = arrRef192
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(13, 1, 13)
def update_R13C2():
    print("R13C2 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R13C2
        aref = arrRef193
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(13, 2, 13)
def update_R13C3():
    print("R13C3 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R13C3
        aref = arrRef194
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(13, 3, 13)
def update_R13C4():
    print("R13C4 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R13C4
        aref = arrRef195
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(13, 4, 13)
def update_R13C5():
    print("R13C5 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R13C5
        aref = arrRef196
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(13, 5, 14)
def update_R13C6():
    print("R13C6 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R13C6
        aref = arrRef197
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(13, 6, 14)
def update_R13C7():
    print("R13C7 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R13C7
        aref = arrRef198
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(13, 7, 14)
def update_R13C8():
    print("R13C8 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R13C8
        aref = arrRef199
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(13, 8, 14)
def update_R13C9():
    print("R13C9 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R13C9
        aref = arrRef200
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(13, 9, 15)
def update_R13C10():
    print("R13C10 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R13C10
        aref = arrRef201
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(13, 10, 15)
def update_R13C11():
    print("R13C11 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R13C11
        aref = arrRef202
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(13, 11, 15)
def update_R13C12():
    print("R13C12 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R13C12
        aref = arrRef203
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(12, 12, 15)
def update_R13C13():
    print("R13C13 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R13C13
        aref = arrRef204
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(13, 13, 16)
def update_R13C14():
    print("R13C14 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R13C14
        aref = arrRef205
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(13, 14, 16)
def update_R13C15():
    print("R13C15 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R13C15
        aref = arrRef206
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(13, 15, 16)
def update_R13C16():
    print("R13C16 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R13C16
        aref = arrRef207
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(13, 16, 16)

def update_R14C1():
    print("R14C1 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R14C1
        aref = arrRef208
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(14, 1, 13)
def update_R14C2():
    print("R14C2 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R14C2
        aref = arrRef209
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(14, 2, 13)
def update_R14C3():
    print("R14C3 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R14C3
        aref = arrRef210
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(14, 3, 13)
def update_R14C4():
    print("R14C4 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R14C4
        aref = arrRef211
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(14, 4, 13)
def update_R14C5():
    print("R14C5 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R14C5
        aref = arrRef212
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(14, 5, 14)
def update_R14C6():
    print("R14C6 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R14C6
        aref = arrRef213
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(14, 6, 14)
def update_R14C7():
    print("R14C7 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R14C7
        aref = arrRef214
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(14, 7, 14)
def update_R14C8():
    print("R14C8 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R14C8
        aref = arrRef215
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(14, 8, 14)
def update_R14C9():
    print("R14C9 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R14C9
        aref = arrRef216
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(14, 9, 15)
def update_R14C10():
    print("R14C10 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R14C10
        aref = arrRef217
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(14, 10, 15)
def update_R14C11():
    print("R14C11 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R14C11
        aref = arrRef218
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(14, 11, 15)
def update_R14C12():
    print("R14C12 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R14C12
        aref = arrRef219
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(14, 12, 15)
def update_R14C13():
    print("R14C13 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R14C13
        aref = arrRef220
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(14, 13, 16)
def update_R14C14():
    print("R14C14 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R14C14
        aref = arrRef221
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(14, 14, 16)
def update_R14C15():
    print("R14C15 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R14C15
        aref = arrRef222
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(14, 15, 16)
def update_R14C16():
    print("R14C16 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R14C16
        aref = arrRef223
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(14, 16, 16)
# start 15
def update_R15C1():
    print("R15C1 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R15C1
        aref = arrRef224
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(15, 1, 13)
def update_R15C2():
    print("R15C2 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R15C2
        aref = arrRef225
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(15, 2, 13)
def update_R15C3():
    print("R15C3 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R15C3
        aref = arrRef226
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(15, 3, 13)
def update_R15C4():
    print("R15C4 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R15C4
        aref = arrRef227
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(15, 4, 13)
def update_R15C5():
    print("R15C5 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R15C5
        aref = arrRef228
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(15, 5, 14)
def update_R15C6():
    print("R15C6 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R15C6
        aref = arrRef229
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(15, 6, 14)
def update_R15C7():
    print("R15C7 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R15C7
        aref = arrRef230
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(15, 7, 14)
def update_R15C8():
    print("R15C8 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R15C8
        aref = arrRef231
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(15, 8, 14)
def update_R15C9():
    print("R15C9 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R15C9
        aref = arrRef232
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(15, 9, 15)
def update_R15C10():
    print("R15C10 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R15C10
        aref = arrRef233
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(15, 10, 15)
def update_R15C11():
    print("R15C11 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R15C11
        aref = arrRef234
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(15, 11, 15)
def update_R15C12():
    print("R15C12 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R15C12
        aref = arrRef235
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(15, 12, 15)
def update_R15C13():
    print("R15C13 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R15C13
        aref = arrRef236
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(15, 13, 16)
def update_R15C14():
    print("R15C14 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R15C14
        aref = arrRef237
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(15, 14, 16)
def update_R15C15():
    print("R15C15 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R15C15
        aref = arrRef238
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(15, 15, 16)
def update_R15C16():
    print("R15C16 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R15C16
        aref = arrRef239
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(15, 16, 16)

def update_R16C1():
    print("R16C1 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R16C1
        aref = arrRef240
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(16, 1, 13)
def update_R16C2():
    print("R16C2 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R16C2
        aref = arrRef241
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(16, 2, 13)
def update_R16C3():
    print("R16C3 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R16C3
        aref = arrRef242
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(16, 3, 13)
def update_R16C4():
    print("R16C4 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R16C4
        aref = arrRef243
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(16, 4, 13)
def update_R16C5():
    print("R16C5 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R16C5
        aref = arrRef244
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(16, 5, 14)
def update_R16C6():
    print("R16C6 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R16C6
        aref = arrRef245
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(16, 6, 14)
def update_R16C7():
    print("R16C7 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R16C7
        aref = arrRef246
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(16, 7, 14)
def update_R16C8():
    print("R16C8 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R16C8
        aref = arrRef247
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(16, 8, 14)
def update_R16C9():
    print("R16C9 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R16C9
        aref = arrRef248
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(16, 9, 15)
def update_R16C10():
    print("R16C10 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R16C10
        aref = arrRef249
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(16, 10, 15)
def update_R16C11():
    print("R16C11 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R16C11
        aref = arrRef250
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(16, 11, 15)
def update_R16C12():
    print("R16C12 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R16C12
        aref = arrRef251
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(16, 12, 15)
def update_R16C13():
    print("R16C13 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R16C13
        aref = arrRef252
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(16, 13, 16)
def update_R16C14():
    print("R16C14 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R16C14
        aref = arrRef253
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(16, 14, 16)
def update_R16C15():
    print("R16C15 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R16C15
        aref = arrRef254
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(16, 15, 16)
def update_R16C16():
    print("R16C16 button pressed.")
    if bRemoveANumberFromACell == "False":
        current_btn = btn_R16C16
        aref = arrRef255
        refresh_display_aux(current_btn, aref)
        aref['done'] = True
        update_puzzle(16, 16, 16)

def ButtonRemoveANumber(): #sender As Object, e As EventArgs) Handles ButtonRemoveANumber.Click
        bRemoveANumberFromACell = True

def build_RCS_strings():
    print("2388 Entering CheckForOnlyOneNumber.")
    for aref in not_done_arefs:
        if aref['row'] == 1:
            print("2797 row 1 nums", aref['row'])


def CheckForOnlyOneNumber():
    print("2388 Entering CheckForOnlyOneNumber.")
    for aref in arrRefs_List:
        if not aref['done']:
            for row in range(1, 16):
                strTemp = ""
            for chr in StartingString:
                # do rows, then columns, then squares
                strTemp = ""    #arrValues(i)
                char_Count = 0
            if len(aref['nums']) > 2 and aref['row'] == 1:
               print("aref info ", aref['btn'], len(aref['nums']), aref['nums'])
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

solution_1 = {}

def save_solution_1():
    print("2764 Emtered save_solution_1")
    i = 0
    for cell in arrRefs_List:
        # print("2766 cell is ", cell, cell['done'])
        current_btn = cell['btn']
        aref = eval(btn_dict[current_btn])
        arefID = "aref" + str(i)
        solution_1 = dict(aref=arefID, btn=aref['btn'], done=aref['done'], nums=aref['nums'], fg=aref['fg'])
        if cell['done'] == True:
            print("2900 solution 1", solution_1)
            # print("2768 aref0['btn'] ", arefID,  aref['btn'], aref['done'], aref['nums'], aref['fg'])
        i += 1


                 # [aref1[btn='btn_R1C2', done=False, nums="0123\n4567\n89AB\nCDEF", fg="black"]]
    # print("2766 solution 1 ", solution_1)

    # arrRef0 = dict(btn='btn_R1C1', row=1, col=1, sq=1, done=False, nums="0123\n4567\n89AB\nCDEF", width=6, height=hit,
    #                font=labelfont, fg="black")
    # with open('data.json', 'w') as f:
    #     json.dump(data, f)
    # aref0('done') = aref0('done')
    # aref0('nums') = aref0('nums')


def load_solution_1(btn_R1C1=None):
    print("2917 Entered load_solution_1")
    currentNumber = D
    aref = arrRef0
    # aref['done'] = True
    current_btn = btn_R1C1
    update_R1C1()
    # refresh_display_aux(current_btn, aref)

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
    # refresh_display_aux(current_btn, aref)
    # aref['done'] = True
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

btn_R1C1 = tk.Button(F1_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R1C1, width=6, height=hit)
btn_R1C1.grid(row=1, column=0, sticky='w')
btn_R1C1.config(font=labelfont)
# btn_R1C1.bind("<<ButtonPress>>", update_R1C1())
btn_R1C2 = Button(F1_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R1C2, width=6, height=hit)
btn_R1C2.grid(row=1, column=1, sticky='w')
btn_R1C2.config(font=labelfont)
# btn_R1C2.bind("<<ComboboxSelected>>", create_record())
btn_R1C3 = Button(F1_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R1C3, width=6, height=hit)
btn_R1C3.grid(row=1, column=2, sticky='w')
btn_R1C3.config(font=labelfont)
# btn_R1C3.bind("<<ComboboxSelected>>", create_record())
btn_R1C4 = Button(F1_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R1C4, width=6, height=hit)
btn_R1C4.grid(row=1, column=3, sticky='w')
btn_R1C4.config(font=labelfont)
btn_R1C4.bind("<<ComboboxSelected>>", create_record())

btn_R1C5 = Button(F2_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R1C5, width=6, height=hit)
btn_R1C5.grid(row=1, column=0, sticky='w')
btn_R1C5.config(font=labelfont)
# btn_R1C5.bind("<<ComboboxSelected>>", create_record())
btn_R1C6 = Button(F2_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R1C6, width=6, height=hit)
btn_R1C6.grid(row=1, column=1, sticky='w')
btn_R1C6.config(font=labelfont)
btn_R1C6.bind("<<ComboboxSelected>>", create_record())
btn_R1C7 = Button(F2_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R1C7, width=6, height=hit)
btn_R1C7.grid(row=1, column=2, sticky='w')
btn_R1C7.config(font=labelfont)
# btn_R1C7.bind("<<ComboboxSelected>>", create_record())
btn_R1C8 = Button(F2_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R1C8, width=6, height=hit)
btn_R1C8.grid(row=1, column=3, sticky='w')
btn_R1C8.config(font=labelfont)
# btn_R1C8.bind("<<ComboboxSelected>>", create_record())

btn_R1C9 = Button(F3_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R1C9, width=6, height=hit)
btn_R1C9.grid(row=1, column=0, sticky='w')
btn_R1C9.config(font=labelfont)
# btn_R1C9.bind("<<ComboboxSelected>>", create_record())
btn_R1C10 = Button(F3_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R1C10, width=6, height=hit)
btn_R1C10.grid(row=1, column=1, sticky='w')
btn_R1C10.config(font=labelfont)
# btn_R1C10.bind("<<ComboboxSelected>>", create_record())
btn_R1C11 = Button(F3_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R1C11, width=6, height=hit)
btn_R1C11.grid(row=1, column=2, sticky='w')
btn_R1C11.config(font=labelfont)
btn_R1C12 = Button(F3_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R1C12, width=6, height=hit)
btn_R1C12.grid(row=1, column=3, sticky='w')
btn_R1C12.config(font=labelfont)
# btn_R1C12.bind("<<ComboboxSelected>>", create_record())
btn_R1C13 = Button(F4_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R1C13, width=6, height=hit)
btn_R1C13.grid(row=1, column=0, sticky='w')
btn_R1C13.config(font=labelfont)
# btn_R1C13.bind("<<ComboboxSelected>>", create_record())
btn_R1C14 = Button(F4_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R1C14, width=6, height=hit)
btn_R1C14.grid(row=1, column=1, sticky='w')
btn_R1C14.config(font=labelfont)
# btn_R1C14.bind("<<ComboboxSelected>>", create_record())
btn_R1C15 = Button(F4_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R1C15, width=6, height=hit)
btn_R1C15.grid(row=1, column=2, sticky='w')
btn_R1C15.config(font=labelfont)
btn_R1C16 = Button(F4_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
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
btn_R2C1 = Button(F1_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R2C1, width=6, height=hit)
btn_R2C1.grid(row=2, column=0, sticky='w')
btn_R2C1.config(font=labelfont)
btn_R2C1.bind("<<ComboboxSelected>>", create_record())
btn_R2C2 = Button(F1_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R2C2, width=6, height=hit)
btn_R2C2.grid(row=2, column=1, sticky='w')
btn_R2C2.config(font=labelfont)
btn_R2C2.bind("<<ComboboxSelected>>", create_record())
btn_R2C3 = Button(F1_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R2C3, width=6, height=hit)
btn_R2C3.grid(row=2, column=2, sticky='w')
btn_R2C3.config(font=labelfont)
btn_R2C3.bind("<<ComboboxSelected>>", create_record())
btn_R2C4 = Button(F1_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R2C4, width=6, height=hit)
btn_R2C4.grid(row=2, column=3, sticky='w')
btn_R2C4.config(font=labelfont)
btn_R2C4.bind("<<ComboboxSelected>>", create_record())

btn_R2C5 = Button(F2_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R2C5, width=6, height=hit)
btn_R2C5.grid(row=2, column=0, sticky='w')
btn_R2C5.config(font=labelfont)
btn_R2C5.bind("<<ComboboxSelected>>", create_record())
btn_R2C6 = Button(F2_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R2C6, width=6, height=hit)
btn_R2C6.grid(row=2, column=1, sticky='w')
btn_R2C6.config(font=labelfont)
btn_R2C6.bind("<<ComboboxSelected>>", create_record())
btn_R2C7 = Button(F2_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R2C7, width=6, height=hit)
btn_R2C7.grid(row=2, column=2, sticky='w')
btn_R2C7.config(font=labelfont)
btn_R2C7.bind("<<ComboboxSelected>>", create_record())
btn_R2C8 = Button(F2_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R2C8, width=6, height=hit)
btn_R2C8.grid(row=2, column=3, sticky='w')
btn_R2C8.config(font=labelfont)
btn_R2C8.bind("<<ComboboxSelected>>", create_record())

btn_R2C9 = Button(F3_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R2C9, width=6, height=hit)
btn_R2C9.grid(row=2, column=0, sticky='w')
btn_R2C9.config(font=labelfont)
btn_R2C9.bind("<<ComboboxSelected>>", create_record())
btn_R2C10 = Button(F3_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R2C10, width=6, height=hit)
btn_R2C10.grid(row=2, column=1, sticky='w')
btn_R2C10.config(font=labelfont)
# btn_R2C10.bind("<<ComboboxSelected>>", create_record())
btn_R2C11 = Button(F3_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R2C11, width=6, height=hit)
btn_R2C11.grid(row=2, column=2, sticky='w')
btn_R2C11.config(font=labelfont)
btn_R2C12 = Button(F3_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R2C12, width=6, height=hit)
btn_R2C12.grid(row=2, column=3, sticky='w')
btn_R2C12.config(font=labelfont)
# btn_R2C12.bind("<<ComboboxSelected>>", create_record())
btn_R2C13 = Button(F4_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R2C13, width=6, height=hit)
btn_R2C13.grid(row=2, column=0, sticky='w')
btn_R2C13.config(font=labelfont)
# btn_R2C13.bind("<<ComboboxSelected>>", create_record())
btn_R2C14 = Button(F4_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R2C14, width=6, height=hit)
btn_R2C14.grid(row=2, column=1, sticky='w')
btn_R2C14.config(font=labelfont)
btn_R2C14.bind("<<ComboboxSelected>>", create_record())
btn_R2C15 = Button(F4_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R2C15, width=6, height=hit)
btn_R2C15.grid(row=2, column=2, sticky='w')
btn_R2C15.config(font=labelfont)
btn_R2C16 = Button(F4_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
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
btn_R3C1 = Button(F1_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R3C1, width=6, height=hit)
btn_R3C1.grid(row=3, column=0, sticky='w')
btn_R3C1.config(font=labelfont)
btn_R3C1.bind("<<ComboboxSelected>>", create_record())
btn_R3C2 = Button(F1_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R3C2, width=6, height=hit)
btn_R3C2.grid(row=3, column=1, sticky='w')
btn_R3C2.config(font=labelfont)
btn_R3C2.bind("<<ComboboxSelected>>", create_record())
btn_R3C3 = Button(F1_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R3C3, width=6, height=hit)
btn_R3C3.grid(row=3, column=2, sticky='w')
btn_R3C3.config(font=labelfont)
# btn_R3C3.bind("<<ComboboxSelected>>", create_record())
btn_R3C4 = Button(F1_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R3C4, width=6, height=hit)
btn_R3C4.grid(row=3, column=3, sticky='w')
btn_R3C4.config(font=labelfont)
# btn_R3C4.bind("<<ComboboxSelected>>", create_record())

btn_R3C5 = Button(F2_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R3C5, width=6, height=hit)
btn_R3C5.grid(row=3, column=0, sticky='w')
btn_R3C5.config(font=labelfont)
# btn_R3C5.bind("<<ComboboxSelected>>", create_record())
btn_R3C6 = Button(F2_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R3C6, width=6, height=hit)
btn_R3C6.grid(row=3, column=1, sticky='w')
btn_R3C6.config(font=labelfont)
# btn_R3C6.bind("<<ComboboxSelected>>", create_record())
btn_R3C7 = Button(F2_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R3C7, width=6, height=hit)
btn_R3C7.grid(row=3, column=2, sticky='w')
btn_R3C7.config(font=labelfont)
btn_R3C7.bind("<<ComboboxSelected>>", create_record())
btn_R3C8 = Button(F2_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R3C8, width=6, height=hit)
btn_R3C8.grid(row=3, column=3, sticky='w')
btn_R3C8.config(font=labelfont)
btn_R3C8.bind("<<ComboboxSelected>>", create_record())

btn_R3C9 = Button(F3_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R3C9, width=6, height=hit)
btn_R3C9.grid(row=3, column=0, sticky='w')
btn_R3C9.config(font=labelfont)
btn_R3C9.bind("<<ComboboxSelected>>", create_record())
btn_R3C10 = Button(F3_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R3C10, width=6, height=hit)
btn_R3C10.grid(row=3, column=1, sticky='w')
btn_R3C10.config(font=labelfont)
btn_R3C10.bind("<<ComboboxSelected>>", create_record())
btn_R3C11 = Button(F3_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R3C11, width=6, height=hit)
btn_R3C11.grid(row=3, column=2, sticky='w')
btn_R3C11.config(font=labelfont)
btn_R3C12 = Button(F3_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R3C12, width=6, height=hit)
btn_R3C12.grid(row=3, column=3, sticky='w')
btn_R3C12.config(font=labelfont)
btn_R3C12.bind("<<ComboboxSelected>>", create_record())
btn_R3C13 = Button(F4_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R3C13, width=6, height=hit)
btn_R3C13.grid(row=3, column=0, sticky='w')
btn_R3C13.config(font=labelfont)
btn_R3C13.bind("<<ComboboxSelected>>", create_record())
btn_R3C14 = Button(F4_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R3C14, width=6, height=hit)
btn_R3C14.grid(row=3, column=1, sticky='w')
btn_R3C14.config(font=labelfont)
btn_R3C14.bind("<<ComboboxSelected>>", create_record())
btn_R3C15 = Button(F4_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R3C15, width=6, height=hit)
btn_R3C15.grid(row=3, column=2, sticky='w')
btn_R3C15.config(font=labelfont)
btn_R3C16 = Button(F4_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
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
btn_R4C1 = Button(F1_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R4C1, width=6, height=hit)
btn_R4C1.grid(row=4, column=0, sticky='nw')
btn_R4C1.config(font=labelfont)
btn_R4C1.bind("<<ComboboxSelected>>", create_record())
btn_R4C2 = Button(F1_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R4C2, width=6, height=hit)
btn_R4C2.grid(row=4, column=1, sticky='w')
btn_R4C2.config(font=labelfont)
btn_R4C2.bind("<<ComboboxSelected>>", create_record())
btn_R4C3 = Button(F1_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R4C3, width=6, height=hit)
btn_R4C3.grid(row=4, column=2, sticky='w')
btn_R4C3.config(font=labelfont)
btn_R4C3.bind("<<ComboboxSelected>>", create_record())
btn_R4C4 = Button(F1_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R4C4, width=6, height=hit)
btn_R4C4.grid(row=4, column=3, sticky='w')
btn_R4C4.config(font=labelfont)
btn_R4C4.bind("<<ComboboxSelected>>", create_record())

btn_R4C5 = Button(F2_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R4C5, width=6, height=hit)
btn_R4C5.grid(row=4, column=0, sticky='w')
btn_R4C5.config(font=labelfont)
btn_R4C5.bind("<<ComboboxSelected>>", create_record())
btn_R4C6 = Button(F2_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R4C6, width=6, height=hit)
btn_R4C6.grid(row=4, column=1, sticky='w')
btn_R4C6.config(font=labelfont)
btn_R4C7 = Button(F2_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R4C7, width=6, height=hit)
btn_R4C7.grid(row=4, column=2, sticky='w')
btn_R4C7.config(font=labelfont)
btn_R4C8 = Button(F2_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R4C8, width=6, height=hit)
btn_R4C8.grid(row=4, column=3, sticky='w')
btn_R4C8.config(font=labelfont)
btn_R4C9 = Button(F3_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R4C9, width=6, height=hit)
btn_R4C9.grid(row=4, column=0, sticky='w')
btn_R4C9.config(font=labelfont)
btn_R4C10 = Button(F3_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R4C10, width=6, height=hit)
btn_R4C10.grid(row=4, column=1, sticky='w')
btn_R4C10.config(font=labelfont)
btn_R4C11 = Button(F3_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R4C11, width=6, height=hit)
btn_R4C11.grid(row=4, column=2, sticky='w')
btn_R4C11.config(font=labelfont)
btn_R4C12 = Button(F3_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R4C12, width=6, height=hit)
btn_R4C12.grid(row=4, column=3, sticky='w')
btn_R4C12.config(font=labelfont)
btn_R4C13 = Button(F4_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R4C13, width=6, height=hit)
btn_R4C13.grid(row=4, column=0, sticky='w')
btn_R4C13.config(font=labelfont)
btn_R4C14 = Button(F4_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R4C14, width=6, height=hit)
btn_R4C14.grid(row=4, column=1, sticky='w')
btn_R4C14.config(font=labelfont)
btn_R4C15 = Button(F4_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R4C15, width=6, height=hit)
btn_R4C15.grid(row=4, column=2, sticky='w')
btn_R4C15.config(font=labelfont)
btn_R4C16 = Button(F4_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
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
btn_R5C1 = tk.Button(F5_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R5C1, width=6, height=hit)
btn_R5C1.grid(row=1, column=0, sticky='w')
btn_R5C1.config(font=labelfont)
# btn_R1C1.bind("<<ButtonPress>>", update_R1C1())
btn_R5C2 = Button(F5_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R5C2, width=6, height=hit)
btn_R5C2.grid(row=1, column=1, sticky='w')
btn_R5C2.config(font=labelfont)
btn_R5C2.bind("<<ComboboxSelected>>", create_record())
btn_R5C3 = Button(F5_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R5C3, width=6, height=hit)
btn_R5C3.grid(row=1, column=2, sticky='w')
btn_R5C3.config(font=labelfont)
btn_R5C3.bind("<<ComboboxSelected>>", create_record())
btn_R5C4 = Button(F5_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R5C4, width=6, height=hit)
btn_R5C4.grid(row=1, column=3, sticky='w')
btn_R5C4.config(font=labelfont)
btn_R5C4.bind("<<ComboboxSelected>>", create_record())

btn_R5C5 = Button(F6_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R5C5, width=6, height=hit)
btn_R5C5.grid(row=1, column=0, sticky='w')
btn_R5C5.config(font=labelfont)
btn_R5C5.bind("<<ComboboxSelected>>", create_record())
btn_R5C6 = Button(F6_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R5C6, width=6, height=hit)
btn_R5C6.grid(row=1, column=1, sticky='w')
btn_R5C6.config(font=labelfont)
btn_R5C6.bind("<<ComboboxSelected>>", create_record())
btn_R5C7 = Button(F6_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R5C7, width=6, height=hit)
btn_R5C7.grid(row=1, column=2, sticky='w')
btn_R5C7.config(font=labelfont)
btn_R5C7.bind("<<ComboboxSelected>>", create_record())
btn_R5C8 = Button(F6_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R5C8, width=6, height=hit)
btn_R5C8.grid(row=1, column=3, sticky='w')
btn_R5C8.config(font=labelfont)
btn_R5C8.bind("<<ComboboxSelected>>", create_record())

btn_R5C9 = Button(F7_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R5C9, width=6, height=hit)
btn_R5C9.grid(row=1, column=0, sticky='w')
btn_R5C9.config(font=labelfont)
btn_R5C9.bind("<<ComboboxSelected>>", create_record())
btn_R5C10 = Button(F7_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R5C10, width=6, height=hit)
btn_R5C10.grid(row=1, column=1, sticky='w')
btn_R5C10.config(font=labelfont)
btn_R5C10.bind("<<ComboboxSelected>>", create_record())
btn_R5C11 = Button(F7_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R5C11, width=6, height=hit)
btn_R5C11.grid(row=1, column=2, sticky='w')
btn_R5C11.config(font=labelfont)
btn_R5C12 = Button(F7_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R5C12, width=6, height=hit)
btn_R5C12.grid(row=1, column=3, sticky='w')
btn_R5C12.config(font=labelfont)
btn_R5C12.bind("<<ComboboxSelected>>", create_record())
btn_R5C13 = Button(F8_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R5C13, width=6, height=hit)
btn_R5C13.grid(row=1, column=0, sticky='w')
btn_R5C13.config(font=labelfont)
btn_R5C13.bind("<<ComboboxSelected>>", create_record())
btn_R5C14 = Button(F8_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R5C14, width=6, height=hit)
btn_R5C14.grid(row=1, column=1, sticky='w')
btn_R5C14.config(font=labelfont)
btn_R5C14.bind("<<ComboboxSelected>>", create_record())
btn_R5C15 = Button(F8_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R5C15, width=6, height=hit)
btn_R5C15.grid(row=1, column=2, sticky='w')
btn_R5C15.config(font=labelfont)
btn_R5C16 = Button(F8_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R5C16, width=6, height=hit)
btn_R5C16.grid(row=1, column=3, sticky='w')
btn_R5C16.config(font=labelfont)
# btn_R1C16.bind("<<ComboboxSelected>>", create_record())
# btn_x = Button(fn_frame, wraplength=40, justify=LEFT, text='0',
#             command=set_current_num_to_0, width=6, height=hit)
# btn_x.grid(row=1, column=0, sticky='nw')
# btn_x.config(font=entryfont)
# btn_y = Button(fn_frame, wraplength=40, justify=LEFT, text='1',
#             command=set_current_num_to_1, width=6, height=hit)
# btn_y.grid(row=1, column=1, sticky='n')
# btn_y.config(font=entryfont)
# btn_z = Button(fn_frame, wraplength=40, justify=LEFT, text='2',
#             command=set_current_num_to_2, width=6, height=hit)
# btn_z.grid(row=1, column=2, sticky='n')
# btn_z.config(font=entryfont)
# btn_z = Button(fn_frame, wraplength=40, justify=LEFT, text='3',
#             command=set_current_num_to_3, width=6, height=hit)
# btn_z.grid(row=1, column=3, sticky='n')
# btn_z.config(font=entryfont)
btn_R6C1 = tk.Button(F5_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R6C1, width=6, height=hit)
btn_R6C1.grid(row=2, column=0, sticky='w')
btn_R6C1.config(font=labelfont)
# btn_R6C1.bind("<<ButtonPress>>", update_R1C1())
btn_R6C2 = Button(F5_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R6C2, width=6, height=hit)
btn_R6C2.grid(row=2, column=1, sticky='w')
btn_R6C2.config(font=labelfont)
btn_R6C2.bind("<<ComboboxSelected>>", create_record())
btn_R6C3 = Button(F5_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R6C3, width=6, height=hit)
btn_R6C3.grid(row=2, column=2, sticky='w')
btn_R6C3.config(font=labelfont)
btn_R6C3.bind("<<ComboboxSelected>>", create_record())
btn_R6C4 = Button(F5_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R6C4, width=6, height=hit)
btn_R6C4.grid(row=2, column=3, sticky='w')
btn_R6C4.config(font=labelfont)
btn_R6C4.bind("<<ComboboxSelected>>", create_record())

btn_R6C5 = Button(F6_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R6C5, width=6, height=hit)
btn_R6C5.grid(row=2, column=0, sticky='w')
btn_R6C5.config(font=labelfont)
btn_R6C5.bind("<<ComboboxSelected>>", create_record())
btn_R6C6 = Button(F6_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R6C6, width=6, height=hit)
btn_R6C6.grid(row=2, column=1, sticky='w')
btn_R6C6.config(font=labelfont)
btn_R6C6.bind("<<ComboboxSelected>>", create_record())
btn_R6C7 = Button(F6_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R6C7, width=6, height=hit)
btn_R6C7.grid(row=2, column=2, sticky='w')
btn_R6C7.config(font=labelfont)
btn_R6C7.bind("<<ComboboxSelected>>", create_record())
btn_R6C8 = Button(F6_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R6C8, width=6, height=hit)
btn_R6C8.grid(row=2, column=3, sticky='w')
btn_R6C8.config(font=labelfont)
btn_R6C8.bind("<<ComboboxSelected>>", create_record())

btn_R6C9 = Button(F7_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R6C9, width=6, height=hit)
btn_R6C9.grid(row=2, column=0, sticky='w')
btn_R6C9.config(font=labelfont)
btn_R6C9.bind("<<ComboboxSelected>>", create_record())
btn_R6C10 = Button(F7_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R6C10, width=6, height=hit)
btn_R6C10.grid(row=2, column=1, sticky='w')
btn_R6C10.config(font=labelfont)
btn_R6C10.bind("<<ComboboxSelected>>", create_record())
btn_R6C11 = Button(F7_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R6C11, width=6, height=hit)
btn_R6C11.grid(row=2, column=2, sticky='w')
btn_R6C11.config(font=labelfont)
btn_R6C12 = Button(F7_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R6C12, width=6, height=hit)
btn_R6C12.grid(row=2, column=3, sticky='w')
btn_R6C12.config(font=labelfont)
btn_R6C12.bind("<<ComboboxSelected>>", create_record())
btn_R6C13 = Button(F8_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R6C13, width=6, height=hit)
btn_R6C13.grid(row=2, column=0, sticky='w')
btn_R6C13.config(font=labelfont)
btn_R6C13.bind("<<ComboboxSelected>>", create_record())
btn_R6C14 = Button(F8_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R6C14, width=6, height=hit)
btn_R6C14.grid(row=2, column=1, sticky='w')
btn_R6C14.config(font=labelfont)
btn_R6C14.bind("<<ComboboxSelected>>", create_record())
btn_R6C15 = Button(F8_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R6C15, width=6, height=hit)
btn_R6C15.grid(row=2, column=2, sticky='w')
btn_R6C15.config(font=labelfont)
btn_R6C16 = Button(F8_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R6C16, width=6, height=hit)
btn_R6C16.grid(row=2, column=3, sticky='w')
btn_R6C16.config(font=labelfont)
# ***********
btn_R7C1 = tk.Button(F5_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R7C1, width=6, height=hit)
btn_R7C1.grid(row=3, column=0, sticky='w')
btn_R7C1.config(font=labelfont)
# btn_R1C1.bind("<<ButtonPress>>", update_R1C1())
btn_R7C2 = Button(F5_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R7C2, width=6, height=hit)
btn_R7C2.grid(row=3, column=1, sticky='w')
btn_R7C2.config(font=labelfont)
btn_R7C2.bind("<<ComboboxSelected>>", create_record())
btn_R7C3 = Button(F5_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R7C3, width=6, height=hit)
btn_R7C3.grid(row=3, column=2, sticky='w')
btn_R7C3.config(font=labelfont)
btn_R7C3.bind("<<ComboboxSelected>>", create_record())
btn_R7C4 = Button(F5_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R7C4, width=6, height=hit)
btn_R7C4.grid(row=3, column=3, sticky='w')
btn_R7C4.config(font=labelfont)
btn_R7C4.bind("<<ComboboxSelected>>", create_record())

btn_R7C5 = Button(F6_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R7C5, width=6, height=hit)
btn_R7C5.grid(row=3, column=0, sticky='w')
btn_R7C5.config(font=labelfont)
btn_R7C5.bind("<<ComboboxSelected>>", create_record())
btn_R7C6 = Button(F6_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R7C6, width=6, height=hit)
btn_R7C6.grid(row=3, column=1, sticky='w')
btn_R7C6.config(font=labelfont)
btn_R7C6.bind("<<ComboboxSelected>>", create_record())
btn_R7C7 = Button(F6_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R7C7, width=6, height=hit)
btn_R7C7.grid(row=3, column=2, sticky='w')
btn_R7C7.config(font=labelfont)
btn_R7C7.bind("<<ComboboxSelected>>", create_record())
btn_R7C8 = Button(F6_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R7C8, width=6, height=hit)
btn_R7C8.grid(row=3, column=3, sticky='w')
btn_R7C8.config(font=labelfont)
btn_R7C8.bind("<<ComboboxSelected>>", create_record())

btn_R7C9 = Button(F7_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R7C9, width=6, height=hit)
btn_R7C9.grid(row=3, column=0, sticky='w')
btn_R7C9.config(font=labelfont)
btn_R7C9.bind("<<ComboboxSelected>>", create_record())
btn_R7C10 = Button(F7_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R7C10, width=6, height=hit)
btn_R7C10.grid(row=3, column=1, sticky='w')
btn_R7C10.config(font=labelfont)
btn_R7C10.bind("<<ComboboxSelected>>", create_record())
btn_R7C11 = Button(F7_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R7C11, width=6, height=hit)
btn_R7C11.grid(row=3, column=2, sticky='w')
btn_R7C11.config(font=labelfont)
btn_R7C12 = Button(F7_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R7C12, width=6, height=hit)
btn_R7C12.grid(row=3, column=3, sticky='w')
btn_R7C12.config(font=labelfont)
btn_R7C12.bind("<<ComboboxSelected>>", create_record())
btn_R7C13 = Button(F8_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R7C13, width=6, height=hit)
btn_R7C13.grid(row=3, column=0, sticky='w')
btn_R7C13.config(font=labelfont)
btn_R7C13.bind("<<ComboboxSelected>>", create_record())
btn_R7C14 = Button(F8_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R7C14, width=6, height=hit)
btn_R7C14.grid(row=3, column=1, sticky='w')
btn_R7C14.config(font=labelfont)
btn_R7C14.bind("<<ComboboxSelected>>", create_record())
btn_R7C15 = Button(F8_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R7C15, width=6, height=hit)
btn_R7C15.grid(row=3, column=2, sticky='w')
btn_R7C15.config(font=labelfont)
btn_R7C16 = Button(F8_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R7C16, width=6, height=hit)
btn_R7C16.grid(row=3, column=3, sticky='w')
btn_R7C16.config(font=labelfont)
# btn_R1C16.bind("<<ComboboxSelected>>", create_record())
btn_test = Button(fn_frame, wraplength=40, justify=LEFT, text='Check\nonly\none\nnumber',
            command=CheckForOnlyOneNumber, width=6, height=hit)
btn_test.grid(row=0, column=0, sticky='nw')
btn_test.config(font=entryfont)
find_1 = Button(fn_frame, wraplength=40, justify=LEFT, text='Find\nSingle',
            command=set_current_num_to_1, width=6, height=hit)
find_1.grid(row=0, column=1, sticky='nw')
find_1.config(font=entryfont)
find_2 = Button(fn_frame, wraplength=40, justify=LEFT, text='Find\nDuple',
            command=set_current_num_to_2, width=6, height=hit)
find_2.grid(row=0, column=2, sticky='nw')
find_2.config(font=entryfont)
find_3 = Button(fn_frame, wraplength=40, justify=LEFT, text='Find\nDuple',
            command=set_current_num_to_3, width=6, height=hit)
find_3.grid(row=0, column=3, sticky='nw')
find_3.config(font=entryfont)
btn_R8C1 = tk.Button(F5_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R8C1, width=6, height=hit)
btn_R8C1.grid(row=4, column=0, sticky='w')
btn_R8C1.config(font=labelfont)
# btn_R8C1.bind("<<ButtonPress>>", update_R1C1())
btn_R8C2 = Button(F5_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R8C2, width=6, height=hit)
btn_R8C2.grid(row=4, column=1, sticky='w')
btn_R8C2.config(font=labelfont)
btn_R8C2.bind("<<ComboboxSelected>>", create_record())
btn_R8C3 = Button(F5_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R8C3, width=6, height=hit)
btn_R8C3.grid(row=4, column=2, sticky='w')
btn_R8C3.config(font=labelfont)
btn_R8C3.bind("<<ComboboxSelected>>", create_record())
btn_R8C4 = Button(F5_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R8C4, width=6, height=hit)
btn_R8C4.grid(row=4, column=3, sticky='w')
btn_R8C4.config(font=labelfont)
btn_R8C4.bind("<<ComboboxSelected>>", create_record())

btn_R8C5 = Button(F6_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R8C5, width=6, height=hit)
btn_R8C5.grid(row=4, column=0, sticky='w')
btn_R8C5.config(font=labelfont)
btn_R8C5.bind("<<ComboboxSelected>>", create_record())
btn_R8C6 = Button(F6_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R8C6, width=6, height=hit)
btn_R8C6.grid(row=4, column=1, sticky='w')
btn_R8C6.config(font=labelfont)
btn_R8C6.bind("<<ComboboxSelected>>", create_record())
btn_R8C7 = Button(F6_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R8C7, width=6, height=hit)
btn_R8C7.grid(row=4, column=2, sticky='w')
btn_R8C7.config(font=labelfont)
btn_R8C7.bind("<<ComboboxSelected>>", create_record())
btn_R8C8 = Button(F6_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R8C8, width=6, height=hit)
btn_R8C8.grid(row=4, column=3, sticky='w')
btn_R8C8.config(font=labelfont)
btn_R8C8.bind("<<ComboboxSelected>>", create_record())

btn_R8C9 = Button(F7_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R8C9, width=6, height=hit)
btn_R8C9.grid(row=4, column=0, sticky='w')
btn_R8C9.config(font=labelfont)
btn_R8C9.bind("<<ComboboxSelected>>", create_record())
btn_R8C10 = Button(F7_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R8C10, width=6, height=hit)
btn_R8C10.grid(row=4, column=1, sticky='w')
btn_R8C10.config(font=labelfont)
btn_R8C10.bind("<<ComboboxSelected>>", create_record())
btn_R8C11 = Button(F7_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R8C11, width=6, height=hit)
btn_R8C11.grid(row=4, column=2, sticky='w')
btn_R8C11.config(font=labelfont)
btn_R8C12 = Button(F7_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R8C12, width=6, height=hit)
btn_R8C12.grid(row=4, column=3, sticky='w')
btn_R8C12.config(font=labelfont)
btn_R8C12.bind("<<ComboboxSelected>>", create_record())
btn_R8C13 = Button(F8_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R8C13, width=6, height=hit)
btn_R8C13.grid(row=4, column=0, sticky='w')
btn_R8C13.config(font=labelfont)
btn_R8C13.bind("<<ComboboxSelected>>", create_record())
btn_R8C14 = Button(F8_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R8C14, width=6, height=hit)
btn_R8C14.grid(row=4, column=1, sticky='w')
btn_R8C14.config(font=labelfont)
btn_R8C14.bind("<<ComboboxSelected>>", create_record())
btn_R8C15 = Button(F8_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R8C15, width=6, height=hit)
btn_R8C15.grid(row=4, column=2, sticky='w')
btn_R8C15.config(font=labelfont)
btn_R8C16 = Button(F8_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R8C16, width=6, height=hit)
btn_R8C16.grid(row=4, column=3, sticky='w')
btn_R8C16.config(font=labelfont)

################

btn_R9C1 = Button(F9_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R9C1, width=6, height=hit)
btn_R9C1.grid(row=1, column=0, sticky='w')
btn_R9C1.config(font=labelfont)
btn_R9C1.bind("<<ComboboxSelected>>", create_record())
btn_R9C2 = Button(F9_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R9C2, width=6, height=hit)
btn_R9C2.grid(row=1, column=1, sticky='w')
btn_R9C2.config(font=labelfont)
btn_R9C2.bind("<<ComboboxSelected>>", create_record())
btn_R9C3 = Button(F9_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R9C3, width=6, height=hit)
btn_R9C3.grid(row=1, column=2, sticky='w')
btn_R9C3.config(font=labelfont)
btn_R9C3.bind("<<ComboboxSelected>>", create_record())
btn_R9C4 = Button(F9_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R9C4, width=6, height=hit)
btn_R9C4.grid(row=1, column=3, sticky='w')
btn_R9C4.config(font=labelfont)
btn_R9C4.bind("<<ComboboxSelected>>", create_record())

btn_R9C5 = Button(F10_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R9C5, width=6, height=hit)
btn_R9C5.grid(row=1, column=0, sticky='w')
btn_R9C5.config(font=labelfont)
btn_R9C5.bind("<<ComboboxSelected>>", create_record())
btn_R9C6 = Button(F10_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R9C6, width=6, height=hit)
btn_R9C6.grid(row=1, column=1, sticky='w')
btn_R9C6.config(font=labelfont)
btn_R9C6.bind("<<ComboboxSelected>>", create_record())
btn_R9C7 = Button(F10_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R9C7, width=6, height=hit)
btn_R9C7.grid(row=1, column=2, sticky='w')
btn_R9C7.config(font=labelfont)
btn_R9C7.bind("<<ComboboxSelected>>", create_record())
btn_R9C8 = Button(F10_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R9C8, width=6, height=hit)
btn_R9C8.grid(row=1, column=3, sticky='w')
btn_R9C8.config(font=labelfont)
btn_R9C8.bind("<<ComboboxSelected>>", create_record())

btn_R9C9 = Button(F11_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R2C9, width=6, height=hit)
btn_R9C9.grid(row=1, column=0, sticky='w')
btn_R9C9.config(font=labelfont)
btn_R9C9.bind("<<ComboboxSelected>>", create_record())
btn_R9C10 = Button(F11_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R9C10, width=6, height=hit)
btn_R9C10.grid(row=1, column=1, sticky='w')
btn_R9C10.config(font=labelfont)
btn_R9C10.bind("<<ComboboxSelected>>", create_record())
btn_R9C11 = Button(F11_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R9C11, width=6, height=hit)
btn_R9C11.grid(row=1, column=2, sticky='w')
btn_R9C11.config(font=labelfont)
btn_R9C12 = Button(F11_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R9C12, width=6, height=hit)
btn_R9C12.grid(row=1, column=3, sticky='w')
btn_R9C12.config(font=labelfont)
btn_R9C12.bind("<<ComboboxSelected>>", create_record())
btn_R9C13 = Button(F12_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R9C13, width=6, height=hit)
btn_R9C13.grid(row=1, column=0, sticky='w')
btn_R9C13.config(font=labelfont)
btn_R9C13.bind("<<ComboboxSelected>>", create_record())
btn_R9C14 = Button(F12_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R9C14, width=6, height=hit)
btn_R9C14.grid(row=1, column=1, sticky='w')
btn_R9C14.config(font=labelfont)
btn_R9C14.bind("<<ComboboxSelected>>", create_record())
btn_R9C15 = Button(F12_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R9C15, width=6, height=hit)
btn_R9C15.grid(row=1, column=2, sticky='w')
btn_R9C15.config(font=labelfont)
btn_R9C16 = Button(F12_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R9C16, width=6, height=hit)
btn_R9C16.grid(row=1, column=3, sticky='w')
btn_R9C16.config(font=labelfont)
# btn_R2C16.bind("<<ComboboxSelected>>", create_record())
btn_w = Button(fn_frame, wraplength=40, justify=LEFT, text='w',
            command=set_current_num_to_4, width=6, height=hit)
btn_w.grid(row=2, column=0, sticky='nw')
btn_w.config(font=entryfont)
btn_x = Button(fn_frame, wraplength=40, justify=LEFT, text='x',
            command=set_current_num_to_5, width=6, height=hit)
btn_x.grid(row=2, column=1, sticky='nw')
btn_x.config(font=entryfont)
btn_y = Button(fn_frame, wraplength=40, justify=LEFT, text='y',
            command=set_current_num_to_6, width=6, height=hit)
btn_y.grid(row=2, column=2, sticky='nw')
btn_y.config(font=entryfont)
btn_z = Button(fn_frame, wraplength=48, justify=LEFT, text='z',
            command=set_current_num_to_7, width=6, height=hit)
btn_z.grid(row=2, column=3, sticky='nw')
btn_z.config(font=entryfont)
btn_z.bind("<<ButtonPress>>", set_current_num_to_7)
###
btn_a = Button(fn_frame, wraplength=40, justify=LEFT, text='a',
            command=set_current_num_to_4, width=6, height=hit)
btn_a.grid(row=3, column=0, sticky='nw')
btn_a.config(font=entryfont)
btn_b = Button(fn_frame, wraplength=40, justify=LEFT, text='b',
            command=set_current_num_to_5, width=6, height=hit)
btn_b.grid(row=3, column=1, sticky='nw')
btn_b.config(font=entryfont)
btn_c = Button(fn_frame, wraplength=40, justify=LEFT, text='c',
            command=set_current_num_to_6, width=6, height=hit)
btn_c.grid(row=3, column=2, sticky='nw')
btn_c.config(font=entryfont)
btn_d = Button(fn_frame, wraplength=48, justify=LEFT, text='d',
            command=set_current_num_to_7, width=6, height=hit)
btn_d.grid(row=3, column=3, sticky='nw')
btn_d.config(font=entryfont)
btn_d.bind("<<ButtonPress>>", set_current_num_to_7)

btn_e = Button(fn_frame, wraplength=40, justify=LEFT, text='e',
            command=set_current_num_to_4, width=6, height=hit)
btn_e.grid(row=4, column=0, sticky='nw')
btn_e.config(font=entryfont)
btn_load = Button(fn_frame, wraplength=40, justify=LEFT, text='Load\nsoln',
            command=load_solution_1, width=6, height=hit)
btn_load.grid(row=4, column=1, sticky='nw')
btn_load.config(font=entryfont)
btn_g = Button(fn_frame, wraplength=40, justify=LEFT, text='Make\nRCS',
            command=make_RCS_nums, width=6, height=hit)
btn_g.grid(row=4, column=2, sticky='nw')
btn_g.config(font=entryfont)
btn_h = Button(fn_frame, wraplength=48, justify=LEFT, text='save\nsol\n1',
            command=save_solution_1, width=6, height=hit)
btn_h.grid(row=4, column=3, sticky='nw')
btn_h.config(font=entryfont)
btn_h.bind("<<ButtonPress>>", set_current_num_to_7)
#%%%%%%%%%%%%%
btn_R10C1 = Button(F9_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R10C1, width=6, height=hit)
btn_R10C1.grid(row=2, column=0, sticky='w')
btn_R10C1.config(font=labelfont)
btn_R10C2 = Button(F9_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R10C2, width=6, height=hit)
btn_R10C2.grid(row=2, column=1, sticky='w')
btn_R10C2.config(font=labelfont)
btn_R10C3 = Button(F9_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R10C3, width=6, height=hit)
btn_R10C3.grid(row=2, column=2, sticky='w')
btn_R10C3.config(font=labelfont)
btn_R10C4 = Button(F9_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R10C4, width=6, height=hit)
btn_R10C4.grid(row=2, column=3, sticky='w')
btn_R10C4.config(font=labelfont)
btn_R10C5 = Button(F10_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R10C5, width=6, height=hit)
btn_R10C5.grid(row=2, column=0, sticky='w')
btn_R10C5.config(font=labelfont)
btn_R10C6 = Button(F10_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R10C6, width=6, height=hit)
btn_R10C6.grid(row=2, column=1, sticky='w')
btn_R10C6.config(font=labelfont)
btn_R10C7 = Button(F10_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R10C7, width=6, height=hit)
btn_R10C7.grid(row=2, column=2, sticky='w')
btn_R10C7.config(font=labelfont)
btn_R10C8 = Button(F10_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R10C8, width=6, height=hit)
btn_R10C8.grid(row=2, column=3, sticky='w')
btn_R10C8.config(font=labelfont)
btn_R10C9 = Button(F11_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R10C9, width=6, height=hit)
btn_R10C9.grid(row=2, column=0, sticky='w')
btn_R10C9.config(font=labelfont)
btn_R10C10 = Button(F11_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R10C10, width=6, height=hit)
btn_R10C10.grid(row=2, column=1, sticky='w')
btn_R10C10.config(font=labelfont)
btn_R10C11 = Button(F11_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R10C11, width=6, height=hit)
btn_R10C11.grid(row=2, column=2, sticky='w')
btn_R10C11.config(font=labelfont)
btn_R10C12 = Button(F11_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R10C12, width=6, height=hit)
btn_R10C12.grid(row=2, column=3, sticky='w')
btn_R10C12.config(font=labelfont)
btn_R10C13 = Button(F12_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R10C13, width=6, height=hit)
btn_R10C13.grid(row=2, column=0, sticky='w')
btn_R10C13.config(font=labelfont)
btn_R10C14 = Button(F12_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R10C14, width=6, height=hit)
btn_R10C14.grid(row=2, column=1, sticky='w')
btn_R10C14.config(font=labelfont)
btn_R10C15 = Button(F12_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R10C15, width=6, height=hit)
btn_R10C15.grid(row=2, column=2, sticky='w')
btn_R10C15.config(font=labelfont)
btn_R10C16 = Button(F12_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R10C16, width=6, height=hit)
btn_R10C16.grid(row=2, column=3, sticky='w')
btn_R10C16.config(font=labelfont)
#111
btn_R11C1 = Button(F9_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R11C1, width=6, height=hit)
btn_R11C1.grid(row=3, column=0, sticky='w')
btn_R11C1.config(font=labelfont)
btn_R11C2 = Button(F9_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R11C2, width=6, height=hit)
btn_R11C2.grid(row=3, column=1, sticky='w')
btn_R11C2.config(font=labelfont)
btn_R11C3 = Button(F9_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R11C3, width=6, height=hit)
btn_R11C3.grid(row=3, column=2, sticky='w')
btn_R11C3.config(font=labelfont)
btn_R11C4 = Button(F9_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R11C4, width=6, height=hit)
btn_R11C4.grid(row=3, column=3, sticky='w')
btn_R11C4.config(font=labelfont)
btn_R11C5 = Button(F10_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R11C5, width=6, height=hit)
btn_R11C5.grid(row=3, column=0, sticky='w')
btn_R11C5.config(font=labelfont)
btn_R11C6 = Button(F10_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R11C6, width=6, height=hit)
btn_R11C6.grid(row=3, column=1, sticky='w')
btn_R11C6.config(font=labelfont)
btn_R11C7 = Button(F10_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R11C7, width=6, height=hit)
btn_R11C7.grid(row=3, column=2, sticky='w')
btn_R11C7.config(font=labelfont)
btn_R11C8 = Button(F10_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R11C8, width=6, height=hit)
btn_R11C8.grid(row=3, column=3, sticky='w')
btn_R11C8.config(font=labelfont)
btn_R11C9 = Button(F11_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R11C9, width=6, height=hit)
btn_R11C9.grid(row=3, column=0, sticky='w')
btn_R11C9.config(font=labelfont)
btn_R11C10 = Button(F11_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R11C10, width=6, height=hit)
btn_R11C10.grid(row=3, column=1, sticky='w')
btn_R11C10.config(font=labelfont)
btn_R11C11 = Button(F11_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R11C11, width=6, height=hit)
btn_R11C11.grid(row=3, column=2, sticky='w')
btn_R11C11.config(font=labelfont)
btn_R11C12 = Button(F11_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R11C12, width=6, height=hit)
btn_R11C12.grid(row=3, column=3, sticky='w')
btn_R11C12.config(font=labelfont)
btn_R11C13 = Button(F12_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R11C13, width=6, height=hit)
btn_R11C13.grid(row=3, column=0, sticky='w')
btn_R11C13.config(font=labelfont)
btn_R11C14 = Button(F12_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R11C14, width=6, height=hit)
btn_R11C14.grid(row=3, column=1, sticky='w')
btn_R11C14.config(font=labelfont)
btn_R11C15 = Button(F12_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R11C15, width=6, height=hit)
btn_R11C15.grid(row=3, column=2, sticky='w')
btn_R11C15.config(font=labelfont)
btn_R11C16 = Button(F12_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R11C16, width=6, height=hit)
btn_R11C16.grid(row=3, column=3, sticky='w')
btn_R11C16.config(font=labelfont)
btn_R12C1 = Button(F9_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R12C1, width=6, height=hit)
btn_R12C1.grid(row=4, column=0, sticky='w')
btn_R12C1.config(font=labelfont)
btn_R12C2 = Button(F9_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R12C2, width=6, height=hit)
btn_R12C2.grid(row=4, column=1, sticky='w')
btn_R12C2.config(font=labelfont)
btn_R12C3 = Button(F9_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R12C3, width=6, height=hit)
btn_R12C3.grid(row=4, column=2, sticky='w')
btn_R12C3.config(font=labelfont)
btn_R12C4 = Button(F9_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R12C4, width=6, height=hit)
btn_R12C4.grid(row=4, column=3, sticky='w')
btn_R12C4.config(font=labelfont)
btn_R12C5 = Button(F10_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R12C5, width=6, height=hit)
btn_R12C5.grid(row=4, column=0, sticky='w')
btn_R12C5.config(font=labelfont)
btn_R12C6 = Button(F10_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R12C6, width=6, height=hit)
btn_R12C6.grid(row=4, column=1, sticky='w')
btn_R12C6.config(font=labelfont)
btn_R12C7 = Button(F10_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R12C7, width=6, height=hit)
btn_R12C7.grid(row=4, column=2, sticky='w')
btn_R12C7.config(font=labelfont)
btn_R12C8 = Button(F10_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R12C8, width=6, height=hit)
btn_R12C8.grid(row=4, column=3, sticky='w')
btn_R12C8.config(font=labelfont)
btn_R12C9 = Button(F11_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R12C9, width=6, height=hit)
btn_R12C9.grid(row=4, column=0, sticky='w')
btn_R12C9.config(font=labelfont)
btn_R12C10 = Button(F11_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R12C10, width=6, height=hit)
btn_R12C10.grid(row=4, column=1, sticky='w')
btn_R12C10.config(font=labelfont)
btn_R12C11 = Button(F11_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R12C11, width=6, height=hit)
btn_R12C11.grid(row=4, column=2, sticky='w')
btn_R12C11.config(font=labelfont)
btn_R12C12 = Button(F11_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R12C12, width=6, height=hit)
btn_R12C12.grid(row=4, column=3, sticky='w')
btn_R12C12.config(font=labelfont)
btn_R12C13 = Button(F12_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R12C13, width=6, height=hit)
btn_R12C13.grid(row=4, column=0, sticky='w')
btn_R12C13.config(font=labelfont)
btn_R12C14 = Button(F12_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R12C14, width=6, height=hit)
btn_R12C14.grid(row=4, column=1, sticky='w')
btn_R12C14.config(font=labelfont)
btn_R12C15 = Button(F12_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R12C15, width=6, height=hit)
btn_R12C15.grid(row=4, column=2, sticky='w')
btn_R12C15.config(font=labelfont)
btn_R12C16 = Button(F12_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R12C16, width=6, height=hit)
btn_R12C16.grid(row=4, column=3, sticky='w')
btn_R12C16.config(font=labelfont)
btn_R13C1 = Button(F13_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R13C1, width=6, height=hit)
btn_R13C1.grid(row=0, column=0, sticky='w')
btn_R13C1.config(font=labelfont)
btn_R13C2 = Button(F13_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R13C2, width=6, height=hit)
btn_R13C2.grid(row=0, column=1, sticky='w')
btn_R13C2.config(font=labelfont)
btn_R13C3 = Button(F13_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R13C3, width=6, height=hit)
btn_R13C3.grid(row=0, column=2, sticky='w')
btn_R13C3.config(font=labelfont)
btn_R13C4 = Button(F13_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R13C4, width=6, height=hit)
btn_R13C4.grid(row=0, column=3, sticky='w')
btn_R13C4.config(font=labelfont)
btn_R13C5 = Button(F14_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R13C5, width=6, height=hit)
btn_R13C5.grid(row=0, column=0, sticky='w')
btn_R13C5.config(font=labelfont)
btn_R13C6 = Button(F14_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R13C6, width=6, height=hit)
btn_R13C6.grid(row=0, column=1, sticky='w')
btn_R13C6.config(font=labelfont)
btn_R13C7 = Button(F14_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R13C7, width=6, height=hit)
btn_R13C7.grid(row=0, column=2, sticky='w')
btn_R13C7.config(font=labelfont)
btn_R13C8 = Button(F14_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R13C8, width=6, height=hit)
btn_R13C8.grid(row=0, column=3, sticky='w')
btn_R13C8.config(font=labelfont)
btn_R13C9 = Button(F15_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R13C9, width=6, height=hit)
btn_R13C9.grid(row=0, column=0, sticky='w')
btn_R13C9.config(font=labelfont)
btn_R13C10 = Button(F15_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R13C10, width=6, height=hit)
btn_R13C10.grid(row=0, column=1, sticky='w')
btn_R13C10.config(font=labelfont)
btn_R13C11 = Button(F15_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R13C11, width=6, height=hit)
btn_R13C11.grid(row=0, column=2, sticky='w')
btn_R13C11.config(font=labelfont)
btn_R13C12 = Button(F15_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R13C12, width=6, height=hit)
btn_R13C12.grid(row=0, column=3, sticky='w')
btn_R13C12.config(font=labelfont)
btn_R13C13 = Button(F16_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R13C13, width=6, height=hit)
btn_R13C13.grid(row=0, column=0, sticky='w')
btn_R13C13.config(font=labelfont)
btn_R13C14 = Button(F16_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R13C14, width=6, height=hit)
btn_R13C14.grid(row=0, column=1, sticky='w')
btn_R13C14.config(font=labelfont)
btn_R13C15 = Button(F16_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R13C15, width=6, height=hit)
btn_R13C15.grid(row=0, column=2, sticky='w')
btn_R13C15.config(font=labelfont)
btn_R13C16 = Button(F16_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R13C16, width=6, height=hit)
btn_R13C16.grid(row=0, column=3, sticky='w')
btn_R13C16.config(font=labelfont)

btn_R14C1 = Button(F13_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R14C1, width=6, height=hit)
btn_R14C1.grid(row=1, column=0, sticky='w')
btn_R14C1.config(font=labelfont)
btn_R14C2 = Button(F13_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R14C2, width=6, height=hit)
btn_R14C2.grid(row=1, column=1, sticky='w')
btn_R14C2.config(font=labelfont)
btn_R14C3 = Button(F13_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R14C3, width=6, height=hit)
btn_R14C3.grid(row=1, column=2, sticky='w')
btn_R14C3.config(font=labelfont)
btn_R14C4 = Button(F13_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R14C4, width=6, height=hit)
btn_R14C4.grid(row=1, column=3, sticky='w')
btn_R14C4.config(font=labelfont)
btn_R14C5 = Button(F14_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R14C5, width=6, height=hit)
btn_R14C5.grid(row=1, column=0, sticky='w')
btn_R14C5.config(font=labelfont)
btn_R14C6 = Button(F14_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R14C6, width=6, height=hit)
btn_R14C6.grid(row=1, column=1, sticky='w')
btn_R14C6.config(font=labelfont)
btn_R14C7 = Button(F14_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R14C7, width=6, height=hit)
btn_R14C7.grid(row=1, column=2, sticky='w')
btn_R14C7.config(font=labelfont)
btn_R14C8 = Button(F14_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R14C8, width=6, height=hit)
btn_R14C8.grid(row=1, column=3, sticky='w')
btn_R14C8.config(font=labelfont)
btn_R14C9 = Button(F15_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R14C9, width=6, height=hit)
btn_R14C9.grid(row=1, column=0, sticky='w')
btn_R14C9.config(font=labelfont)
btn_R14C10 = Button(F15_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R14C10, width=6, height=hit)
btn_R14C10.grid(row=1, column=1, sticky='w')
btn_R14C10.config(font=labelfont)
btn_R14C11 = Button(F15_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R14C11, width=6, height=hit)
btn_R14C11.grid(row=1, column=2, sticky='w')
btn_R14C11.config(font=labelfont)
btn_R14C12 = Button(F15_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R14C12, width=6, height=hit)
btn_R14C12.grid(row=1, column=3, sticky='w')
btn_R14C12.config(font=labelfont)
btn_R14C13 = Button(F16_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R14C13, width=6, height=hit)
btn_R14C13.grid(row=1, column=0, sticky='w')
btn_R14C13.config(font=labelfont)
btn_R14C14 = Button(F16_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R14C14, width=6, height=hit)
btn_R14C14.grid(row=1, column=1, sticky='w')
btn_R14C14.config(font=labelfont)
btn_R14C15 = Button(F16_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R14C15, width=6, height=hit)
btn_R14C15.grid(row=1, column=2, sticky='w')
btn_R14C15.config(font=labelfont)
btn_R14C16 = Button(F16_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R14C16, width=6, height=hit)
btn_R14C16.grid(row=1, column=3, sticky='w')
btn_R14C16.config(font=labelfont)
#start 16
btn_R15C1 = Button(F13_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R15C1, width=6, height=hit)
btn_R15C1.grid(row=2, column=0, sticky='w')
btn_R15C1.config(font=labelfont)
btn_R15C2 = Button(F13_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R15C2, width=6, height=hit)
btn_R15C2.grid(row=2, column=1, sticky='w')
btn_R15C2.config(font=labelfont)
btn_R15C3 = Button(F13_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R15C3, width=6, height=hit)
btn_R15C3.grid(row=2, column=2, sticky='w')
btn_R15C3.config(font=labelfont)
btn_R15C4 = Button(F13_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R15C4, width=6, height=hit)
btn_R15C4.grid(row=2, column=3, sticky='w')
btn_R15C4.config(font=labelfont)
btn_R15C5 = Button(F14_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R15C5, width=6, height=hit)
btn_R15C5.grid(row=2, column=0, sticky='w')
btn_R15C5.config(font=labelfont)
btn_R15C6 = Button(F14_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R15C6, width=6, height=hit)
btn_R15C6.grid(row=2, column=1, sticky='w')
btn_R15C6.config(font=labelfont)
btn_R15C7 = Button(F14_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R15C7, width=6, height=hit)
btn_R15C7.grid(row=2, column=2, sticky='w')
btn_R15C7.config(font=labelfont)
btn_R15C8 = Button(F14_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R15C8, width=6, height=hit)
btn_R15C8.grid(row=2, column=3, sticky='w')
btn_R15C8.config(font=labelfont)
btn_R15C9 = Button(F15_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R15C9, width=6, height=hit)
btn_R15C9.grid(row=2, column=0, sticky='w')
btn_R15C9.config(font=labelfont)
btn_R15C10 = Button(F15_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R15C10, width=6, height=hit)
btn_R15C10.grid(row=2, column=1, sticky='w')
btn_R15C10.config(font=labelfont)
btn_R15C11 = Button(F15_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R15C11, width=6, height=hit)
btn_R15C11.grid(row=2, column=2, sticky='w')
btn_R15C11.config(font=labelfont)
btn_R15C12 = Button(F15_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R15C12, width=6, height=hit)
btn_R15C12.grid(row=2, column=3, sticky='w')
btn_R15C12.config(font=labelfont)
btn_R15C13 = Button(F16_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R15C13, width=6, height=hit)
btn_R15C13.grid(row=2, column=0, sticky='w')
btn_R15C13.config(font=labelfont)
btn_R15C14 = Button(F16_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R15C14, width=6, height=hit)
btn_R15C14.grid(row=2, column=1, sticky='w')
btn_R15C14.config(font=labelfont)
btn_R15C15 = Button(F16_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R15C15, width=6, height=hit)
btn_R15C15.grid(row=2, column=2, sticky='w')
btn_R15C15.config(font=labelfont)
btn_R15C16 = Button(F16_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R15C16, width=6, height=hit)
btn_R15C16.grid(row=2, column=3, sticky='w')
btn_R15C16.config(font=labelfont)

btn_R16C1 = Button(F13_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R16C1, width=6, height=hit)
btn_R16C1.grid(row=3, column=0, sticky='w')
btn_R16C1.config(font=labelfont)
btn_R16C2 = Button(F13_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R16C2, width=6, height=hit)
btn_R16C2.grid(row=3, column=1, sticky='w')
btn_R16C2.config(font=labelfont)
btn_R16C3 = Button(F13_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R16C3, width=6, height=hit)
btn_R16C3.grid(row=3, column=2, sticky='w')
btn_R16C3.config(font=labelfont)
btn_R16C4 = Button(F13_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R16C4, width=6, height=hit)
btn_R16C4.grid(row=3, column=3, sticky='w')
btn_R16C4.config(font=labelfont)
btn_R16C5 = Button(F14_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R16C5, width=6, height=hit)
btn_R16C5.grid(row=3, column=0, sticky='w')
btn_R16C5.config(font=labelfont)
btn_R16C6 = Button(F14_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R16C6, width=6, height=hit)
btn_R16C6.grid(row=3, column=1, sticky='w')
btn_R16C6.config(font=labelfont)
btn_R16C7 = Button(F14_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R16C7, width=6, height=hit)
btn_R16C7.grid(row=3, column=2, sticky='w')
btn_R16C7.config(font=labelfont)
btn_R16C8 = Button(F14_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R16C8, width=6, height=hit)
btn_R16C8.grid(row=3, column=3, sticky='w')
btn_R16C8.config(font=labelfont)
btn_R16C9 = Button(F15_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R16C9, width=6, height=hit)
btn_R16C9.grid(row=3, column=0, sticky='w')
btn_R16C9.config(font=labelfont)
btn_R16C10 = Button(F15_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R16C10, width=6, height=hit)
btn_R16C10.grid(row=3, column=1, sticky='w')
btn_R16C10.config(font=labelfont)
btn_R16C11 = Button(F15_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R16C11, width=6, height=hit)
btn_R16C11.grid(row=3, column=2, sticky='w')
btn_R16C11.config(font=labelfont)
btn_R16C12 = Button(F15_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R16C12, width=6, height=hit)
btn_R16C12.grid(row=3, column=3, sticky='w')
btn_R16C12.config(font=labelfont)
btn_R16C13 = Button(F16_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R16C13, width=6, height=hit)
btn_R16C13.grid(row=3, column=0, sticky='w')
btn_R16C13.config(font=labelfont)
btn_R16C14 = Button(F16_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R16C14, width=6, height=hit)
btn_R16C14.grid(row=3, column=1, sticky='w')
btn_R16C14.config(font=labelfont)
btn_R16C15 = Button(F16_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R16C15, width=6, height=hit)
btn_R16C15.grid(row=3, column=2, sticky='w')
btn_R16C15.config(font=labelfont)
btn_R16C16 = Button(F16_frame, wraplength=48, justify=LEFT, text='0123\n4567\n89AB\nCDEF',
            command=update_R16C16, width=6, height=hit)
btn_R16C16.grid(row=3, column=3, sticky='w')
btn_R16C16.config(font=labelfont)

btn_dict = {}
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
# "eci_1_d=dict(eci='eci_1', formula= ""
# eci_1_d=dict(eci='eci_1'
# "compound_names_dict={'aluminum_carbide': 'Al4C3', 'aluminum_chloride': 'AlCl3', 'air': 'Ar2He2Kr2Ne2Xe2Rn2',
if __name__ == '__main__':
    root.mainloop()