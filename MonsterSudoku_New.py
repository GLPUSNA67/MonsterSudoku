import sys  # 2/22
import pickle
import json
import ctypes
from tkinter import *  # get widget classes
# from tkinter import Combobox, Entry, Label, font
# import ttk
# import logging
# logging.basicConfig(
#     filename = 'app.log',            # Name of the log file (omit to use stderr)
#     filemode = 'w',                  # File mode (use 'a' to append)
#     level    = logging.WARNING,      # Logging level (DEBUG, INFO, WARNING, ERROR, or CRITICAL)
# )
import tkinter as tk
# import numpy as np
# import matplotlib as mpl
# import matplotlib.pyplot as plt
# from scipy import *
# from scipy import constants
# from sqlite3 import *
# from sqlite3 import Error
# import SQL_tables_to_dict_str as sq
# import pdb
# from tkinter import messagebox as mb #*  # get standard dialogs
# from MessageBoxes import *
# from tkinter import messagebox as mb
# from tkinter import font
root = Tk()
screen_height = root.winfo_screenheight()
puzzle_height = int(screen_height * 7 / 8)
puzzle_width = int(puzzle_height * 1.3)
root.geometry(f"{puzzle_width}x{puzzle_height}")
print("33 puzzle_width screen_height", puzzle_width, screen_height)
root.geometry(f"{puzzle_width}x{puzzle_height}")
titlefont = ('Ariel', 12, 'bold')
donefont = ('Ariel', 16, 'bold')
labelfont = ('Ariel', 10, 'bold')
buttonfont = ('Ariel', 10)
entryfont = ('Ariel', 10)
exlanationfont = ('Ariel', 10)
size6font = ('Ariel', 6)
size8font = ('Ariel', 8)
size9font = ('Ariel', 9)
wid = 4
wid4 = 4
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
bRemoveANumberFromACell = False
bAutoComplete = False
bSolve_singles = False
bShowRemainders = False
bInitialShowRemainders = False
bIDDuples = False
bIDTriples = False
bIDQuads = False
duples_list = []
triples_list = []
triples_rcs_list = []
quads_list = []
quads_rcs_list = []
quints_list = []
quints_rcs_list = []
completed_duples_list = []
completed_triples_list = []
cells_remaining_num = 256
n_in_row_sq = []
n_in_col_sq = []
D = 0
R = 0
NullValue = "Null"
triple = None
history = ""
# current_solution_file = 'C:\PythonProjects\MonsterSudoku\MS_Current_Solution.txt'

row_nums = [[1, ""], [2, ""], [3, ""], [4, ""], [5, ""], [6, ""], [7, ""], [
    8, ""], [9, ""], [10, ''], [11, ''], [12, ""], [13, ""], [14, ""], [15, ''], [16, '']]
col_nums = [[1, ""], [2, ""], [3, ""], [4, ""], [5, ""], [6, ""], [7, ""], [
    8, ""], [9, ""], [10, ''], [11, ''], [12, ""], [13, ""], [14, ""], [15, ''], [16, '']]
sq_nums = [[1, ""], [2, ""], [3, ""], [4, ""], [5, ""], [6, ""], [7, ""], [
    8, ""], [9, ""], [10, ''], [11, ''], [12, ""], [13, ""], [14, ""], [15, ''], [16, '']]

# row_1_arefs = ['arrRef0', 'arrRef1', 'arrRef2', 'arrRef3', 'arrRef4', 'arrRef5', 'arrRef6', 'arrRef7',
#                'arrRef8', 'arrRef9', 'arrRef10', 'arrRef11', 'arrRef12', 'arrRef13', 'arrRef14', 'arrRef15']
row_1_arefs = []
row_2_arefs = []
row_3_arefs = []
row_4_arefs = []
row_5_arefs = []
row_6_arefs = []
row_7_arefs = []
row_8_arefs = []
row_9_arefs = []
row_10_arefs = []
row_11_arefs = []
row_12_arefs = []
row_13_arefs = []
row_14_arefs = []
row_15_arefs = []
row_16_arefs = []
row_arefs = [row_1_arefs, row_2_arefs, row_3_arefs, row_4_arefs, row_5_arefs, row_6_arefs, row_7_arefs, row_8_arefs,
             row_9_arefs, row_10_arefs, row_11_arefs, row_12_arefs, row_13_arefs, row_14_arefs, row_15_arefs, row_16_arefs]
col_1_arefs = []
col_2_arefs = []
col_3_arefs = []
col_4_arefs = []
col_5_arefs = []
col_6_arefs = []
col_7_arefs = []
col_8_arefs = []
col_9_arefs = []
col_10_arefs = []
col_11_arefs = []
col_12_arefs = []
col_13_arefs = []
col_14_arefs = []
col_15_arefs = []
col_16_arefs = []
col_arefs = [col_1_arefs, col_2_arefs, col_3_arefs, col_4_arefs, col_5_arefs, col_6_arefs, col_7_arefs, col_8_arefs,
             col_9_arefs, col_10_arefs, col_11_arefs, col_12_arefs, col_13_arefs, col_14_arefs, col_15_arefs, col_16_arefs]

sq_1_arefs = []
sq_2_arefs = []
sq_3_arefs = []
sq_4_arefs = []
sq_5_arefs = []
sq_6_arefs = []
sq_7_arefs = []
sq_8_arefs = []
sq_9_arefs = []
# sq_9_arefs = ['arrRef128', 'arrRef129', 'arrRef130', 'arrRef131', 'arrRef144', 'arrRef145', 'arrRef146', 'arrRef147',
#               'arrRef160', 'arrRef161', 'arrRef162', 'arrRef163', 'arrRef176', 'arrRef177', 'arrRef178', 'arrRef179']
sq_10_arefs = []
sq_11_arefs = []
sq_12_arefs = []
sq_13_arefs = []
sq_14_arefs = []
sq_15_arefs = []
sq_16_arefs = []
sq_arefs = (sq_1_arefs, sq_2_arefs, sq_3_arefs, sq_4_arefs,
            sq_5_arefs, sq_6_arefs, sq_7_arefs, sq_7_arefs,
            sq_8_arefs, sq_9_arefs, sq_10_arefs, sq_11_arefs,
            sq_12_arefs, sq_13_arefs, sq_14_arefs, sq_15_arefs, sq_16_arefs)

# nums = 0
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
r_nums_list = ['r_1_nums', 'r_2_nums', 'r_3_nums', 'r_4_nums', 'r_5_nums', 'r_6_nums', 'r_7_nums', 'r_8_nums',
               'r_9_nums', 'r_10_nums', 'r_11_nums', 'r_12_nums', 'r_13_nums', 'r_14_nums', 'r_15_nums', 'r_16_nums']
c_nums_list = ['c_1_nums', 'c_2_nums', 'c_3_nums', 'c_4_nums', 'c_5_nums', 'c_6_nums', 'c_7_nums', 'c_8_nums',
               'c_9_nums', 'c_10_nums', 'c_11_nums', 'c_12_nums', 'c_13_nums', 'c_14_nums', 'c_15_nums', 'c_16_nums']
sq_nums_list = ['s_1_nums', 's_2_nums', 's_3_nums', 's_4_nums', 's_5_nums', 's_6_nums', 's_7_nums', 's_8_nums',
                's_9_nums', 's_10_nums', 's_11_nums', 's_12_nums', 's_13_nums', 's_14_nums', 's_15_nums', 's_16_nums']

row_1_nums = "0123456789ABCDEF"
row_2_nums = "0123456789ABCDEF"
row_3_nums = "0123456789ABCDEF"
row_4_nums = "0123456789ABCDEF"
row_5_nums = "0123456789ABCDEF"
row_6_nums = "0123456789ABCDEF"
row_7_nums = "0123456789ABCDEF"
row_8_nums = "0123456789ABCDEF"
row_9_nums = "0123456789ABCDEF"
row_10_nums = "0123456789ABCDEF"
row_11_nums = "0123456789ABCDEF"
row_12_nums = "0123456789ABCDEF"
row_13_nums = "0123456789ABCDEF"
row_14_nums = "0123456789ABCDEF"
row_15_nums = "0123456789ABCDEF"
row_16_nums = "0123456789ABCDEF"
col_1_nums = "0123456789ABCDEF"
col_2_nums = "0123456789ABCDEF"
col_3_nums = "0123456789ABCDEF"
col_4_nums = "0123456789ABCDEF"
col_5_nums = "0123456789ABCDEF"
col_6_nums = "0123456789ABCDEF"
col_7_nums = "0123456789ABCDEF"
col_8_nums = "0123456789ABCDEF"
col_9_nums = "0123456789ABCDEF"
col_10_nums = "0123456789ABCDEF"
col_11_nums = "0123456789ABCDEF"
col_12_nums = "0123456789ABCDEF"
col_13_nums = "0123456789ABCDEF"
col_14_nums = "0123456789ABCDEF"
col_15_nums = "0123456789ABCDEF"
col_16_nums = "0123456789ABCDEF"
sq_1_nums = "0123456789ABCDEF"
sq_2_nums = "0123456789ABCDEF"
sq_3_nums = "0123456789ABCDEF"
sq_4_nums = "0123456789ABCDEF"
sq_5_nums = "0123456789ABCDEF"
sq_6_nums = "0123456789ABCDEF"
sq_7_nums = "0123456789ABCDEF"
sq_8_nums = "0123456789ABCDEF"
sq_9_nums = "0123456789ABCDEF"
sq_10_nums = "0123456789ABCDEF"
sq_11_nums = "0123456789ABCDEF"
sq_12_nums = "0123456789ABCDEF"
sq_13_nums = "0123456789ABCDEF"
sq_14_nums = "0123456789ABCDEF"
sq_15_nums = "0123456789ABCDEF"
sq_16_nums = "0123456789ABCDEF"
row_nums_list = ['row_1_nums', 'row_2_nums', 'row_3_nums', 'row_4_nums', 'row_5_nums', 'row_6_nums', 'row_7_nums', 'row_8_nums',
                 'row_9_nums', 'row_10_nums', 'row_11_nums', 'row_12_nums', 'row_13_nums', 'row_14_nums', 'row_15_nums', 'row_16_nums']
col_nums_list = ['col_1_nums', 'col_2_nums', 'col_3_nums', 'col_4_nums', 'col_5_nums', 'col_6_nums', 'col_7_nums', 'col_8_nums',
                 'col_9_nums', 'col_10_nums', 'col_11_nums', 'col_12_nums', 'col_13_nums', 'col_14_nums', 'col_15_nums', 'col_16_nums']
sqr_nums_list = ['sq_1_nums', 'sq_2_nums', 'sq_3_nums', 'sq_4_nums', 'sq_5_nums', 'sq_6_nums', 'sq_7_nums', 'sq_8_nums',
                 'sq_9_nums', 'sq_10_nums', 'sq_11_nums', 'sq_12_nums', 'sq_13_nums', 'sq_14_nums', 'sq_15_nums', 'sq_16_nums']

# row_1_arefs = ['arrRef0', 'arrRef1', 'arrRef2', 'arrRef3', 'arrRef4', 'arrRef5', 'arrRef6', 'arrRef7',
#                'arrRef8', 'arrRef9', 'arrRef10', 'arrRef11', 'arrRef12', 'arrRef13', 'arrRef14', 'arrRef15']
# col_1_arefs = ['arrRef0', 'arrRef32', 'arrRef48', 'arrRef64', 'arrRef16',
#                'arrRef16', 'arrRef16', 'arrRef16', 'arrRef16', 'arrRef16', 'arrRef16', 'arrRef16']
# sq_1_arefs = ['arrRef0', 'arrRef1', 'arrRef2',
#               'arrRef3''arrRef16', 'arrRef17', 'arrRef18', 'arrRef19''arrRef32', 'arrRef33', 'arrRef34', 'arrRef35''arrRef48', 'arrRef49', 'arrRef50', 'arrRef51']
# row_9_arefs = ['arrRef128', 'arrRef129', 'arrRef130', 'arrRef131', 'arrRef132', 'arrRef133', 'arrRef134',
#                'arrRef135', 'arrRef136', 'arrRef137', 'arrRef138', 'arrRef139', 'arrRef140', 'arrRef141', 'arrRef142', 'arrRef143']
# col_9_arefs = []
# sq_9_arefs = ['arrRef128', 'arrRef129', 'arrRef130', 'arrRef131', 'arrRef144', 'arrRef145', 'arrRef146', 'arrRef147',
#               'arrRef160', 'arrRef162', 'arrRef163', 'arrRef164', 'arrRef176', 'arrRef177', 'arrRef178', 'arrRef179']

delete_singles_row_list = []
delete_singles_col_list = []
delete_singles_sq_list = []
n_1_16 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
nums = ""
done_arefs_list = []
r1 = dict(nums='', n0="", ct_0=0, ct_0__col_refs=[], n1="", ct_1=0, ct_1__col_refs=[], n2="", ct_2=0, ct_2__col_refs=[], n3="", ct_3=0, ct_3__col_refs=[], n4="", ct_4=0, ct_4__col_refs=[], n5="", ct_5=0, ct_5__col_refs=[], n6="", ct_6=0, ct_6__col_refs=[], n7="", ct_7=0, ct_7__col_refs=[
], n8="", ct_8=0, ct_8__col_refs=[], n9="", ct_9=0, ct_9__col_refs=[], nA="", ct_A=0, ct_A__col_refs=[], nB="", ct_B=0, ct_B__col_refs=[], nC="", ct_C=0, ct_C__col_refs=[], nD="", ct_D=0, ct_D__col_refs=[], nE="", ct_E=0, ct_E__col_refs=[], nF="", ct_F=0, ct_F__col_refs=[])
r2 = dict(nums='', n0="", ct_0=0, ct_0__col_refs=[], n1="", ct_1=0, ct_1__col_refs=[], n2="", ct_2=0, ct_2__col_refs=[], n3="", ct_3=0, ct_3__col_refs=[], n4="", ct_4=0, ct_4__col_refs=[], n5="", ct_5=0, ct_5__col_refs=[], n6="", ct_6=0, ct_6__col_refs=[], n7="", ct_7=0, ct_7__col_refs=[
], n8="", ct_8=0, ct_8__col_refs=[], n9="", ct_9=0, ct_9__col_refs=[], nA="", ct_A=0, ct_A__col_refs=[], nB="", ct_B=0, ct_B__col_refs=[], nC="", ct_C=0, ct_C__col_refs=[], nD="", ct_D=0, ct_D__col_refs=[], nE="", ct_E=0, ct_E__col_refs=[], nF="", ct_F=0, ct_F__col_refs=[])
r3 = dict(nums='', n0="", ct_0=0, ct_0__col_refs=[], n1="", ct_1=0, ct_1__col_refs=[], n2="", ct_2=0, ct_2__col_refs=[], n3="", ct_3=0, ct_3__col_refs=[], n4="", ct_4=0, ct_4__col_refs=[], n5="", ct_5=0, ct_5__col_refs=[], n6="", ct_6=0, ct_6__col_refs=[], n7="", ct_7=0, ct_7__col_refs=[
], n8="", ct_8=0, ct_8__col_refs=[], n9="", ct_9=0, ct_9__col_refs=[], nA="", ct_A=0, ct_A__col_refs=[], nB="", ct_B=0, ct_B__col_refs=[], nC="", ct_C=0, ct_C__col_refs=[], nD="", ct_D=0, ct_D__col_refs=[], nE="", ct_E=0, ct_E__col_refs=[], nF="", ct_F=0, ct_F__col_refs=[])
r4 = dict(nums='', n0="", ct_0=0, ct_0__col_refs=[], n1="", ct_1=0, ct_1__col_refs=[], n2="", ct_2=0, ct_2__col_refs=[], n3="", ct_3=0, ct_3__col_refs=[], n4="", ct_4=0, ct_4__col_refs=[], n5="", ct_5=0, ct_5__col_refs=[], n6="", ct_6=0, ct_6__col_refs=[], n7="", ct_7=0, ct_7__col_refs=[
], n8="", ct_8=0, ct_8__col_refs=[], n9="", ct_9=0, ct_9__col_refs=[], nA="", ct_A=0, ct_A__col_refs=[], nB="", ct_B=0, ct_B__col_refs=[], nC="", ct_C=0, ct_C__col_refs=[], nD="", ct_D=0, ct_D__col_refs=[], nE="", ct_E=0, ct_E__col_refs=[], nF="", ct_F=0, ct_F__col_refs=[])
r5 = dict(nums='', n0="", ct_0=0, ct_0__col_refs=[], n1="", ct_1=0, ct_1__col_refs=[], n2="", ct_2=0, ct_2__col_refs=[], n3="", ct_3=0, ct_3__col_refs=[], n4="", ct_4=0, ct_4__col_refs=[], n5="", ct_5=0, ct_5__col_refs=[], n6="", ct_6=0, ct_6__col_refs=[], n7="", ct_7=0, ct_7__col_refs=[
], n8="", ct_8=0, ct_8__col_refs=[], n9="", ct_9=0, ct_9__col_refs=[], nA="", ct_A=0, ct_A__col_refs=[], nB="", ct_B=0, ct_B__col_refs=[], nC="", ct_C=0, ct_C__col_refs=[], nD="", ct_D=0, ct_D__col_refs=[], nE="", ct_E=0, ct_E__col_refs=[], nF="", ct_F=0, ct_F__col_refs=[])
r6 = dict(nums='', n0="", ct_0=0, ct_0__col_refs=[], n1="", ct_1=0, ct_1__col_refs=[], n2="", ct_2=0, ct_2__col_refs=[], n3="", ct_3=0, ct_3__col_refs=[], n4="", ct_4=0, ct_4__col_refs=[], n5="", ct_5=0, ct_5__col_refs=[], n6="", ct_6=0, ct_6__col_refs=[], n7="", ct_7=0, ct_7__col_refs=[
], n8="", ct_8=0, ct_8__col_refs=[], n9="", ct_9=0, ct_9__col_refs=[], nA="", ct_A=0, ct_A__col_refs=[], nB="", ct_B=0, ct_B__col_refs=[], nC="", ct_C=0, ct_C__col_refs=[], nD="", ct_D=0, ct_D__col_refs=[], nE="", ct_E=0, ct_E__col_refs=[], nF="", ct_F=0, ct_F__col_refs=[])
r7 = dict(nums='', n0="", ct_0=0, ct_0__col_refs=[], n1="", ct_1=0, ct_1__col_refs=[], n2="", ct_2=0, ct_2__col_refs=[], n3="", ct_3=0, ct_3__col_refs=[], n4="", ct_4=0, ct_4__col_refs=[], n5="", ct_5=0, ct_5__col_refs=[], n6="", ct_6=0, ct_6__col_refs=[], n7="", ct_7=0, ct_7__col_refs=[
], n8="", ct_8=0, ct_8__col_refs=[], n9="", ct_9=0, ct_9__col_refs=[], nA="", ct_A=0, ct_A__col_refs=[], nB="", ct_B=0, ct_B__col_refs=[], nC="", ct_C=0, ct_C__col_refs=[], nD="", ct_D=0, ct_D__col_refs=[], nE="", ct_E=0, ct_E__col_refs=[], nF="", ct_F=0, ct_F__col_refs=[])
r8 = dict(nums='', n0="", ct_0=0, ct_0__col_refs=[], n1="", ct_1=0, ct_1__col_refs=[], n2="", ct_2=0, ct_2__col_refs=[], n3="", ct_3=0, ct_3__col_refs=[], n4="", ct_4=0, ct_4__col_refs=[], n5="", ct_5=0, ct_5__col_refs=[], n6="", ct_6=0, ct_6__col_refs=[], n7="", ct_7=0, ct_7__col_refs=[
], n8="", ct_8=0, ct_8__col_refs=[], n9="", ct_9=0, ct_9__col_refs=[], nA="", ct_A=0, ct_A__col_refs=[], nB="", ct_B=0, ct_B__col_refs=[], nC="", ct_C=0, ct_C__col_refs=[], nD="", ct_D=0, ct_D__col_refs=[], nE="", ct_E=0, ct_E__col_refs=[], nF="", ct_F=0, ct_F__col_refs=[])
r9 = dict(nums='', n0="", ct_0=0, ct_0__col_refs=[], n1="", ct_1=0, ct_1__col_refs=[], n2="", ct_2=0, ct_2__col_refs=[], n3="", ct_3=0, ct_3__col_refs=[], n4="", ct_4=0, ct_4__col_refs=[], n5="", ct_5=0, ct_5__col_refs=[], n6="", ct_6=0, ct_6__col_refs=[], n7="", ct_7=0, ct_7__col_refs=[
], n8="", ct_8=0, ct_8__col_refs=[], n9="", ct_9=0, ct_9__col_refs=[], nA="", ct_A=0, ct_A__col_refs=[], nB="", ct_B=0, ct_B__col_refs=[], nC="", ct_C=0, ct_C__col_refs=[], nD="", ct_D=0, ct_D__col_refs=[], nE="", ct_E=0, ct_E__col_refs=[], nF="", ct_F=0, ct_F__col_refs=[])
r10 = dict(nums='', n0="", ct_0=0, ct_0__col_refs=[], n1="", ct_1=0, ct_1__col_refs=[], n2="", ct_2=0, ct_2__col_refs=[], n3="", ct_3=0, ct_3__col_refs=[], n4="", ct_4=0, ct_4__col_refs=[], n5="", ct_5=0, ct_5__col_refs=[], n6="", ct_6=0, ct_6__col_refs=[], n7="", ct_7=0, ct_7__col_refs=[
], n8="", ct_8=0, ct_8__col_refs=[], n9="", ct_9=0, ct_9__col_refs=[], nA="", ct_A=0, ct_A__col_refs=[], nB="", ct_B=0, ct_B__col_refs=[], nC="", ct_C=0, ct_C__col_refs=[], nD="", ct_D=0, ct_D__col_refs=[], nE="", ct_E=0, ct_E__col_refs=[], nF="", ct_F=0, ct_F__col_refs=[])
r11 = dict(nums='', n0="", ct_0=0, ct_0__col_refs=[], n1="", ct_1=0, ct_1__col_refs=[], n2="", ct_2=0, ct_2__col_refs=[], n3="", ct_3=0, ct_3__col_refs=[], n4="", ct_4=0, ct_4__col_refs=[], n5="", ct_5=0, ct_5__col_refs=[], n6="", ct_6=0, ct_6__col_refs=[], n7="", ct_7=0, ct_7__col_refs=[
], n8="", ct_8=0, ct_8__col_refs=[], n9="", ct_9=0, ct_9__col_refs=[], nA="", ct_A=0, ct_A__col_refs=[], nB="", ct_B=0, ct_B__col_refs=[], nC="", ct_C=0, ct_C__col_refs=[], nD="", ct_D=0, ct_D__col_refs=[], nE="", ct_E=0, ct_E__col_refs=[], nF="", ct_F=0, ct_F__col_refs=[])
r12 = dict(nums='', n0="", ct_0=0, ct_0__col_refs=[], n1="", ct_1=0, ct_1__col_refs=[], n2="", ct_2=0, ct_2__col_refs=[], n3="", ct_3=0, ct_3__col_refs=[], n4="", ct_4=0, ct_4__col_refs=[], n5="", ct_5=0, ct_5__col_refs=[], n6="", ct_6=0, ct_6__col_refs=[], n7="", ct_7=0, ct_7__col_refs=[
], n8="", ct_8=0, ct_8__col_refs=[], n9="", ct_9=0, ct_9__col_refs=[], nA="", ct_A=0, ct_A__col_refs=[], nB="", ct_B=0, ct_B__col_refs=[], nC="", ct_C=0, ct_C__col_refs=[], nD="", ct_D=0, ct_D__col_refs=[], nE="", ct_E=0, ct_E__col_refs=[], nF="", ct_F=0, ct_F__col_refs=[])
r13 = dict(nums='', n0="", ct_0=0, ct_0__col_refs=[], n1="", ct_1=0, ct_1__col_refs=[], n2="", ct_2=0, ct_2__col_refs=[], n3="", ct_3=0, ct_3__col_refs=[], n4="", ct_4=0, ct_4__col_refs=[], n5="", ct_5=0, ct_5__col_refs=[], n6="", ct_6=0, ct_6__col_refs=[], n7="", ct_7=0, ct_7__col_refs=[
], n8="", ct_8=0, ct_8__col_refs=[], n9="", ct_9=0, ct_9__col_refs=[], nA="", ct_A=0, ct_A__col_refs=[], nB="", ct_B=0, ct_B__col_refs=[], nC="", ct_C=0, ct_C__col_refs=[], nD="", ct_D=0, ct_D__col_refs=[], nE="", ct_E=0, ct_E__col_refs=[], nF="", ct_F=0, ct_F__col_refs=[])
r14 = dict(nums='', n0="", ct_0=0, ct_0__col_refs=[], n1="", ct_1=0, ct_1__col_refs=[], n2="", ct_2=0, ct_2__col_refs=[], n3="", ct_3=0, ct_3__col_refs=[], n4="", ct_4=0, ct_4__col_refs=[], n5="", ct_5=0, ct_5__col_refs=[], n6="", ct_6=0, ct_6__col_refs=[], n7="", ct_7=0, ct_7__col_refs=[
], n8="", ct_8=0, ct_8__col_refs=[], n9="", ct_9=0, ct_9__col_refs=[], nA="", ct_A=0, ct_A__col_refs=[], nB="", ct_B=0, ct_B__col_refs=[], nC="", ct_C=0, ct_C__col_refs=[], nD="", ct_D=0, ct_D__col_refs=[], nE="", ct_E=0, ct_E__col_refs=[], nF="", ct_F=0, ct_F__col_refs=[])
r15 = dict(nums='', n0="", ct_0=0, ct_0__col_refs=[], n1="", ct_1=0, ct_1__col_refs=[], n2="", ct_2=0, ct_2__col_refs=[], n3="", ct_3=0, ct_3__col_refs=[], n4="", ct_4=0, ct_4__col_refs=[], n5="", ct_5=0, ct_5__col_refs=[], n6="", ct_6=0, ct_6__col_refs=[], n7="", ct_7=0, ct_7__col_refs=[
], n8="", ct_8=0, ct_8__col_refs=[], n9="", ct_9=0, ct_9__col_refs=[], nA="", ct_A=0, ct_A__col_refs=[], nB="", ct_B=0, ct_B__col_refs=[], nC="", ct_C=0, ct_C__col_refs=[], nD="", ct_D=0, ct_D__col_refs=[], nE="", ct_E=0, ct_E__col_refs=[], nF="", ct_F=0, ct_F__col_refs=[])
r16 = dict(nums='', n0="", ct_0=0, ct_0__col_refs=[], n1="", ct_1=0, ct_1__col_refs=[], n2="", ct_2=0, ct_2__col_refs=[], n3="", ct_3=0, ct_3__col_refs=[], n4="", ct_4=0, ct_4__col_refs=[], n5="", ct_5=0, ct_5__col_refs=[], n6="", ct_6=0, ct_6__col_refs=[], n7="", ct_7=0, ct_7__col_refs=[
], n8="", ct_8=0, ct_8__col_refs=[], n9="", ct_9=0, ct_9__col_refs=[], nA="", ct_A=0, ct_A__col_refs=[], nB="", ct_B=0, ct_B__col_refs=[], nC="", ct_C=0, ct_C__col_refs=[], nD="", ct_D=0, ct_D__col_refs=[], nE="", ct_E=0, ct_E__col_refs=[], nF="", ct_F=0, ct_F__col_refs=[])
c1 = dict(nums='', n0="", ct_0=0, ct_0__row_refs=[], n1="", ct_1=0, ct_1__row_refs=[], n2="", ct_2=0, ct_2__row_refs=[], n3="", ct_3=0, ct_3__row_refs=[], n4="", ct_4=0, ct_4__row_refs=[], n5="", ct_5=0, ct_5__row_refs=[], n6="", ct_6=0, ct_6__row_refs=[], n7="", ct_7=0, ct_7__row_refs=[
], n8="", ct_8=0, ct_8__row_refs=[], n9="", ct_9=0, ct_9__row_refs=[], nA="", ct_A=0, ct_A__row_refs=[], nB="", ct_B=0, ct_B__row_refs=[], nC="", ct_C=0, ct_C__row_refs=[], nD="", ct_D=0, ct_D__row_refs=[], ct_D__col_refs=[], nE="", ct_E=0, ct_E__row_refs=[], nF="", ct_F=0, ct_F__row_refs=[])
c2 = dict(nums='', n0="", ct_0=0, ct_0__row_refs=[], n1="", ct_1=0, ct_1__row_refs=[], n2="", ct_2=0, ct_2__row_refs=[], n3="", ct_3=0, ct_3__row_refs=[], n4="", ct_4=0, ct_4__row_refs=[], n5="", ct_5=0, ct_5__row_refs=[], n6="", ct_6=0, ct_6__row_refs=[], n7="", ct_7=0, ct_7__row_refs=[
], n8="", ct_8=0, ct_8__row_refs=[], n9="", ct_9=0, ct_9__row_refs=[], nA="", ct_A=0, ct_A__row_refs=[], nB="", ct_B=0, ct_B__row_refs=[], nC="", ct_C=0, ct_C__row_refs=[], nD="", ct_D=0, ct_D__col_refs=[], nE="", ct_E=0, ct_E__row_refs=[], nF="", ct_F=0, ct_F__row_refs=[])
c3 = dict(nums='', n0="", ct_0=0, ct_0__row_refs=[], n1="", ct_1=0, ct_1__row_refs=[], n2="", ct_2=0, ct_2__row_refs=[], n3="", ct_3=0, ct_3__row_refs=[], n4="", ct_4=0, ct_4__row_refs=[], n5="", ct_5=0, ct_5__row_refs=[], n6="", ct_6=0, ct_6__row_refs=[], n7="", ct_7=0, ct_7__row_refs=[
], n8="", ct_8=0, ct_8__row_refs=[], n9="", ct_9=0, ct_9__row_refs=[], nA="", ct_A=0, ct_A__row_refs=[], nB="", ct_B=0, ct_B__row_refs=[], nC="", ct_C=0, ct_C__row_refs=[], nD="", ct_D=0, ct_D__col_refs=[], nE="", ct_E=0, ct_E__row_refs=[], nF="", ct_F=0, ct_F__row_refs=[])
c4 = dict(nums='', n0="", ct_0=0, ct_0__row_refs=[], n1="", ct_1=0, ct_1__row_refs=[], n2="", ct_2=0, ct_2__row_refs=[], n3="", ct_3=0, ct_3__row_refs=[], n4="", ct_4=0, ct_4__row_refs=[], n5="", ct_5=0, ct_5__row_refs=[], n6="", ct_6=0, ct_6__row_refs=[], n7="", ct_7=0, ct_7__row_refs=[
], n8="", ct_8=0, ct_8__row_refs=[], n9="", ct_9=0, ct_9__row_refs=[], nA="", ct_A=0, ct_A__row_refs=[], nB="", ct_B=0, ct_B__row_refs=[], nC="", ct_C=0, ct_C__row_refs=[], nD="", ct_D=0, ct_D__col_refs=[], nE="", ct_E=0, ct_E__row_refs=[], nF="", ct_F=0, ct_F__row_refs=[])
c5 = dict(nums='', n0="", ct_0=0, ct_0__row_refs=[], n1="", ct_1=0, ct_1__row_refs=[], n2="", ct_2=0, ct_2__row_refs=[], n3="", ct_3=0, ct_3__row_refs=[], n4="", ct_4=0, ct_4__row_refs=[], n5="", ct_5=0, ct_5__row_refs=[], n6="", ct_6=0, ct_6__row_refs=[], n7="", ct_7=0, ct_7__row_refs=[
], n8="", ct_8=0, ct_8__row_refs=[], n9="", ct_9=0, ct_9__row_refs=[], nA="", ct_A=0, ct_A__row_refs=[], nB="", ct_B=0, ct_B__row_refs=[], nC="", ct_C=0, ct_C__row_refs=[], nD="", ct_D=0, ct_D__col_refs=[], nE="", ct_E=0, ct_E__row_refs=[], nF="", ct_F=0, ct_F__row_refs=[])
c6 = dict(nums='', n0="", ct_0=0, ct_0__row_refs=[], n1="", ct_1=0, ct_1__row_refs=[], n2="", ct_2=0, ct_2__row_refs=[], n3="", ct_3=0, ct_3__row_refs=[], n4="", ct_4=0, ct_4__row_refs=[], n5="", ct_5=0, ct_5__row_refs=[], n6="", ct_6=0, ct_6__row_refs=[], n7="", ct_7=0, ct_7__row_refs=[
], n8="", ct_8=0, ct_8__row_refs=[], n9="", ct_9=0, ct_9__row_refs=[], nA="", ct_A=0, ct_A__row_refs=[], nB="", ct_B=0, ct_B__row_refs=[], nC="", ct_C=0, ct_C__row_refs=[], nD="", ct_D=0, ct_D__col_refs=[], nE="", ct_E=0, ct_E__row_refs=[], nF="", ct_F=0, ct_F__row_refs=[])
c7 = dict(nums='', n0="", ct_0=0, ct_0__row_refs=[], n1="", ct_1=0, ct_1__row_refs=[], n2="", ct_2=0, ct_2__row_refs=[], n3="", ct_3=0, ct_3__row_refs=[], n4="", ct_4=0, ct_4__row_refs=[], n5="", ct_5=0, ct_5__row_refs=[], n6="", ct_6=0, ct_6__row_refs=[], n7="", ct_7=0, ct_7__row_refs=[
], n8="", ct_8=0, ct_8__row_refs=[], n9="", ct_9=0, ct_9__row_refs=[], nA="", ct_A=0, ct_A__row_refs=[], nB="", ct_B=0, ct_B__row_refs=[], nC="", ct_C=0, ct_C__row_refs=[], nD="", ct_D=0, ct_D__col_refs=[], nE="", ct_E=0, ct_E__row_refs=[], nF="", ct_F=0, ct_F__row_refs=[])
c8 = dict(nums='', n0="", ct_0=0, ct_0__row_refs=[], n1="", ct_1=0, ct_1__row_refs=[], n2="", ct_2=0, ct_2__row_refs=[], n3="", ct_3=0, ct_3__row_refs=[], n4="", ct_4=0, ct_4__row_refs=[], n5="", ct_5=0, ct_5__row_refs=[], n6="", ct_6=0, ct_6__row_refs=[], n7="", ct_7=0, ct_7__row_refs=[
], n8="", ct_8=0, ct_8__row_refs=[], n9="", ct_9=0, ct_9__row_refs=[], nA="", ct_A=0, ct_A__row_refs=[], nB="", ct_B=0, ct_B__row_refs=[], nC="", ct_C=0, ct_C__row_refs=[], nD="", ct_D=0, ct_D__col_refs=[], nE="", ct_E=0, ct_E__row_refs=[], nF="", ct_F=0, ct_F__row_refs=[])
c9 = dict(nums='', n0="", ct_0=0, ct_0__row_refs=[], n1="", ct_1=0, ct_1__row_refs=[], n2="", ct_2=0, ct_2__row_refs=[], n3="", ct_3=0, ct_3__row_refs=[], n4="", ct_4=0, ct_4__row_refs=[], n5="", ct_5=0, ct_5__row_refs=[], n6="", ct_6=0, ct_6__row_refs=[], n7="", ct_7=0, ct_7__row_refs=[
], n8="", ct_8=0, ct_8__row_refs=[], n9="", ct_9=0, ct_9__row_refs=[], nA="", ct_A=0, ct_A__row_refs=[], nB="", ct_B=0, ct_B__row_refs=[], nC="", ct_C=0, ct_C__row_refs=[], nD="", ct_D=0, ct_D__col_refs=[], nE="", ct_E=0, ct_E__row_refs=[], nF="", ct_F=0, ct_F__row_refs=[])
c10 = dict(nums='', n0="", ct_0=0, ct_0__row_refs=[], n1="", ct_1=0, ct_1__row_refs=[], n2="", ct_2=0, ct_2__row_refs=[], n3="", ct_3=0, ct_3__row_refs=[], n4="", ct_4=0, ct_4__row_refs=[], n5="", ct_5=0, ct_5__row_refs=[], n6="", ct_6=0, ct_6__row_refs=[], n7="", ct_7=0, ct_7__row_refs=[
], n8="", ct_8=0, ct_8__row_refs=[], n9="", ct_9=0, ct_9__row_refs=[], nA="", ct_A=0, ct_A__row_refs=[], nB="", ct_B=0, ct_B__row_refs=[], nC="", ct_C=0, ct_C__row_refs=[], nD="", ct_D=0, ct_D__col_refs=[], nE="", ct_E=0, ct_E__row_refs=[], nF="", ct_F=0, ct_F__row_refs=[])
c11 = dict(nums='', n0="", ct_0=0, ct_0__row_refs=[], n1="", ct_1=0, ct_1__row_refs=[], n2="", ct_2=0, ct_2__row_refs=[], n3="", ct_3=0, ct_3__row_refs=[], n4="", ct_4=0, ct_4__row_refs=[], n5="", ct_5=0, ct_5__row_refs=[], n6="", ct_6=0, ct_6__row_refs=[], n7="", ct_7=0, ct_7__row_refs=[
], n8="", ct_8=0, ct_8__row_refs=[], n9="", ct_9=0, ct_9__row_refs=[], nA="", ct_A=0, ct_A__row_refs=[], nB="", ct_B=0, ct_B__row_refs=[], nC="", ct_C=0, ct_C__row_refs=[], nD="", ct_D=0, ct_D__col_refs=[], nE="", ct_E=0, ct_E__row_refs=[], nF="", ct_F=0, ct_F__row_refs=[])
c12 = dict(nums='', n0="", ct_0=0, ct_0__row_refs=[], n1="", ct_1=0, ct_1__row_refs=[], n2="", ct_2=0, ct_2__row_refs=[], n3="", ct_3=0, ct_3__row_refs=[], n4="", ct_4=0, ct_4__row_refs=[], n5="", ct_5=0, ct_5__row_refs=[], n6="", ct_6=0, ct_6__row_refs=[], n7="", ct_7=0, ct_7__row_refs=[
], n8="", ct_8=0, ct_8__row_refs=[], n9="", ct_9=0, ct_9__row_refs=[], nA="", ct_A=0, ct_A__row_refs=[], nB="", ct_B=0, ct_B__row_refs=[], nC="", ct_C=0, ct_C__row_refs=[], nD="", ct_D=0, ct_D__col_refs=[], nE="", ct_E=0, ct_E__row_refs=[], nF="", ct_F=0, ct_F__row_refs=[])
c13 = dict(nums='', n0="", ct_0=0, ct_0__row_refs=[], n1="", ct_1=0, ct_1__row_refs=[], n2="", ct_2=0, ct_2__row_refs=[], n3="", ct_3=0, ct_3__row_refs=[], n4="", ct_4=0, ct_4__row_refs=[], n5="", ct_5=0, ct_5__row_refs=[], n6="", ct_6=0, ct_6__row_refs=[], n7="", ct_7=0, ct_7__row_refs=[
], n8="", ct_8=0, ct_8__row_refs=[], n9="", ct_9=0, ct_9__row_refs=[], nA="", ct_A=0, ct_A__row_refs=[], nB="", ct_B=0, ct_B__row_refs=[], nC="", ct_C=0, ct_C__row_refs=[], nD="", ct_D=0, ct_D__col_refs=[], nE="", ct_E=0, ct_E__row_refs=[], nF="", ct_F=0, ct_F__row_refs=[])
c14 = dict(nums='', n0="", ct_0=0, ct_0__row_refs=[], n1="", ct_1=0, ct_1__row_refs=[], n2="", ct_2=0, ct_2__row_refs=[], n3="", ct_3=0, ct_3__row_refs=[], n4="", ct_4=0, ct_4__row_refs=[], n5="", ct_5=0, ct_5__row_refs=[], n6="", ct_6=0, ct_6__row_refs=[], n7="", ct_7=0, ct_7__row_refs=[
], n8="", ct_8=0, ct_8__row_refs=[], n9="", ct_9=0, ct_9__row_refs=[], nA="", ct_A=0, ct_A__row_refs=[], nB="", ct_B=0, ct_B__row_refs=[], nC="", ct_C=0, ct_C__row_refs=[], nD="", ct_D=0, ct_D__col_refs=[], nE="", ct_E=0, ct_E__row_refs=[], nF="", ct_F=0, ct_F__row_refs=[])
c15 = dict(nums='', n0="", ct_0=0, ct_0__row_refs=[], n1="", ct_1=0, ct_1__row_refs=[], n2="", ct_2=0, ct_2__row_refs=[], n3="", ct_3=0, ct_3__row_refs=[], n4="", ct_4=0, ct_4__row_refs=[], n5="", ct_5=0, ct_5__row_refs=[], n6="", ct_6=0, ct_6__row_refs=[], n7="", ct_7=0, ct_7__row_refs=[
], n8="", ct_8=0, ct_8__row_refs=[], n9="", ct_9=0, ct_9__row_refs=[], nA="", ct_A=0, ct_A__row_refs=[], nB="", ct_B=0, ct_B__row_refs=[], nC="", ct_C=0, ct_C__row_refs=[], nD="", ct_D=0, ct_D__col_refs=[], nE="", ct_E=0, ct_E__row_refs=[], nF="", ct_F=0, ct_F__row_refs=[])
c16 = dict(nums='', n0="", ct_0=0, ct_0__row_refs=[], n1="", ct_1=0, ct_1__row_refs=[], n2="", ct_2=0, ct_2__row_refs=[], n3="", ct_3=0, ct_3__row_refs=[], n4="", ct_4=0, ct_4__row_refs=[], n5="", ct_5=0, ct_5__row_refs=[], n6="", ct_6=0, ct_6__row_refs=[], n7="", ct_7=0, ct_7__row_refs=[
], n8="", ct_8=0, ct_8__row_refs=[], n9="", ct_9=0, ct_9__row_refs=[], nA="", ct_A=0, ct_A__row_refs=[], nB="", ct_B=0, ct_B__row_refs=[], nC="", ct_C=0, ct_C__row_refs=[], nD="", ct_D=0, ct_D__col_refs=[], nE="", ct_E=0, ct_E__row_refs=[], nF="", ct_F=0, ct_F__row_refs=[])

# s_9_num_cts_old = dict(n0 = "", n0_row_ct = 0, n0_col_ct = 0, n1 = "", n1_row_ct = 0, n1_col_ct = 0, n2 = "", n2_row_ct = 0, n2_col_ct = 0, n3 = "", n3_row_ct = 0, n3_col_ct = 0, n4 = "", n4_row_ct = 0, n4_col_ct = 0, n5 = "", n5_row_ct = 0, n5_col_ct = 0,n6 = "", n6_row_ct = 0, n6_col_ct = 0, n7 = "", n7_row_ct = 0, n7_col_ct = 0, n8 = "", n8_row_ct = 0, n8_col_ct = 0, n9 = "", n9_row_ct = 0, n9_col_ct = 0, nA = "", nA_row_ct = 0, nA_col_ct = 0, nB = "", nB_row_ct = 0, nB_col_ct = 0, nC = "", nC_row_ct = 0, nC_col_ct = 0, nD = "", nD_row_ct = 0, nD_col_ct = 0, nE = "", nE_row_ct = 0, nE_col_ct = 0, nF = "", nF_row_ct = 0, nF_col_ct = 0)
''' The s_9_num_cts dictionary stores the count of the number of rows, the number of columns, and the number of times a number occurs in the square.
Thus, s_9_num_cts[7][2][1][2] would record that the number 7 occurs in 2 rows, in 1 column and 2 times in the square.'''
# s_9_num_cts = [[0, [], [], []], [1, [], [], []], [2, [], [], []], [3, [], [], []], [4, [], [], []], [5, [], [], []], [6, [], [], []], [7, [], [], []], [
#     8, [], [], []], [9, [], [], []], ['A', [], [], []], ['B', [], [], []], ['C', [], [], []], ['D', [], [], []], ['E', [], [], []], ['F', [], [], []]]
s_9_num_cts = [['0', 0, 0, 0], ['1', 0, 0, 0], ['2', 0, 0, 0], ['3', 0, 0, 0], ['4', 0, 0, 0], ['5', 0, 0, 0], ['6', 0, 0, 0], [
    '7', 0, 0, 0], ['8', 0, 0, 0], ['9', 0, 0, 0], ['A', 0, 0, 0], ['B', 0, 0, 0], ['C', 0, 0, 0], ['D', 0, 0, 0], ['E', 0, 0, 0], ["F", 0, 0, 0]]
""" The following function isn't used."""


def update_done_arefs_list(aref):
    print("134 Entering update_done_arefs_list aref is ", aref)
    for aref in arrRefs_List:
        if aref['done'] == True:
            not_done_arefs.remove(aref)
            done_arefs_list.append(aref)
    print("219 not_done_arefs ", not_done_arefs)
    print("220 done_arefs_list ", done_arefs_list)


btn_ref = {}
# btn_ref = dict(btn='btn_R1C1', aref='arrRef0')

arrStringsRemaining = ""
bShow = False

main_frame = Frame(root)
main_frame.grid(row=0, column=0, columnspan=10)
main_frame.config(highlightbackground="red", highlightthickness=2)
main_canvas = Canvas(main_frame)
main_canvas.grid(row=0, column=0, columnspan=10)
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
sn_frame.grid(row=2, column=16, sticky="nw")
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
fn_frame.grid(row=3, column=16, sticky="nw")
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
ex_frame.grid(row=4, column=16, sticky="nw")
ex_frame.config(highlightbackground="red", highlightthickness=2)
txt_frame = Frame(main_canvas)
txt_frame.grid(row=5, column=16, sticky="nw")
txt_frame.config(highlightbackground="red", highlightthickness=2)


def set_current_num_to_0():
    global currentNumber
    currentNumber = "0"
    txt_Explain.insert(END, 'set_current_num_to_0()\n')
    history = 'set_current_num_to_0()\n'
    save_current_to_history(history)
    print("228 history is ", history)
    print("227 Current number is ", currentNumber)


def set_current_num_to_1():
    global currentNumber
    currentNumber = "1"
    txt_Explain.insert(END, 'set_current_num_to_1()\n')
    history = 'set_current_num_to_1()\n'
    save_current_to_history(history)
    print("228 history is ", history)
    print("233 Current number is ", currentNumber)


def set_current_num_to_2():
    global currentNumber
    currentNumber = "2"
    txt_Explain.insert(END, 'set_current_num_to_2()\n')
    history = 'set_current_num_to_2()\n'
    save_current_to_history(history)
    print("239 Current number is ", currentNumber)


def set_current_num_to_3():
    global currentNumber
    currentNumber = "3"
    txt_Explain.insert(END, 'set_current_num_to_3()\n')
    history = 'set_current_num_to_3()\n'
    save_current_to_history(history)
    print("245 Current number is ", currentNumber)


def set_current_num_to_4():
    global currentNumber
    currentNumber = "4"
    txt_Explain.insert(END, 'set_current_num_to_4()\n')
    history = 'set_current_num_to_4()\n'
    save_current_to_history(history)
    print("251 Current number is ", currentNumber)


def set_current_num_to_5():
    global currentNumber
    currentNumber = "5"
    txt_Explain.insert(END, 'set_current_num_to_5()\n')
    history = 'set_current_num_to_5()\n'
    save_current_to_history(history)
    print("257 Current number is ", currentNumber)


def set_current_num_to_6():
    global currentNumber
    currentNumber = "6"
    txt_Explain.insert(END, 'set_current_num_to_6()\n')
    history = 'set_current_num_to_6()\n'
    save_current_to_history(history)
    print("263 Current number is ", currentNumber)


def set_current_num_to_7():
    print("button 7 pressed.")
    global currentNumber
    currentNumber = "7"
    txt_Explain.insert(END, 'set_current_num_to_7()\n')
    history = 'set_current_num_to_7()\n'
    save_current_to_history(history)
    print("270 Current number is ", currentNumber)


def set_current_num_to_8():
    global currentNumber
    currentNumber = "8"
    txt_Explain.insert(END, 'set_current_num_to_8()\n')
    history = 'set_current_num_to_8()\n'
    save_current_to_history(history)
    print("276 Current number is ", currentNumber)


def set_current_num_to_9():
    global currentNumber
    currentNumber = "9"
    txt_Explain.insert(END, 'set_current_num_to_9()\n')
    history = 'set_current_num_to_9()\n'
    save_current_to_history(history)
    print("282 Current number is ", currentNumber)


def set_current_num_to_A():
    global currentNumber
    currentNumber = "A"
    txt_Explain.insert(END, 'set_current_num_to_A()\n')
    history = 'set_current_num_to_A()\n'
    save_current_to_history(history)
    print("288 Current number is ", currentNumber)


def set_current_num_to_B():
    global currentNumber
    currentNumber = "B"
    txt_Explain.insert(END, 'set_current_num_to_B()\n')
    history = 'set_current_num_to_B()\n'
    save_current_to_history(history)
    print("294 Current number is ", currentNumber)


def set_current_num_to_C():
    global currentNumber
    currentNumber = "C"
    txt_Explain.insert(END, 'set_current_num_to_C()\n')
    history = 'set_current_num_to_C()\n'
    save_current_to_history(history)
    print("300 Current number is ", currentNumber)


def set_current_num_to_D():
    global currentNumber
    currentNumber = "D"
    txt_Explain.insert(END, 'set_current_num_to_D()\n')
    history = 'set_current_num_to_D()\n'
    save_current_to_history(history)
    print("306 Current number is ", currentNumber)


def set_current_num_to_E():
    global currentNumber
    currentNumber = "E"
    txt_Explain.insert(END, 'set_current_num_to_E()\n')
    history = 'set_current_num_to_E()\n'
    save_current_to_history(history)
    print("312 Current number is ", currentNumber)


def set_current_num_to_F():
    global currentNumber
    currentNumber = "F"
    txt_Explain.insert(END, 'set_current_num_to_F()\n')
    history = 'set_current_num_to_F()\n'
    save_current_to_history(history)
    print("318 Current number is ", currentNumber)


def num_in_row_col_of_sq():
    print("638 entering new num_in_row_col_of_sq")
    global s_9_num_cts
    global sq_1_arefs
    sq_1_arefs = []
    global sq_2_arefs
    sq_2_arefs = []
    global sq_3_arefs
    sq_3_arefs = []
    global sq_4_arefs
    sq_4_arefs = []
    global sq_5_arefs
    sq_5_arefs = []
    global sq_6_arefs
    sq_6_arefs = []
    global sq_7_arefs
    sq_7_arefs = []
    global sq_8_arefs
    sq_8_arefs = []
    global sq_9_arefs
    sq_9_arefs = []
    global sq_10_arefs
    sq_10_arefs = []
    global sq_11_arefs
    sq_11_arefs = []
    global sq_12_arefs
    sq_12_arefs = []
    global sq_13_arefs
    sq_13_arefs = []
    global sq_14_arefs
    sq_14_arefs = []
    global sq_15_arefs
    sq_15_arefs = []
    global sq_16_arefs
    sq_16_arefs = []
    global n_in_row_sq
    global n_in_col_sq
    make_current_arefs()
    print("700 after make_arefs")
    s_1_nums_set = []
    s_2_nums_set = []
    s_3_nums_set = []
    s_4_nums_set = []
    s_5_nums_set = []
    s_6_nums_set = []
    s_7_nums_set = []
    s_8_nums_set = []
    s_9_nums_set = []
    s_10_nums_set = []
    s_11_nums_set = []
    s_12_nums_set = []
    s_13_nums_set = []
    s_14_nums_set = []
    s_15_nums_set = []
    s_16_nums_set = []
    sq = 0
    for sq in n_1_16:
        '''Get the square references
           check each for not done
           process the whole square
           and store and report the results
           so user can use a fix function.
           The main concern is to limit complexity
           by completing only one square at a time.
           '''
        # Start by setting all row and col strings to ""
        print("685 square is ", sq)
        s_x_rows = []
        s_x_cols = []
        s_x_nums_set = []
        sr_1_nums = ""
        sr_2_nums = ""
        sr_3_nums = ""
        sr_4_nums = ""
        sc_1_nums = ""
        sc_2_nums = ""
        sc_3_nums = ""
        sc_4_nums = ""
        if sq == 1:
            sq_aref = sq_1_arefs
            s_x_nums_set = s_1_nums_set
        elif sq == 2:
            sq_aref = sq_2_arefs
            s_x_nums_set = s_2_nums_set
        elif sq == 3:
            sq_aref = sq_3_arefs
            s_x_nums_set = s_3_nums_set
        elif sq == 4:
            sq_aref = sq_4_arefs
            s_x_nums_set = s_4_nums_set
        elif sq == 5:
            sq_aref = sq_5_arefs
            s_x_nums_set = s_5_nums_set
        elif sq == 6:
            sq_aref = sq_6_arefs
            s_x_nums_set = s_6_nums_set
        elif sq == 7:
            sq_aref = sq_7_arefs
            s_x_nums_set = s_7_nums_set
        elif sq == 8:
            sq_aref = sq_8_arefs
            s_x_nums_set = s_8_nums_set
        elif sq == 9:
            sq_aref = sq_9_arefs
            s_x_nums_set = s_9_nums_set
        elif sq == 10:
            sq_aref = sq_10_arefs
            s_x_nums_set = s_10_nums_set
        elif sq == 11:
            sq_aref = sq_11_arefs
            s_x_nums_set = s_11_nums_set
        elif sq == 12:
            sq_aref = sq_12_arefs
            s_x_nums_set = s_12_nums_set
        elif sq == 13:
            sq_aref = sq_13_arefs
            s_x_nums_set = s_13_nums_set
        elif sq == 14:
            sq_aref = sq_14_arefs
            s_x_nums_set = s_14_nums_set
        elif sq == 15:
            sq_aref = sq_15_arefs
            s_x_nums_set = s_15_nums_set
        elif sq == 16:
            sq_aref = sq_16_arefs
            s_x_nums_set = s_16_nums_set
        # print("742 sq_aref is ", sq_aref)
        # s_9_rows = [r_9_nums, r_10_nums, r_11_nums, r_12_nums]
        # s_9_cols = [c_1_nums, c_2_nums, c_3_nums, c_4_nums]
        # print("745 s_9_cols ", s_9_cols)
        for aref in sq_aref:
            # print("747 sq_aref ", aref)
            sq = aref['sq']
            if aref['done'] == False:
                btn = aref['btn_str']
                # print("536 sq_9 ", aref['sq'], btn)
                row = aref['row']
                col = aref['col']
                sq = aref['sq']
                num = aref['nums']
                # print("541 aref in sq 9 is ", btn, row, col, sq, num)
                for n in num:
                    if not n in s_x_nums_set:
                        s_x_nums_set.append(n)
                #     # print("761 s_9_nums_set is ", s_9_nums_set)
                #     # s_9_num_cts[n][1].append(n)
                #     # s_9_num_cts[n][2].append(n)
                #     if n == 1:
                #         s_9_num_cts[1][1] += 1
                #         s_9_num_cts[1][2] += 1
                #         s_9_num_cts[1][3] += 1
                #         # print("641 s_9_num_cts ", s_9_num_cts)
                if row == 1:  # and not n in r_1_nums
                    sr_1_nums += aref['nums']
                    r_1_nums = row_nums[0][1]
                elif row == 2:
                    sr_2_nums += aref['nums']
                    r_2_nums = row_nums[1][1]
                elif row == 3:
                    sr_3_nums += aref['nums']
                    r_3_nums = row_nums[2][1]
                elif row == 4:  # and not n in r_4_nums
                    sr_4_nums += aref['nums']
                    r_4_nums = row_nums[3][1]
                elif row == 5:
                    sr_1_nums += aref['nums']
                    r_1_nums = row_nums[4][1]
                elif row == 6:
                    sr_2_nums += aref['nums']
                    r_2_nums = row_nums[5][1]
                elif row == 7:
                    sr_3_nums += aref['nums']
                    r_3_nums = row_nums[6][1]
                elif row == 8:
                    sr_4_nums += aref['nums']
                    r_4_nums = row_nums[7][1]
                elif row == 9:
                    sr_1_nums += aref['nums']
                    r_1_nums = row_nums[8][1]
                elif row == 10:
                    sr_2_nums += aref['nums']
                    r_2_nums = row_nums[9][1]
                elif row == 11:
                    sr_3_nums += aref['nums']
                    r_3_nums = row_nums[10][1]
                elif row == 12:
                    sr_4_nums += aref['nums']
                    r_4_nums = row_nums[11][1]
                elif row == 13:
                    sr_1_nums += aref['nums']
                    r_1_nums = row_nums[12][1]
                elif row == 14:
                    sr_2_nums += aref['nums']
                    r_2_nums = row_nums[13][1]
                elif row == 15:
                    sr_3_nums += aref['nums']
                    r_3_nums = row_nums[14][1]
                elif row == 16:
                    sr_4_nums += aref['nums']
                    r_4_nums = row_nums[15][1]
                if col == 1:  # and not n in c_1_nums
                    sc_1_nums += aref['nums']
                    c_1_nums = col_nums[0][1]
                elif col == 2:
                    sc_2_nums += aref['nums']
                    c_2_nums = col_nums[1][1]
                elif col == 3:
                    sc_3_nums += aref['nums']
                    c_3_nums = col_nums[2][1]
                elif col == 4:
                    sc_4_nums += aref['nums']
                    c_4_nums = col_nums[3][1]
                elif col == 5:
                    sc_1_nums += aref['nums']
                    c_1_nums = col_nums[4][1]
                elif col == 6:
                    sc_2_nums += aref['nums']
                    c_2_nums = col_nums[5][1]
                elif col == 7:
                    sc_3_nums += aref['nums']
                    c_3_nums = col_nums[6][1]
                elif col == 8:
                    sc_4_nums += aref['nums']
                    c_4_nums = col_nums[7][1]
                elif col == 9:
                    sc_1_nums += aref['nums']
                    c_1_nums = col_nums[8][1]
                elif col == 10:
                    sc_2_nums += aref['nums']
                    c_2_nums = col_nums[9][1]
                elif col == 11:
                    sc_3_nums += aref['nums']
                    c_3_nums = col_nums[10][1]
                elif col == 12:
                    sc_4_nums += aref['nums']
                    c_4_nums = col_nums[11][1]
                elif col == 13:
                    sc_1_nums += aref['nums']
                    c_1_nums = col_nums[12][1]
                elif col == 14:
                    sc_2_nums += aref['nums']
                    c_2_nums = col_nums[13][1]
                elif col == 15:
                    sc_3_nums += aref['nums']
                    c_3_nums = col_nums[14][1]
                elif col == 16:
                    sc_4_nums += aref['nums']
                    c_4_nums = col_nums[15][1]
        s_x_rows = [sr_1_nums, sr_2_nums, sr_3_nums, sr_4_nums]
        # s_x_rows = [r_1_nums, r_2_nums, r_3_nums, r_4_nums]
        s_x_cols = [sc_1_nums, sc_2_nums, sc_3_nums, sc_4_nums]
        # print("655 s_9_num_cts ", s_9_num_cts)
        print("800 s_x_rows ", s_x_rows)
        print("801 s_x_cols ", s_x_cols)
        print("802 s_x_nums_set", s_x_nums_set)
        for num in s_x_nums_set:
            if (num in sr_1_nums) and (num not in sr_2_nums) and (num not in sr_3_nums) and (num not in sr_4_nums):
                cnt = sr_1_nums.count(num)
                r_nums = r_1_nums.count(num)
                if r_nums > cnt:
                    ex_text = f"{num} is only in row 1 of square {sq}\n"
                    ex_text = ex_text + \
                        f"But {num} is in other cells of that row "
                    ex_text = ex_text + \
                        f"outside of that square\n"
                    ex_text = ex_text + f"{sq}, {num}, {cnt}, {r_nums}\n"
                    txt_Explain.insert(END, ex_text)
                    if not num in n_in_row_sq:
                        n_list = [sq, num]
                        n_in_row_sq.append(n_list)
            if (num in sr_2_nums) and (num not in sr_1_nums) and (num not in sr_3_nums) and (num not in sr_4_nums):
                cnt = sr_2_nums.count(num)
                r_nums = r_2_nums.count(num)
                if r_nums > cnt:
                    ex_text = f"{num} is only in row 2 of square {sq}\n"
                    ex_text = ex_text + \
                        f"But {num} is in other cells of that row "
                    ex_text = ex_text + \
                        f"outside of that square\n"
                    ex_text = ex_text + f"{sq}, {num}, {cnt}, {r_nums}\n"
                    txt_Explain.insert(END, ex_text)
                    if not num in n_in_row_sq:
                        n_list = [sq, num]
                        n_in_row_sq.append(n_list)
            if (num in sr_3_nums) and (num not in sr_1_nums) and (num not in sr_2_nums) and (num not in sr_4_nums):
                cnt = sr_3_nums.count(num)
                r_nums = r_3_nums.count(num)
                if r_nums > cnt:
                    ex_text = f"{num} is only in row 3 of square {sq}\n"
                    ex_text = ex_text + \
                        f"But {num} is in other cells of that row "
                    ex_text = ex_text + \
                        f"outside of that square\n"
                    ex_text = ex_text + f"{sq}, {num}, {cnt}, {r_nums}\n"
                    txt_Explain.insert(END, ex_text)
                    if not num in n_in_row_sq:
                        n_list = [sq, num]
                        n_in_row_sq.append(n_list)
            if (num in sr_4_nums) and (num not in sr_1_nums) and (num not in sr_2_nums) and (num not in sr_3_nums):
                cnt = sr_4_nums.count(num)
                r_nums = r_4_nums.count(num)
                if r_nums > cnt:
                    ex_text = f"{num} is only in row 4 of square {sq}\n"
                    ex_text = ex_text + \
                        f"But {num} is in other cells of that row "
                    ex_text = ex_text + \
                        f"outside of that square\n"
                    ex_text = ex_text + f"{sq}, {num}, {cnt}, {r_nums}\n"
                    txt_Explain.insert(END, ex_text)
                    if not num in n_in_row_sq:
                        n_list = [sq, num]
                        n_in_row_sq.append(n_list)
        for num in s_x_nums_set:
            if (num in sc_1_nums) and (num not in sc_2_nums) and (num not in sc_3_nums) and (num not in sc_4_nums):
                cnt = sc_1_nums.count(num)
                c_nums = c_1_nums.count(num)
                if c_nums > cnt:
                    ex_text = f"{num} is only in column 1 of square {sq}\n"
                    ex_text = ex_text + \
                        f"But {num} is in other cells of that column "
                    ex_text = ex_text + \
                        f"outside of that square\n"
                    ex_text = ex_text + f"{sq}, {num}, {cnt}, {r_nums}\n"
                    txt_Explain.insert(END, ex_text)
                    if not num in n_in_col_sq:
                        n_list = [sq, num]
                        n_in_col_sq.append(n_list)
            if (num in sc_2_nums) and (num not in sc_1_nums) and (num not in sc_3_nums) and (num not in sc_4_nums):
                cnt = sc_2_nums.count(num)
                c_nums = c_2_nums.count(num)
                if c_nums > cnt:
                    ex_text = f"{num} is only in column 2 of square {sq}\n"
                    ex_text = ex_text + \
                        f"But {num} is in other cells of that column "
                    ex_text = ex_text + \
                        f"outside of that square\n"
                    ex_text = ex_text + f"{sq}, {num}, {cnt}, {r_nums}\n"
                    txt_Explain.insert(END, ex_text)
                    if not num in n_in_col_sq:
                        n_list = [sq, num]
                        n_in_col_sq.append(n_list)
            if (num in sc_3_nums) and (num not in sc_1_nums) and (num not in sc_2_nums) and (num not in sc_4_nums):
                cnt = sc_3_nums.count(num)
                c_nums = c_3_nums.count(num)
                if c_nums > cnt:
                    ex_text = f"{num} is only in col 3 of square {sq}\n"
                    ex_text = ex_text + \
                        f"But {num} is in other cells of that column "
                    ex_text = ex_text + \
                        f"outside of that square\n"
                    ex_text = ex_text + f"{sq}, {num}, {cnt}, {r_nums}\n"
                    txt_Explain.insert(END, ex_text)
                    if not num in n_in_col_sq:
                        n_list = [sq, num]
                        n_in_col_sq.append(n_list)
            if (num in sc_4_nums) and (num not in sc_1_nums) and (num not in sc_2_nums) and (num not in sc_3_nums):
                cnt = sc_4_nums.count(num)
                c_nums = c_4_nums.count(num)
                if c_nums > cnt:
                    ex_text = f"{num} is only in col 4 of square {sq}\n"
                    ex_text = ex_text + \
                        f"But {num} is in other cells of that column "
                    ex_text = ex_text + \
                        f"outside of that square\n"
                    ex_text = ex_text + f"{sq}, {num}, {cnt}, {r_nums}\n"
                    txt_Explain.insert(END, ex_text)
                    if not num in n_in_col_sq:
                        n_list = [sq, num]
                        n_in_col_sq.append(n_list)


def remove_num_in_row_sq():
    print("955 entering remove_num_in_row_sq")
    print("956 n_in_row_sq ", n_in_row_sq, n_in_row_sq[0])
    print("957 n_in_row_sq ", n_in_row_sq[0],
          n_in_row_sq[0][0], n_in_row_sq[0][1])
    global bRemoveANumberFromACell
    global currentNumber
    for lsts in n_in_row_sq:
        print("960 n_in_row_sq ", lsts)
        r_sq = lsts[0]
        r_num = lsts[1]
        if r_sq in [1, 2, 3, 4]:
            r_sq_list = [1, 2, 3, 4]
        elif r_sq in [5, 6, 7, 8]:
            r_sq_list = [5, 6, 7, 8]
        elif r_sq in [9, 10, 11, 12]:
            r_sq_list = [9, 10, 11, 12]
        elif r_sq in [13, 14, 15, 16]:
            r_sq_list = [13, 14, 15, 16]

        print("957 row nums are ", r_sq, r_num)
        for aref in not_done_arefs:
            sq = aref['sq']
            nums = aref['nums']
            # row = aref['row']
            btn = aref['btn']
            btn_str = aref['btn_str']
            if sq in r_sq_list and r_num in nums:
                r_row = aref['row']
                print("971 sq and number are ", sq, nums)
                for aref in not_done_arefs:
                    str1_aref = aref['aref']
                    sq1 = aref['sq']
                    nums1 = aref['nums']
                    row1 = aref['row']
                    btn1 = aref['btn']
                    btn1_str = aref['btn_str']
                    if (not sq1 == sq) and (r_row == row1):
                        if r_num in nums1:
                            bRemoveANumberFromACell = True
                            currentNumber = r_num
                            update_cell(btn1, aref, btn1_str, str1_aref)
                            print("992 btn1 etc. ", btn1,
                                  aref, btn1_str, str1_aref)


def remove_num_in_col_sq():
    print("955 entering remove_num_in_col_sq")
    print("956 n_in_col_sq ", n_in_col_sq, n_in_col_sq[0])
    print("957 n_in_col_sq ", n_in_col_sq[0],
          n_in_col_sq[0][0], n_in_col_sq[0][1])
    global bRemoveANumberFromACell
    global currentNumber
    global not_done_arefs
    for lsts in n_in_col_sq:
        print("960 n_in_col_sq ", lsts)
        c_sq = lsts[0]
        c_num = lsts[1]
        if c_sq in [1, 5, 9, 13]:
            c_sq_list = [1, 2, 3, 4]
        elif c_sq in [2, 6, 10, 14]:
            c_sq_list = [5, 6, 7, 8]
        elif c_sq in [3, 7, 11, 15]:
            c_sq_list = [9, 10, 11, 12]
        elif c_sq in [4, 8, 12, 16]:
            c_sq_list = [13, 14, 15, 16]
    # first, get the correct column in the square
        for aref in not_done_arefs:
            sq = aref['sq']
            nums = aref['nums']
            if (sq == c_sq) and (c_num in nums):
                c_col = aref['col']
            else:
                print("1036 error finding sq column")
        print("957 row nums are ", c_sq, c_num)
        for aref in not_done_arefs:
            sq = aref['sq']
            nums = aref['nums']
            # row = aref['row']
            btn = aref['btn']
            btn_str = aref['btn_str']
            if sq in c_sq_list and c_num in nums:
                col1 = aref['col']
                print("971 sq and number are ", sq, nums)
                for aref in not_done_arefs:
                    str1_aref = aref['aref']
                    sq1 = aref['sq']
                    nums1 = aref['nums']
                    col1 = aref['col']
                    btn1 = aref['btn']
                    btn1_str = aref['btn_str']
                    if (not sq1 == c_sq) and (c_col == col1):
                        if c_num in nums1:
                            bRemoveANumberFromACell = True
                            currentNumber = c_num
                            update_cell(btn1, aref, btn1_str, str1_aref)
                            print("992 btn1 etc. ", btn1,
                                  aref, btn1_str, str1_aref)


def num_in_row_col_of_sq_too_complex():
    print("638 entering new num_in_row_col_of_sq")
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
    global s_9_nums
    global c_10_nums
    global c_11_nums
    global c_12_nums
    global c_13_nums
    global c_14_nums
    global c_15_nums
    global s_9_num_cts
    s1_r_1_nums = ""
    s1_r_2_nums = ""
    s1_r_3_nums = ""
    s1_r_4_nums = ""
    s2_r_1_nums = ""
    s2_r_2_nums = ""
    s2_r_3_nums = ""
    s2_r_4_nums = ""
    s3_r_1_nums = ""
    s3_r_2_nums = ""
    s3_r_3_nums = ""
    s3_r_4_nums = ""
    s4_r_1_nums = ""
    s4_r_2_nums = ""
    s4_r_3_nums = ""
    s4_r_4_nums = ""
    s5_r_5_nums = ""
    s5_r_6_nums = ""
    s5_r_7_nums = ""
    s5_r_8_nums = ""
    s6_r_5_nums = ""
    s6_r_6_nums = ""
    s6_r_7_nums = ""
    s6_r_8_nums = ""
    s7_r_5_nums = ""
    s7_r_6_nums = ""
    s7_r_7_nums = ""
    s7_r_8_nums = ""
    s8_r_5_nums = ""
    s8_r_6_nums = ""
    s8_r_7_nums = ""
    s8_r_8_nums = ""
    s9_r_9_nums = ""
    s9_r_10_nums = ""
    s9_r_11_nums = ""
    s9_r_12_nums = ""
    s10_r_9_nums = ""
    s10_r_10_nums = ""
    s10_r_11_nums = ""
    s10_r_12_nums = ""
    s11_r_9_nums = ""
    s11_r_10_nums = ""
    s11_r_11_nums = ""
    s11_r_12_nums = ""
    s12_r_9_nums = ""
    s12_r_10_nums = ""
    s12_r_11_nums = ""
    s12_r_12_nums = ""
    s13_r_13_nums = ""
    s13_r_14_nums = ""
    s13_r_15_nums = ""
    s13_r_16_nums = ""
    s14_r_13_nums = ""
    s14_r_14_nums = ""
    s14_r_15_nums = ""
    s14_r_16_nums = ""
    s15_r_13_nums = ""
    s15_r_14_nums = ""
    s15_r_15_nums = ""
    s15_r_16_nums = ""
    s16_r_13_nums = ""
    s16_r_14_nums = ""
    s16_r_15_nums = ""
    s16_r_16_nums = ""
    s1_c_1_nums = ""
    s1_c_2_nums = ""
    s1_c_3_nums = ""
    s1_c_4_nums = ""
    s2_c_5_nums = ""
    s2_c_6_nums = ""
    s2_c_7_nums = ""
    s2_c_8_nums = ""
    s3_c_9_nums = ""
    s3_c_10_nums = ""
    s3_c_11_nums = ""
    s3_c_12_nums = ""
    s4_c_13_nums = ""
    s4_c_14_nums = ""
    s4_c_15_nums = ""
    s4_c_16_nums = ""
    s5_c_1_nums = ""
    s5_c_2_nums = ""
    s5_c_3_nums = ""
    s5_c_4_nums = ""
    s6_c_5_nums = ""
    s6_c_6_nums = ""
    s6_c_7_nums = ""
    s6_c_8_nums = ""
    s7_c_9_nums = ""
    s7_c_10_nums = ""
    s7_c_11_nums = ""
    s7_c_12_nums = ""
    s8_c_13_nums = ""
    s8_c_14_nums = ""
    s8_c_15_nums = ""
    s8_c_16_nums = ""
    s9_c_1_nums = ""
    s9_c_2_nums = ""
    s9_c_3_nums = ""
    s9_c_4_nums = ""
    s10_c_5_nums = ""
    s10_c_6_nums = ""
    s10_c_7_nums = ""
    s10_c_8_nums = ""
    s11_c_9_nums = ""
    s11_c_10_nums = ""
    s11_c_11_nums = ""
    s11_c_12_nums = ""
    s12_c_13_nums = ""
    s12_c_14_nums = ""
    s12_c_15_nums = ""
    s12_c_16_nums = ""
    s13_c_1_nums = ""
    s13_c_2_nums = ""
    s13_c_3_nums = ""
    s13_c_4_nums = ""
    s14_c_5_nums = ""
    s14_c_6_nums = ""
    s14_c_7_nums = ""
    s14_c_8_nums = ""
    s15_c_9_nums = ""
    s15_c_10_nums = ""
    s15_c_11_nums = ""
    s15_c_12_nums = ""
    s16_c_13_nums = ""
    s16_c_14_nums = ""
    s16_c_15_nums = ""
    s16_c_16_nums = ""
    s_x_nums_set = []
    global sq_1_arefs
    sq_1_arefs = []
    global sq_2_arefs
    sq_2_arefs = []
    global sq_3_arefs
    sq_3_arefs = []
    global sq_4_arefs
    sq_4_arefs = []
    global sq_5_arefs
    sq_5_arefs = []
    global sq_6_arefs
    sq_6_arefs = []
    global sq_7_arefs
    sq_7_arefs = []
    global sq_8_arefs
    sq_8_arefs = []
    global sq_9_arefs
    sq_9_arefs = []
    global sq_10_arefs
    sq_10_arefs = []
    global sq_11_arefs
    sq_11_arefs = []
    global sq_12_arefs
    sq_12_arefs = []
    global sq_13_arefs
    sq_13_arefs = []
    global sq_14_arefs
    sq_14_arefs = []
    global sq_15_arefs
    sq_15_arefs = []
    global sq_16_arefs
    sq_16_arefs = []

    make_current_arefs()

    print("700 after make_arefs")
    row_adj = 0
    col_adj = 0
    # print("701 sq_9_arefs)", sq_9_arefs)
    for sq in n_1_16:
        # print("746 sq done? ", sq["done"])
        # if not sq["done"] == False:
        #     continue
        # print("746 sq in sq_arefs is ", sq)
        if sq == 1:
            sq_aref = sq_1_arefs
            row_adj = 0
            col_adj = 0
        # if (sq[0] in sq_1_arefs) or (sq[3] in sq_1_arefs) or (sq[7] in sq_1_arefs) or (sq[9] in sq_1_arefs):
        elif sq == 2:
            sq_aref = sq_2_arefs
            row_adj = 0
            col_adj = - 4
        # elif (sq[0] in sq_2_arefs) or (sq[3] in sq_2_arefs) or (sq[7] in sq_2_arefs) or (sq[9] in sq_2_arefs):

        # elif (sq[0] in sq_3_arefs) or (sq[3] in sq_3_arefs) or (sq[7] in sq_3_arefs) or (sq[9] in sq_3_arefs):
        elif sq == 3:
            sq_aref = sq_3_arefs
            row_adj = 0
            col_adj = - 8
        elif sq == 4:
            sq_aref = sq_4_arefs
            row_adj = 0
            col_adj = - 12
        elif sq == 5:
            sq_aref = sq_5_arefs
            row_adj = - 4
            col_adj = 0
        elif sq == 6:
            sq_aref = sq_6_arefs
            row_adj = - 4
            col_adj = - 4
        elif sq == 7:
            sq_aref = sq_7_arefs
            row_adj = - 4
            col_adj = - 8
        elif sq == 8:
            sq_aref = sq_8_arefs
            row_adj = - 4
            col_adj = - 12
        elif sq == 9:
            sq_aref = sq_9_arefs
            row_adj = - 8
            col_adj = 0
        elif sq == 10:
            sq_aref = sq_10_arefs
            row_adj = - 8
            col_adj = - 4
        elif sq == 11:
            sq_aref = sq_11_arefs
            row_adj = - 8
            col_adj = - 8
        elif sq == 12:
            sq_aref = sq_12_arefs
            row_adj = - 8
            col_adj = - 12
        elif sq == 13:
            sq_aref = sq_13_arefs
            row_adj = - 12
            col_adj = 0
        elif sq == 14:
            sq_aref = sq_14_arefs
            row_adj = - 12
            col_adj = - 4
        elif sq == 15:
            sq_aref = sq_15_arefs
            row_adj = - 12
            col_adj = - 8
        elif sq == 16:
            sq_aref = sq_16_arefs
            row_adj = - 12
            col_adj = - 12
        else:
            print("1245 error, no matching sq and aref")
            # or (sq[0] in sq_3_arefs) or (sq[0] in sq_8_arefs) or (sq[0] in sq_9_arefs):
        for aref in sq_aref:
            # print("786 aref is ", aref, sq_aref)
            sq = aref['sq']
            if aref['done'] == False:
                btn = aref['btn_str']
                row = aref['row']
                col = aref['col']
                # adj_row = aref['row'] + row_adj
                # adj_col = aref['col'] + col_adj
                sq = aref['sq']
                num = aref['nums']
                # print("757 aref in sq 9 is ", btn,
                #       adj_row, adj_col, sq, num)
                for n in num:
                    # n = int(nm)
                    if not n in s_x_nums_set:
                        s_x_nums_set.append(n)
                        # print("716 s_9_nums_set is ", s_9_nums_set)
                    if n == 1:
                        s_9_num_cts[1][1] += 1
                        s_9_num_cts[1][2] += 1
                        s_9_num_cts[1][3] += 1
                        print("767 s_9_num_cts ", s_9_num_cts)
                    if sq == 1 and row == 1:
                        s1_r_1_nums += n
                    elif sq == 1 and row == 2:
                        s1_r_2_nums += n
                    elif sq == 1 and row == 3:
                        s1_r_3_nums += n
                    elif sq == 1 and row == 4:
                        s1_r_4_nums += n
                    elif sq == 2 and row == 1:
                        s2_r_1_nums += n
                    elif sq == 2 and row == 2:
                        s2_r_2_nums += n
                    elif sq == 2 and row == 3:
                        s2_r_3_nums += n
                    elif sq == 2 and row == 4:
                        s2_r_4_nums += n
                    elif sq == 3 and row == 1:
                        s3_r_1_nums += n
                    elif sq == 3 and row == 2:
                        s3_r_2_nums += n
                    elif sq == 3 and row == 3:
                        s3_r_3_nums += n
                    elif sq == 3 and row == 4:
                        s3_r_4_nums += n
                    elif sq == 4 and row == 1:
                        s4_r_1_nums += n
                    elif sq == 4 and row == 2:
                        s4_r_2_nums += n
                    elif sq == 4 and row == 3:
                        s4_r_3_nums += n
                    elif sq == 4 and row == 4:
                        s4_r_4_nums += n
                    elif sq == 5 and row == 5:
                        s5_r_5_nums += n
                    elif sq == 5 and row == 6:
                        s5_r_6_nums += n
                    elif sq == 5 and row == 7:
                        s5_r_7_nums += n
                    elif sq == 5 and row == 8:
                        s5_r_8_nums += n
                    elif sq == 6 and row == 5:
                        s6_r_5_nums += n
                    elif sq == 6 and row == 6:
                        s6_r_6_nums += n
                    elif sq == 6 and row == 7:
                        s6_r_7_nums += n
                    elif sq == 6 and row == 8:
                        s6_r_8_nums += n
                    elif sq == 7 and row == 5:
                        s7_r_5_nums += n
                    elif sq == 7 and row == 6:
                        s7_r_6_nums += n
                    elif sq == 7 and row == 7:
                        s7_r_7_nums += n
                    elif sq == 7 and row == 8:
                        s7_r_8_nums += n
                    elif sq == 8 and row == 5:
                        s8_r_5_nums += n
                    elif sq == 8 and row == 6:
                        s8_r_6_nums += n
                    elif sq == 8 and row == 7:
                        s8_r_7_nums += n
                    elif sq == 8 and row == 8:
                        s8_r_8_nums += n
                    elif sq == 9 and row == 9:
                        s9_r_9_nums += n
                    elif sq == 9 and row == 10:
                        s9_r_10_nums += n
                    elif sq == 9 and row == 11:
                        s9_r_11_nums += n
                    elif sq == 9 and row == 12:
                        s9_r_12_nums += n
                    elif sq == 10 and row == 9:
                        s10_r_9_nums += n
                    elif sq == 10 and row == 10:
                        s10_r_10_nums += n
                    elif sq == 10 and row == 11:
                        s10_r_11_nums += n
                    elif sq == 10 and row == 12:
                        s10_r_12_nums += n
                    elif sq == 11 and row == 9:
                        s11_r_9_nums += n
                    elif sq == 11 and row == 10:
                        s11_r_10_nums += n
                    elif sq == 11 and row == 11:
                        s11_r_11_nums += n
                    elif sq == 11 and row == 12:
                        s11_r_12_nums += n
                    elif sq == 12 and row == 9:
                        s12_r_9_nums += n
                    elif sq == 12 and row == 10:
                        s12_r_10_nums += n
                    elif sq == 12 and row == 11:
                        s12_r_11_nums += n
                    elif sq == 12 and row == 12:
                        s12_r_12_nums += n
                    elif sq == 13 and row == 13:
                        s13_r_13_nums += n
                    elif sq == 13 and row == 14:
                        s13_r_14_nums += n
                    elif sq == 13 and row == 15:
                        s13_r_15_nums += n
                    elif sq == 13 and row == 16:
                        s13_r_16_nums += n
                    elif sq == 14 and row == 13:
                        s14_r_13_nums += n
                    elif sq == 14 and row == 14:
                        s14_r_14_nums += n
                    elif sq == 14 and row == 15:
                        s14_r_15_nums += n
                    elif sq == 14 and row == 16:
                        s14_r_16_nums += n
                    elif sq == 15 and row == 13:
                        s15_r_13_nums += n
                    elif sq == 15 and row == 14:
                        s15_r_14_nums += n
                    elif sq == 15 and row == 15:
                        s15_r_15_nums += n
                    elif sq == 15 and row == 16:
                        s15_r_16_nums += n
                    elif sq == 16 and row == 13:
                        s16_r_13_nums += n
                    elif sq == 16 and row == 14:
                        s16_r_14_nums += n
                    elif sq == 16 and row == 15:
                        s16_r_15_nums += n
                    elif sq == 16 and row == 16:
                        s16_r_16_nums += n

                    if sq == 1 and col == 1:
                        s1_c_1_nums += n
                    elif sq == 1 and col == 2:
                        s1_c_2_nums += n
                    elif sq == 1 and col == 3:
                        s1_c_3_nums += n
                    elif sq == 1 and col == 4:
                        s1_c_4_nums += n
                    elif sq == 2 and col == 5:
                        s2_c_5_nums += n
                    elif sq == 2 and col == 6:
                        s2_c_6_nums += n
                    elif sq == 2 and col == 7:
                        s2_c_7_nums += n
                    elif sq == 2 and col == 8:
                        s2_c_8_nums += n
                    elif sq == 3 and col == 9:
                        s3_c_9_nums += n
                    elif sq == 3 and col == 10:
                        s3_c_10_nums += n
                    elif sq == 3 and col == 11:
                        s3_c_11_nums += n
                    elif sq == 3 and col == 12:
                        s3_c_12_nums += n
                    elif sq == 4 and col == 13:
                        s4_c_13_nums += n
                    elif sq == 4 and col == 14:
                        s4_c_14_nums += n
                    elif sq == 4 and col == 15:
                        s4_c_15_nums += n
                    elif sq == 4 and col == 16:
                        s4_c_16_nums += n
                    elif sq == 5 and col == 1:
                        s5_c_1_nums += n
                    elif sq == 5 and col == 2:
                        s5_c_2_nums += n
                    elif sq == 5 and col == 3:
                        s5_c_3_nums += n
                    elif sq == 5 and col == 4:
                        s5_c_4_nums += n
                    elif sq == 6 and col == 5:
                        s6_c_5_nums += n
                    elif sq == 6 and col == 6:
                        s6_c_6_nums += n
                    elif sq == 6 and col == 7:
                        s6_c_7_nums += n
                    elif sq == 6 and col == 8:
                        s6_c_8_nums += n
                    elif sq == 7 and col == 9:
                        s7_c_9_nums += n
                    elif sq == 7 and col == 10:
                        s7_c_10_nums += n
                    elif sq == 7 and col == 11:
                        s7_c_11_nums += n
                    elif sq == 7 and col == 12:
                        s7_c_12_nums += n
                    elif sq == 8 and col == 13:
                        s8_c_13_nums += n
                    elif sq == 8 and col == 14:
                        s8_c_14_nums += n
                    elif sq == 8 and col == 15:
                        s8_c_15_nums += n
                    elif sq == 8 and col == 16:
                        s8_c_16_nums += n
                    elif sq == 9 and col == 1:
                        s9_c_1_nums += n
                    elif sq == 9 and col == 2:
                        s9_c_2_nums += n
                    elif sq == 9 and col == 3:
                        s9_c_3_nums += n
                    elif sq == 9 and col == 4:
                        s9_c_4_nums += n
                    elif sq == 10 and col == 5:
                        s10_c_5_nums += n
                    elif sq == 10 and col == 6:
                        s10_c_6_nums += n
                    elif sq == 10 and col == 7:
                        s10_c_7_nums += n
                    elif sq == 10 and col == 8:
                        s10_c_8_nums += n
                    elif sq == 11 and col == 9:
                        s11_c_9_nums += n
                    elif sq == 11 and col == 10:
                        s11_c_10_nums += n
                    elif sq == 11 and col == 11:
                        s11_c_11_nums += n
                    elif sq == 11 and col == 12:
                        s11_c_12_nums += n
                    elif sq == 12 and col == 13:
                        s12_c_13_nums += n
                    elif sq == 12 and col == 14:
                        s12_c_14_nums += n
                    elif sq == 12 and col == 15:
                        s12_c_15_nums += n
                    elif sq == 12 and col == 16:
                        s12_c_16_nums += n
                    elif sq == 13 and col == 1:
                        s13_c_1_nums += n
                    elif sq == 13 and col == 2:
                        s13_c_2_nums += n
                    elif sq == 13 and col == 3:
                        s13_c_3_nums += n
                    elif sq == 13 and col == 4:
                        s13_c_4_nums += n
                    elif sq == 14 and col == 5:
                        s14_c_5_nums += n
                    elif sq == 14 and col == 6:
                        s14_c_6_nums += n
                    elif sq == 14 and col == 7:
                        s14_c_7_nums += n
                    elif sq == 14 and col == 8:
                        s14_c_8_nums += n
                    elif sq == 15 and col == 9:
                        s15_c_9_nums += n
                    elif sq == 15 and col == 10:
                        s15_c_10_nums += n
                    elif sq == 15 and col == 11:
                        s15_c_11_nums += n
                    elif sq == 15 and col == 12:
                        s15_c_12_nums += n
                    elif sq == 16 and col == 13:
                        s16_c_13_nums += n
                    elif sq == 16 and col == 14:
                        s16_c_14_nums += n
                    elif sq == 16 and col == 15:
                        s16_c_15_nums += n
                    elif sq == 16 and col == 16:
                        s16_c_16_nums += n

    # s_9_rows = [r_9_nums, r_10_nums, r_11_nums, r_12_nums]
    # s_9_cols = [c_1_nums, c_2_nums, c_3_nums, c_4_nums]
    # print("655 s_9_num_cts ", s_9_num_cts)
    # print("570 s_9_cols ", s_9_cols)
    print("789 s_x_nums_set", sq, s_x_nums_set)
    # for num in s_9_nums_set:
    #     c = 8
    #     # print("569 num is ", num)
    #     for row_n in s_9_rows:
    #         c += 1
    #         if num in row_n:
    #             pass
    # print("749 s_9_nums_set ", s_9_nums_set)
    for num in s_x_nums_set:
        # print("751 num ", num, c_1_nums, c_2_nums, c_3_nums, c_4_nums)
        print("797 num ", num, c_1_nums)
        # print("798 num ", num, c_2_nums)
        # print("799 num ", num, c_3_nums)
        # print("800 num ", num, c_4_nums)
        if (num in c_1_nums) and (num not in c_2_nums) and (num not in c_3_nums) and (num not in c_4_nums):
            print("675 num in only col 1 ", sq, num)
        if (num in c_2_nums) and (num not in c_1_nums) and (num not in c_3_nums) and (num not in c_4_nums):
            print("677 num in only col 2 ", sq, num)
        if (num in c_3_nums) and (num not in c_1_nums) and (num not in c_2_nums) and (num not in c_4_nums):
            print("679 num in only col 3 ", sq, num)
        if (num in c_4_nums) and (num not in c_1_nums) and (num not in c_2_nums) and (num not in c_3_nums):
            print("681 num in only col 4 ", sq, num)


def num_in_row_col_of_sq_old():
    global r_9_nums
    global r_10_nums
    global r_11_nums
    global r_12_nums
    global c_1_nums
    global c_2_nums
    global c_3_nums
    global c_4_nums
    global s_9_nums
    global s_9_num_cts
    r_9_nums = ""
    r_10_nums = ""
    r_11_nums = ""
    r_12_nums = ""
    c_1_nums = ""
    c_2_nums = ""
    c_3_nums = ""
    c_4_nums = ""
    s_1_nums_set = []
    s_2_nums_set = []
    s_3_nums_set = []
    s_4_nums_set = []
    s_5_nums_set = []
    s_6_nums_set = []
    s_7_nums_set = []
    s_8_nums_set = []
    s_9_nums_set = []
    s_10_nums_set = []
    s_11_nums_set = []
    s_12_nums_set = []
    s_13_nums_set = []
    s_14_nums_set = []
    s_15_nums_set = []
    s_16_nums_set = []
    # s_9_rows = [9, 10, 11, 12]
    s_9_rows = [r_9_nums, r_10_nums, r_11_nums, r_12_nums]
    s_9_cols = [c_1_nums, c_2_nums, c_3_nums, c_4_nums]
    print("534 s_9_cols ", s_9_cols)
    for aref in sq_9_arefs:
        print("662 sq_9_arefs ", aref)
        sq = aref['sq']
        if aref['done'] == False:
            btn = aref['btn_str']
            # print("536 sq_9 ", aref['sq'], btn)
            row = aref['row']
            col = aref['col']
            sq = aref['sq']
            num = aref['nums']
            # print("541 aref in sq 9 is ", btn, row, col, sq, num)
            for n in num:
                # n = int(nm)
                if not n in s_9_nums_set:
                    s_9_nums_set.append(n)
                print("676 s_9_nums_set is ", s_9_nums_set)
                # s_9_num_cts[n][1].append(n)
                # s_9_num_cts[n][2].append(n)
                if n == 1:
                    s_9_num_cts[1][1] += 1
                    s_9_num_cts[1][2] += 1
                    s_9_num_cts[1][3] += 1
                    print("641 s_9_num_cts ", s_9_num_cts)

            if row == 9:
                r_9_nums += aref['nums']
            elif row == 10:
                r_10_nums += aref['nums']
            elif row == 11:
                r_11_nums += aref['nums']
            elif row == 12:
                r_12_nums += aref['nums']
            if col == 1:
                c_1_nums += aref['nums']
            elif col == 2:
                c_2_nums += aref['nums']
            elif col == 3:
                c_3_nums += aref['nums']
            elif col == 4:
                c_4_nums += aref['nums']

    s_9_rows = [r_9_nums, r_10_nums, r_11_nums, r_12_nums]
    s_9_cols = [c_1_nums, c_2_nums, c_3_nums, c_4_nums]
    # print("655 s_9_num_cts ", s_9_num_cts)
    print("570 s_9_cols ", s_9_cols)
    print("665 s_9_nums_set", s_9_nums_set)
    for num in s_9_nums_set:
        c = 8
        # print("569 num is ", num)
        for row_n in s_9_rows:
            c += 1
            if num in row_n:
                pass
                # print("584 num in row ", num, c)
    for num in s_9_nums_set:
        if (num in c_1_nums) and (num not in c_2_nums) and (num not in c_3_nums) and (num not in c_4_nums):
            print("675 num in only col 1 ", num)
        if (num in c_2_nums) and (num not in c_1_nums) and (num not in c_3_nums) and (num not in c_4_nums):
            print("677 num in only col 1 ", num)
        if (num in c_3_nums) and (num not in c_1_nums) and (num not in c_2_nums) and (num not in c_4_nums):
            print("679 num in only col 1 ", num)
        if (num in c_4_nums) and (num not in c_1_nums) and (num not in c_2_nums) and (num not in c_3_nums):
            print("681 num in only col 1 ", num)
        # c = 0
        # col_ct = 0
        # # print("569 num is ", num)
        # for col_n in s_9_cols:
        #     c += 1
        #     # print("571 col_n is ", col_n)
        #     if num in col_n:
        #         col_ct += 1
        #         print("592 num in column ", num, c)
        #         if col_ct == 1:
        #             print("664 num in only 1 col of sq ", num, c)


def make_RCS_sets_1():
    ''' Make sets of the sets of nums in each cell in
        each row, col, and sq. --> r_1_s = {'378A', '89AE', '37', '18', '139', '089A', '07A', '39AE'}
    '''
    print("322 Entered make_RCS_sets_1")
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
    # print("396 len(not_done_arefs) is ", len(not_done_arefs))

    for cell in not_done_arefs:
        nums = (cell['nums'])
        if nums:  # > len(cell['nums']):
            btn = (cell['btn_str'])
            row = (cell['row'])
            col = (cell['col'])
            sq = (cell['sq'])
            print("400 cell ", btn, row, col, sq)
            if cell['row'] == 1 and len(cell['nums']) < 14:
                r_1_set.add(cell['nums'])
            elif cell['row'] == 2 and len(cell['nums']) < 14:
                r_2_set.add(cell['nums'])
            elif cell['row'] == 3 and len(cell['nums']) < 14:
                r_3_set.add(cell['nums'])
            elif cell['row'] == 4 and len(cell['nums']) < 14:
                r_4_set.add(cell['nums'])
            elif cell['row'] == 5 and len(cell['nums']) < 14:
                r_5_set.add(cell['nums'])
            elif cell['row'] == 6 and len(cell['nums']) < 14:
                r_6_set.add(cell['nums'])
            elif cell['row'] == 7 and len(cell['nums']) < 14:
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
            if cell['sq'] == 9 and len(cell['nums']) < 14:
                s_9_set.add(cell['nums'])
    print("461 r_X_set are ", r_1_set, r_2_set, r_3_set, r_4_set, r_5_set, r_6_set, r_7_set, r_8_set,
          r_9_set, r_10_set, r_11_set, r_12_set, r_13_set, r_14_set, r_15_set, r_16_set, s_9_set)


def only_1_num_in_cell():
    for cell in not_done_arefs:
        global currentNumber
        if cell['done'] == False and len(cell['nums']) == 1:
            row_num = cell['row']
            col_num = cell['col']
            sq_num = cell['sq']
            num = cell['nums']
            btn = cell['btn']
            btn_name = cell['btn_str']
            print("527 not done cell num is ",
                  row_num, col_num, sq_num, num)
            currentNumber = num
            # eval(f"set_current_num_to_{num}()")
            update_cell(btn, cell, btn_name, str(cell))


def CheckForOnlyOneNumber():
    print("670 Entered CheckForOnlyOneNumber")
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
    ex_text = ""

    for cell in not_done_arefs:
        current_button = cell['btn']
        btn_name = cell['btn_str']
        print("709 ", cell, current_button)
        print("710 ", btn_name)
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

    temp_list = []
    for row in r_nums_list:
        row_nums = eval(row)
        for char in startingString:
            if char in row_nums:
                if row_nums.count(char) == 1:
                    row_num = row.strip('r_')
                    row_num = row_num.strip('_nums')
                    temp_list = [row_num, char]
                    delete_singles_row_list.append(temp_list)
                    ex_text = char + " only occurs once in row " + row_num + "\n"
                    txt_Explain.insert(END, ex_text)
                    if bSolve_singles == True:
                        print("823 bSolve_singles == True")
                        currentNumber = char
                        btn = cell['btn']
                        # aref = btn_dict[btn]
                        update_cell(btn, cell)

    for col in c_nums_list:
        col_nums = eval(col)
        for char in startingString:
            if char in col_nums:
                if col_nums.count(char) == 1:
                    col_num = col.strip('c_')
                    col_num = col_num.strip('_nums')
                    temp_list = [col_num, char]
                    delete_singles_col_list.append(temp_list)
                    ex_text = char + " only occurs once in col " + col_num + "\n"
                    txt_Explain.insert(END, ex_text)
                    if bSolve_singles == True:
                        currentNumber = char
                        btn = cell['btn']
                        update_cell(btn, cell)
    for sq in sq_nums_list:
        sq_nums = eval(sq)
        for char in startingString:
            if char in sq_nums:
                if sq_nums.count(char) == 1:
                    sq_num = sq.strip('r_')
                    sq_num = sq_num.strip('_nums')
                    temp_list = [sq_num, char]
                    delete_singles_sq_list.append(temp_list)
                    ex_text = char + " only occurs once in square " + sq_num + "\n"
                    txt_Explain.insert(END, ex_text)
                    if bSolve_singles == True:
                        currentNumber = char
                        btn = cell['btn']
                        update_cell(btn, cell)
    cells_done()
    cells_remaining()


def solve_rcs_singles():
    print("564 Entering solve_singles")
    bSolve_singles = True
    print("877 delete_singles_row_list is ", delete_singles_row_list)
    for cell in not_done_arefs:
        print("1103 cell and type ", cell, type(cell))
        nums = cell['nums']
        row = cell['row']
        col = cell['col']
        sq = cell['sq']
        for item in delete_singles_row_list:
            if row == int(item[0]) and item[1] in nums:
                currentNumber = item[1]
                current_button = cell['btn']
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
                remove_aref_from_not_done_arefs(cell)
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
        nums = cell['nums']
        row = cell['row']
        col = cell['col']
        sq = cell['sq']
        for item in delete_singles_col_list:
            if col == int(item[0]) and item[1] in nums:
                print("521 col item ", col, type(row),
                      item[0], type(int(item[0])), item[1])
                currentNumber = item[1]
                current_button = cell['btn']
                print("572 cell and type are ", type(current_button),
                      current_button, type(cell), cell)
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
                remove_aref_from_not_done_arefs(cell)
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
        nums = cell['nums']
        row = cell['row']
        col = cell['col']
        sq = cell['sq']
        for item in delete_singles_sq_list:
            if sq == int(item[0]) and item[1] in nums:
                currentNumber = item[1]
                current_button = cell['btn']
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
                remove_aref_from_not_done_arefs(cell)
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


def make_RCS_sets():
    """ 1072
    Use make_RCS_lists to fill in the numbers in a R, C, or S
    Iterate through all done cells and remove the num from the row_X_nums =
    string "0123456789ABCDEF" These are the numbers remaining in the RCS.
    Use this list to check for "in" the row nums
    """
    global row_1_nums
    global row_2_nums
    global row_3_nums
    global row_4_nums
    global row_5_nums
    global row_6_nums
    global row_7_nums
    global row_8_nums
    global row_9_nums
    global row_10_nums
    global row_11_nums
    global row_12_nums
    global row_13_nums
    global row_14_nums
    global row_15_nums
    global row_16_nums
    global row_1_nums
    global col_1_nums
    global col_2_nums
    global col_3_nums
    global col_4_nums
    global col_5_nums
    global col_6_nums
    global col_7_nums
    global col_8_nums
    global col_9_nums
    global col_10_nums
    global col_11_nums
    global col_12_nums
    global col_13_nums
    global col_14_nums
    global col_15_nums
    global col_16_nums
    global sq_1_nums
    global sq_2_nums
    global sq_3_nums
    global sq_4_nums
    global sq_5_nums
    global sq_6_nums
    global sq_7_nums
    global sq_8_nums
    global sq_9_nums
    global sq_10_nums
    global sq_11_nums
    global sq_12_nums
    global sq_13_nums
    global sq_14_nums
    global sq_15_nums
    global sq_16_nums

    for cell in done_arefs_list:
        btn = cell['btn_str']
        row = cell['row']
        col = cell['col']
        sq = cell['sq']
        num = cell['nums']
        # print("1084 btn ", btn, row, col, sq, num)
        if row == 1:
            temp_str = row_1_nums.replace(num, "")
            row_1_nums = temp_str
        elif row == 2:
            temp_str = row_2_nums.replace(num, "")
            row_2_nums = temp_str
        elif row == 3:
            temp_str = row_3_nums.replace(num, "")
            row_3_nums = temp_str
        elif row == 4:
            temp_str = row_4_nums.replace(num, "")
            row_4_nums = temp_str
        elif row == 5:
            temp_str = row_5_nums.replace(num, "")
            row_5_nums = temp_str
        elif row == 6:
            temp_str = row_6_nums.replace(num, "")
            row_6_nums = temp_str
        elif row == 7:
            temp_str = row_7_nums.replace(num, "")
            row_7_nums = temp_str
        elif row == 8:
            temp_str = row_8_nums.replace(num, "")
            row_8_nums = temp_str
        elif row == 9:
            temp_str = row_9_nums.replace(num, "")
            row_9_nums = temp_str
        elif row == 10:
            temp_str = row_10_nums.replace(num, "")
            row_10_nums = temp_str
        elif row == 11:
            temp_str = row_11_nums.replace(num, "")
            row_11_nums = temp_str
        elif row == 12:
            temp_str = row_12_nums.replace(num, "")
            row_12_nums = temp_str
        elif row == 13:
            temp_str = row_13_nums.replace(num, "")
            row_13_nums = temp_str
        elif row == 14:
            temp_str = row_14_nums.replace(num, "")
            row_14_nums = temp_str
        elif row == 15:
            temp_str = row_15_nums.replace(num, "")
            row_15_nums = temp_str
        elif row == 16:
            temp_str = row_16_nums.replace(num, "")
            row_16_nums = temp_str

        if col == 1:
            temp_str = col_1_nums.replace(num, "")
            col_1_nums = temp_str
        elif col == 2:
            temp_str = col_2_nums.replace(num, "")
            col_2_nums = temp_str
        elif col == 3:
            temp_str = col_3_nums.replace(num, "")
            col_3_nums = temp_str
        elif col == 4:
            temp_str = col_4_nums.replace(num, "")
            col_4_nums = temp_str
        elif col == 5:
            temp_str = col_5_nums.replace(num, "")
            col_5_nums = temp_str
        elif col == 6:
            temp_str = col_6_nums.replace(num, "")
            col_6_nums = temp_str
        elif col == 7:
            temp_str = col_7_nums.replace(num, "")
            col_7_nums = temp_str
        elif col == 8:
            temp_str = col_8_nums.replace(num, "")
            col_8_nums = temp_str
        elif col == 9:
            temp_str = col_9_nums.replace(num, "")
            col_9_nums = temp_str
        elif col == 10:
            temp_str = col_10_nums.replace(num, "")
            col_10_nums = temp_str
        elif col == 11:
            temp_str = col_11_nums.replace(num, "")
            col_11_nums = temp_str
        elif col == 12:
            temp_str = col_12_nums.replace(num, "")
            col_12_nums = temp_str
        elif col == 13:
            temp_str = col_13_nums.replace(num, "")
            col_13_nums = temp_str
        elif col == 14:
            temp_str = col_14_nums.replace(num, "")
            col_14_nums = temp_str
        elif col == 15:
            temp_str = col_15_nums.replace(num, "")
            col_15_nums = temp_str
        elif col == 16:
            temp_str = col_16_nums.replace(num, "")
            col_16_nums = temp_str

        if sq == 1:
            temp_str = sq_1_nums.replace(num, "")
            sq_1_nums = temp_str
        elif sq == 2:
            temp_str = sq_2_nums.replace(num, "")
            sq_2_nums = temp_str
        elif sq == 3:
            temp_str = sq_3_nums.replace(num, "")
            sq_3_nums = temp_str
        elif sq == 4:
            temp_str = sq_4_nums.replace(num, "")
            sq_4_nums = temp_str
        elif sq == 5:
            temp_str = sq_5_nums.replace(num, "")
            sq_5_nums = temp_str
        elif sq == 6:
            temp_str = sq_6_nums.replace(num, "")
            sq_6_nums = temp_str
        elif sq == 7:
            temp_str = sq_7_nums.replace(num, "")
            sq_7_nums = temp_str
        elif sq == 8:
            temp_str = sq_8_nums.replace(num, "")
            sq_8_nums = temp_str
        elif sq == 9:
            temp_str = sq_9_nums.replace(num, "")
            sq_9_nums = temp_str
        elif sq == 10:
            temp_str = sq_10_nums.replace(num, "")
            sq_1_nums = temp_str
        elif sq == 11:
            temp_str = sq_11_nums.replace(num, "")
            sq_11_nums = temp_str
        elif sq == 12:
            temp_str = sq_12_nums.replace(num, "")
            sq_12_nums = temp_str
        elif sq == 13:
            temp_str = sq_13_nums.replace(num, "")
            sq_13_nums = temp_str
        elif sq == 14:
            temp_str = sq_14_nums.replace(num, "")
            sq_14_nums = temp_str
        elif sq == 15:
            temp_str = sq_15_nums.replace(num, "")
            sq_15_nums = temp_str
        elif sq == 16:
            temp_str = sq_16_nums.replace(num, "")
            sq_16_nums = temp_str


def make_row_dicts():
    row_arefs = []
    nums = []
    ct = 0
    col_arefs = []

    global r1
    global r2
    global r3
    global r4
    global r5
    global r7
    global r8
    global r9
    global r10
    global r11
    global r12
    global r13
    global r14
    global r15
    global r16

    for cell in not_done_arefs:
        aref = cell['aref']
        row = cell['row']
        col = cell['col']
        sq = cell['sq']
        nums = cell['nums']
        ct = 0
        cols = []
        col_ct = 0
        if row == 1:
            r1['nums'] = row_1_nums
            for num in nums:
                if num == '0':
                    r1['n0'] = '0'
                    ct = r1['ct_0'] + 1
                    r1['ct_0'] = ct
                    r1['ct_0__col_refs'].append(aref)
                elif num == '1':
                    r1['n1'] = '1'
                    ct = r1['ct_1'] + 1
                    r1['ct_1'] = ct
                    r1['ct_1__col_refs'].append(aref)
                elif num == '2':
                    r1['n2'] = '2'
                    ct = r1['ct_2'] + 1
                    r1['ct_2'] = ct
                    r1['ct_2__col_refs'].append(aref)
                elif num == '3':
                    r1['n3'] = '3'
                    ct = r1['ct_3'] + 1
                    r1['ct_3'] = ct
                    r1['ct_3__col_refs'].append(aref)
                elif num == '4':
                    r1['n4'] = '4'
                    ct = r1['ct_4'] + 1
                    r1['ct_4'] = ct
                    r1['ct_4__col_refs'].append(aref)
                elif num == '5':
                    r1['n5'] = '5'
                    ct = r1['ct_5'] + 1
                    r1['ct_5'] = ct
                    r1['ct_5__col_refs'].append(aref)
                elif num == '6':
                    r1['n6'] = '6'
                    ct = r1['ct_6'] + 1
                    r1['ct_6'] = ct
                    r1['ct_6__col_refs'].append(aref)
                elif num == '7':
                    r1['n7'] = '7'
                    ct = r1['ct_7'] + 1
                    r1['ct_7'] = ct
                    r1['ct_7__col_refs'].append(aref)
                elif num == '8':
                    r1['n8'] = '8'
                    ct = r1['ct_8'] + 1
                    r1['ct_8'] = ct
                    r1['ct_8__col_refs'].append(aref)
                elif num == '9':
                    r1['n9'] = '9'
                    ct = r1['ct_9'] + 1
                    r1['ct_9'] = ct
                    r1['ct_9__col_refs'].append(aref)
                elif num == 'A':
                    r1['nA'] = 'A'
                    ct = r1['ct_A'] + 1
                    r1['ct_A'] = ct
                    r1['ct_A__col_refs'].append(aref)
                elif num == 'B':
                    r1['nB'] = 'B'
                    ct = r1['ct_B'] + 1
                    r1['ct_B'] = ct
                    r1['ct_B__col_refs'].append(aref)
                elif num == 'C':
                    r1['nC'] = 'C'
                    ct = r1['ct_C'] + 1
                    r1['ct_C'] = ct
                    r1['ct_C__col_refs'].append(aref)
                elif num == 'D':
                    r1['nD'] = 'D'
                    ct = r1['ct_D'] + 1
                    r1['ct_D'] = ct
                    r1['ct_D__col_refs'].append(aref)
                elif num == 'E':
                    r1['nE'] = 'E'
                    ct = r1['ct_E'] + 1
                    r1['ct_E'] = ct
                    r1['ct_E__col_refs'].append(aref)
                elif num == 'F':
                    r1['nF'] = 'F'
                    ct = r1['ct_F'] + 1
                    r1['ct_F'] = ct
                    r1['ct_F__col_refs'].append(aref)
                else:
                    print("1448 fell through if num")

        elif row == 2:
            r2['nums'] = row_2_nums
            for num in nums:
                if num == '0':
                    r2['n0'] = '0'
                    ct = r2['ct_0'] + 1
                    r2['ct_0'] = ct
                    r2['ct_0__col_refs'].append(aref)
                elif num == '1':
                    r2['n1'] = '1'
                    ct = r2['ct_1'] + 1
                    r2['ct_1'] = ct
                    r2['ct_1__col_refs'].append(aref)
                elif num == '2':
                    r2['n2'] = '2'
                    ct = r2['ct_2'] + 1
                    r2['ct_2'] = ct
                    r2['ct_2__col_refs'].append(aref)
                elif num == '3':
                    r2['n3'] = '3'
                    ct = r2['ct_3'] + 1
                    r2['ct_3'] = ct
                    r2['ct_3__col_refs'].append(aref)
                elif num == '4':
                    r2['n4'] = '4'
                    ct = r2['ct_4'] + 1
                    r2['ct_4'] = ct
                    r2['ct_4__col_refs'].append(aref)
                elif num == '5':
                    r2['n5'] = '5'
                    ct = r2['ct_5'] + 1
                    r2['ct_5'] = ct
                    r2['ct_5__col_refs'].append(aref)
                elif num == '6':
                    r2['n6'] = '6'
                    ct = r2['ct_6'] + 1
                    r2['ct_6'] = ct
                    r2['ct_6__col_refs'].append(aref)
                elif num == '7':
                    r2['n7'] = '7'
                    ct = r2['ct_7'] + 1
                    r2['ct_7'] = ct
                    r2['ct_7__col_refs'].append(aref)
                elif num == '8':
                    r2['n8'] = '8'
                    ct = r2['ct_8'] + 1
                    r2['ct_8'] = ct
                    r2['ct_8__col_refs'].append(aref)
                elif num == '9':
                    r2['n9'] = '9'
                    ct = r2['ct_9'] + 1
                    r2['ct_9'] = ct
                    r2['ct_9__col_refs'].append(aref)
                elif num == 'A':
                    r2['nA'] = 'A'
                    ct = r2['ct_A'] + 1
                    r2['ct_A'] = ct
                    r2['ct_A__col_refs'].append(aref)
                elif num == 'B':
                    r2['nB'] = 'B'
                    ct = r2['ct_B'] + 1
                    r2['ct_B'] = ct
                    r2['ct_B__col_refs'].append(aref)
                elif num == 'C':
                    r2['nC'] = 'C'
                    ct = r2['ct_C'] + 1
                    r2['ct_C'] = ct
                    r2['ct_C__col_refs'].append(aref)
                elif num == 'D':
                    r2['nD'] = 'D'
                    ct = r2['ct_D'] + 1
                    r2['ct_D'] = ct
                    r2['ct_D__col_refs'].append(aref)
                elif num == 'E':
                    r2['nE'] = 'E'
                    ct = r2['ct_E'] + 1
                    r2['ct_E'] = ct
                    r2['ct_E__col_refs'].append(aref)
                elif num == 'F':
                    r2['nF'] = 'F'
                    ct = r2['ct_F'] + 1
                    r2['ct_F'] = ct
                    r2['ct_F__col_refs'].append(aref)
                else:
                    print("1448 fell through if num")
        elif row == 3:
            r3['nums'] = row_3_nums
            for num in nums:
                if num == '0':
                    r3['n0'] = '0'
                    ct = r3['ct_0'] + 1
                    r3['ct_0'] = ct
                    r3['ct_0__col_refs'].append(aref)
                elif num == '1':
                    r3['n1'] = '1'
                    ct = r3['ct_1'] + 1
                    r3['ct_1'] = ct
                    r3['ct_1__col_refs'].append(aref)
                elif num == '2':
                    r3['n2'] = '2'
                    ct = r3['ct_2'] + 1
                    r3['ct_2'] = ct
                    r3['ct_2__col_refs'].append(aref)
                elif num == '3':
                    r3['n3'] = '3'
                    ct = r3['ct_3'] + 1
                    r3['ct_3'] = ct
                    r3['ct_3__col_refs'].append(aref)
                elif num == '4':
                    r3['n4'] = '4'
                    ct = r3['ct_4'] + 1
                    r3['ct_4'] = ct
                    r3['ct_4__col_refs'].append(aref)
                elif num == '5':
                    r3['n5'] = '5'
                    ct = r3['ct_5'] + 1
                    r3['ct_5'] = ct
                    r3['ct_5__col_refs'].append(aref)
                elif num == '6':
                    r3['n6'] = '6'
                    ct = r3['ct_6'] + 1
                    r3['ct_6'] = ct
                    r3['ct_6__col_refs'].append(aref)
                elif num == '7':
                    r3['n7'] = '7'
                    ct = r3['ct_7'] + 1
                    r3['ct_7'] = ct
                    r3['ct_7__col_refs'].append(aref)
                elif num == '8':
                    r3['n8'] = '8'
                    ct = r3['ct_8'] + 1
                    r3['ct_8'] = ct
                    r3['ct_8__col_refs'].append(aref)
                elif num == '9':
                    r3['n9'] = '9'
                    ct = r3['ct_9'] + 1
                    r3['ct_9'] = ct
                    r3['ct_9__col_refs'].append(aref)
                elif num == 'A':
                    r3['nA'] = 'A'
                    ct = r3['ct_A'] + 1
                    r3['ct_A'] = ct
                    r3['ct_A__col_refs'].append(aref)
                elif num == 'B':
                    r3['nB'] = 'B'
                    ct = r3['ct_B'] + 1
                    r3['ct_B'] = ct
                    r3['ct_B__col_refs'].append(aref)
                elif num == 'C':
                    r3['nC'] = 'C'
                    ct = r3['ct_C'] + 1
                    r3['ct_C'] = ct
                    r3['ct_C__col_refs'].append(aref)
                elif num == 'D':
                    r3['nD'] = 'D'
                    ct = r3['ct_D'] + 1
                    r3['ct_D'] = ct
                    r3['ct_D__col_refs'].append(aref)
                elif num == 'E':
                    r3['nE'] = 'E'
                    ct = r3['ct_E'] + 1
                    r3['ct_E'] = ct
                    r3['ct_E__col_refs'].append(aref)
                elif num == 'F':
                    r3['nF'] = 'F'
                    ct = r3['ct_F'] + 1
                    r3['ct_F'] = ct
                    r3['ct_F__col_refs'].append(aref)
                else:
                    print("1448 fell through if num")
        if row == 4:
            r4['nums'] = row_4_nums
            for num in nums:
                if num == '0':
                    r4['n0'] = '0'
                    ct = r4['ct_0'] + 1
                    r4['ct_0'] = ct
                    r4['ct_0__col_refs'].append(aref)
                elif num == '1':
                    r4['n1'] = '1'
                    ct = r4['ct_1'] + 1
                    r4['ct_1'] = ct
                    r4['ct_1__col_refs'].append(aref)
                elif num == '2':
                    r4['n2'] = '2'
                    ct = r4['ct_2'] + 1
                    r4['ct_2'] = ct
                    r4['ct_2__col_refs'].append(aref)
                elif num == '3':
                    r4['n3'] = '3'
                    ct = r4['ct_3'] + 1
                    r4['ct_3'] = ct
                    r4['ct_3__col_refs'].append(aref)
                elif num == '4':
                    r4['n4'] = '4'
                    ct = r4['ct_4'] + 1
                    r4['ct_4'] = ct
                    r4['ct_4__col_refs'].append(aref)
                elif num == '5':
                    r4['n5'] = '5'
                    ct = r4['ct_5'] + 1
                    r4['ct_5'] = ct
                    r4['ct_5__col_refs'].append(aref)
                elif num == '6':
                    r4['n6'] = '6'
                    ct = r4['ct_6'] + 1
                    r4['ct_6'] = ct
                    r4['ct_6__col_refs'].append(aref)
                elif num == '7':
                    r4['n7'] = '7'
                    ct = r4['ct_7'] + 1
                    r4['ct_7'] = ct
                    r4['ct_7__col_refs'].append(aref)
                elif num == '8':
                    r4['n8'] = '8'
                    ct = r4['ct_8'] + 1
                    r4['ct_8'] = ct
                    r4['ct_8__col_refs'].append(aref)
                elif num == '9':
                    r4['n9'] = '9'
                    ct = r4['ct_9'] + 1
                    r4['ct_9'] = ct
                    r4['ct_9__col_refs'].append(aref)
                elif num == 'A':
                    r4['nA'] = 'A'
                    ct = r4['ct_A'] + 1
                    r4['ct_A'] = ct
                    r4['ct_A__col_refs'].append(aref)
                elif num == 'B':
                    r4['nB'] = 'B'
                    ct = r4['ct_B'] + 1
                    r4['ct_B'] = ct
                    r4['ct_B__col_refs'].append(aref)
                elif num == 'C':
                    r4['nC'] = 'C'
                    ct = r4['ct_C'] + 1
                    r4['ct_C'] = ct
                    r4['ct_C__col_refs'].append(aref)
                elif num == 'D':
                    r4['nD'] = 'D'
                    ct = r4['ct_D'] + 1
                    r4['ct_D'] = ct
                    r4['ct_D__col_refs'].append(aref)
                elif num == 'E':
                    r4['nE'] = 'E'
                    ct = r4['ct_E'] + 1
                    r4['ct_E'] = ct
                    r4['ct_E__col_refs'].append(aref)
                elif num == 'F':
                    r4['nF'] = 'F'
                    ct = r4['ct_F'] + 1
                    r4['ct_F'] = ct
                    r4['ct_F__col_refs'].append(aref)
                else:
                    print("1448 fell through if num")
        if row == 5:
            r5['nums'] = row_5_nums
            for num in nums:
                if num == '0':
                    r5['n0'] = '0'
                    ct = r5['ct_0'] + 1
                    r5['ct_0'] = ct
                    r5['ct_0__col_refs'].append(aref)
                elif num == '1':
                    r5['n1'] = '1'
                    ct = r5['ct_1'] + 1
                    r5['ct_1'] = ct
                    r5['ct_1__col_refs'].append(aref)
                elif num == '2':
                    r5['n2'] = '2'
                    ct = r5['ct_2'] + 1
                    r5['ct_2'] = ct
                    r5['ct_2__col_refs'].append(aref)
                elif num == '3':
                    r5['n3'] = '3'
                    ct = r5['ct_3'] + 1
                    r5['ct_3'] = ct
                    r5['ct_3__col_refs'].append(aref)
                elif num == '4':
                    r5['n4'] = '4'
                    ct = r5['ct_4'] + 1
                    r5['ct_4'] = ct
                    r5['ct_4__col_refs'].append(aref)
                elif num == '5':
                    r5['n5'] = '5'
                    ct = r5['ct_5'] + 1
                    r5['ct_5'] = ct
                    r5['ct_5__col_refs'].append(aref)
                elif num == '6':
                    r5['n6'] = '6'
                    ct = r5['ct_6'] + 1
                    r5['ct_6'] = ct
                    r5['ct_6__col_refs'].append(aref)
                elif num == '7':
                    r5['n7'] = '7'
                    ct = r5['ct_7'] + 1
                    r5['ct_7'] = ct
                    r5['ct_7__col_refs'].append(aref)
                elif num == '8':
                    r5['n8'] = '8'
                    ct = r5['ct_8'] + 1
                    r5['ct_8'] = ct
                    r5['ct_8__col_refs'].append(aref)
                elif num == '9':
                    r5['n9'] = '9'
                    ct = r5['ct_9'] + 1
                    r5['ct_9'] = ct
                    r5['ct_9__col_refs'].append(aref)
                elif num == 'A':
                    r5['nA'] = 'A'
                    ct = r5['ct_A'] + 1
                    r5['ct_A'] = ct
                    r5['ct_A__col_refs'].append(aref)
                elif num == 'B':
                    r5['nB'] = 'B'
                    ct = r5['ct_B'] + 1
                    r5['ct_B'] = ct
                    r5['ct_B__col_refs'].append(aref)
                elif num == 'C':
                    r5['nC'] = 'C'
                    ct = r5['ct_C'] + 1
                    r5['ct_C'] = ct
                    r5['ct_C__col_refs'].append(aref)
                elif num == 'D':
                    r5['nD'] = 'D'
                    ct = r5['ct_D'] + 1
                    r5['ct_D'] = ct
                    r5['ct_D__col_refs'].append(aref)
                elif num == 'E':
                    r5['nE'] = 'E'
                    ct = r5['ct_E'] + 1
                    r5['ct_E'] = ct
                    r5['ct_E__col_refs'].append(aref)
                elif num == 'F':
                    r5['nF'] = 'F'
                    ct = r5['ct_F'] + 1
                    r5['ct_F'] = ct
                    r5['ct_F__col_refs'].append(aref)
                else:
                    print("1448 fell through if num")
        if row == 6:
            r6['nums'] = row_6_nums
            for num in nums:
                if num == '0':
                    r6['n0'] = '0'
                    ct = r6['ct_0'] + 1
                    r6['ct_0'] = ct
                    r6['ct_0__col_refs'].append(aref)
                elif num == '1':
                    r6['n1'] = '1'
                    ct = r6['ct_1'] + 1
                    r6['ct_1'] = ct
                    r6['ct_1__col_refs'].append(aref)
                elif num == '2':
                    r6['n2'] = '2'
                    ct = r6['ct_2'] + 1
                    r6['ct_2'] = ct
                    r6['ct_2__col_refs'].append(aref)
                elif num == '3':
                    r6['n3'] = '3'
                    ct = r6['ct_3'] + 1
                    r6['ct_3'] = ct
                    r6['ct_3__col_refs'].append(aref)
                elif num == '4':
                    r6['n4'] = '4'
                    ct = r6['ct_4'] + 1
                    r6['ct_4'] = ct
                    r6['ct_4__col_refs'].append(aref)
                elif num == '5':
                    r6['n5'] = '5'
                    ct = r6['ct_5'] + 1
                    r6['ct_5'] = ct
                    r6['ct_5__col_refs'].append(aref)
                elif num == '6':
                    r6['n6'] = '6'
                    ct = r6['ct_6'] + 1
                    r6['ct_6'] = ct
                    r6['ct_6__col_refs'].append(aref)
                elif num == '7':
                    r6['n7'] = '7'
                    ct = r6['ct_7'] + 1
                    r6['ct_7'] = ct
                    r6['ct_7__col_refs'].append(aref)
                elif num == '8':
                    r6['n8'] = '8'
                    ct = r6['ct_8'] + 1
                    r6['ct_8'] = ct
                    r6['ct_8__col_refs'].append(aref)
                elif num == '9':
                    r6['n9'] = '9'
                    ct = r6['ct_9'] + 1
                    r6['ct_9'] = ct
                    r6['ct_9__col_refs'].append(aref)
                elif num == 'A':
                    r6['nA'] = 'A'
                    ct = r6['ct_A'] + 1
                    r6['ct_A'] = ct
                    r6['ct_A__col_refs'].append(aref)
                elif num == 'B':
                    r6['nB'] = 'B'
                    ct = r6['ct_B'] + 1
                    r6['ct_B'] = ct
                    r6['ct_B__col_refs'].append(aref)
                elif num == 'C':
                    r6['nC'] = 'C'
                    ct = r6['ct_C'] + 1
                    r6['ct_C'] = ct
                    r6['ct_C__col_refs'].append(aref)
                elif num == 'D':
                    r6['nD'] = 'D'
                    ct = r6['ct_D'] + 1
                    r6['ct_D'] = ct
                    r6['ct_D__col_refs'].append(aref)
                elif num == 'E':
                    r6['nE'] = 'E'
                    ct = r6['ct_E'] + 1
                    r6['ct_E'] = ct
                    r6['ct_E__col_refs'].append(aref)
                elif num == 'F':
                    r6['nF'] = 'F'
                    ct = r6['ct_F'] + 1
                    r6['ct_F'] = ct
                    r6['ct_F__col_refs'].append(aref)
                else:
                    print("1448 fell through if num")
        if row == 7:
            r7['nums'] = row_7_nums
            for num in nums:
                if num == '0':
                    r7['n0'] = '0'
                    ct = r7['ct_0'] + 1
                    r7['ct_0'] = ct
                    r7['ct_0__col_refs'].append(aref)
                elif num == '1':
                    r7['n1'] = '1'
                    ct = r7['ct_1'] + 1
                    r7['ct_1'] = ct
                    r7['ct_1__col_refs'].append(aref)
                elif num == '2':
                    r7['n2'] = '2'
                    ct = r7['ct_2'] + 1
                    r7['ct_2'] = ct
                    r7['ct_2__col_refs'].append(aref)
                elif num == '3':
                    r7['n3'] = '3'
                    ct = r7['ct_3'] + 1
                    r7['ct_3'] = ct
                    r7['ct_3__col_refs'].append(aref)
                elif num == '4':
                    r7['n4'] = '4'
                    ct = r7['ct_4'] + 1
                    r7['ct_4'] = ct
                    r7['ct_4__col_refs'].append(aref)
                elif num == '5':
                    r7['n5'] = '5'
                    ct = r7['ct_5'] + 1
                    r7['ct_5'] = ct
                    r7['ct_5__col_refs'].append(aref)
                elif num == '6':
                    r7['n6'] = '6'
                    ct = r7['ct_6'] + 1
                    r7['ct_6'] = ct
                    r7['ct_6__col_refs'].append(aref)
                elif num == '7':
                    r7['n7'] = '7'
                    ct = r7['ct_7'] + 1
                    r7['ct_7'] = ct
                    r7['ct_7__col_refs'].append(aref)
                elif num == '8':
                    r7['n8'] = '8'
                    ct = r7['ct_8'] + 1
                    r7['ct_8'] = ct
                    r7['ct_8__col_refs'].append(aref)
                elif num == '9':
                    r7['n9'] = '9'
                    ct = r7['ct_9'] + 1
                    r7['ct_9'] = ct
                    r7['ct_9__col_refs'].append(aref)
                elif num == 'A':
                    r7['nA'] = 'A'
                    ct = r7['ct_A'] + 1
                    r7['ct_A'] = ct
                    r7['ct_A__col_refs'].append(aref)
                elif num == 'B':
                    r7['nB'] = 'B'
                    ct = r7['ct_B'] + 1
                    r7['ct_B'] = ct
                    r7['ct_B__col_refs'].append(aref)
                elif num == 'C':
                    r7['nC'] = 'C'
                    ct = r7['ct_C'] + 1
                    r7['ct_C'] = ct
                    r7['ct_C__col_refs'].append(aref)
                elif num == 'D':
                    r7['nD'] = 'D'
                    ct = r7['ct_D'] + 1
                    r7['ct_D'] = ct
                    r7['ct_D__col_refs'].append(aref)
                elif num == 'E':
                    r7['nE'] = 'E'
                    ct = r7['ct_E'] + 1
                    r7['ct_E'] = ct
                    r7['ct_E__col_refs'].append(aref)
                elif num == 'F':
                    r7['nF'] = 'F'
                    ct = r7['ct_F'] + 1
                    r7['ct_F'] = ct
                    r7['ct_F__col_refs'].append(aref)
                else:
                    print("1448 fell through if num")
        if row == 8:
            r8['nums'] = row_8_nums
            for num in nums:
                if num == '0':
                    r8['n0'] = '0'
                    ct = r8['ct_0'] + 1
                    r8['ct_0'] = ct
                    r8['ct_0__col_refs'].append(aref)
                elif num == '1':
                    r8['n1'] = '1'
                    ct = r8['ct_1'] + 1
                    r8['ct_1'] = ct
                    r8['ct_1__col_refs'].append(aref)
                elif num == '2':
                    r8['n2'] = '2'
                    ct = r8['ct_2'] + 1
                    r8['ct_2'] = ct
                    r8['ct_2__col_refs'].append(aref)
                elif num == '3':
                    r8['n3'] = '3'
                    ct = r8['ct_3'] + 1
                    r8['ct_3'] = ct
                    r8['ct_3__col_refs'].append(aref)
                elif num == '4':
                    r8['n4'] = '4'
                    ct = r8['ct_4'] + 1
                    r8['ct_4'] = ct
                    r8['ct_4__col_refs'].append(aref)
                elif num == '5':
                    r8['n5'] = '5'
                    ct = r8['ct_5'] + 1
                    r8['ct_5'] = ct
                    r8['ct_5__col_refs'].append(aref)
                elif num == '6':
                    r8['n6'] = '6'
                    ct = r8['ct_6'] + 1
                    r8['ct_6'] = ct
                    r8['ct_6__col_refs'].append(aref)
                elif num == '7':
                    r8['n7'] = '7'
                    ct = r8['ct_7'] + 1
                    r8['ct_7'] = ct
                    r8['ct_7__col_refs'].append(aref)
                elif num == '8':
                    r8['n8'] = '8'
                    ct = r8['ct_8'] + 1
                    r8['ct_8'] = ct
                    r8['ct_8__col_refs'].append(aref)
                elif num == '9':
                    r8['n9'] = '9'
                    ct = r8['ct_9'] + 1
                    r8['ct_9'] = ct
                    r8['ct_9__col_refs'].append(aref)
                elif num == 'A':
                    r8['nA'] = 'A'
                    ct = r8['ct_A'] + 1
                    r8['ct_A'] = ct
                    r8['ct_A__col_refs'].append(aref)
                elif num == 'B':
                    r8['nB'] = 'B'
                    ct = r8['ct_B'] + 1
                    r8['ct_B'] = ct
                    r8['ct_B__col_refs'].append(aref)
                elif num == 'C':
                    r8['nC'] = 'C'
                    ct = r8['ct_C'] + 1
                    r8['ct_C'] = ct
                    r8['ct_C__col_refs'].append(aref)
                elif num == 'D':
                    r8['nD'] = 'D'
                    ct = r8['ct_D'] + 1
                    r8['ct_D'] = ct
                    r8['ct_D__col_refs'].append(aref)
                elif num == 'E':
                    r8['nE'] = 'E'
                    ct = r8['ct_E'] + 1
                    r8['ct_E'] = ct
                    r8['ct_E__col_refs'].append(aref)
                elif num == 'F':
                    r8['nF'] = 'F'
                    ct = r8['ct_F'] + 1
                    r8['ct_F'] = ct
                    r8['ct_F__col_refs'].append(aref)
                else:
                    print("1448 fell through if num")
        if row == 9:
            r9['nums'] = row_9_nums
            for num in nums:
                if num == '0':
                    r9['n0'] = '0'
                    ct = r9['ct_0'] + 1
                    r9['ct_0'] = ct
                    r9['ct_0__col_refs'].append(aref)
                elif num == '1':
                    r9['n1'] = '1'
                    ct = r9['ct_1'] + 1
                    r9['ct_1'] = ct
                    r9['ct_1__col_refs'].append(aref)
                elif num == '2':
                    r9['n2'] = '2'
                    ct = r9['ct_2'] + 1
                    r9['ct_2'] = ct
                    r9['ct_2__col_refs'].append(aref)
                elif num == '3':
                    r9['n3'] = '3'
                    ct = r9['ct_3'] + 1
                    r9['ct_3'] = ct
                    r9['ct_3__col_refs'].append(aref)
                elif num == '4':
                    r9['n4'] = '4'
                    ct = r9['ct_4'] + 1
                    r9['ct_4'] = ct
                    r9['ct_4__col_refs'].append(aref)
                elif num == '5':
                    r9['n5'] = '5'
                    ct = r9['ct_5'] + 1
                    r9['ct_5'] = ct
                    r9['ct_5__col_refs'].append(aref)
                elif num == '6':
                    r9['n6'] = '6'
                    ct = r9['ct_6'] + 1
                    r9['ct_6'] = ct
                    r9['ct_6__col_refs'].append(aref)
                elif num == '7':
                    r9['n7'] = '7'
                    ct = r9['ct_7'] + 1
                    r9['ct_7'] = ct
                    r9['ct_7__col_refs'].append(aref)
                elif num == '8':
                    r9['n8'] = '8'
                    ct = r9['ct_8'] + 1
                    r9['ct_8'] = ct
                    r9['ct_8__col_refs'].append(aref)
                elif num == '9':
                    r9['n9'] = '9'
                    ct = r9['ct_9'] + 1
                    r9['ct_9'] = ct
                    r9['ct_9__col_refs'].append(aref)
                elif num == 'A':
                    r9['nA'] = 'A'
                    ct = r9['ct_A'] + 1
                    r9['ct_A'] = ct
                    r9['ct_A__col_refs'].append(aref)
                elif num == 'B':
                    r9['nB'] = 'B'
                    ct = r9['ct_B'] + 1
                    r9['ct_B'] = ct
                    r9['ct_B__col_refs'].append(aref)
                elif num == 'C':
                    r9['nC'] = 'C'
                    ct = r9['ct_C'] + 1
                    r9['ct_C'] = ct
                    r9['ct_C__col_refs'].append(aref)
                elif num == 'D':
                    r9['nD'] = 'D'
                    ct = r9['ct_D'] + 1
                    r9['ct_D'] = ct
                    r9['ct_D__col_refs'].append(aref)
                elif num == 'E':
                    r9['nE'] = 'E'
                    ct = r9['ct_E'] + 1
                    r9['ct_E'] = ct
                    r9['ct_E__col_refs'].append(aref)
                elif num == 'F':
                    r9['nF'] = 'F'
                    ct = r9['ct_F'] + 1
                    r9['ct_F'] = ct
                    r9['ct_F__col_refs'].append(aref)
                else:
                    print("1448 fell through if num")
        if row == 10:
            r10['nums'] = row_10_nums
            for num in nums:
                if num == '0':
                    r10['n0'] = '0'
                    ct = r10['ct_0'] + 1
                    r10['ct_0'] = ct
                    r10['ct_0__col_refs'].append(aref)
                elif num == '1':
                    r10['n1'] = '1'
                    ct = r10['ct_1'] + 1
                    r10['ct_1'] = ct
                    r10['ct_1__col_refs'].append(aref)
                elif num == '2':
                    r10['n2'] = '2'
                    ct = r10['ct_2'] + 1
                    r10['ct_2'] = ct
                    r10['ct_2__col_refs'].append(aref)
                elif num == '3':
                    r10['n3'] = '3'
                    ct = r10['ct_3'] + 1
                    r10['ct_3'] = ct
                    r10['ct_3__col_refs'].append(aref)
                elif num == '4':
                    r10['n4'] = '4'
                    ct = r10['ct_4'] + 1
                    r10['ct_4'] = ct
                    r10['ct_4__col_refs'].append(aref)
                elif num == '5':
                    r10['n5'] = '5'
                    ct = r10['ct_5'] + 1
                    r10['ct_5'] = ct
                    r10['ct_5__col_refs'].append(aref)
                elif num == '6':
                    r10['n6'] = '6'
                    ct = r10['ct_6'] + 1
                    r10['ct_6'] = ct
                    r10['ct_6__col_refs'].append(aref)
                elif num == '7':
                    r10['n7'] = '7'
                    ct = r10['ct_7'] + 1
                    r10['ct_7'] = ct
                    r10['ct_7__col_refs'].append(aref)
                elif num == '8':
                    r10['n8'] = '8'
                    ct = r10['ct_8'] + 1
                    r10['ct_8'] = ct
                    r10['ct_8__col_refs'].append(aref)
                elif num == '9':
                    r10['n9'] = '9'
                    ct = r10['ct_9'] + 1
                    r10['ct_9'] = ct
                    r10['ct_9__col_refs'].append(aref)
                elif num == 'A':
                    r10['nA'] = 'A'
                    ct = r10['ct_A'] + 1
                    r10['ct_A'] = ct
                    r10['ct_A__col_refs'].append(aref)
                elif num == 'B':
                    r10['nB'] = 'B'
                    ct = r10['ct_B'] + 1
                    r10['ct_B'] = ct
                    r10['ct_B__col_refs'].append(aref)
                elif num == 'C':
                    r10['nC'] = 'C'
                    ct = r10['ct_C'] + 1
                    r10['ct_C'] = ct
                    r10['ct_C__col_refs'].append(aref)
                elif num == 'D':
                    r10['nD'] = 'D'
                    ct = r10['ct_D'] + 1
                    r10['ct_D'] = ct
                    r10['ct_D__col_refs'].append(aref)
                elif num == 'E':
                    r10['nE'] = 'E'
                    ct = r10['ct_E'] + 1
                    r10['ct_E'] = ct
                    r10['ct_E__col_refs'].append(aref)
                elif num == 'F':
                    r10['nF'] = 'F'
                    ct = r10['ct_F'] + 1
                    r10['ct_F'] = ct
                    r10['ct_F__col_refs'].append(aref)
                else:
                    print("1448 fell through if num")
        if row == 11:
            r11['nums'] = row_11_nums
            for num in nums:
                if num == '0':
                    r11['n0'] = '0'
                    ct = r11['ct_0'] + 1
                    r11['ct_0'] = ct
                    r11['ct_0__col_refs'].append(aref)
                elif num == '1':
                    r11['n1'] = '1'
                    ct = r11['ct_1'] + 1
                    r11['ct_1'] = ct
                    r11['ct_1__col_refs'].append(aref)
                elif num == '2':
                    r11['n2'] = '2'
                    ct = r11['ct_2'] + 1
                    r11['ct_2'] = ct
                    r11['ct_2__col_refs'].append(aref)
                elif num == '3':
                    r11['n3'] = '3'
                    ct = r11['ct_3'] + 1
                    r11['ct_3'] = ct
                    r11['ct_3__col_refs'].append(aref)
                elif num == '4':
                    r11['n4'] = '4'
                    ct = r11['ct_4'] + 1
                    r11['ct_4'] = ct
                    r11['ct_4__col_refs'].append(aref)
                elif num == '5':
                    r11['n5'] = '5'
                    ct = r11['ct_5'] + 1
                    r11['ct_5'] = ct
                    r11['ct_5__col_refs'].append(aref)
                elif num == '6':
                    r11['n6'] = '6'
                    ct = r11['ct_6'] + 1
                    r11['ct_6'] = ct
                    r11['ct_6__col_refs'].append(aref)
                elif num == '7':
                    r11['n7'] = '7'
                    ct = r11['ct_7'] + 1
                    r11['ct_7'] = ct
                    r11['ct_7__col_refs'].append(aref)
                elif num == '8':
                    r11['n8'] = '8'
                    ct = r11['ct_8'] + 1
                    r11['ct_8'] = ct
                    r11['ct_8__col_refs'].append(aref)
                elif num == '9':
                    r11['n9'] = '9'
                    ct = r11['ct_9'] + 1
                    r11['ct_9'] = ct
                    r11['ct_9__col_refs'].append(aref)
                elif num == 'A':
                    r11['nA'] = 'A'
                    ct = r11['ct_A'] + 1
                    r11['ct_A'] = ct
                    r11['ct_A__col_refs'].append(aref)
                elif num == 'B':
                    r11['nB'] = 'B'
                    ct = r11['ct_B'] + 1
                    r11['ct_B'] = ct
                    r11['ct_B__col_refs'].append(aref)
                elif num == 'C':
                    r11['nC'] = 'C'
                    ct = r11['ct_C'] + 1
                    r11['ct_C'] = ct
                    r11['ct_C__col_refs'].append(aref)
                elif num == 'D':
                    r11['nD'] = 'D'
                    ct = r11['ct_D'] + 1
                    r11['ct_D'] = ct
                    r11['ct_D__col_refs'].append(aref)
                elif num == 'E':
                    r11['nE'] = 'E'
                    ct = r11['ct_E'] + 1
                    r11['ct_E'] = ct
                    r11['ct_E__col_refs'].append(aref)
                elif num == 'F':
                    r11['nF'] = 'F'
                    ct = r11['ct_F'] + 1
                    r11['ct_F'] = ct
                    r11['ct_F__col_refs'].append(aref)
                else:
                    print("1448 fell through if num")
        if row == 12:
            r12['nums'] = row_12_nums
            for num in nums:
                if num == '0':
                    r12['n0'] = '0'
                    ct = r12['ct_0'] + 1
                    r12['ct_0'] = ct
                    r12['ct_0__col_refs'].append(aref)
                elif num == '1':
                    r12['n1'] = '1'
                    ct = r12['ct_1'] + 1
                    r12['ct_1'] = ct
                    r12['ct_1__col_refs'].append(aref)
                elif num == '2':
                    r12['n2'] = '2'
                    ct = r12['ct_2'] + 1
                    r12['ct_2'] = ct
                    r12['ct_2__col_refs'].append(aref)
                elif num == '3':
                    r12['n3'] = '3'
                    ct = r12['ct_3'] + 1
                    r12['ct_3'] = ct
                    r12['ct_3__col_refs'].append(aref)
                elif num == '4':
                    r12['n4'] = '4'
                    ct = r12['ct_4'] + 1
                    r12['ct_4'] = ct
                    r12['ct_4__col_refs'].append(aref)
                elif num == '5':
                    r12['n5'] = '5'
                    ct = r12['ct_5'] + 1
                    r12['ct_5'] = ct
                    r12['ct_5__col_refs'].append(aref)
                elif num == '6':
                    r12['n6'] = '6'
                    ct = r12['ct_6'] + 1
                    r12['ct_6'] = ct
                    r12['ct_6__col_refs'].append(aref)
                elif num == '7':
                    r12['n7'] = '7'
                    ct = r12['ct_7'] + 1
                    r12['ct_7'] = ct
                    r12['ct_7__col_refs'].append(aref)
                elif num == '8':
                    r12['n8'] = '8'
                    ct = r12['ct_8'] + 1
                    r12['ct_8'] = ct
                    r12['ct_8__col_refs'].append(aref)
                elif num == '9':
                    r12['n9'] = '9'
                    ct = r12['ct_9'] + 1
                    r12['ct_9'] = ct
                    r12['ct_9__col_refs'].append(aref)
                elif num == 'A':
                    r12['nA'] = 'A'
                    ct = r12['ct_A'] + 1
                    r12['ct_A'] = ct
                    r12['ct_A__col_refs'].append(aref)
                elif num == 'B':
                    r12['nB'] = 'B'
                    ct = r12['ct_B'] + 1
                    r12['ct_B'] = ct
                    r12['ct_B__col_refs'].append(aref)
                elif num == 'C':
                    r12['nC'] = 'C'
                    ct = r12['ct_C'] + 1
                    r12['ct_C'] = ct
                    r12['ct_C__col_refs'].append(aref)
                elif num == 'D':
                    r12['nD'] = 'D'
                    ct = r12['ct_D'] + 1
                    r12['ct_D'] = ct
                    r12['ct_D__col_refs'].append(aref)
                elif num == 'E':
                    r12['nE'] = 'E'
                    ct = r12['ct_E'] + 1
                    r12['ct_E'] = ct
                    r12['ct_E__col_refs'].append(aref)
                elif num == 'F':
                    r12['nF'] = 'F'
                    ct = r12['ct_F'] + 1
                    r12['ct_F'] = ct
                    r12['ct_F__col_refs'].append(aref)
                else:
                    print("1448 fell through if num")
        if row == 13:
            r13['nums'] = row_13_nums
            for num in nums:
                if num == '0':
                    r13['n0'] = '0'
                    ct = r13['ct_0'] + 1
                    r13['ct_0'] = ct
                    r13['ct_0__col_refs'].append(aref)
                elif num == '1':
                    r13['n1'] = '1'
                    ct = r13['ct_1'] + 1
                    r13['ct_1'] = ct
                    r13['ct_1__col_refs'].append(aref)
                elif num == '2':
                    r13['n2'] = '2'
                    ct = r13['ct_2'] + 1
                    r13['ct_2'] = ct
                    r13['ct_2__col_refs'].append(aref)
                elif num == '3':
                    r13['n3'] = '3'
                    ct = r13['ct_3'] + 1
                    r13['ct_3'] = ct
                    r13['ct_3__col_refs'].append(aref)
                elif num == '4':
                    r13['n4'] = '4'
                    ct = r13['ct_4'] + 1
                    r13['ct_4'] = ct
                    r13['ct_4__col_refs'].append(aref)
                elif num == '5':
                    r13['n5'] = '5'
                    ct = r13['ct_5'] + 1
                    r13['ct_5'] = ct
                    r13['ct_5__col_refs'].append(aref)
                elif num == '6':
                    r13['n6'] = '6'
                    ct = r13['ct_6'] + 1
                    r13['ct_6'] = ct
                    r13['ct_6__col_refs'].append(aref)
                elif num == '7':
                    r13['n7'] = '7'
                    ct = r13['ct_7'] + 1
                    r13['ct_7'] = ct
                    r13['ct_7__col_refs'].append(aref)
                elif num == '8':
                    r13['n8'] = '8'
                    ct = r13['ct_8'] + 1
                    r13['ct_8'] = ct
                    r13['ct_8__col_refs'].append(aref)
                elif num == '9':
                    r13['n9'] = '9'
                    ct = r13['ct_9'] + 1
                    r13['ct_9'] = ct
                    r13['ct_9__col_refs'].append(aref)
                elif num == 'A':
                    r13['nA'] = 'A'
                    ct = r13['ct_A'] + 1
                    r13['ct_A'] = ct
                    r13['ct_A__col_refs'].append(aref)
                elif num == 'B':
                    r13['nB'] = 'B'
                    ct = r13['ct_B'] + 1
                    r13['ct_B'] = ct
                    r13['ct_B__col_refs'].append(aref)
                elif num == 'C':
                    r13['nC'] = 'C'
                    ct = r13['ct_C'] + 1
                    r13['ct_C'] = ct
                    r13['ct_C__col_refs'].append(aref)
                elif num == 'D':
                    r13['nD'] = 'D'
                    ct = r13['ct_D'] + 1
                    r13['ct_D'] = ct
                    r13['ct_D__col_refs'].append(aref)
                elif num == 'E':
                    r13['nE'] = 'E'
                    ct = r13['ct_E'] + 1
                    r13['ct_E'] = ct
                    r13['ct_E__col_refs'].append(aref)
                elif num == 'F':
                    r13['nF'] = 'F'
                    ct = r13['ct_F'] + 1
                    r13['ct_F'] = ct
                    r13['ct_F__col_refs'].append(aref)
                else:
                    print("1448 fell through if num")
        if row == 14:
            r14['nums'] = row_14_nums
            for num in nums:
                if num == '0':
                    r14['n0'] = '0'
                    ct = r14['ct_0'] + 1
                    r14['ct_0'] = ct
                    r14['ct_0__col_refs'].append(aref)
                elif num == '1':
                    r14['n1'] = '1'
                    ct = r14['ct_1'] + 1
                    r14['ct_1'] = ct
                    r14['ct_1__col_refs'].append(aref)
                elif num == '2':
                    r14['n2'] = '2'
                    ct = r14['ct_2'] + 1
                    r14['ct_2'] = ct
                    r14['ct_2__col_refs'].append(aref)
                elif num == '3':
                    r14['n3'] = '3'
                    ct = r14['ct_3'] + 1
                    r14['ct_3'] = ct
                    r14['ct_3__col_refs'].append(aref)
                elif num == '4':
                    r14['n4'] = '4'
                    ct = r14['ct_4'] + 1
                    r14['ct_4'] = ct
                    r14['ct_4__col_refs'].append(aref)
                elif num == '5':
                    r14['n5'] = '5'
                    ct = r14['ct_5'] + 1
                    r14['ct_5'] = ct
                    r14['ct_5__col_refs'].append(aref)
                elif num == '6':
                    r14['n6'] = '6'
                    ct = r14['ct_6'] + 1
                    r14['ct_6'] = ct
                    r14['ct_6__col_refs'].append(aref)
                elif num == '7':
                    r14['n7'] = '7'
                    ct = r14['ct_7'] + 1
                    r14['ct_7'] = ct
                    r14['ct_7__col_refs'].append(aref)
                elif num == '8':
                    r14['n8'] = '8'
                    ct = r14['ct_8'] + 1
                    r14['ct_8'] = ct
                    r14['ct_8__col_refs'].append(aref)
                elif num == '9':
                    r14['n9'] = '9'
                    ct = r14['ct_9'] + 1
                    r14['ct_9'] = ct
                    r14['ct_9__col_refs'].append(aref)
                elif num == 'A':
                    r14['nA'] = 'A'
                    ct = r14['ct_A'] + 1
                    r14['ct_A'] = ct
                    r14['ct_A__col_refs'].append(aref)
                elif num == 'B':
                    r14['nB'] = 'B'
                    ct = r14['ct_B'] + 1
                    r14['ct_B'] = ct
                    r14['ct_B__col_refs'].append(aref)
                elif num == 'C':
                    r14['nC'] = 'C'
                    ct = r14['ct_C'] + 1
                    r14['ct_C'] = ct
                    r14['ct_C__col_refs'].append(aref)
                elif num == 'D':
                    r14['nD'] = 'D'
                    ct = r14['ct_D'] + 1
                    r14['ct_D'] = ct
                    r14['ct_D__col_refs'].append(aref)
                elif num == 'E':
                    r14['nE'] = 'E'
                    ct = r14['ct_E'] + 1
                    r14['ct_E'] = ct
                    r14['ct_E__col_refs'].append(aref)
                elif num == 'F':
                    r14['nF'] = 'F'
                    ct = r14['ct_F'] + 1
                    r14['ct_F'] = ct
                    r14['ct_F__col_refs'].append(aref)
                else:
                    print("1448 fell through if num")
        if row == 15:
            r15['nums'] = row_15_nums
            for num in nums:
                if num == '0':
                    r15['n0'] = '0'
                    ct = r15['ct_0'] + 1
                    r15['ct_0'] = ct
                    r15['ct_0__col_refs'].append(aref)
                elif num == '1':
                    r15['n1'] = '1'
                    ct = r15['ct_1'] + 1
                    r15['ct_1'] = ct
                    r15['ct_1__col_refs'].append(aref)
                elif num == '2':
                    r15['n2'] = '2'
                    ct = r15['ct_2'] + 1
                    r15['ct_2'] = ct
                    r15['ct_2__col_refs'].append(aref)
                elif num == '3':
                    r15['n3'] = '3'
                    ct = r15['ct_3'] + 1
                    r15['ct_3'] = ct
                    r15['ct_3__col_refs'].append(aref)
                elif num == '4':
                    r15['n4'] = '4'
                    ct = r15['ct_4'] + 1
                    r15['ct_4'] = ct
                    r15['ct_4__col_refs'].append(aref)
                elif num == '5':
                    r15['n5'] = '5'
                    ct = r15['ct_5'] + 1
                    r15['ct_5'] = ct
                    r15['ct_5__col_refs'].append(aref)
                elif num == '6':
                    r15['n6'] = '6'
                    ct = r15['ct_6'] + 1
                    r15['ct_6'] = ct
                    r15['ct_6__col_refs'].append(aref)
                elif num == '7':
                    r15['n7'] = '7'
                    ct = r15['ct_7'] + 1
                    r15['ct_7'] = ct
                    r15['ct_7__col_refs'].append(aref)
                elif num == '8':
                    r15['n8'] = '8'
                    ct = r15['ct_8'] + 1
                    r15['ct_8'] = ct
                    r15['ct_8__col_refs'].append(aref)
                elif num == '9':
                    r15['n9'] = '9'
                    ct = r15['ct_9'] + 1
                    r15['ct_9'] = ct
                    r15['ct_9__col_refs'].append(aref)
                elif num == 'A':
                    r15['nA'] = 'A'
                    ct = r15['ct_A'] + 1
                    r15['ct_A'] = ct
                    r15['ct_A__col_refs'].append(aref)
                elif num == 'B':
                    r15['nB'] = 'B'
                    ct = r15['ct_B'] + 1
                    r15['ct_B'] = ct
                    r15['ct_B__col_refs'].append(aref)
                elif num == 'C':
                    r15['nC'] = 'C'
                    ct = r15['ct_C'] + 1
                    r15['ct_C'] = ct
                    r15['ct_C__col_refs'].append(aref)
                elif num == 'D':
                    r15['nD'] = 'D'
                    ct = r15['ct_D'] + 1
                    r15['ct_D'] = ct
                    r15['ct_D__col_refs'].append(aref)
                elif num == 'E':
                    r15['nE'] = 'E'
                    ct = r15['ct_E'] + 1
                    r15['ct_E'] = ct
                    r15['ct_E__col_refs'].append(aref)
                elif num == 'F':
                    r15['nF'] = 'F'
                    ct = r15['ct_F'] + 1
                    r15['ct_F'] = ct
                    r15['ct_F__col_refs'].append(aref)
                else:
                    print("1448 fell through if num")
        if row == 16:
            r16['nums'] = row_16_nums
            for num in nums:
                if num == '0':
                    r16['n0'] = '0'
                    ct = r16['ct_0'] + 1
                    r16['ct_0'] = ct
                    r16['ct_0__col_refs'].append(aref)
                elif num == '1':
                    r16['n1'] = '1'
                    ct = r16['ct_1'] + 1
                    r16['ct_1'] = ct
                    r16['ct_1__col_refs'].append(aref)
                elif num == '2':
                    r16['n2'] = '2'
                    ct = r16['ct_2'] + 1
                    r16['ct_2'] = ct
                    r16['ct_2__col_refs'].append(aref)
                elif num == '3':
                    r16['n3'] = '3'
                    ct = r16['ct_3'] + 1
                    r16['ct_3'] = ct
                    r16['ct_3__col_refs'].append(aref)
                elif num == '4':
                    r16['n4'] = '4'
                    ct = r16['ct_4'] + 1
                    r16['ct_4'] = ct
                    r16['ct_4__col_refs'].append(aref)
                elif num == '5':
                    r16['n5'] = '5'
                    ct = r16['ct_5'] + 1
                    r16['ct_5'] = ct
                    r16['ct_5__col_refs'].append(aref)
                elif num == '6':
                    r16['n6'] = '6'
                    ct = r16['ct_6'] + 1
                    r16['ct_6'] = ct
                    r16['ct_6__col_refs'].append(aref)
                elif num == '7':
                    r16['n7'] = '7'
                    ct = r16['ct_7'] + 1
                    r16['ct_7'] = ct
                    r16['ct_7__col_refs'].append(aref)
                elif num == '8':
                    r16['n8'] = '8'
                    ct = r16['ct_8'] + 1
                    r16['ct_8'] = ct
                    r16['ct_8__col_refs'].append(aref)
                elif num == '9':
                    r16['n9'] = '9'
                    ct = r16['ct_9'] + 1
                    r16['ct_9'] = ct
                    r16['ct_9__col_refs'].append(aref)
                elif num == 'A':
                    r16['nA'] = 'A'
                    ct = r16['ct_A'] + 1
                    r16['ct_A'] = ct
                    r16['ct_A__col_refs'].append(aref)
                elif num == 'B':
                    r16['nB'] = 'B'
                    ct = r16['ct_B'] + 1
                    r16['ct_B'] = ct
                    r16['ct_B__col_refs'].append(aref)
                elif num == 'C':
                    r16['nC'] = 'C'
                    ct = r16['ct_C'] + 1
                    r16['ct_C'] = ct
                    r16['ct_C__col_refs'].append(aref)
                elif num == 'D':
                    r16['nD'] = 'D'
                    ct = r16['ct_D'] + 1
                    r16['ct_D'] = ct
                    r16['ct_D__col_refs'].append(aref)
                elif num == 'E':
                    r16['nE'] = 'E'
                    ct = r16['ct_E'] + 1
                    r16['ct_E'] = ct
                    r16['ct_E__col_refs'].append(aref)
                elif num == 'F':
                    r16['nF'] = 'F'
                    ct = r16['ct_F'] + 1
                    r16['ct_F'] = ct
                    r16['ct_F__col_refs'].append(aref)
                else:
                    print("1448 fell through if num")

    # print("17xx r1 is ", r1)
    # print("17xx r2 is ", r2)
    # print("17xx r3 is ", r3)
    # print("17xx r4 is ", r4)
    # print("17xx r5 is ", r5)
    # print("17xx r6 is ", r6)
    # print("17xx r7 is ", r7)
    # print("17xx r8 is ", r8)
    # print("17xx r9 is ", r9)
    # print("17xx r10 is ", r10)
    # print("17xx r11 is ", r11)
    # print("17xx r12 is ", r12)
    # print("17xx r13 is ", r13)
    # print("17xx r14 is ", r14)
    # print("17xx r15 is ", r15)
    # print("17xx r16 is ", r16)


def make_col_dicts():
    row_arefs = []
    nums = []
    ct = 0
    col_arefs = []

    global c1
    global c2
    global c3
    global c4
    global c5
    global c7
    global c8
    global c9
    global c10
    global c11
    global c12
    global c13
    global c14
    global c15
    global c16

    for cell in not_done_arefs:
        aref = cell['aref']
        row = cell['row']
        col = cell['col']
        sq = cell['sq']
        nums = cell['nums']
        ct = 0
        rows = []
        row_ct = 0
        if col == 1:
            c1['nums'] = col_1_nums
            for num in nums:
                if num == '0':
                    c1['n0'] = '0'
                    ct = c1['ct_0'] + 1
                    c1['ct_0'] = ct
                    c1['ct_0__row_refs'].append(aref)
                elif num == '1':
                    c1['n1'] = '1'
                    ct = c1['ct_1'] + 1
                    c1['ct_1'] = ct
                    c1['ct_1__row_refs'].append(aref)
                elif num == '2':
                    c1['n2'] = '2'
                    ct = c1['ct_2'] + 1
                    c1['ct_2'] = ct
                    c1['ct_2__row_refs'].append(aref)
                elif num == '3':
                    c1['n3'] = '3'
                    ct = c1['ct_3'] + 1
                    c1['ct_3'] = ct
                    c1['ct_3__row_refs'].append(aref)
                elif num == '4':
                    c1['n4'] = '4'
                    ct = c1['ct_4'] + 1
                    c1['ct_4'] = ct
                    c1['ct_4__row_refs'].append(aref)
                elif num == '5':
                    c1['n5'] = '5'
                    ct = c1['ct_5'] + 1
                    c1['ct_5'] = ct
                    c1['ct_5__row_refs'].append(aref)
                elif num == '6':
                    c1['n6'] = '6'
                    ct = c1['ct_6'] + 1
                    c1['ct_6'] = ct
                    c1['ct_6__row_refs'].append(aref)
                elif num == '7':
                    c1['n7'] = '7'
                    ct = c1['ct_7'] + 1
                    c1['ct_7'] = ct
                    c1['ct_7__row_refs'].append(aref)
                elif num == '8':
                    c1['n8'] = '8'
                    ct = c1['ct_8'] + 1
                    c1['ct_8'] = ct
                    c1['ct_8__row_refs'].append(aref)
                elif num == '9':
                    c1['n9'] = '9'
                    ct = c1['ct_9'] + 1
                    c1['ct_9'] = ct
                    c1['ct_9__row_refs'].append(aref)
                elif num == 'A':
                    c1['nA'] = 'A'
                    ct = c1['ct_A'] + 1
                    c1['ct_A'] = ct
                    c1['ct_A__row_refs'].append(aref)
                elif num == 'B':
                    c1['nB'] = 'B'
                    ct = c1['ct_B'] + 1
                    c1['ct_B'] = ct
                    c1['ct_B__row_refs'].append(aref)
                elif num == 'C':
                    c1['nC'] = 'C'
                    ct = c1['ct_C'] + 1
                    c1['ct_C'] = ct
                    c1['ct_C__row_refs'].append(aref)
                elif num == 'D':
                    c1['nD'] = 'D'
                    ct = c1['ct_D'] + 1
                    c1['ct_D'] = ct
                    c1['ct_D__row_refs'].append(aref)
                elif num == 'E':
                    c1['nE'] = 'E'
                    ct = c1['ct_E'] + 1
                    c1['ct_E'] = ct
                    c1['ct_E__row_refs'].append(aref)
                elif num == 'F':
                    c1['nF'] = 'F'
                    ct = c1['ct_F'] + 1
                    c1['ct_F'] = ct
                    c1['ct_F__row_refs'].append(aref)
                else:
                    print("1448 fell through if num")
    # print("2919 col c1 is ", c1)
    # print("17xx r1 is ", r1)


def find_Duples():
    ''' Find duples and display list in text box.'''
    duples_list = []
    print("1132 Entering find_Duples")
    # develop the duple candidate list, e.g, all cells with len numbers == 2
    duple_candidate_list = []
    duple_candidate_list = make_Duple_Candidate_list()
    print("1136 duple_candidate_list is ", duple_candidate_list)
    # sort the list to identify duples that haven't yet been processed
    id_duples(duple_candidate_list)


def id_duples(duple_candidate_list):
    ''' sort the list to identify duples that haven't yet been processed '''
    global duples_list
    print("878 Entering id_duples")
    # print("879 duple_candidate_list is ", duple_candidate_list)
    for item in duple_candidate_list:
        if item:
            # print("716 item nums are ", item[0], item[1], item[2], item[3])
            i_row = int(item[0])
            i_col = int(item[1])
            i_sq = int(item[2])
            i_pair = item[3]
            i_aref = item[4]
            i_btn = item[5]
            # i_pair is the duple (the two numbers) being considered as an initial potential duple

        try:
            for item1 in duple_candidate_list:
                # if item[0] and item[1] and item[2] and item[3]:
                c_row = int(item1[0])
                c_col = int(item1[1])
                c_sq = int(item1[2])
                c_pair = item1[3]
                c_aref = item1[4]
                c_btn = item[5]

                ''' This section gets the data for the current cell
                    so it can be compared with the initial cell.'''
                # If the cell to compare is the original cell, pass
                if item1 == item:
                    pass
                if i_pair == c_pair and i_row == c_row and i_col == c_col and i_sq == c_sq:
                    pass
                # If the current cell is not the same as the original cell, process it
                elif i_pair == c_pair and (i_row == c_row or i_col == c_col or i_sq == c_sq):
                    ex_text = f"{i_row}, {i_col}, {i_sq},{i_pair} "
                    ex_text = ex_text + \
                        f"{c_row}, {c_col}, {c_sq}, {c_pair}"
                    print("913 pairs are ", i_row, i_col, i_sq, i_pair, i_aref, i_btn,
                          c_row, c_col, c_sq, c_pair, c_pair[0], c_pair[1], c_aref, c_btn)
                    # duple_first = {i_row}, {i_col}, {i_sq}, {i_pair}
                    duple_first = f"{i_row}, {i_col}, \
                        {i_sq}, {i_pair}, {i_aref}"
                    duple_first = duple_first.split(',')
                    duple_second = f"{c_row}, {c_col}, \
                        {c_sq}, {c_pair}, {c_aref}, {c_btn}"
                    duple_second = duple_second.split(',')
                    current_duple = [duple_first, duple_second]
                    print("912 duple_first is ", duple_first)
                    print("913 duple_second is ", duple_second)
                    print("914 current_duple is ", current_duple)
                    print("915 duples_list is ", duples_list)
                    if duples_list == []:
                        print("917 duples_list is ", duples_list)
                    if current_duple in completed_duples_list:
                        pass
                    elif not current_duple in duples_list:
                        duples_list.append(current_duple)
                        print("921 duples_list is ",
                              duples_list)
                    txt_Explain.insert(END, ex_text)
                    txt_Explain.insert(END, "\n")
                    # print("940 duples_list is ", duples_list)
            process_duple_list(duples_list)

        except Exception as e:
            pass


def make_Duple_Candidate_list():
    print("955 Entering make_Duple_Candidate_list")
    ex_text = ""
    temp_list = []
    temp_list_1 = []
    duple_candidate_list = []
    dup_list = []
    for cell in not_done_arefs:
        if len(cell['nums']) == 2:
            ex_text = str(cell['row']) + ", " + str(cell['col']) + \
                ", " + str(cell['sq']) + ", " + str(cell['nums']) + "\n "
            list_text = str(cell['row']) + ", " + str(cell['col']) + \
                ", " + str(cell['sq']) + ", " + str(cell['nums'])
            row = cell['row']
            col = cell['col']
            sq = cell['sq']
            nums = cell['nums']
            aref = cell['aref']
            btn = cell['btn']
            dup_list = [row, col, sq, nums, aref, btn]
            duple_candidate_list.append(dup_list)
    return duple_candidate_list


def fix_duples():
    global duples_list
    print("1280 in fix_duples.", duples_list)
    # for duple in duples_list:
    #     print("1283 duple is ", duple)
    process_duple_list()


def fix_triples():
    ''' The fix function compares the first two items in the rcs
        resources list to determine whether the row, columns or squares
        are the common feature and calls the approriate function.
    '''
    print("4153 entered fix_triples.")
    print("4154 triples_list is ", triples_list)
    for triple in triples_list:
        tuple_found = False
        print("4157 triple is ", triple, type(triple))
        if type(triple) == set:
            triple_set = triple
            print("4160 triple set is ", triple_set)
            tuple_found = True
            nums = str(" ".join(map(str, triple_set)))
            n0 = nums[0]
            n1 = nums[2]
            n2 = nums[4]
            print("4166 nums ", nums, n0, n1, n2)
        elif type(triple) == list:
            triple_list = triple
            print("4169 triple as list ", triple_list)
            l0 = triple[0]
            l1 = triple[1]
            l2 = triple[2]
            print("4173 lists are ", l0, l1, l2)
            if not tuple_found == True:
                pass
            row0 = l0[0]
            col0 = l0[1]
            sq0 = l0[2]
            nums0 = l0[3]
            row1 = l1[0]
            col1 = l1[1]
            sq1 = l1[2]
            nums1 = l2[3]
            row2 = l2[0]
            col2 = l2[1]
            sq2 = l2[2]
            nums2 = l2[3]
            print("4188 triple list is ", row0, row1, row2,
                  col0, col1, col2, sq0, sq1, sq2, nums0, nums1, nums2)
            if row0 == row1 == row2:
                print("4191 rows are common")
                print(row0, row1, col0, col1, sq0, sq1)
                process_row_triple(row0, triple_set, triple_list)
            if col0 == col1 == col2:
                print("4195 cols are common")
                print(row0, row1, col0, col1, sq0, sq1)
                process_column_triple(col0, triple_set, triple_list)
            if sq0 == sq1 == sq2:
                print("4199 sqs are common")
                print(row0, row1, col0, col1, sq0, sq1)
                process_sq_triple(sq0, triple_set, triple_list)
        else:
            print("4203 no match for object type.")

    print("4205 triples_list ", triples_list)
    for item in triples_list:
        triples_list.remove(item)
    print("4208 triples_list ", triples_list)


def fix_quads():
    ''' The fix function compares the first two items in the rcs
        resources list to determine whether the row, columns or squares
        are the common feature and calls the approriate function.
    '''
    global quads_list
    print("4121 entered fix_quads.")
    print("4122 quads_list is ", quads_list)
    for quad in quads_list:
        tuple_found = False
        print("1310 triple is ", quad, type(quad))
        if type(quad) == set:
            quads_set = quad
            print("1312 triple set is ", quads_set)
            tuple_found = True
            nums = str(" ".join(map(str, quads_set)))
            n0 = nums[0]
            n1 = nums[2]
            n2 = nums[4]
            print("4134 nums ", nums, n0, n1, n2)
        elif type(quad) == list:
            quads_list = quad
            print("1398 triple as list ", quads_list)
            l0 = quad[0]
            l1 = quad[1]
            l2 = quad[2]
            l3 = quad[3]
            print("1403 lists are ", l0, l1, l2, l3)
            if not tuple_found == True:
                pass
            row0 = l0[0]
            col0 = l0[1]
            sq0 = l0[2]
            nums0 = l0[3]
            row1 = l1[0]
            col1 = l1[1]
            sq1 = l1[2]
            nums1 = l2[3]
            row2 = l2[0]
            col2 = l2[1]
            sq2 = l2[2]
            nums2 = l2[3]
            print("1418 triple list is ", row0, row1, row2,
                  col0, col1, col2, sq0, sq1, sq2, nums0, nums1, nums2)
            if row0 == row1 == row2:
                print("4256 rows are common")
                print(row0, row1, col0, col1, sq0, sq1)
                process_row_triple(row0, quads_set, quads_list)
            if col0 == col1 == col2:
                print("4260 cols are common")
                print(row0, row1, col0, col1, sq0, sq1)
                process_column_triple(col0, quads_set, quads_list)
            if sq0 == sq1 == sq2:
                print("4264 sqs are common")
                print(row0, row1, col0, col1, sq0, sq1)
                process_sq_quad(sq0, quads_set, quads_list)
        else:
            print("4268 no match for object type.")

    print("4270 quads_list ", quads_list)
    for item in quads_list:
        quads_list.remove(item)
    print("4273 quads_list ", quads_list)


def process_duple_list():
    print("1116 duples_list is ", duples_list)
    for duple in duples_list:
        print("1122 duple is ", duple)
        duple_first = duple[0]
        duple_second = duple[1]
        print("1124  parts are ", duple_first)
        print("1125  parts are ", duple_second)
        first_row = int(duple_first[0])
        print("1127 first_row is ", first_row)
        first_col = int(duple_first[1])
        print("1129 first_col is ", first_col)
        first_sq = int(duple_first[2])
        print("1131 first_sq is ", first_sq)
        first_nums = str(duple_first[3])
        print("1133 first_nums are ", first_nums)
        first_aref = duple_first[4]
        print("1133 first_nums are ", first_nums)
        first_chr_1 = first_nums[-2]
        second_chr_1 = first_nums[-1]
        # print("1136 duple parts, first_row, etc, are ", first_row,
        #       first_col, first_sq, first_nums, first_chr_1, second_chr_1)
        second_row = int(duple_second[0])
        second_col = int(duple_second[1])
        second_sq = int(duple_second[2])
        second_nums = str(duple_second[3])
        second_aref = duple_second[3]
        duple_row = 0
        duple_col = 0
        duple_sq = 0
        print("1145 duple_first  ", duple_first)
        print("1146 duple_second  ", duple_second)
        print("1147 duples_list  ", duples_list)
        print("1148 completed_duples_list ", completed_duples_list)

        if first_row == second_row:
            duple_row = first_row
            # print("791 duple row is ", first_row, second_row, duple_row)
        if first_col == second_col:
            duple_col = first_col
            # print("794 duple col is ", first_col, second_col, duple_col)
        if first_sq == second_sq:
            duple_sq = first_sq

        for aref in not_done_arefs:
            current_btn = aref['btn']
            a_row = aref['row']
            a_col = aref['col']
            a_sq = aref['sq']
            a_nums = aref['nums']
            if (a_row == duple_row and a_col == duple_col and a_sq == duple_sq) or (a_row == second_row and a_col == second_col and a_sq == second_sq) or (a_nums == first_nums):
                ''' The cell is being compared with itself.'''
                print("1162 cells are the same ", a_row, first_row,
                      second_row, a_col, first_col, second_col, a_sq, first_sq, second_sq, first_nums)
            elif duple_row == a_row:
                print("1165 partial match in aref", duple_row, duple_col,
                      duple_sq, first_row, a_row, first_chr_1, a_nums)
                if a_nums in first_nums or first_nums in a_nums:
                    print("1170 a_nums ~= first_nums ", a_nums, first_nums)
                    pass
                elif first_chr_1 in a_nums:
                    new_nums = aref['nums'].replace(first_chr_1, "")
                    # print("723 new_nums ", new_nums)
                    aref['nums'] = new_nums
                    current_btn['text'] = aref['nums']
                elif second_chr_1 in a_nums:
                    new_nums = aref['nums'].replace(second_chr_1, "")
                    print("1170 new_nums ", new_nums)
                    aref['nums'] = new_nums
                    current_btn['text'] = aref['nums']
            elif duple_col == a_col:
                if a_nums in first_nums or first_nums in a_nums:
                    print("1184 a_nums ~= first_nums ", a_nums, first_nums)
                    pass
                elif first_chr_1 in a_nums:
                    new_nums = aref['nums'].replace(first_chr_1, "")
                    print("1178 new_nums ", new_nums)
                    aref['nums'] = new_nums
                    current_btn['text'] = aref['nums']
                elif second_chr_1 in a_nums:
                    new_nums = aref['nums'].replace(second_chr_1, "")
                    print("1183 new_nums ", new_nums)
                    aref['nums'] = new_nums
                    current_btn['text'] = aref['nums']
            elif duple_sq == a_sq:
                if a_nums in first_nums or first_nums in a_nums:
                    print("1198 a_nums ~= first_nums ", a_nums, first_nums)
                    pass
                elif first_chr_1 in a_nums:
                    new_nums = aref['nums'].replace(first_chr_1, "")
                    print("1191 new_nums ", new_nums)
                    aref['nums'] = new_nums
                    current_btn['text'] = aref['nums']
                elif second_chr_1 in a_nums:
                    new_nums = aref['nums'].replace(second_chr_1, "")
                    print("1196 new_nums ", new_nums)
                    aref['nums'] = new_nums
                    current_btn['text'] = aref['nums']
            #     print("1150")
            # print("1151")
        for duple in duples_list:
            print("1495 duple is ", duple)

        # print("1237 duples_list is ",
        #       duples_list)  # , completed_duples_list and
        # add_duples_to_completed_duples_list()


def add_duples_to_completed_duples_list():
    print("1506 entered add_duples_to_completed_duples_list ")
    print("1507 ", duples_list)
    print("1508 ", completed_duples_list)
    # print("1244 duple_first, duple_second ", duple_first, duple_second)
    # print("1510 completed_duples_list ", completed_duples_list)
    if completed_duples_list == []:
        completed_duples_list.append(duples_list)
    for d_list in completed_duples_list:
        print("1514 duple_list is ", d_list)
        if not d_list in completed_duples_list:
            completed_duples_list.append(d_list)
    print("1517 ", completed_duples_list)


def make_aref_RCS_lists():
    row_2_arefs = []
    for aref in not_done_arefs:
        current_btn = aref['btn_str']
        a_row = int(aref['row'])
        a_col = aref['col']
        a_sq = aref['sq']
        a_nums = aref['nums']
        if a_row == 2:
            row_2_arefs.append(current_btn)
    print("1559 row_2_arefs lists ", row_2_arefs)


def process_duple_list1(duples_list):
    print("1216 old process_duple_list duples_list is ", duples_list)
    global not_done_arefs
    global currentNumber
    duple_first = duples_list[0][0]
    print("1223 duple_first is ", duple_first)
    duple_second = duples_list[0][1]
    print("1225 duple_second is ", duple_second)
    first_row = duple_first[0]
    print("1227 duple parts first_row, is ", first_row)
    first_col = int(duple_first[1])
    print("1231 duple parts first_col is ", first_col)
    first_sq = int(duple_first[2])
    print("1233 duple parts first_sq is ", first_sq)
    first_nums = str(duple_first[3])
    print("1235 duple parts, first_nums are ", first_nums)
    print("1234 duple parts, first_row, etc, are ",
          first_row, first_col, first_sq, first_nums)
    first_chr_1 = first_nums[-2]
    second_chr_1 = first_nums[-1]
    print("1238 duple parts, first_row, etc, are ",
          first_row, first_col, first_sq, first_nums, first_chr_1)  #
    second_row = int(duple_second[0])
    # print("1137 duple parts, first_row, etc, are ", second_row)
    second_col = int(duple_second[1])
    second_sq = int(duple_second[2])
    second_nums = str(duple_second[3])
    duple_row = 0
    duple_col = 0
    duple_sq = 0
    print("1250 duples_list and completed_duples_list ", duple_first,
          duple_second, duples_list, completed_duples_list)
    if duple_first in completed_duples_list:
        print("1252 in remove ", duple_first)
        print("1253 in remove ", duples_list)
        for sublist in completed_duples_list:
            if duple_first in sublist:
                sublist.remove(duple_first)
        # duples_list = duples_list.remove(list(duple_first))
        print("1255 completed_duples_list after remove ", completed_duples_list)
    if duple_second in completed_duples_list:
        duples_list = duples_list.remove(list(duple_second))
    print("1256 duples_list and completed_duples_list ", duple_first,
          duple_second, duples_list, completed_duples_list)
    # process_duple_list(duples_list)
    # , first_row, first_col) #,
    print("1249 duple parts, second_row, etc, are ",
          second_row, second_col, second_sq, second_nums, second_chr_1)
    # first_sq, first_nums, second_row, second_col, second_sq, second_nums)
    if first_row == second_row:
        duple_row = first_row
        # print("791 duple row is ", first_row, second_row, duple_row)
    if first_col == second_col:
        duple_col = first_col
        # print("794 duple col is ", first_col, second_col, duple_col)
    if first_sq == second_sq:
        duple_sq = first_sq
    for aref in not_done_arefs:
        current_btn = aref['btn']
        a_row = aref['row']
        a_col = aref['col']
        a_sq = aref['sq']
        a_nums = str(aref['nums'])
        # print("1266 aref parts are ", a_row, a_col, a_sq, a_nums)
        duple_sq = first_sq
        if (a_row == duple_row and a_col == duple_col and a_sq == duple_sq) or (a_row == second_row and a_col == second_col and a_sq == second_sq):
            ''' The cell is being compared with itself.'''
            pass
        elif duple_row == a_row:
            print("1272 partial match row", duple_row, duple_col,
                  duple_sq, first_row, a_row, first_chr_1, a_nums)
            if a_nums in first_nums or first_nums in a_nums:
                print("1290 a_nums ~= first_nums ", a_nums, first_nums)
                pass
            elif first_chr_1 in a_nums:
                new_nums = aref['nums'].replace(first_chr_1, "")
                # print("723 new_nums ", new_nums)
                aref['nums'] = new_nums
                current_btn['text'] = aref['nums']
            elif second_chr_1 in a_nums:
                new_nums = aref['nums'].replace(second_chr_1, "")
                print("1170 new_nums ", new_nums)
                aref['nums'] = new_nums
                current_btn['text'] = aref['nums']
        elif duple_col == a_col:  # duple_col != 0 and
            print("1285 partial match in col", duple_row, duple_col)
            #       duple_sq, first_row, a_row, first_chr_1, a_nums)
            print("1287 a_nums and first_nums ", a_nums, first_nums)
            print("1288 a_nums and first_nums types",
                  type(a_nums), type(first_nums))
            if a_nums in first_nums or first_nums in a_nums:
                print("1290 a_nums ~= first_nums ", a_nums, first_nums)
                pass
            elif first_chr_1 in a_nums:
                print("1292 a_nums are ", a_nums)
                new_nums = aref['nums'].replace(first_chr_1, "")
                print("1292 new_nums ", new_nums)
                aref['nums'] = new_nums
                current_btn['text'] = aref['nums']
            elif second_chr_1 in a_nums:
                new_nums = aref['nums'].replace(second_chr_1, "")
                print("1299 new_nums ", new_nums)
                aref['nums'] = new_nums
                current_btn['text'] = aref['nums']
        elif duple_sq == a_sq:
            if a_nums in first_nums or first_nums in a_nums:
                print("1309 a_nums ~= first_nums ", a_nums, first_nums)
                pass
            # print("1187 partial match in aref", duple_row, duple_col,
            #       duple_sq, first_row, a_row, first_chr_1, second_chr_1, a_nums)
            elif first_chr_1 in a_nums:
                new_nums = aref['nums'].replace(first_chr_1, "")
                print("1191 new_nums ", new_nums)
                aref['nums'] = new_nums
                current_btn['text'] = aref['nums']
            elif second_chr_1 in a_nums:
                new_nums = aref['nums'].replace(second_chr_1, "")
                print("1196 new_nums ", new_nums)
                aref['nums'] = new_nums
                current_btn['text'] = aref['nums']
        #     print("1150")
        # print("1151")
    print("1201 duples_list is ",
          duples_list)  # , completed_duples_list and completed_duples_list are
    if not duple_first in completed_duples_list:
        completed_duples_list.append(duple_first)
    if not duple_second in completed_duples_list:
        completed_duples_list.append(duple_second)
    # print("1205 duple_list is ", duples_list)
    # duples_list = []
    print("1332 completed_duples_list is ", completed_duples_list)


def find_Triples_1():
    print("4387 Entering find_Triple")
    # txt_Explain.insert(END, "potential triple cell and values  are \n")
    triple_candidate_list = make_triple_candidate_list()
    RCS_lists = make_RCS_lists_for_triples(triple_candidate_list)
    id_triples(RCS_lists[1])


def make_triple_candidate_list():
    print("1458 enter make_triple_candidate_list")
    ex_text = ""
    temp_list = []
    temp_list_1 = []
    triple_candidate_list = []
    triple_list = []
    for cell in not_done_arefs:
        if len(cell['nums']) <= 3:
            ex_text = str(cell['row']) + ", " + str(cell['col']) + \
                ", " + str(cell['sq']) + ", " + str(cell['nums']) + "\n "
            list_ex_text = list[str(cell['row']), str(
                cell['col']), str(cell['sq']), str(cell['nums'])]
            row = cell['row']
            col = cell['col']
            sq = cell['sq']
            nums = str(cell['nums'])
            temp_list = [row, col, sq, nums]
            txt_Explain.insert(END, ex_text)
            triple_candidate_list.append(temp_list)
            temp_list = []
            # r_1_nums.append(temp_list)
    print("1729 ", r_1_nums)
    return triple_candidate_list


def make_RCS_lists_for_triples(triple_candidate_list):
    print("1482 enter make_RCS_lists_for_tripless ", triple_candidate_list)
    row_list = [[1, ""], [2, ""], [3, ""], [4, ""], [5, ""], [6, ""], [7, ""], [
        8, ""], [9, ""], [10, ''], [11, ''], [12, ""], [13, ""], [14, ""], [15, ''], [16, '']]
    col_list = [[1, ""], [2, ""], [3, ""], [4, ""], [5, ""], [6, ""], [7, ""], [
        8, ""], [9, ""], [10, ''], [11, ''], [12, ""], [13, ""], [14, ""], [15, ''], [16, '']]
    sq_list = [[1, ""], [2, ""], [3, ""], [4, ""], [5, ""], [6, ""], [7, ""], [
        8, ""], [9, ""], [10, ''], [11, ''], [12, ""], [13, ""], [14, ""], [15, ''], [16, '']]
    for item in triple_candidate_list:
        row_num = item[0]
        col_num = item[1]
        sq_num = item[2]
        nums = item[3]
        row_lists = [row_num, col_num, sq_num, nums]
        col_lists = [row_num, col_num, sq_num, nums]
        sq_lists = [row_num, col_num, sq_num, nums]
        print("1917 row, col, and sq  _lists are ",
              row_lists, col_lists, sq_lists)
        row_list[row_num - 1][1] += str(row_lists)
        col_list[col_num - 1][1] += str(row_lists)
        sq_list[sq_num - 1][1] += str(row_lists)
    RCS_lists = [row_list, col_list, sq_list]
    return RCS_lists


def id_triples(candidate_list):
    print("4446 enter id_triples")
    print("1927 *** id_triples is still being used. ***")
    print("1528 candidate_list = ", candidate_list)
    for item in candidate_list:
        print("1504 triple item is ", item)
        num_cells = 1
        tcl_set0 = set()
        temp_set = set()
        row0 = item[0]
        list0 = item[1][1]
        row_0 = item[1][1:3]
        col0 = item[1][2:4]
        sq0 = item[1][7:9]
        num0 = item[1][10:13]
        print("1544 col extracted ", row0, row_0,
              col0, sq0, num0)
        col_0 = list0[0]
        sq0 = item[2]
        nums0 = item[3]
        l0 = len(nums0)
        n1 = nums0[0]
        tcl_set0.add(n1)
        n2 = nums0[1]
        tcl_set0.add(n2)
        if l0 == 3:
            n3 = nums0[2]
            tcl_set0.add(n3)
        print("1501 ", row0, col0, sq0, nums0, tcl_set0)
        for item1 in candidate_list:
            row1 = item1[0]
            col1 = item1[1]
            sq1 = item1[2]
            nums1 = item1[3]
            print("1507 triple item and item1 are ", item, item1)
            if item1 == item:
                pass
            elif item1 != item and ((row0 == row1) or (col0 == col1) or (sq0 == sq1)):
                num_cells = 2
                temp_set = tcl_set0.copy()
                print("4644 sets are ", tcl_set0, temp_set)
                ''' The correct cells are being checked!'''
                """ Now check for triples by checking for a 'set' of 3 nums"""
                """ Each set of numbers must have at least 2 and at most 3 numbers."""
                nums1 = item1[3]
                l1 = len(nums1)
                ns1 = nums1[0]
                temp_set.add(ns1)
                ns2 = nums1[1]
                temp_set.add(ns2)
                if l1 == 3:
                    ns3 = nums1[2]
                    temp_set.add(ns3)
                print("4657 sets are ", tcl_set0, temp_set)
                if len(temp_set) > 3:
                    num_cells = 1
                    temp_set = tcl_set0.copy()
                    continue
                elif len(temp_set) <= 3:

                    for item2 in candidate_list:
                        num_cells = 3
                        row2 = item2[0]
                        col2 = item2[1]
                        sq2 = item2[2]
                        nums2 = item2[3]
                        print("4670 triple item and item1 are ",
                              item, item1, item2)
                        if item2 == item or item2 == item1:
                            num_cells = 2
                            continue
                        elif item2 != item and ((row0 == row1 == row2) or (col0 == col1 == col2) or (sq0 == sq1 == sq2)):
                            print(
                                "4677 triple item not equal to item2 and RCS are the same", item, item2)
                            l2 = len(nums2)
                            nt1 = nums2[0]
                            temp_set.add(nt1)
                            nt2 = nums2[1]
                            temp_set.add(nt2)
                            if l2 == 3:
                                nt3 = nums2[2]
                                temp_set.add(nt3)
                            print("1560 sets are ", tcl_set0, temp_set)
                            if len(temp_set) > 3:
                                num_cells = 2
                                temp_set = tcl_set0.copy()
                                # continue
                                # print("1266 sets exceeds size. No triple. ",
                                #       tcl_set0, temp_set)
                            elif len(temp_set) == 3 and num_cells == 3:
                                print("1568 Triple found. ",
                                      tcl_set0, temp_set, item, item1, item2)
                                ex_text = f"{item}, {item1}, {item2}"
                                txt_Explain.insert(
                                    END, "A triple is \n")
                                txt_Explain.insert(
                                    END, ex_text)
                                # process_triple_list(
                                #     temp_set, item, item1, item2)
                                tcl_set0 = {}
                                temp_set = {}
                                num_cells = 1

            else:
                pass


def find_Quads():
    print("4712 find_Quads")
    global quads_list
    _find_Tuples(4)
    # show_Triple()


def find_Triples():
    print("4707 find_triples")
    global triples_list
    triples_list = []
    _find_Tuples(3)
    # show_Triple()


def _find_Tuples(num):
    r_1_tuples = []
    r_2_tuples = []
    r_3_tuples = []
    r_4_tuples = []
    r_5_tuples = []
    r_6_tuples = []
    r_7_tuples = []
    r_8_tuples = []
    r_9_tuples = []
    r_10_tuples = []
    r_11_tuples = []
    r_12_tuples = []
    r_13_tuples = []
    r_14_tuples = []
    r_15_tuples = []
    r_16_tuples = []
    r_1_tuples = []
    r_2_tuples = []
    r_3_tuples = []
    r_4_tuples = []
    r_5_tuples = []
    r_6_tuples = []
    r_7_tuples = []
    r_8_tuples = []
    r_9_tuples = []
    r_10_tuples = []
    r_11_tuples = []
    r_12_tuples = []
    r_13_tuples = []
    r_14_tuples = []
    r_15_tuples = []
    r_16_tuples = []
    c_1_tuples = []
    c_2_tuples = []
    c_3_tuples = []
    c_4_tuples = []
    c_5_tuples = []
    c_6_tuples = []
    c_7_tuples = []
    c_8_tuples = []
    c_9_tuples = []
    c_10_tuples = []
    c_11_tuples = []
    c_12_tuples = []
    c_13_tuples = []
    c_14_tuples = []
    c_15_tuples = []
    c_16_tuples = []
    s_1_tuples = []
    s_2_tuples = []
    s_3_tuples = []
    s_4_tuples = []
    s_5_tuples = []
    s_6_tuples = []
    s_7_tuples = []
    s_8_tuples = []
    s_9_tuples = []
    s_10_tuples = []
    s_11_tuples = []
    s_12_tuples = []
    s_13_tuples = []
    s_14_tuples = []
    s_15_tuples = []
    s_16_tuples = []
    temp_list = []

    for aref in not_done_arefs:
        row = int(aref['row'])
        col = int(aref['col'])
        sq = int(aref['sq'])
        nums = str(aref['nums'])
        arefs = aref['aref']
        # This ref to current_btn sets the string name of the button.
        current_btn = aref['btn_str']
        temp_list = [row, col, sq, nums]  # , arefs, current_btn]
        if len(nums) <= num:
            # print("1947 ", row, col, sq, nums)
            if row == 1:
                r_1_tuples.append(temp_list)
            elif row == 2:
                r_2_tuples.append(temp_list)
            elif row == 3:
                r_3_tuples.append(temp_list)
            elif row == 4:
                r_4_tuples.append(temp_list)
            elif row == 5:
                r_5_tuples.append(temp_list)
            elif row == 6:
                r_6_tuples.append(temp_list)
            elif row == 7:
                r_7_tuples.append(temp_list)
            elif row == 8:
                r_8_tuples.append(temp_list)
            elif row == 9:
                r_9_tuples.append(temp_list)
            elif row == 10:
                r_10_tuples.append(temp_list)
            elif row == 11:
                r_11_tuples.append(temp_list)
            elif row == 12:
                r_12_tuples.append(temp_list)
            elif row == 13:
                r_13_tuples.append(temp_list)
            elif row == 14:
                r_14_tuples.append(temp_list)
            elif row == 15:
                r_15_tuples.append(temp_list)
            elif row == 16:
                r_16_tuples.append(temp_list)
            if col == 1:
                c_1_tuples.append(temp_list)
            elif col == 2:
                c_2_tuples.append(temp_list)
            elif col == 3:
                c_3_tuples.append(temp_list)
            elif col == 4:
                c_4_tuples.append(temp_list)
            elif col == 5:
                c_5_tuples.append(temp_list)
            elif col == 6:
                c_6_tuples.append(temp_list)
            elif col == 7:
                c_7_tuples.append(temp_list)
            elif col == 8:
                c_8_tuples.append(temp_list)
            elif col == 9:
                c_9_tuples.append(temp_list)
            elif col == 10:
                c_10_tuples.append(temp_list)
            elif col == 11:
                c_11_tuples.append(temp_list)
            elif col == 12:
                c_12_tuples.append(temp_list)
            elif col == 13:
                c_13_tuples.append(temp_list)
            elif col == 14:
                c_14_tuples.append(temp_list)
            elif col == 15:
                c_15_tuples.append(temp_list)
            elif col == 16:
                c_16_tuples.append(temp_list)
            if sq == 1:
                s_1_tuples.append(temp_list)
            elif sq == 2:
                s_2_tuples.append(temp_list)
            elif sq == 3:
                s_3_tuples.append(temp_list)
            elif sq == 4:
                s_4_tuples.append(temp_list)
            elif sq == 5:
                s_5_tuples.append(temp_list)
            elif sq == 6:
                s_6_tuples.append(temp_list)
            elif sq == 7:
                s_7_tuples.append(temp_list)
            elif sq == 8:
                s_8_tuples.append(temp_list)
            elif sq == 9:
                s_9_tuples.append(temp_list)
            elif sq == 10:
                s_10_tuples.append(temp_list)
            elif sq == 11:
                s_11_tuples.append(temp_list)
            elif sq == 12:
                s_12_tuples.append(temp_list)
            elif sq == 13:
                s_13_tuples.append(temp_list)
            elif sq == 14:
                s_14_tuples.append(temp_list)
            elif sq == 15:
                s_15_tuples.append(temp_list)
            elif sq == 16:
                s_16_tuples.append(temp_list)
            row_tuples = (r_1_tuples, r_2_tuples, r_3_tuples, r_4_tuples, r_5_tuples, r_6_tuples, r_7_tuples, r_8_tuples,
                          r_9_tuples, r_10_tuples, r_11_tuples, r_12_tuples, r_13_tuples, r_14_tuples, r_15_tuples, r_16_tuples)
            col_tuples = (c_1_tuples, c_2_tuples, c_3_tuples, c_4_tuples, c_5_tuples, c_6_tuples, c_7_tuples, c_8_tuples,
                          c_9_tuples, c_10_tuples, c_11_tuples, c_12_tuples, c_13_tuples, c_14_tuples, c_15_tuples, c_16_tuples)
            sq_tuples = (s_1_tuples, s_2_tuples, s_3_tuples, s_4_tuples, s_5_tuples, s_6_tuples, s_7_tuples, s_8_tuples,
                         s_9_tuples, s_10_tuples, s_11_tuples, s_12_tuples, s_13_tuples, s_14_tuples, s_15_tuples, s_16_tuples)
    print("2054 row tuple candidates are: ", r_8_tuples)
    for r in row_tuples:
        if len(r) >= num:
            print("2056 ", r)
            _process_tuple_RCS(r, r, num)
    print("2057 column tuple candidates are:")
    for c in col_tuples:
        if len(c) >= num:
            print("2059 ", c)
            _process_tuple_RCS(c, c, num)
    print("2060 square tuple candidates are:")
    for s in sq_tuples:
        if len(s) >= num:
            print("2062 ", s)
            _process_tuple_RCS(s, s, num)


def _process_tuple_RCS(tuple_candidate, rcs, num):
    ''' Process each row, column, and square to identify
    tuples of size 'num' which was a parameter of the function.
    '''
    print("2076 tuple_candidate list is ", tuple_candidate, rcs)
    global triple
    global triples_list

    tcl = len(tuple_candidate)
    tc = tuple_candidate
    print("2094 ", tc)

    print("2087 tuple is ", tuple_candidate[0])
    print("2088 tuple number is ", tuple_candidate[0][3])

    for item in tuple_candidate:
        row = item[0]
        col = item[1]
        sq = item[2]
        nums = item[3]
        print("2094 rcsn ", row, col, sq, nums)
        tc = tuple_candidate
        tcl = len(tuple_candidate)
        s3012 = []
        s3013 = []
        s3014 = []
        s3015 = []
        s3023 = []
        s3024 = []
        s3025 = []
        s3123 = []
        s3124 = []
        s3125 = []
        s3234 = []
        s3235 = []
        s3567 = []
        s40123 = []
        s40134 = []
        s41234 = []
        print("2114 tcl is ", tcl)
        s0 = set(tc[0][3])
        s1 = set(tc[1][3])
        s2 = set(tc[2][3])
        if tcl == 3 and num == 3:
            # sa = s0.union(s1)
            s3012 = s0.union(s1).union(s2)
            if len(s3012) == 3:
                print(f"4836 Triples are {s3012}")
                ex_text = f"4835 Triple is s3012 {s3012} \n"
                txt_Explain.insert(END, ex_text)
            # s_set_list = [s3012]
            # if len(item) == 3:
                triples_list.append(s3012)
                triples_list.append(rcs)
            # if len(item) == 3:
            #     triples_list.append(item)
            #     triples_list.append(rcs)
        if tcl == 4 and num == 3:
            s3 = set(tc[3][3])
            # sa = s0.union(s1)
            s3012 = s0.union(s1).union(s2)
            if len(s3012) == 3:
                print(f"2154 Triples are {s3012}")
                ex_text = f"2154 Triple is {s3012} \n"
                txt_Explain.insert(END, ex_text)
            s3013 = s0.union(s1).union(s3)
            if len(s3013) == 3:
                print(f"2159 Triples are {s3013}")
                ex_text = f"2154 Triple is {s3013} \n"
                txt_Explain.insert(END, ex_text)
            s3123 = s1.union(s2).union(s3)
            if len(s3123) == 3:
                print(f"2164 Triples are {s3123}")
                ex_text = f"2165 Triple is {s3123} \n"
                txt_Explain.insert(END, ex_text)
            s_set_list = [s3012, s3013, s3123]
            for item in s_set_list:
                if len(item) == 3:
                    ex_text = f"2159 Triple is {item} \n"
                    txt_Explain.insert(END, ex_text)
                    triples_list.append(item)
                    triples_list.append(rcs)

        if tcl == 4 and num == 4:
            s3 = set(tc[3][3])
            s4 = set(tc[3][3])
            s40123 = s0.union(s1).union(s2).union(s3)
            if len(s40123) == 4:
                print(f"2154 Quad is {s40123}")
                ex_text = f"2154 Quad is {s40123} \n"
                txt_Explain.insert(END, ex_text)

        if tcl == 5 and num == 3:
            s3 = set(tc[3][3])
            s4 = set(tc[4][3])
            s3012 = s0.union(s1).union(s2)
            if len(s3012) == 3:
                print(f"2180 Triples are {s3012}")
                ex_text = f"2181 Triple is {s3012} \n"
                txt_Explain.insert(END, ex_text)
            s3013 = s0.union(s1).union(s3)
            if len(s3013) == 3:
                print(f"2184 Triples are {s3013}")
                ex_text = f"2186 Triple is {s3013} \n"
                txt_Explain.insert(END, ex_text)
            s3014 = s0.union(s1).union(s4)
            if len(s3014) == 3:
                print(f"4893 Triples are {s3014}")
                ex_text = f"4894 Triple is {s3014} \n"
                txt_Explain.insert(END, ex_text)
            s3023 = s0.union(s2).union(s3)
            if len(s3023) == 3:
                print(f"2196 Triples are {s3023}")
                ex_text = f"2198 Triple is {s3023} \n"
                txt_Explain.insert(END, ex_text)
            s3024 = s0.union(s2).union(s4)
            if len(s3024) == 3:
                print(f"2202 Triples are {s3024}")
                ex_text = f"2203 Triple is {s3024} \n"
                txt_Explain.insert(END, ex_text)
            s3123 = s1.union(s2).union(s3)
            if len(s3123) == 3:
                print(f"2202 Triples are {s3123}")
                ex_text = f"2203 Triple is {s3123} \n"
                txt_Explain.insert(END, ex_text)
            s3124 = s1.union(s2).union(s4)
            if len(s3124) == 3:
                print(f"4913 Triples are {s3124}")
                ex_text = f"4914 Triple is s3124, {s3124} \n"
                txt_Explain.insert(END, ex_text)
            s3134 = s1.union(s3).union(s4)
            if len(s3134) == 3:
                print(f"4913 Triples are s3134 {s3134}")
                ex_text = f"4914 Triple is s3134, {s3134} \n"
                txt_Explain.insert(END, ex_text)
            s3234 = s2.union(s3).union(s4)
            if len(s3234) == 3:
                print(f"2207 Triples are s3234 {s3234}")
                ex_text = f"2209 Triple is s3234 {s3234} \n"
                txt_Explain.insert(END, ex_text)
            s_set_list = [s3012, s3013, s3014,
                          s3023, s3024, s3123, s3124, s3134, s3234]
            for item in s_set_list:
                if len(item) == 3:
                    # if not item in triples_list:
                    triples_list.append(item)
                    triples_list.append(rcs)
                    # triples_rcs_list.append(rcs)
                    print("4929 triple set is ", item, rcs)

        if tcl == 5 and num == 4:
            s3 = set(tc[3][3])
            s4 = set(tc[4][3])
            s40123 = s0.union(s1).union(s2).union(s3)
            if len(s40123) == 4:
                print(f"5097 Quad is {s40123}")
                ex_text = f"5098 Quad is {s40123} \n"
                txt_Explain.insert(END, ex_text)
            s40124 = s0.union(s1).union(s2).union(s4)
            if len(s40124) == 4:
                print(f"5102 Quad is {s40124}")
                ex_text = f"5103 Quad is {s40124} \n"
                txt_Explain.insert(END, ex_text)
            s41234 = s1.union(s2).union(s3).union(s4)
            if len(s41234) == 4:
                print(f"5107 Quad is {s41234}")
                ex_text = f"5108 Quad is {s41234} \n"
                txt_Explain.insert(END, ex_text)
            s_set_list = [s40123, s40124, s41234]
            for item in s_set_list:
                if len(item) == 4:
                    # if not item in quads_list:
                    quads_list.append(item)
                    quads_list.append(rcs)
                    # triples_rcs_list.append(rcs)
                    print("4956 Quad is ", item, rcs)

        if tcl == 6 and num == 3:
            s3 = set(tc[3][3])
            s4 = set(tc[4][3])
            s5 = set(tc[5][3])
            # s6 = set(tc[6][3])
            s3012 = s0.union(s1).union(s2)
            if len(s3012) == 3:
                print(f"5090 Triples are s3012 {s3012}")
                ex_text = f"5091 Triple is s3012 {s3012} \n"
                txt_Explain.insert(END, ex_text)
            s3013 = s0.union(s1).union(s3)
            if len(s3013) == 3:
                print(f"4970 Triples are {s3013}")
                ex_text = f"4971 Triple is {s3013} \n"
                txt_Explain.insert(END, ex_text)
            s3014 = s0.union(s1).union(s4)
            if len(s3014) == 3:
                print(f"2237 Triples are {s3014}")
                ex_text = f"2238 Triple is {s3014} \n"
                txt_Explain.insert(END, ex_text)
            s3015 = s0.union(s1).union(s5)
            if len(s3015) == 3:
                print(f"2237 Triples are {s3015}")
                ex_text = f"2238 Triple is {s3015} \n"
                txt_Explain.insert(END, ex_text)
            s3023 = s0.union(s2).union(s3)
            if len(s3023) == 3:
                print(f"2237 Triples are {s3023}")
                ex_text = f"2238 Triple is {s3023} \n"
                txt_Explain.insert(END, ex_text)
            s3024 = s0.union(s2).union(s4)
            if len(s3024) == 3:
                print(f"2237 Triples are {s3024}")
                ex_text = f"2238 Triple is {s3024} \n"
                txt_Explain.insert(END, ex_text)
            s3025 = s0.union(s2).union(s5)
            if len(s3025) == 3:
                print(f"2237 Triples are {s3025}")
                ex_text = f"2238 Triple is {s3025} \n"
                txt_Explain.insert(END, ex_text)
            s3123 = s1.union(s2).union(s3)
            if len(s3123) == 3:
                print(f"5065 Triples are {s3123}")
                ex_text = f"5066 Triple is {s3123} \n"
                txt_Explain.insert(END, ex_text)
            s3124 = s1.union(s2).union(s4)
            if len(s3124) == 3:
                print(f"5070 Triples are {s3124}")
                ex_text = f"5071 Triple is {s3124} \n"
                txt_Explain.insert(END, ex_text)
            s3125 = s1.union(s2).union(s5)
            if len(s3125) == 3:
                print(f"2254 Triples are {s3125}")
                ex_text = f"2255 Triple is {s3125} \n"
                txt_Explain.insert(END, ex_text)
            s3234 = s2.union(s3).union(s4)
            if len(s3234) == 3:
                print(f"2261 Triples are s3234 {s3234}")
                ex_text = f"2262 Triple is s3234 {s3234} \n"
                txt_Explain.insert(END, ex_text)
            s3235 = s2.union(s3).union(s5)
            if len(s3235) == 3:
                print(f"2266 Tuples are {s3235}")
                ex_text = f"2267 Tuple is {s3235} \n"
                txt_Explain.insert(END, ex_text)
            s3345 = s3.union(s4).union(s5)
            if len(s3345) == 3:
                print(f"2184 Tuples are {s3345}")
                ex_text = f"2274 Tuple is s3345, {s3345} \n"
                txt_Explain.insert(END, ex_text)

            #     txt_Explain.insert(END, ex_text)
            s_set_list = [s3012, s3013, s3014, s3015, s3023, s3024,
                          s3025, s3123, s3124, s3125, s3234, s3235, s3345]
            for item in s_set_list:
                if len(item) == 3:
                    # if not item in triples_list:
                    triples_list.append(item)
                    triples_list.append(rcs)
                    # triples_rcs_list.append(rcs)
                    print("5035 triple set is ", item, rcs)

        if tcl == 6 and num == 4:
            s3 = set(tc[3][3])
            s4 = set(tc[4][3])
            s5 = set(tc[5][3])
            # s6 = set(tc[6][3])
            s40123 = s0.union(s1).union(s2).union(s3)
            if len(s40123) == 4:
                print(f"5044 Quad is {s40123}")
                ex_text = f"5045 Quad is {s40123} \n"
                txt_Explain.insert(END, ex_text)
            s40124 = s0.union(s1).union(s2).union(s4)
            if len(s40124) == 4:
                print(f"5049 Quad ise {s40124}")
                ex_text = f"5050 Quad is {s40124} \n"
                txt_Explain.insert(END, ex_text)
            s40125 = s0.union(s1).union(s2).union(s5)
            if len(s40125) == 4:
                print(f"5054 Quad is {s40125}")
                ex_text = f"5055 Quad is {s40125} \n"
                txt_Explain.insert(END, ex_text)
            s40134 = s0.union(s1).union(s3).union(s4)
            if len(s40134) == 4:
                print(f"5054 Quad is {s40134}")
                ex_text = f"5055 Quad is s40134 {s40134} \n"
                txt_Explain.insert(END, ex_text)
            s40135 = s0.union(s1).union(s3).union(s5)
            if len(s40135) == 4:
                print(f"5054 Quad is {s40135}")
                ex_text = f"5055 Quad is {s40135} \n"
                txt_Explain.insert(END, ex_text)
            s40145 = s0.union(s1).union(s4).union(s5)
            if len(s40134) == 4:
                print(f"5054 Quad is {s40145}")
                ex_text = f"5055 Quad is s40134 {s40145} \n"
                txt_Explain.insert(END, ex_text)
            s40234 = s0.union(s2).union(s3).union(s4)
            if len(s40234) == 4:
                print(f"5054 Quad is s40234 {s40234}")
                ex_text = f"5055 Quad is s40234 {s40234} \n"
                txt_Explain.insert(END, ex_text)
            s40235 = s0.union(s2).union(s3).union(s5)
            if len(s40235) == 4:
                print(f"5054 Quad is s40235 {s40235}")
                ex_text = f"5055 Quad is s40235 {s40235} \n"
                txt_Explain.insert(END, ex_text)
            s40345 = s0.union(s3).union(s4).union(s5)
            if len(s40345) == 4:
                print(f"5054 Quad is s40345 {s40345}")
                ex_text = f"5055 Quad is s40345 {s40345} \n"
                txt_Explain.insert(END, ex_text)
            s41234 = s1.union(s2).union(s3).union(s4)
            if len(s41234) == 4:
                print(f"5059 Quad is s41234 {s41234}")
                ex_text = f"5060 Quad is s41234 {s41234} \n"
                txt_Explain.insert(END, ex_text)
            s41235 = s1.union(s2).union(s3).union(s5)
            if len(s41235) == 4:
                print(f"5064 Quad is {s41235}")
                ex_text = f"5065 Quad is {s41235} \n"
                txt_Explain.insert(END, ex_text)
            s42345 = s2.union(s3).union(s4).union(s5)
            if len(s42345) == 4:
                print(f"2232 Quad is {s42345}")
                ex_text = f"2233 Quad is {s42345} \n"
                txt_Explain.insert(END, ex_text)
            s_set_list = [s40123, s40124, s40125, s40134,
                          s40135, s40145, s40234, s40235, s40345, s41234, s41235, s42345]
            for item in s_set_list:
                if len(item) == 4:
                    if not item in quads_list:
                        quads_list.append(item)
                        quads_list.append(rcs)
                        print("5078 Quad is ", item, rcs)

        if tcl == 7 and num == 3:
            s3 = set(tc[3][3])
            s4 = set(tc[4][3])
            s5 = set(tc[5][3])
            s6 = set(tc[6][3])
            s3234 = s2.union(s3).union(s4)
            if len(s3234) == 3:
                print(f"5182 Tuples are s3234 {s3234}")
                ex_text = f"5283 Tuple is s3234, {s3234} \n"
            s3456 = s4.union(s5).union(s6)
            if len(s3456) == 3:
                print(f"5182 Tuples are {s3456}")
                ex_text = f"5283 Tuple is s3456, {s3456} \n"
            s_set_list = [s3234, s3456]  # , s3567
            for item in s_set_list:
                if len(item) == 3:
                    # if not item in triples_list:
                    triples_list.append(item)
                    triples_list.append(rcs)
                    print("5245 triple set is ", item, rcs)
                    ex_text = f"5245 triple is {item} \n"
                    txt_Explain.insert(END, ex_text)

        if tcl == 8 and num == 3:
            s3 = set(tc[3][3])
            s4 = set(tc[4][3])
            s5 = set(tc[5][3])
            s6 = set(tc[6][3])
            s7 = set(tc[7][3])
            s3567 = s5.union(s6).union(s7)
            if len(s3567) == 3:
                print(f"5182 Tuples are {s3567}")
                ex_text = f"5283 Tuple is s3567, {s3567} \n"
            s_set_list = [s3567]  # , s3567
            for item in s_set_list:
                if len(item) == 3:
                    triples_list.append(item)
                    triples_list.append(rcs)
                    print("5284 triple set is ", item, rcs)
                    ex_text = f"5285 triple is {item} \n"
                    txt_Explain.insert(END, ex_text)

        if tcl == 7 and num == 4:
            s3 = set(tc[3][3])
            s4 = set(tc[4][3])
            s5 = set(tc[5][3])
            s6 = set(tc[6][3])
            s40123 = s0.union(s1).union(s2).union(s3)
            if len(s40123) == 4:
                print(f"5282 Quad is {s40123}")
                ex_text = f"5283 Quad is {s40123} \n"
                txt_Explain.insert(END, ex_text)
            s40124 = s0.union(s1).union(s2).union(s4)
            if len(s40124) == 4:
                print(f"2232 Quad is {s40124}")
                ex_text = f"2233 Quad is {s40124} \n"
                txt_Explain.insert(END, ex_text)
            s40125 = s0.union(s1).union(s2).union(s5)
            if len(s40125) == 4:
                print(f"2232 Quad is {s40125}")
                ex_text = f"2233 Quad is {s40125} \n"
                txt_Explain.insert(END, ex_text)
            s40126 = s0.union(s1).union(s2).union(s6)
            if len(s40126) == 4:
                print(f"2232 Quad is {s40126}")
                ex_text = f"2233 Quad is {s40126} \n"
                txt_Explain.insert(END, ex_text)
            s40234 = s0.union(s2).union(s3).union(s4)
            if len(s40234) == 4:
                print(f"2232 Quad is {s40234}")
                ex_text = f"2233 Quad is {s40234} \n"
                txt_Explain.insert(END, ex_text)
            s40235 = s0.union(s2).union(s3).union(s5)
            if len(s40235) == 4:
                print(f"2232 Quad are {s40235}")
                ex_text = f"2233 Quad is {s40235} \n"
                txt_Explain.insert(END, ex_text)
            s40236 = s0.union(s2).union(s3).union(s6)
            if len(s40236) == 4:
                print(f"2232 Quad are {s40236}")
                ex_text = f"2233 Quad is {s40236} \n"
                txt_Explain.insert(END, ex_text)
            s40245 = s0.union(s2).union(s4).union(s5)
            if len(s40245) == 4:
                print(f"2232 Quad are {s40245}")
                ex_text = f"2233 Quad is {s40245} \n"
                txt_Explain.insert(END, ex_text)
            s40246 = s0.union(s2).union(s4).union(s6)
            if len(s40246) == 4:
                print(f"2232 Quad are {s40246}")
                ex_text = f"2233 Quad is {s40246} \n"
                txt_Explain.insert(END, ex_text)
            s40256 = s0.union(s2).union(s5).union(s6)
            if len(s40256) == 4:
                print(f"5133 Quad are {s40256}")
                ex_text = f"5134 Quad is s40256 {s40256} \n"
                txt_Explain.insert(END, ex_text)
            s40345 = s0.union(s3).union(s4).union(s5)
            if len(s40345) == 4:
                print(f"2232 Quad are {s40345}")
                ex_text = f"2233 Quad is {s40345} \n"
                txt_Explain.insert(END, ex_text)
            s40346 = s0.union(s3).union(s4).union(s6)
            if len(s40346) == 4:
                print(f"2232 Quad are {s40346}")
                ex_text = f"2233 Quad is {s40346} \n"
                txt_Explain.insert(END, ex_text)
            s40456 = s0.union(s4).union(s5).union(s6)
            if len(s40456) == 4:
                print(f"2232 Quad are {s40456}")
                ex_text = f"2233 Quad is {s40456} \n"
                txt_Explain.insert(END, ex_text)
            s41234 = s1.union(s2).union(s3).union(s4)
            if len(s41234) == 4:
                print(f"2232 Quad are {s41234}")
                ex_text = f"2233 Quad is {s41234} \n"
                txt_Explain.insert(END, ex_text)
            s41235 = s1.union(s2).union(s3).union(s5)
            if len(s41235) == 4:
                print(f"2232 Quad are {s41235}")
                ex_text = f"2233 Quad is {s41235} \n"
                txt_Explain.insert(END, ex_text)
            s41236 = s1.union(s2).union(s3).union(s6)
            if len(s41236) == 4:
                print(f"2232 Quad are {s41236}")
                ex_text = f"2233 Quad is {s41236} \n"
                txt_Explain.insert(END, ex_text)
            s41345 = s1.union(s3).union(s4).union(s5)
            if len(s41345) == 4:
                print(f"2232 Quad are {s41345}")
                ex_text = f"2233 Quad is {s41345} \n"
                txt_Explain.insert(END, ex_text)
            s41346 = s1.union(s3).union(s4).union(s6)
            if len(s41346) == 4:
                print(f"4063 Quad are {s41346}")
                ex_text = f"4064 Quad is {s41346} \n"
                txt_Explain.insert(END, ex_text)
            s41456 = s1.union(s4).union(s5).union(s6)
            if len(s41456) == 4:
                print(f"4063 Quad are {s41456}")
                ex_text = f"4064 Quad is {s41456} \n"
                txt_Explain.insert(END, ex_text)
            s42345 = s2.union(s3).union(s4).union(s5)
            if len(s42345) == 4:
                print(f"2232 Quad are {s42345}")
                ex_text = f"2233 Quad is {s42345} \n"
                txt_Explain.insert(END, ex_text)
            s42346 = s2.union(s3).union(s4).union(s6)
            if len(s42346) == 4:
                print(f"2232 Quad are {s42346}")
                ex_text = f"2233 Quad is {s42346} \n"
                txt_Explain.insert(END, ex_text)
            s43456 = s3.union(s4).union(s5).union(s6)
            if len(s43456) == 4:
                print(f"2232 Quad are {s43456}")
                ex_text = f"2233 Quad is {s43456} \n"
                txt_Explain.insert(END, ex_text)
            s_set_list = [s40123, s40124, s40125, s40126, s40234, s40235, s40236, s40245, s40246, s40256, s40345,
                          s40346, s40456, s41234, s41235, s41236, s41345, s41346, s41456, s42345, s42346, s43456]
            for item in s_set_list:
                # if not item == []:
                # print("4016 item is ", item)
                if len(item) == 4:
                    # if not item in quads_list:
                    quads_list.append(item)
                    quads_list.append(rcs)
                    print("5205 quads_list is ", item, rcs)
                    ex_text = f"5206 Quad is {item} \n"
                    txt_Explain.insert(END, ex_text)

        print("5208 triples_list is ", triples_list)
        print("5209 quads_list is ", quads_list)


def show_Triple(triple):
    ex_text = f"Triple is {str(triple)} \n"
    txt_Explain.insert(END, ex_text)


def parse_list_items():
    i_start = 0
    i_end = 0
    i_sb = 0
    i_eb = 0
    i_c = 0
    li = [1, "[2, 1, 1, '156'][8, 1, 5, 'CE'][15, 1, 13, '59D']"]
    row0 = li[0]
    li_lists = li[1]
    ts = li_lists
    print(ts)
    num = 0
    for char in li_lists:
        if char == '[':
            i_sb = li_lists.index('[')
            print("1661 i_sb = ", i_sb)
        elif char == ']':
            i_eb = li_lists.index(']')
            print("1664 i_eb = ", i_eb)
        elif char == ',':
            i_c = li_lists.index(',')
            print("1667 i_c = ", i_c)
        elif char == "'":
            i_q = li_lists.index("'")
            print("1670 i_q = ", i_q)
        else:
            num = ts[0:i_c]
            # i_ch = li_lists.slice(i_sb, )
            print("1670 num = ", num)


def process_row_triple(t_row, triple_set, triple_list):
    print("2736 process_row_triple ", t_row)
    print("2737 triple_list is ", t_row,
          triple_set, triple_list)  # triples_list)
    c_set = triple_set
    print("2744 t_set ", c_set)
    nums = " ".join(map(str, c_set))
    # nums = str(" ".join(map(str, triple))) #old
    n0 = nums[0]
    n1 = nums[2]
    n2 = nums[4]
    print("2746 nums ", c_set, nums, n0, n1, n2)
    print("2418 triple_list is ", triple_list)

    for aref in not_done_arefs:
        row0 = aref['row']
        if row0 != t_row:
            pass
        elif row0 == t_row:
            current_btn = aref['btn']
            col0 = aref['col']
            sq0 = aref['sq']
            nums0 = aref['nums']
            total_nums = c_set.union(nums0)
            print("2587 triple ", current_btn,
                  row0, col0, sq0, nums0, total_nums)
            if len(total_nums) > 3:
                for num in c_set:
                    if num in nums0:
                        print("2592 num is ", num)
                        nums1 = aref['nums'].replace(num, "")
                        print("2594 nums0 are ", nums1)
                        aref['nums'] = str(nums1)
                        print("2596 new text is ", aref['nums'])
                        current_btn['text'] = aref['nums']
                    else:
                        print(
                            "1450 Else fall through in triple remove number.")
        else:
            pass


def process_row_triple_Old(r_row):
    print("2612 process_row_triple ", r_row)
    print("2613 triple list is ", triples_list)
    found_triple = False
    for triple in triples_list:
        print("2338 triple is ", triple, type(triple))
        if type(triple) == set:
            print("2741 triple set is ", triple)
            found_triple = True
            r_set = triple
            print("2744 t_set ", r_set)
            nums = " ".join(map(str, triple))
            # nums = str(" ".join(map(str, triple))) #old
            n0 = nums[0]
            n1 = nums[2]
            n2 = nums[4]
            print("2746 nums ", r_set, nums, n0, n1, n2)
        elif type(triple) == list:
            l0 = triple[0]
            l1 = triple[1]
            l2 = triple[2]
            print("2469 lists are ", l0, l1, l2)
            if not found_triple == True:
                continue

        for aref in not_done_arefs:
            row0 = aref['row']
            if row0 != r_row:
                pass
            elif row0 == r_row:
                current_btn = aref['btn']
                col0 = aref['col']
                sq0 = aref['sq']
                nums0 = aref['nums']
                total_nums = r_set.union(nums0)
                print("2720 triple ", current_btn,
                      row0, col0, sq0, nums0, total_nums)
                if len(total_nums) > 3:
                    for num in r_set:
                        if num in nums0:
                            print("2592 num is ", num)
                            nums1 = aref['nums'].replace(num, "")
                            print("2594 nums0 are ", nums1)
                            aref['nums'] = str(nums1)
                            print("2596 new text is ", aref['nums'])
                            current_btn['text'] = aref['nums']
                        else:
                            print("1450 Else fall through in triple remove number.")
            else:
                pass
    else:
        print("2709 no set or list ", triple, type(triple))
    found_triple = False


def process_column_triple(t_col, triple_set, triple_list):
    print("2736 process_column_triple ", t_col)
    print("2737 triple_list is ", t_col,
          triple_set, triple_list)  # triples_list)
    c_set = triple_set
    print("2744 t_set ", c_set)
    nums = " ".join(map(str, c_set))
    # nums = str(" ".join(map(str, triple))) #old
    n0 = nums[0]
    n1 = nums[2]
    n2 = nums[4]
    print("2746 nums ", c_set, nums, n0, n1, n2)
    print("2418 triple_list is ", triple_list)

    for aref in not_done_arefs:
        col0 = aref['col']
        if col0 != t_col:
            pass
        elif col0 == t_col:
            current_btn = aref['btn']
            row0 = aref['row']
            sq0 = aref['sq']
            nums0 = aref['nums']
            total_nums = c_set.union(nums0)
            print("2587 triple ", current_btn,
                  row0, col0, sq0, nums0, total_nums)
            if len(total_nums) > 3:
                for num in c_set:
                    if num in nums0:
                        print("2592 num is ", num)
                        nums1 = aref['nums'].replace(num, "")
                        print("2594 nums0 are ", nums1)
                        aref['nums'] = str(nums1)
                        print("2596 new text is ", aref['nums'])
                        current_btn['text'] = aref['nums']
                    else:
                        print(
                            "1450 Else fall through in triple remove number.")
        else:
            pass


def process_column_triple_Old(t_col):
    print("2736 process_column_triple ", t_col)
    print("2737 triple_list is ", triples_list)
    found_triple = False
    for triple in triples_list:
        print("2445 triple is ", triple, type(triple))
        if type(triple) == set:
            print("2741 triple set is ", triple)
            found_triple = True
            c_set = triple
            print("2744 t_set ", c_set)
            nums = " ".join(map(str, triple))
            # nums = str(" ".join(map(str, triple))) #old
            n0 = nums[0]
            n1 = nums[2]
            n2 = nums[4]
            print("2746 nums ", c_set, nums, n0, n1, n2)
        elif type(triple) == list:
            l0 = triple[0]
            l1 = triple[1]
            l2 = triple[2]
            print("2469 lists are ", l0, l1, l2)
            if not found_triple == True:
                continue

            for aref in not_done_arefs:
                col0 = aref['col']
                if col0 != t_col:
                    pass
                elif col0 == t_col:
                    current_btn = aref['btn']
                    row0 = aref['row']
                    sq0 = aref['sq']
                    nums0 = aref['nums']
                    total_nums = c_set.union(nums0)
                    print("2587 triple ", current_btn,
                          row0, col0, sq0, nums0, total_nums)
                    if len(total_nums) > 3:
                        for num in c_set:
                            if num in nums0:
                                print("2592 num is ", num)
                                nums1 = aref['nums'].replace(num, " ")
                                print("2594 nums0 are ", nums1)
                                aref['nums'] = str(nums1)
                                print("2596 new text is ", aref['nums'])
                                current_btn['text'] = aref['nums']
                            else:
                                print(
                                    "1450 Else fall through in triple remove number.")
        else:
            pass
    found_triple = False


def process_sq_triple(t_sq, triple_set, triple_list):
    print("5441 process_sq_triple ", t_sq)
    print("2737 triple_list is ", t_sq,
          triple_set, triple_list)  # triples_list)
    c_set = triple_set
    print("2744 t_set ", c_set)
    nums = " ".join(map(str, c_set))
    # nums = str(" ".join(map(str, triple))) #old
    n0 = nums[0]
    n1 = nums[2]
    n2 = nums[4]
    print("2746 nums ", c_set, nums, n0, n1, n2)
    print("2418 triple_list is ", triple_list)

    for aref in not_done_arefs:
        sq0 = aref['sq']
        if sq0 != t_sq:
            pass
        elif sq0 == t_sq:
            current_btn = aref['btn']
            row0 = aref['row']
            col0 = aref['col']
            sq0 = aref['sq']
            nums0 = aref['nums']
            total_nums = c_set.union(nums0)
            print("2587 triple ", current_btn,
                  row0, col0, sq0, nums0, total_nums)
            if len(total_nums) > 3:
                for num in c_set:
                    if num in nums0:
                        print("2592 num is ", num)
                        nums1 = aref['nums'].replace(num, "")
                        print("2594 nums0 are ", nums1)
                        aref['nums'] = str(nums1)
                        print("2596 new text is ", aref['nums'])
                        current_btn['text'] = aref['nums']
                    else:
                        print(
                            "1450 Else fall through in triple remove number.")
        else:
            pass


def process_sq_quad(t_sq, quads_set, quads_list):
    print("5550 process_sq_quad ", t_sq)
    print("2737 quads_list is ", t_sq,
          quads_set, quads_list)  # triples_list)
    c_set = quads_set
    print("2744 t_set ", c_set)
    nums = " ".join(map(str, c_set))
    # nums = str(" ".join(map(str, triple))) #old
    n0 = nums[0]
    n1 = nums[2]
    n2 = nums[4]
    n3 = nums[6]
    print("5561 nums ", c_set, nums, n0, n1, n2, n3)
    print("5562 triple_list is ", quads_list)

    for aref in not_done_arefs:
        sq0 = aref['sq']
        if sq0 != t_sq:
            pass
        elif sq0 == t_sq:
            current_btn = aref['btn']
            row0 = aref['row']
            col0 = aref['col']
            sq0 = aref['sq']
            nums0 = aref['nums']
            total_nums = c_set.union(nums0)
            print("5573 quad ", current_btn,
                  row0, col0, sq0, nums0, total_nums)
            if len(total_nums) > 4:
                for num in c_set:
                    if num in nums0:
                        print("5578 num is ", num)
                        nums1 = aref['nums'].replace(num, "")
                        print("2594 nums0 are ", nums1)
                        aref['nums'] = str(nums1)
                        print("2596 new text is ", aref['nums'])
                        current_btn['text'] = aref['nums']
                    else:
                        print(
                            "5586 Else fall through in quads remove number.")
        else:
            pass


def process_sq_triple_old(t_sq):
    print("2862 process_sq_triple ", t_sq)
    print("2863 triple list is ", triples_list)
    found_triple = False
    for triple in triples_list:
        print("2338 triple is ", triple, type(triple))
        if type(triple) == set:
            print("2741 triple set is ", triple)
            found_triple = True
            s_set = triple
            print("2744 t_set ", s_set)
            nums = " ".join(map(str, triple))
            # nums = str(" ".join(map(str, triple))) #old
            n0 = nums[0]
            n1 = nums[2]
            n2 = nums[4]
            print("2746 nums ", s_set, nums, n0, n1, n2)
        elif type(triple) == list:
            l0 = triple[0]
            l1 = triple[1]
            l2 = triple[2]
            print("2469 lists are ", l0, l1, l2)
            if not found_triple == True:
                continue

        for aref in not_done_arefs:
            sq0 = aref['sq']
            if sq0 != t_sq:
                pass
            elif sq0 == t_sq:
                current_btn = aref['btn']
                row0 = aref['row']
                col0 = aref['col']
                sq0 = aref['sq']
                nums0 = aref['nums']
                total_nums = s_set.union(nums0)
                print("2905 triple ", current_btn,
                      row0, col0, sq0, nums0, total_nums)
                if len(total_nums) > 3:
                    for num in s_set:
                        if num in nums0:
                            print("2910 num is ", num)
                            nums1 = aref['nums'].replace(num, "")
                            print("2912 nums0 are ", nums1)
                            aref['nums'] = str(nums1)
                            print("2914 new text is ", aref['nums'])
                            current_btn['text'] = aref['nums']

    else:
        print("2709 no set or list ", triple, type(triple))
    found_triple = False


def process_column_triple_old(col0, item, item1, item2, temp_set):
    print("1411 process_column_triple ", col0, item, item1, item2, temp_set)
    # global currentNumber
    for aref in not_done_arefs:
        current_btn = aref['btn']
        a_row = aref['row']
        a_col = aref['col']
        a_sq = aref['sq']
        a_nums = aref['nums']
        row0 = item[0]
        col0 = item[1]
        sq0 = item[2]
        nums0 = item[3]
        row1 = item1[0]
        col1 = item1[1]
        sq1 = item1[2]
        nums1 = item1[3]
        row2 = item2[0]
        col2 = item2[1]
        sq2 = item2[2]
        nums2 = item2[3]
        if (a_row == row0 and a_col == col0 and a_sq == sq0) or (a_row == row1 and a_col == col1 and a_sq == sq1) or (a_row == row2 and a_col == col2 and a_sq == sq2):
            ''' The cell is being compared with itself.'''
            print("1432 process_column_triple ", a_row, a_col, a_sq)
        elif a_col == col0:
            print("1434 process_column_triple else clause",
                  aref, a_row, a_col, a_sq, a_nums)
            for num in temp_set:
                print("1437 ", num, temp_set)
                if num in a_nums:
                    print("1439 ", num, a_nums)
                    new_nums = aref['nums'].replace(num, "")
                    print("1441 ", new_nums)
                    aref['nums'] = new_nums
                    print("1443 ", aref['nums'])
                    print("1444 ", current_btn['text'])
                    # aref['nums'].replace(num, "")  # Remove num from a_nums
                    # # current_button = aref['btn']
                    print("1446 ", current_btn, aref)
                    # bRemoveANumberFromACell = True
                    current_btn['text'] = aref['nums']

                    # currentNumber = ""
                    # update_cell(current_btn, aref)
                    print("1448 aref['nums'], a_nums ", aref['nums'], a_nums)
                else:
                    print("1450 Else fall through in triple remove number.")


def process_square_triple_Old(sq0, item, item1, item2, temp_set):
    print("1460 process_square_triple ", sq0, item, item1, item2, temp_set)
    for aref in not_done_arefs:
        current_btn = aref['btn']
        a_row = aref['row']
        a_col = aref['col']
        a_sq = aref['sq']
        a_nums = aref['nums']
        row0 = item[0]
        col0 = item[1]
        sq0 = item[2]
        nums0 = item[3]
        row1 = item1[0]
        col1 = item1[1]
        sq1 = item1[2]
        nums1 = item1[3]
        row2 = item2[0]
        col2 = item2[1]
        sq2 = item2[2]
        nums2 = item2[3]
        if (a_row == row0 and a_col == col0 and a_sq == sq0) or (a_row == row1 and a_col == col1 and a_sq == sq1) or (a_row == row2 and a_col == col2 and a_sq == sq2):
            ''' The cell is being compared with itself.'''
            print("1432 process_square_triple_Old ", a_row, a_col, a_sq)
        elif a_sq == sq0:
            print("1434 process_square_triple_Old else clause",
                  aref, a_row, a_col, a_sq, a_nums)
            for num in temp_set:
                print("1437 ", num, temp_set)
                if num in a_nums:
                    print("1439 ", num, a_nums)
                    new_nums = aref['nums'].replace(num, "")
                    print("1441 ", new_nums)
                    aref['nums'] = new_nums
                    print("1443 ", aref['nums'])
                    print("1444 ", current_btn['text'])
                    # aref['nums'].replace(num, "")  # Remove num from a_nums
                    # # current_button = aref['btn']
                    print("1446 ", current_btn, aref)
                    current_btn['text'] = aref['nums']
                    print("1448 aref['nums'], a_nums ", aref['nums'], a_nums)
                else:
                    print("1450 Else fall through in triple remove number.")


def make_quad_candidate_list():
    print("1458 enter make_triple_candidate_list")
    ex_text = ""
    temp_list = []
    temp_list_1 = []
    triple_candidate_list = []
    triple_list = []
    for cell in not_done_arefs:
        if len(cell['nums']) <= 4:
            ex_text = str(cell['row']) + ", " + str(cell['col']) + \
                ", " + str(cell['sq']) + ", " + str(cell['nums']) + "\n "
            list_ex_text = list[str(cell['row']), str(
                cell['col']), str(cell['sq']), str(cell['nums'])]
            row = cell['row']
            col = cell['col']
            sq = cell['sq']
            nums = str(cell['nums'])
            temp_list = [row, col, sq, nums]
            txt_Explain.insert(END, ex_text)
            triple_candidate_list.append(temp_list)
            temp_list = []
    return triple_candidate_list


def id_quads(triple_candidate_list):
    pass


def compare_cell_nums(nums0, nums1, nums2, tcl_set0, tcl_set1, tcl_set2):
    print("1271 enter compare_cell_nums")
    ''' Compare cell nums breaks two nums string into numbers
    and adds them to a set to see if the form a triple'''
    # print("1182 nums0, nums1 ", nums0, nums1)
    l = len(nums0)
    n1 = nums0[0]
    tcl_set0.add(n1)
    n2 = nums0[1]
    tcl_set0.add(n2)
    if l == 3:
        n3 = nums0[2]
        tcl_set0.add(n3)

    tcl_set1 = tcl_set0
    l1 = len(nums1)
    n4 = nums1[0]
    tcl_set1.add(n4)
    n5 = nums1[1]
    tcl_set1.add(n5)
    if l1 == 3:
        n6 = nums1[2]
        tcl_set1.add(n6)
    tcl_len = len(tcl_set1)
    if tcl_len > 3:
        tcl_set1 = set()
    else:
        # tcl_set2 = tcl_set1

        if nums2 != "":
            l2 = len(nums2)
            n7 = nums2[0]
            tcl_set2.add(n7)
            n8 = nums2[1]
            tcl_set2.add(n8)
            if len(tcl_set2) > 3:
                tcl_set2 = set()
            else:
                # print("1226 tcl_set2 is ", tcl_set2)
                if l2 == 3:
                    n9 = nums2[2]
                    tcl_set2.add(n9)
                if len(tcl_set2) > 3:
                    tcl_set2 = set()
                elif len(tcl_set2) == 3:
                    print("1315 tcl_set2 is ", tcl_set2)


def triple_parse_test():
    tcl = [['1', '6', '2', '8AC'], ['1', '10', '3', '6A']]
    print("1320 tcl[0] is ", tcl[0])
    # parse the first two items to test functionality of set creation
    nums = tcl[0][3]
    l = len(nums)
    tcl_set = set()
    n1 = nums[0]
    tcl_set.add(n1)
    n2 = nums[1]
    tcl_set.add(n2)
    if l == 3:
        n3 = nums[2]
        tcl_set.add(n3)
    nums1 = tcl[1][3]
    l1 = len(nums1)
    n4 = nums1[0]
    tcl_set.add(n4)
    n5 = nums1[1]
    tcl_set.add(n5)
    if l1 == 3:
        n6 = nums1[2]
        tcl_set.add(n6)
    tcl_len = len(tcl_set)
    if tcl_len > 3:
        print("1343 not a valid set")

    print("1345 tcl[0][3] is ", tcl[0][3])


def ID_Duples():
    bIDDuples = True


def ID_Triples():
    bIDTriples = True


def ID_Quads():
    bIDQuads = True


def find_Quad():
    print("3211 Entering find_Quad")
    txt_Explain.insert(END, "Find Quads is not functinal.\n")
    print("1153 Entering find_Triple")
    txt_Explain.insert(END, "Potential quads are \n")
    quad_candidate_list = make_quad_candidate_list()
    # print("1146 triple_candidate_list ", triple_candidate_list)
    id_quads(quad_candidate_list)


def make_quad_candidate_list():
    print("1716 entered make_quad_candidate_list")
    ex_text = ""
    temp_list = []
    temp_list_1 = []
    quad_candidate_list = []
    quad_list = []
    for cell in not_done_arefs:
        if len(cell['nums']) <= 4:
            # print("1011 potential triple ", cell['row'], cell['col'], cell['sq'], cell['nums'])
            ex_text = str(cell['row']) + ", " + str(cell['col']) + \
                ", " + str(cell['sq']) + ", " + str(cell['nums']) + "\n "
            list_ex_text = list[str(cell['row']), str(
                cell['col']), str(cell['sq']), str(cell['nums'])]
            row = cell['row']
            col = cell['col']
            sq = cell['sq']
            nums = str(cell['nums'])
            # temp_list = [row, col, sq, nums]
            temp_list = [row, col, sq, nums]
            # print("1169 temp_list is ", temp_list)
            # temp_list = "[" + str(cell['row']) + ", " + str(cell['col']) + ", " + str(cell['sq']) + ", " + str(cell['nums']) + "]"
            txt_Explain.insert(END, ex_text)
            # txt_Explain.insert(END, temp_list)
            # txt_Explain.insert(END, "\n")
            quad_candidate_list.append(temp_list)
            # print("1227 triple_candidate_list ", triple_candidate_list)
            temp_list = []
    # txt_Explain.insert(END, "1188\n")
    # txt_Explain.insert(END, triple_candidate_list)
    return quad_candidate_list


def id_quads(quad_candidate_list):
    txt_Explain.insert(END, "Find Quads is not functinal.\n")


def update_RCS(current_button, aref):  # Row, Column, Square):
    print("1370 Entering update_RCS ", current_button, aref)
    current_button['text'] = aref['nums']
    print("1372 in update_RCS ", current_button['text'], aref['nums'])
    # current_btn['text'] = aref['nums']

# def update_not_done_arefs(aref):
#     print("542 Entered update_not_done_arefs(aref)", aref['done'])
#     if aref['done'] == True and aref in not_done_arefs:
#         not_done_arefs.remove(aref)
#     print("545 update_not_done_arefs ", len(not_done_arefs))


def update_puzzle(row, column, square):
    print("529 update_puzzle row, column, square ",
          row, column, square, currentNumber)
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


def reset_initial_cell_values(current_btn, aref):
    aref['done'] = False
    aref['nums'] = startingString
    aref['font'] = donefont
    aref['width'] = wid6
    aref['height'] = 4
    aref['fg'] = "black"
    current_btn['width'] = aref['width']
    current_btn['width'] = aref['width']
    current_btn['text'] = aref['nums']
    current_btn['fg'] = aref['fg']


def reset_cell_values(current_btn, aref):
    '''A single number has been selected, so reset the cell values.'''
    aref['done'] = True
    aref['nums'] = currentNumber
    aref['font'] = donefont
    aref['width'] = wid6
    aref['height'] = 4
    aref['fg'] = "red"
    current_btn['width'] = aref['width']
    current_btn['text'] = aref['nums']
    current_btn['fg'] = aref['fg']
    # current_btn.config(font=donefont, width=4, height=2)
    print("2280 aref values", aref['done'], aref['nums'], aref)


def enlarge_puzzle():
    for aref in arrRefs_List:
        current_btn = aref['btn_str']
        current_btn.config(font=donefont, width=4, height=2)


def refresh_display(current_btn, aref):
    print("2082 Entered refresh_display", current_btn, aref)
    aref['nums'] = currentNumber
    current_btn['text'] = aref['nums']


def set_bRemoveANumberFromACell():
    global bRemoveANumberFromACell
    if bRemoveANumberFromACell == False:
        # set_bRemoveANumber_True()
        bRemoveANumberFromACell = True
        # btn_del_num['text'] = "Del\nnum\nact\nive"
        history = 'set_bRemoveANumberFromACell()\n'
        save_current_to_history(history)
    else:
        # set_bRemoveANumber_False()
        bRemoveANumberFromACell = False
        # btn_del_num['text'] = 'Del\nnum\nfrom\ncell'
        history = 'set_bRemoveANumber_False()\n'
        save_current_to_history(history)
    print("1728 bRemoveANumberFromACell is ", bRemoveANumberFromACell)


def set_bRemoveANumber_True():
    print("2110 set_bRemoveANumber_True")
    bRemoveANumberFromACell = True


def set_bRemoveANumber_False():
    print("2115 set_bRemoveANumber_False")
    bRemoveANumberFromACell = False


def remove_num_from_cell(current_btn, aref):
    print("1727 Entered remove_num_from_cell.")
    global currentNumber
    new_nums = aref['nums'].replace(currentNumber, "")
    print("723 new_nums ", new_nums)
    aref['nums'] = new_nums
    current_btn['text'] = aref['nums']


def remove_aref_from_not_done_arefs(aref):
    print("2346 Entered remove_aref_from_not_done_arefs.")
    if aref in not_done_arefs:
        not_done_arefs.remove(aref)
        done_arefs_list.append(aref)


def make_done_arefs():
    done_arefs_list = []
    print("2346 Entered remove_aref_from_not_done_arefs.")
    for aref in arrRefs_List:
        if aref['done'] == True:
            done_arefs_list.append(aref)
    print("2405 done arefs ", len(done_arefs_list))


def clear_text():
    txt_Explain.delete('1.0', END)  # "insert-1c", END)


def update_cell(btn, aref, btn_ID, aref_ID):
    print("2337 Entered update_cell.", type(btn), btn, type(aref), aref)
    # print("2070 Entered update_cell.", btn_ID, aref_ID)
    # print("2071 current number is ", currentNumber)
    # arrRef0 = dict(btn='btn_R1C1', row=1, col=1, sq=1,
    global bRemoveANumberFromACell
    global bIDDuples
    global bIDTriples
    global bIDQuads
    # global history
    print("2082 bRemoveANumberFromACell = ", bRemoveANumberFromACell)
    if not btn_ID == "" and bRemoveANumberFromACell == False:
        history = f"update_cell( {btn_ID}, {aref_ID}, {btn_ID}, {aref_ID})"
        txt_Explain.insert(END, history)
        txt_Explain.insert(END, "\n")
        # global history
        # history = history.append(list[currentNumber, args, aref])
        # print("2080 history is ", history)
        # print("2081 button is ", *args, currentNumber)

    # print("1756 bRemoveANumberFromACell ", bRemoveANumberFromACell)
    # print("1757 bIDDuples ", bIDDuples, bIDTriples, bIDQuads)
    # print("720 ", btn1, type(btn1))
    row = aref["row"]
    col = aref["col"]
    sq = aref["sq"]
    if bIDDuples == True:
        process_duples(btn, aref)
        # continue
    elif bIDTriples == True:
        process_triples(btn, aref)
        # continue
    elif bIDQuads == True:
        process_quads(btn, aref)
        # continue
    # print("1771 test")
    # print("724 ", btn, row, col, sq)
    # reset_cell_values(current_btn, aref)
    if bRemoveANumberFromACell == False:
        print("2159 Entered bRemoveANumberFromACell.")
        reset_cell_values(btn, aref)
        remove_aref_from_not_done_arefs(aref)
        update_puzzle(row, col, sq)
        cells_done()
        cells_remaining()

    # print("1782 test")
    # print(f"currentNumber = '{currentNumber}'")
    # print(f"update_cell'{btn}, {aref}")
    # print("1785 bRemoveANumberFromACell ", bRemoveANumberFromACell)
    if bRemoveANumberFromACell == True:
        print("1783 Entered bRemoveANumberFromACell.")
        remove_num_from_cell(btn, aref)
        set_bRemoveANumberFromACell()
        # print(f"currentNumber = '{currentNumber}'")
        # print(f"update_cell'{btn}, {aref}")
    # print("1791 test")
    # print_problem_cells()


# def test_y():
#     print("2204 R5C2 values ", arrRef65)

# def test_z():
#     pass
    # print_problem_cells()

def print_problem_cells():
    print("2204 R5C2 values ", arrRef65['done'], arrRef65['nums'])
    print("2205 R5C6 values ", arrRef69['done'], arrRef69['nums'])
    print("2206 R6C7 values ", arrRef86['done'], arrRef86['nums'])
    print("2207 R11C2 values ", arrRef161['done'], arrRef161['nums'])
    print("2208 len(not_done_arefs) ", len(not_done_arefs))
    # print("2209 cells_remaining_num is ", cells_remaining_num)
    for cell in not_done_arefs:
        if cell == arrRef69:
            print("2205 R5C6 values ", arrRef69['done'], arrRef69['nums'])


def process_duples(btn, aref):
    duples_list.append(btn, aref)
    if len(duples_list) != 0:
        print(duples_list)


def process_triples(btn, aref):
    triple_list.append(btn, aref)
    if len(triple_list) != 0:
        print(triple_list)
    triple_list = []


def process_quads(btn, aref):
    quads_list.append(btn, aref)
    if len(quads_list) != 0:
        print(quads_list)


def find_only_num_in_row_or_col_in_square():
    ''' Make a set of all numbers in a square
    Convert that set to an ordered list of numbers'''
    '''For each number in that list, create
    a row set and a column set.
    E.G. 3_row_set, 3_col_set, 7_row_set, 7_col_set, etc.'''
    '''For each not_done cell in the square,
          for each number in the cell
             add that number to the row and col sets
             '''
    '''For each row and col set, if the set.length == 1
       check every not_done cell in that row/col
       If the number is in that cell, remove the number.
       Print the results.'''


def update_R1C1():
    print("2207 R1C1 button pressed.")
    ''' A number has been set by a number button,
        either set that number as the value of the cell in aref['nums'],
        or, if bRemoveANumberFromACell == True,
        remove the number from the current numbers.'''
    update_cell(btn_R1C1, arrRef0, 'btn_R1C1', 'arrRef0')


def update_R1C2():
    print("R1C2 button pressed.")
    update_cell(btn_R1C2, arrRef1, 'btn_R1C2', 'arrRef1')


def update_R1C3():
    print("R1C3 button pressed.")
    update_cell(btn_R1C3, arrRef2, 'btn_R1C3', 'arrRef2')


def update_R1C4():
    print("R1C4 button pressed.")
    update_cell(btn_R1C4, arrRef3, 'btn_R1C4', 'arrRef3')


def update_R1C5():
    print("R1C5 button pressed.")
    update_cell(btn_R1C5, arrRef4, 'btn_R1C5', 'arrRef4')


def update_R1C6():
    print("R1C6 button pressed.")
    update_cell(btn_R1C6, arrRef5, 'btn_R1C6', 'arrRef5')


def update_R1C7():
    print("R1C7 button pressed.")
    update_cell(btn_R1C7, arrRef6, 'btn_R1C7', 'arrRef6')


def update_R1C8():
    print("R1C8 button pressed.")
    update_cell(btn_R1C8, arrRef7, 'btn_R1C8', 'arrRef7')


def update_R1C9():
    print("R1C9 button pressed.")
    update_cell(btn_R1C9, arrRef8, 'btn_R1C9', 'arrRef8')


def update_R1C10():
    print("R1C10 button pressed.")
    update_cell(btn_R1C10, arrRef9, 'btn_R1C10', 'arrRef9')


def update_R1C11():
    print("R1C11 button pressed.")
    update_cell(btn_R1C11, arrRef10, 'btn_R1C11', 'arrRef10')


def update_R1C12():
    print("R1C12 button pressed.")
    update_cell(btn_R1C12, arrRef11, 'btn_R1C12', 'arrRef11')


def update_R1C13():
    print("R1C13 button pressed.")
    update_cell(btn_R1C13, arrRef12, 'btn_R1C13', 'arrRef12')


def update_R1C14():
    print("R1C14 button pressed.")
    update_cell(btn_R1C14, arrRef13, 'btn_R1C14', 'arrRef13')


def update_R1C15():
    print("R1C15 button pressed.")
    update_cell(btn_R1C15, arrRef14, 'btn_R1C15', 'arrRef14')


def update_R1C16():
    print("R2C16 button pressed.")
    update_cell(btn_R1C16, arrRef15, 'btn_R1C16', 'arrRef15')


def update_R2C1():
    print("R2C1 button pressed.")
    update_cell(btn_R2C1, arrRef16, 'btn_R2C1', 'arrRef16')


def update_R2C2():
    print("R2C2 button pressed.")
    update_cell(btn_R2C2, arrRef17, 'btn_R2C2', 'arrRef17')


def update_R2C3():
    print("R2C3 button pressed.")
    update_cell(btn_R2C3, arrRef18, 'btn_R2C3', 'arrRef18')


def update_R2C4():
    print("R2C4 button pressed.")
    update_cell(btn_R2C4, arrRef19, 'btn_R2C4', 'arrRef19')


def update_R2C5():
    print("R2C5 button pressed.")
    update_cell(btn_R2C5, arrRef20, 'btn_R2C5', 'arrRef20')


def update_R2C6():
    print("R2C6 button pressed.")
    update_cell(btn_R2C6, arrRef21, 'btn_R2C6', 'arrRef21')


def update_R2C7():
    print("R2C7 button pressed.")
    update_cell(btn_R2C7, arrRef22, 'btn_R2C7', 'arrRef22')


def update_R2C8():
    print("R2C8 button pressed.")
    update_cell(btn_R2C8, arrRef23, 'btn_R2C8', 'arrRef23')


def update_R2C9():
    print("R2C9 button pressed.")
    update_cell(btn_R2C9, arrRef24, 'btn_R2C9', 'arrRef24')


def update_R2C10():
    print("R2C10 button pressed.")
    update_cell(btn_R2C10, arrRef25, 'btn_R2C10', 'arrRef25')


def update_R2C11():
    print("R2C11 button pressed.")
    update_cell(btn_R2C11, arrRef26, 'btn_R2C11', 'arrRef26')


def update_R2C12():
    print("R2C12 button pressed.")
    update_cell(btn_R2C12, arrRef27, 'btn_R2C12', 'arrRef27')


def update_R2C13():
    print("R2C13 button pressed.")
    update_cell(btn_R2C13, arrRef28, 'btn_R2C13', 'arrRef28')


def update_R2C14():
    print("R2C14 button pressed.")
    update_cell(btn_R2C14, arrRef29, 'btn_R2C14', 'arrRef29')


def update_R2C15():
    print("R2C15 button pressed.")
    update_cell(btn_R2C15, arrRef30, 'btn_R2C15', 'arrRef30')


def update_R2C16():
    print("R2C16 button pressed.")
    update_cell(btn_R2C16, arrRef31, 'btn_R2C16', 'arrRef31')


def update_R3C1():
    print("R3C1 button pressed.")
    update_cell(btn_R3C1, arrRef32, 'btn_R3C1', 'arrRef32')


def update_R3C2():
    print("R3C2 button pressed.")
    update_cell(btn_R3C2, arrRef33, 'btn_R3C2', 'arrRef33')


def update_R3C3():
    print("R3C3 button pressed.")
    update_cell(btn_R3C3, arrRef34, 'btn_R3C3', 'arrRef34')


def update_R3C4():
    print("R3C4 button pressed.")
    update_cell(btn_R3C4, arrRef35, 'btn_R3C4', 'arrRef35')


def update_R3C5():
    print("R3C5 button pressed.")
    update_cell(btn_R3C5, arrRef36, 'btn_R3C5', 'arrRef36')


def update_R3C6():
    print("R3C6 button pressed.")
    update_cell(btn_R3C6, arrRef37, 'btn_R3C6', 'arrRef37')


def update_R3C7():
    print("R3C7 button pressed.")
    update_cell(btn_R3C7, arrRef38, 'btn_R3C7', 'arrRef38')


def update_R3C8():
    print("R3C8 button pressed.")
    update_cell(btn_R3C8, arrRef39, 'btn_R3C8', 'arrRef39')


def update_R3C9():
    print("R3C9 button pressed.")
    update_cell(btn_R3C9, arrRef40, 'btn_R3C9', 'arrRef40')


def update_R3C10():
    print("R3C10 button pressed.")
    update_cell(btn_R3C10, arrRef41, 'btn_R3C10', 'arrRef41')


def update_R3C11():
    print("R3C11 button pressed.")
    update_cell(btn_R3C11, arrRef42, 'btn_R3C11', 'arrRef42')


def update_R3C12():
    print("R3C12 button pressed.")
    update_cell(btn_R3C12, arrRef43, 'btn_R3C12', 'arrRef43')


def update_R3C13():
    print("R3C13 button pressed.")
    update_cell(btn_R3C13, arrRef44, 'btn_R3C13', 'arrRef44')


def update_R3C14():
    print("R3C14 button pressed.")
    update_cell(btn_R3C14, arrRef45, 'btn_R3C14', 'arrRef45')


def update_R3C15():
    print("R3C15 button pressed.")
    update_cell(btn_R3C15, arrRef46, 'btn_R3C15', 'arrRef46')


def update_R3C16():
    print("R3C16 button pressed.")
    update_cell(btn_R3C16, arrRef47, 'btn_R3C16', 'arrRef47')


def update_R4C1():
    print("R4C1 button pressed.")
    update_cell(btn_R4C1, arrRef48, 'btn_R4C1', 'arrRef48')


def update_R4C2():
    print("R4C2 button pressed.")
    update_cell(btn_R4C2, arrRef49, 'btn_R4C2', 'arrRef49')


def update_R4C3():
    print("R4C3 button pressed.")
    update_cell(btn_R4C3, arrRef50, 'btn_R4C3', 'arrRef50')


def update_R4C4():
    print("R4C4 button pressed.")
    update_cell(btn_R4C4, arrRef51, 'btn_R4C4', 'arrRef51')


def update_R4C5():
    print("R4C5 button pressed.")
    update_cell(btn_R4C5, arrRef52, 'btn_R4C5', 'arrRef52')


def update_R4C6():
    print("R4C6 button pressed.")
    update_cell(btn_R4C6, arrRef53, 'btn_R4C6', 'arrRef53')


def update_R4C7():
    print("R4C7 button pressed.")
    update_cell(btn_R4C7, arrRef54, 'btn_R4C7', 'arrRef54')


def update_R4C8():
    print("R4C8 button pressed.")
    update_cell(btn_R4C8, arrRef55, 'btn_R4C8', 'arrRef55')


def update_R4C9():
    print("R4C9 button pressed.")
    update_cell(btn_R4C9, arrRef56, 'btn_R4C9', 'arrRef56')


def update_R4C10():
    print("R4C10 button pressed.")
    update_cell(btn_R4C10, arrRef57, 'btn_R4C10', 'arrRef57')


def update_R4C11():
    print("R4C11 button pressed.")
    update_cell(btn_R4C11, arrRef58, 'btn_R4C11', 'arrRef58')


def update_R4C12():
    print("R4C12 button pressed.")
    update_cell(btn_R4C12, arrRef59, 'btn_R4C12', 'arrRef59')


def update_R4C13():
    print("R4C13 button pressed.")
    update_cell(btn_R4C13, arrRef60, 'btn_R4C13', 'arrRef60')


def update_R4C14():
    print("R4C14 button pressed.")
    update_cell(btn_R4C14, arrRef61, 'btn_R4C14', 'arrRef61')


def update_R4C15():
    print("R4C15 button pressed.")
    update_cell(btn_R4C15, arrRef62, 'btn_R4C15', 'arrRef62')


def update_R4C16():
    print("R4C16 button pressed.")
    update_cell(btn_R4C16, arrRef63, 'btn_R4C16', 'arrRef63')


def update_R5C1():
    print("R5C1 button pressed.")
    update_cell(btn_R5C1, arrRef64, 'btn_R5C1', 'arrRef64')


def update_R5C2():
    print("R5C2 button pressed.")
    update_cell(btn_R5C2, arrRef65, 'btn_R5C2', 'arrRef65')


def update_R5C3():
    print("R5C3 button pressed.")
    update_cell(btn_R5C3, arrRef66, 'btn_R5C3', 'arrRef66')


def update_R5C4():
    print("R5C4 button pressed.")
    update_cell(btn_R5C4, arrRef67, 'btn_R5C4', 'arrRef67')


def update_R5C5():
    print("R5C5 button pressed.")
    update_cell(btn_R5C5, arrRef68, 'btn_R5C5', 'arrRef68')


def update_R5C6():
    print("R5C6 button pressed.")
    update_cell(btn_R5C6, arrRef69, 'btn_R5C6', 'arrRef69')


def update_R5C7():
    print("R5C7 button pressed.")
    update_cell(btn_R5C7, arrRef70, 'btn_R5C7', 'arrRef70')


def update_R5C8():
    print("R5C8 button pressed.")
    update_cell(btn_R5C8, arrRef71, 'btn_R5C8', 'arrRef71')


def update_R5C9():
    print("R5C9 button pressed.")
    update_cell(btn_R5C9, arrRef72, 'btn_R5C9', 'arrRef72')


def update_R5C10():
    print("R5C10 button pressed.")
    update_cell(btn_R5C10, arrRef73, 'btn_R5C10', 'arrRef73')


def update_R5C11():
    print("R5C11 button pressed.")
    update_cell(btn_R5C11, arrRef74, 'btn_R5C11', 'arrRef74')


def update_R5C12():
    print("R5C12 button pressed.")
    update_cell(btn_R5C12, arrRef75, 'btn_R5C12', 'arrRef75')


def update_R5C13():
    print("R5C13 button pressed.")
    update_cell(btn_R5C13, arrRef76, 'btn_R5C13', 'arrRef76')


def update_R5C14():
    print("R5C14 button pressed.")
    update_cell(btn_R5C14, arrRef77, 'btn_R5C14', 'arrRef77')


def update_R5C15():
    print("R5C15 button pressed.")
    update_cell(btn_R5C15, arrRef78, 'btn_R5C15', 'arrRef78')


def update_R5C16():
    print("R5C16 button pressed.")
    update_cell(btn_R5C16, arrRef79, 'btn_R5C16', 'arrRef79')


def update_R6C1():
    print("R6C1 button pressed.")
    update_cell(btn_R6C1, arrRef80, 'btn_R6C1', 'arrRef80')


def update_R6C2():
    print("R6C2 button pressed.")
    update_cell(btn_R6C2, arrRef81, 'btn_R6C2', 'arrRef81')


def update_R6C3():
    print("R6C3 button pressed.")
    update_cell(btn_R6C3, arrRef82, 'btn_R6C3', 'arrRef82')


def update_R6C4():
    print("R6C4 button pressed.")
    update_cell(btn_R6C4, arrRef83, 'btn_R6C4', 'arrRef83')


def update_R6C5():
    print("R6C5 button pressed.")
    update_cell(btn_R6C5, arrRef84, 'btn_R6C5', 'arrRef84')


def update_R6C6():
    print("R6C6 button pressed.")
    update_cell(btn_R6C6, arrRef85, 'btn_R6C6', 'arrRef85')


def update_R6C7():
    print("R6C7 button pressed.")
    update_cell(btn_R6C7, arrRef86, 'btn_R6C7', 'arrRef86')


def update_R6C8():
    print("R6C8 button pressed.")
    update_cell(btn_R6C8, arrRef87, 'btn_R6C8', 'arrRef87')


def update_R6C9():
    print("R6C9 button pressed.")
    update_cell(btn_R6C9, arrRef88, 'btn_R6C9', 'arrRef88')


def update_R6C10():
    print("R6C10 button pressed.")
    update_cell(btn_R6C10, arrRef89, 'btn_R6C10', 'arrRef89')


def update_R6C11():
    print("R6C11 button pressed.")
    update_cell(btn_R6C11, arrRef90, 'btn_R6C11', 'arrRef90')


def update_R6C12():
    print("R6C12 button pressed.")
    update_cell(btn_R6C12, arrRef91, 'btn_R6C12', 'arrRef91')


def update_R6C13():
    print("R6C13 button pressed.")
    update_cell(btn_R6C13, arrRef92, 'btn_R6C13', 'arrRef92')


def update_R6C14():
    print("R6C14 button pressed.")
    update_cell(btn_R6C14, arrRef93, 'btn_R6C14', 'arrRef93')


def update_R6C15():
    print("R6C15 button pressed.")
    update_cell(btn_R6C15, arrRef94, 'btn_R6C15', 'arrRef94')


def update_R6C16():
    print("R6C16 button pressed.")
    update_cell(btn_R6C16, arrRef95, 'btn_R6C16', 'arrRef95')


def update_R7C1():
    print("R7C1 button pressed.")
    update_cell(btn_R7C1, arrRef96, 'btn_R7C1', 'arrRef96')


def update_R7C2():
    print("R7C2 button pressed.")
    update_cell(btn_R7C2, arrRef97, 'btn_R7C2', 'arrRef97')


def update_R7C3():
    print("R7C3 button pressed.")
    update_cell(btn_R7C3, arrRef98, 'btn_R7C3', 'arrRef98')


def update_R7C4():
    print("R7C4 button pressed.")
    update_cell(btn_R7C4, arrRef99, 'btn_R7C4', 'arrRef99')


def update_R7C5():
    print("R7C5 button pressed.")
    update_cell(btn_R7C5, arrRef100, 'btn_R7C5', 'arrRef100')


def update_R7C6():
    print("R7C6 button pressed.")
    update_cell(btn_R7C6, arrRef101, 'btn_R7C6', 'arrRef101')


def update_R7C7():
    print("R7C7 button pressed.")
    update_cell(btn_R7C7, arrRef102, 'btn_R7C7', 'arrRef102')


def update_R7C8():
    print("R7C8 button pressed.")
    update_cell(btn_R7C8, arrRef103, 'btn_R7C8', 'arrRef103')


def update_R7C9():
    print("R7C9 button pressed.")
    update_cell(btn_R7C9, arrRef104, 'btn_R7C9', 'arrRef104')


def update_R7C10():
    print("R7C10 button pressed.")
    update_cell(btn_R7C10, arrRef105, 'btn_R7C10', 'arrRef105')


def update_R7C11():
    print("R7C11 button pressed.")
    update_cell(btn_R7C11, arrRef106, 'btn_R7C11', 'arrRef106')


def update_R7C12():
    print("R7C12 button pressed.")
    update_cell(btn_R7C12, arrRef107, 'btn_R7C12', 'arrRef107')


def update_R7C13():
    print("R7C13 button pressed.")
    update_cell(btn_R7C13, arrRef108, 'btn_R7C13', 'arrRef108')


def update_R7C14():
    print("R7C14 button pressed.")
    update_cell(btn_R7C14, arrRef109, 'btn_R7C14', 'arrRef109')


def update_R7C15():
    print("R7C15 button pressed.")
    update_cell(btn_R7C15, arrRef110, 'btn_R7C15', 'arrRef110')


def update_R7C16():
    print("R7C16 button pressed.")
    update_cell(btn_R7C16, arrRef111, 'btn_R7C16', 'arrRef111')


def update_R8C1():
    print("R8C1 button pressed.")
    update_cell(btn_R8C1, arrRef112, 'btn_R8C1', 'arrRef112')


def update_R8C2():
    print("R8C2 button pressed.")
    update_cell(btn_R8C2, arrRef113, 'btn_R8C2', 'arrRef113')


def update_R8C3():
    print("R8C3 button pressed.")
    update_cell(btn_R8C3, arrRef114, 'btn_R8C3', 'arrRef114')


def update_R8C4():
    print("R8C4 button pressed.")
    update_cell(btn_R8C4, arrRef115, 'btn_R8C4', 'arrRef115')


def update_R8C5():
    print("R8C5 button pressed.")
    update_cell(btn_R8C5, arrRef116, 'btn_R8C5', 'arrRef116')


def update_R8C6():
    print("R8C6 button pressed.")
    update_cell(btn_R8C6, arrRef117, 'btn_R8C6', 'arrRef117')


def update_R8C7():
    print("R8C7 button pressed.")
    update_cell(btn_R8C7, arrRef118, 'btn_R8C7', 'arrRef118')


def update_R8C8():
    print("R8C8 button pressed.")
    update_cell(btn_R8C8, arrRef119, 'btn_R8C8', 'arrRef119')


def update_R8C9():
    print("R8C9 button pressed.")
    update_cell(btn_R8C9, arrRef120, 'btn_R8C9', 'arrRef120')


def update_R8C10():
    print("R8C10 button pressed.")
    update_cell(btn_R8C10, arrRef121, 'btn_R8C10', 'arrRef121')


def update_R8C11():
    print("R8C11 button pressed.")
    update_cell(btn_R8C11, arrRef122, 'btn_R8C11', 'arrRef122')


def update_R8C12():
    print("R8C12 button pressed.")
    update_cell(btn_R8C12, arrRef123, 'btn_R8C12', 'arrRef123')


def update_R8C13():
    print("R7C13 button pressed.")
    update_cell(btn_R8C13, arrRef124, 'btn_R8C13', 'arrRef124')


def update_R8C14():
    print("R8C14 button pressed.")
    update_cell(btn_R8C14, arrRef125, 'btn_R8C14', 'arrRef125')


def update_R8C15():
    print("R8C15 button pressed.")
    update_cell(btn_R8C15, arrRef126, 'btn_R8C15', 'arrRef126')


def update_R8C16():
    print("R8C16 button pressed.")
    update_cell(btn_R8C16, arrRef127, 'btn_R8C16', 'arrRef127')


def update_R9C1():
    print("R9C1 button pressed.")
    update_cell(btn_R9C1, arrRef128, 'btn_R9C1', 'arrRef128')


def update_R9C2():
    print("R9C2 button pressed.")
    update_cell(btn_R9C2, arrRef129, 'btn_R9C2', 'arrRef129')


def update_R9C3():
    print("R9C3 button pressed.")
    update_cell(btn_R9C3, arrRef130, 'btn_R9C3', 'arrRef130')


def update_R9C4():
    print("R9C4 button pressed.")
    update_cell(btn_R9C4, arrRef131, 'btn_R9C4', 'arrRef131')


def update_R9C5():
    print("R9C5 button pressed.")
    update_cell(btn_R9C5, arrRef132, 'btn_R9C5', 'arrRef132')


def update_R9C6():
    print("R9C6 button pressed.")
    update_cell(btn_R9C6, arrRef133, 'btn_R9C6', 'arrRef133')


def update_R9C7():
    print("R9C7 button pressed.")
    update_cell(btn_R9C7, arrRef134, 'btn_R9C7', 'arrRef134')


def update_R9C8():
    print("R9C8 button pressed.")
    update_cell(btn_R9C8, arrRef135, 'btn_R9C8', 'arrRef135')


def update_R9C9():
    print("R9C9 button pressed.")
    update_cell(btn_R9C9, arrRef136, 'btn_R9C9', 'arrRef136')


def update_R9C10():
    print("R9C10 button pressed.")
    update_cell(btn_R9C10, arrRef137, 'btn_R9C10', 'arrRef137')


def update_R9C11():
    print("R9C11 button pressed.")
    update_cell(btn_R9C11, arrRef138, 'btn_R9C11', 'arrRef138')


def update_R9C12():
    print("R9C12 button pressed.")
    update_cell(btn_R9C12, arrRef139, 'btn_R9C12', 'arrRef139')


def update_R9C13():
    print("R9C13 button pressed.")
    update_cell(btn_R9C13, arrRef140, 'btn_R9C13', 'arrRef140')


def update_R9C14():
    print("R9C14 button pressed.")
    update_cell(btn_R9C14, arrRef141, 'btn_R9C14', 'arrRef141')


def update_R9C15():
    print("R9C15 button pressed.")
    update_cell(btn_R9C15, arrRef142, 'btn_R9C15', 'arrRef142')


def update_R9C16():
    print("R7C16 button pressed.")
    update_cell(btn_R9C16, arrRef143, 'btn_R9C16', 'arrRef143')


def update_R10C1():
    print("R10C1 button pressed.")
    update_cell(btn_R10C1, arrRef144, 'btn_R10C1', 'arrRef144')


def update_R10C2():
    print("R10C2 button pressed.")
    update_cell(btn_R10C2, arrRef145, 'btn_R10C2', 'arrRef145')


def update_R10C3():
    print("R10C3 button pressed.")
    update_cell(btn_R10C3, arrRef146, 'btn_R10C3', 'arrRef146')


def update_R10C4():
    print("R10C4 button pressed.")
    update_cell(btn_R10C4, arrRef147, 'btn_R10C4', 'arrRef147')


def update_R10C5():
    print("R10C5 button pressed.")
    update_cell(btn_R10C5, arrRef148, 'btn_R10C5', 'arrRef148')


def update_R10C6():
    print("R10C6 button pressed.")
    update_cell(btn_R10C6, arrRef149, 'btn_R10C6', 'arrRef149')


def update_R10C7():
    print("R10C7 button pressed.")
    update_cell(btn_R10C7, arrRef150, 'btn_R10C7', 'arrRef150')


def update_R10C8():
    print("R10C8 button pressed.")
    update_cell(btn_R10C8, arrRef151, 'btn_R10C8', 'arrRef151')


def update_R10C9():
    print("R10C9 button pressed.")
    update_cell(btn_R10C9, arrRef152, 'btn_R10C9', 'arrRef152')


def update_R10C10():
    print("R10C10 button pressed.")
    update_cell(btn_R10C10, arrRef153, 'btn_R10C10', 'arrRef153')


def update_R10C11():
    print("R10C11 button pressed.")
    update_cell(btn_R10C11, arrRef154, 'btn_R10C11', 'arrRef154')


def update_R10C12():
    print("R10C12 button pressed.")
    update_cell(btn_R10C12, arrRef155, 'btn_R10C12', 'arrRef155')


def update_R10C13():
    print("R10C13 button pressed.")
    update_cell(btn_R10C13, arrRef156, 'btn_R10C13', 'arrRef156')


def update_R10C14():
    print("R10C14 button pressed.")
    update_cell(btn_R10C14, arrRef157, 'btn_R10C14', 'arrRef157')


def update_R10C15():
    print("R10C15 button pressed.")
    update_cell(btn_R10C15, arrRef158, 'btn_R10C15', 'arrRef158')


def update_R10C16():
    print("R10C16 button pressed.")
    update_cell(btn_R10C16, arrRef159, 'btn_R10C16', 'arrRef159')


def update_R11C1():
    print("R11C1 button pressed.")
    update_cell(btn_R11C1, arrRef160, 'btn_R11C1', 'arrRef160')


def update_R11C2():
    print("R11C2 button pressed.")
    update_cell(btn_R11C2, arrRef161, 'btn_R11C2', 'arrRef161')


def update_R11C3():
    print("R11C3 button pressed.")
    update_cell(btn_R11C3, arrRef162, 'btn_R11C3', 'arrRef162')


def update_R11C4():
    update_cell(btn_R11C4, arrRef163, 'btn_R11C4', 'arrRef163')


def update_R11C5():
    print("R11C5 button pressed.")
    update_cell(btn_R11C5, arrRef164, 'btn_R11C5', 'arrRef164')


def update_R11C6():
    print("R11C6 button pressed.")
    update_cell(btn_R11C6, arrRef165, 'btn_R11C6', 'arrRef165')


def update_R11C7():
    print("R11C7 button pressed.")
    update_cell(btn_R11C7, arrRef166, 'btn_R11C7', 'arrRef166')


def update_R11C8():
    print("R11C8 button pressed.")
    update_cell(btn_R11C8, arrRef167, 'btn_R11C8', 'arrRef167')


def update_R11C9():
    print("R11C9 button pressed.")
    update_cell(btn_R11C9, arrRef168, 'btn_R11C9', 'arrRef168')


def update_R11C10():
    print("R11C10 button pressed.")
    update_cell(btn_R11C10, arrRef169, 'btn_R11C10', 'arrRef169')


def update_R11C11():
    print("R11C11 button pressed.")
    update_cell(btn_R11C11, arrRef170, 'btn_R11C11', 'arrRef170')


def update_R11C12():
    print("R11C12 button pressed.")
    update_cell(btn_R11C12, arrRef171, 'btn_R11C12', 'arrRef171')


def update_R11C13():
    print("R11C13 button pressed.")
    update_cell(btn_R11C13, arrRef172, 'btn_R11C13', 'arrRef172')


def update_R11C14():
    print("R11C14 button pressed.")
    update_cell(btn_R11C14, arrRef173, 'btn_R11C14', 'arrRef173')


def update_R11C15():
    print("R11C15 button pressed.")
    update_cell(btn_R11C15, arrRef174, 'btn_R11C15', 'arrRef174')


def update_R11C16():
    print("R11C16 button pressed.")
    update_cell(btn_R11C16, arrRef175, 'btn_R11C16', 'arrRef175')


def update_R12C1():
    print("R12C1 button pressed.")
    update_cell(btn_R12C1, arrRef176, 'btn_R12C1', 'arrRef176')


def update_R12C2():
    print("R12C2 button pressed.")
    update_cell(btn_R12C2, arrRef177, 'btn_R12C2', 'arrRef177')


def update_R12C3():
    print("R12C3 button pressed.")
    update_cell(btn_R12C3, arrRef178, 'btn_R12C3', 'arrRef178')


def update_R12C4():
    print("R12C4 button pressed.")
    update_cell(btn_R12C4, arrRef179, 'btn_R12C4', 'arrRef179')


def update_R12C5():
    print("R12C5 button pressed.")
    update_cell(btn_R12C5, arrRef180, 'btn_R12C5', 'arrRef180')


def update_R12C6():
    print("R12C6 button pressed.")
    update_cell(btn_R12C6, arrRef181, 'btn_R12C6', 'arrRef181')


def update_R12C7():
    print("R12C7 button pressed.")
    update_cell(btn_R12C7, arrRef182, 'btn_R12C7', 'arrRef182')


def update_R12C8():
    print("R12C8 button pressed.")
    update_cell(btn_R12C8, arrRef183, 'btn_R12C8', 'arrRef183')


def update_R12C9():
    print("R12C9 button pressed.")
    update_cell(btn_R12C9, arrRef184, 'btn_R12C9', 'arrRef184')


def update_R12C10():
    print("R12C10 button pressed.")
    update_cell(btn_R12C10, arrRef185, 'btn_R12C10', 'arrRef185')


def update_R12C11():
    print("R12C11 button pressed.")
    update_cell(btn_R12C11, arrRef186, 'btn_R12C11', 'arrRef186')


def update_R12C12():
    print("R12C12 button pressed.")
    update_cell(btn_R12C12, arrRef187, 'btn_R12C12', 'arrRef187')


def update_R12C13():
    print("R12C13 button pressed.")
    update_cell(btn_R12C13, arrRef188, 'btn_R12C13', 'arrRef188')


def update_R12C14():
    print("R12C14 button pressed.")
    update_cell(btn_R12C14, arrRef189, 'btn_R12C14', 'arrRef189')


def update_R12C15():
    print("R12C15 button pressed.")
    update_cell(btn_R12C15, arrRef190, 'btn_R12C15', 'arrRef190')


def update_R12C16():
    print("R12C16 button pressed.")
    update_cell(btn_R12C16, arrRef191, 'btn_R12C16', 'arrRef191')


def update_R13C1():
    print("R13C1 button pressed.")
    update_cell(btn_R13C1, arrRef192, 'btn_R13C1', 'arrRef192')


def update_R13C2():
    print("R13C2 button pressed.")
    update_cell(btn_R13C2, arrRef193, 'btn_R13C2', 'arrRef193')


def update_R13C3():
    print("R13C3 button pressed.")
    update_cell(btn_R13C3, arrRef194, 'btn_R13C3', 'arrRef194')


def update_R13C4():
    print("R13C4 button pressed.")
    update_cell(btn_R13C4, arrRef195, 'btn_R13C4', 'arrRef195')


def update_R13C5():
    print("R13C5 button pressed.")
    update_cell(btn_R13C5, arrRef196, 'btn_R13C5', 'arrRef196')


def update_R13C6():
    print("R13C6 button pressed.")
    update_cell(btn_R13C6, arrRef197, 'btn_R13C6', 'arrRef197')


def update_R13C7():
    print("R13C7 button pressed.")
    update_cell(btn_R13C7, arrRef198, 'btn_R13C7', 'arrRef198')


def update_R13C8():
    print("R13C8 button pressed.")
    update_cell(btn_R13C8, arrRef199, 'btn_R13C8', 'arrRef199')


def update_R13C9():
    print("R13C9 button pressed.")
    update_cell(btn_R13C9, arrRef200, 'btn_R13C9', 'arrRef200')


def update_R13C10():
    print("R13C10 button pressed.")
    update_cell(btn_R13C10, arrRef201, 'btn_R13C10', 'arrRef201')


def update_R13C11():
    print("R13C11 button pressed.")
    update_cell(btn_R13C11, arrRef202, 'btn_R13C11', 'arrRef202')


def update_R13C12():
    print("R13C12 button pressed.")
    update_cell(btn_R13C12, arrRef203, 'btn_R13C12', 'arrRef203')


def update_R13C13():
    print("R13C13 button pressed.")
    update_cell(btn_R13C13, arrRef204, 'btn_R13C13', 'arrRef204')


def update_R13C14():
    print("R13C14 button pressed.")
    update_cell(btn_R13C14, arrRef205, 'btn_R13C14', 'arrRef205')


def update_R13C15():
    print("R13C15 button pressed.")
    update_cell(btn_R13C15, arrRef206, 'btn_R13C15', 'arrRef206')


def update_R13C16():
    print("R13C16 button pressed.")
    update_cell(btn_R13C16, arrRef207, 'btn_R13C16', 'arrRef207')


def update_R14C1():
    print("R14C1 button pressed.")
    update_cell(btn_R14C1, arrRef208, 'btn_R14C1', 'arrRef208')


def update_R14C2():
    print("R14C2 button pressed.")
    update_cell(btn_R14C2, arrRef209, 'btn_R14C2', 'arrRef209')


def update_R14C3():
    print("R14C3 button pressed.")
    update_cell(btn_R14C3, arrRef210, 'btn_R14C3', 'arrRef210')


def update_R14C4():
    print("R14C4 button pressed.")
    update_cell(btn_R14C4, arrRef211, 'btn_R14C4', 'arrRef211')


def update_R14C5():
    print("R14C5 button pressed.")
    update_cell(btn_R14C5, arrRef212, 'btn_R14C5', 'arrRef212')


def update_R14C6():
    print("R14C6 button pressed.")
    update_cell(btn_R14C6, arrRef213, 'btn_R14C6', 'arrRef213')


def update_R14C7():
    print("R14C7 button pressed.")
    update_cell(btn_R14C7, arrRef214, 'btn_R14C7', 'arrRef214')


def update_R14C8():
    print("R14C8 button pressed.")
    update_cell(btn_R14C8, arrRef215, 'btn_R14C8', 'arrRef215')


def update_R14C9():
    print("R14C9 button pressed.")
    update_cell(btn_R14C9, arrRef216, 'btn_R14C9', 'arrRef216')


def update_R14C10():
    print("R14C10 button pressed.")
    update_cell(btn_R14C10, arrRef217, 'btn_R14C10', 'arrRef217')


def update_R14C11():
    print("R14C11 button pressed.")
    update_cell(btn_R14C11, arrRef218, 'btn_R14C11', 'arrRef218')


def update_R14C12():
    print("R14C12 button pressed.")
    update_cell(btn_R14C12, arrRef219, 'btn_R14C12', 'arrRef219')


def update_R14C13():
    print("R14C13 button pressed.")
    update_cell(btn_R14C13, arrRef220, 'btn_R14C13', 'arrRef220')


def update_R14C14():
    print("R14C14 button pressed.")
    update_cell(btn_R14C14, arrRef221, 'btn_R14C14', 'arrRef221')


def update_R14C15():
    print("R14C15 button pressed.")
    update_cell(btn_R14C15, arrRef222, 'btn_R14C15', 'arrRef222')


def update_R14C16():
    print("R14C16 button pressed.")
    update_cell(btn_R14C16, arrRef223, 'btn_R14C16', 'arrRef223')


def update_R15C1():
    print("R15C1 button pressed.")
    update_cell(btn_R15C1, arrRef224, 'btn_R15C1', 'arrRef224')


def update_R15C2():
    print("R15C2 button pressed.")
    update_cell(btn_R15C2, arrRef225, 'btn_R15C2', 'arrRef225')


def update_R15C3():
    print("R15C3 button pressed.")
    update_cell(btn_R15C3, arrRef226, 'btn_R15C3', 'arrRef226')


def update_R15C4():
    print("R15C4 button pressed.")
    update_cell(btn_R15C4, arrRef227, 'btn_R15C4', 'arrRef227')


def update_R15C5():
    print("R15C5 button pressed.")
    update_cell(btn_R15C5, arrRef228, 'btn_R15C5', 'arrRef228')


def update_R15C6():
    print("R15C6 button pressed.")
    update_cell(btn_R15C6, arrRef229, 'btn_R15C6', 'arrRef229')


def update_R15C7():
    print("R15C7 button pressed.")
    update_cell(btn_R15C7, arrRef230, 'btn_R15C7', 'arrRef230')


def update_R15C8():
    print("R15C8 button pressed.")
    update_cell(btn_R15C8, arrRef231, 'btn_R15C8', 'arrRef231')


def update_R15C9():
    print("R15C9 button pressed.")
    update_cell(btn_R15C9, arrRef232, 'btn_R15C9', 'arrRef232')


def update_R15C10():
    print("R15C10 button pressed.")
    update_cell(btn_R15C10, arrRef233, 'btn_R15C10', 'arrRef233')


def update_R15C11():
    print("R15C11 button pressed.")
    update_cell(btn_R15C11, arrRef234, 'btn_R15C11', 'arrRef234')


def update_R15C12():
    print("R15C12 button pressed.")
    update_cell(btn_R15C12, arrRef235, 'btn_R15C12', 'arrRef235')


def update_R15C13():
    print("R15C13 button pressed.")
    update_cell(btn_R15C13, arrRef236, 'btn_R15C13', 'arrRef236')


def update_R15C14():
    print("R15C14 button pressed.")
    update_cell(btn_R15C14, arrRef237, 'btn_R15C14', 'arrRef237')


def update_R15C15():
    print("R15C15 button pressed.")
    update_cell(btn_R15C15, arrRef238, 'btn_R15C15', 'arrRef238')


def update_R15C16():
    print("R15C16 button pressed.")
    update_cell(btn_R15C16, arrRef239, 'btn_R15C16', 'arrRef239')


def update_R16C1():
    print("R16C1 button pressed.")
    update_cell(btn_R16C1, arrRef240, 'btn_R16C1', 'arrRef240')


def update_R16C2():
    print("R16C2 button pressed.")
    update_cell(btn_R16C2, arrRef241, 'btn_R16C2', 'arrRef241')


def update_R16C3():
    print("R16C3 button pressed.")
    update_cell(btn_R16C3, arrRef242, 'btn_R16C3', 'arrRef242')


def update_R16C4():
    print("R16C4 button pressed.")
    update_cell(btn_R16C4, arrRef243, 'btn_R16C4', 'arrRef243')


def update_R16C5():
    print("R16C5 button pressed.")
    update_cell(btn_R16C5, arrRef244, 'btn_R16C5', 'arrRef244')


def update_R16C6():
    print("R16C6 button pressed.")
    update_cell(btn_R16C6, arrRef245, 'btn_R16C6', 'arrRef245')


def update_R16C7():
    print("R16C7 button pressed.")
    update_cell(btn_R16C7, arrRef246, 'btn_R16C7', 'arrRef246')


def update_R16C8():
    print("R16C8 button pressed.")
    update_cell(btn_R16C8, arrRef247, 'btn_R16C8', 'arrRef247')


def update_R16C9():
    print("R16C9 button pressed.")
    update_cell(btn_R16C9, arrRef248, 'btn_R16C9', 'arrRef248')


def update_R16C10():
    print("R16C10 button pressed.")
    update_cell(btn_R16C10, arrRef249, 'btn_R16C10', 'arrRef249')


def update_R16C11():
    print("R16C11 button pressed.")
    update_cell(btn_R16C11, arrRef250, 'btn_R16C11', 'arrRef250')


def update_R16C12():
    print("R16C12 button pressed.")
    update_cell(btn_R16C12, arrRef251, 'btn_R16C12', 'arrRef251')


def update_R16C13():
    print("R16C13 button pressed.")
    update_cell(btn_R16C13, arrRef252, 'btn_R16C13', 'arrRef252')


def update_R16C14():
    print("R16C14 button pressed.")
    update_cell(btn_R16C14, arrRef253, 'btn_R16C14', 'arrRef253')


def update_R16C15():
    print("R16C15 button pressed.")
    update_cell(btn_R16C15, arrRef254, 'btn_R16C15', 'arrRef254')


def update_R16C16():
    print("R16C16 button pressed.")
    update_cell(btn_R16C16, arrRef255, 'btn_R16C16', 'arrRef255')


def ButtonRemoveANumber():
    """ sender As Object, e As EventArgs) Handles ButtonRemoveANumber.Click
        sets the flag for one time use.
    """
    bRemoveANumberFromACell = True


def cells_done():
    cells_done = 256 - len(not_done_arefs)
    btn_done['text'] = f"Cells\nDone\n  {cells_done}"


def cells_remaining():
    cells_remaining_num = len(not_done_arefs)
    btn_remaining['text'] = f"Cells\nTo do\n {cells_remaining_num}"


def load_solution_1():
    print("3504 Entered load_solution_1")
    global currentNumber
    # file = open("C:\MonsterSudoku\MS_4Star_1.txt", "r")
    file = open("C:\MonsterSudoku\MS_5Star_2.txt", "r")
    # file = open("C:\PythonProjects\MonsterSudoku\MS_5Star_1.txt", "r")
    print("File opened")
    for line in file:
        print("line is ", line)
        eval(line)
    file.close()
    print("File closed.")
    cells_done()
    cells_remaining()


def CheckForOnlyNumberInARow():
    pass


def num_in_only_RC_in_Sq():
    # CheckForOnlyOneNumber()
    print("3527 n_1_16 ", n_1_16)
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
    s_1_nums = ""
    for cell in not_done_arefs:
        # current_button = cell['btn']
        # print("3546 ", current_button)
        # for num in n_1_16
        if cell['sq'] == 1:
            for num in startingString:
                print("3548 num in startingString is ", num)
                if num in cell['nums']:
                    print("3550 num and cell['nums'] are ", num, cell['nums'])
                    if num in s_1_nums:
                        print("3552 num in s_1_nums ", num, s_1_nums)
                    elif not num in s_1_nums:
                        print("3554 not num in s_1_nums ", num, s_1_nums)
                        s_1_nums = s_1_nums + num
                        print("3557 not num in s_1_nums ", s_1_nums)
            ex_text = ''.join(sorted(s_1_nums))
            s_1_nums = ex_text
            txt_Explain.delete('1.0', END)  # "insert-1c", END)
            txt_Explain.insert(END, s_1_nums)
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
    print("3576 Entered num_in_only_RC_in_Sq, s_1_nums are: ", s_1_nums)


def create_record():
    pass


def test_1():
    make_arefs()


def make_arefs():
    '''Make rcs references lists'''
    print("6510 type not_done_arefs is ", type(not_done_arefs))
    for aref in not_done_arefs:
        row = aref['row']
        col = aref['col']
        sq = aref['sq']
        if row == 1:
            row_1_arefs.append(aref)
        elif row == 2:
            sq_2_arefs.append(aref)
        elif row == 3:
            row_3_arefs.append(aref)
        elif row == 4:
            row_4_arefs.append(aref)
        elif row == 5:
            row_5_arefs.append(aref)
        elif row == 6:
            row_6_arefs.append(aref)
        elif row == 7:
            row_7_arefs.append(aref)
        elif row == 8:
            row_8_arefs.append(aref)
        elif row == 9:
            row_9_arefs.append(aref)
        elif row == 10:
            row_10_arefs.append(aref)
        elif row == 11:
            row_11_arefs.append(aref)
        elif row == 12:
            row_12_arefs.append(aref)
        elif row == 13:
            row_13_arefs.append(aref)
        elif row == 14:
            row_14_arefs.append(aref)
        elif row == 15:
            row_15_arefs.append(aref)
        elif row == 16:
            row_16_arefs.append(aref)

        col = aref['col']
        if col == 1:
            col_1_arefs.append(aref)
        elif col == 2:
            col_2_arefs.append(aref)
        elif col == 3:
            col_3_arefs.append(aref)
        elif col == 4:
            col_4_arefs.append(aref)
        elif col == 5:
            col_5_arefs.append(aref)
        elif col == 6:
            col_6_arefs.append(aref)
        elif col == 7:
            col_7_arefs.append(aref)
        elif col == 8:
            col_8_arefs.append(aref)
        elif col == 9:
            col_9_arefs.append(aref)
        elif col == 10:
            col_10_arefs.append(aref)
        elif col == 11:
            col_11_arefs.append(aref)
        elif col == 12:
            col_12_arefs.append(aref)
        elif col == 13:
            col_13_arefs.append(aref)
        elif col == 14:
            col_14_arefs.append(aref)
        elif col == 15:
            col_15_arefs.append(aref)
        elif col == 16:
            col_16_arefs.append(aref)

        sq = aref['sq']
        if sq == 1:
            sq_1_arefs.append(aref)
        elif sq == 2:
            sq_2_arefs.append(aref)
        elif sq == 3:
            sq_3_arefs.append(aref)
        elif sq == 4:
            sq_4_arefs.append(aref)
        elif sq == 5:
            sq_5_arefs.append(aref)
        elif sq == 6:
            sq_6_arefs.append(aref)
        elif sq == 7:
            sq_7_arefs.append(aref)
        elif sq == 8:
            sq_8_arefs.append(aref)
        elif sq == 9:
            sq_9_arefs.append(aref)
        elif sq == 10:
            sq_10_arefs.append(aref)
        elif sq == 11:
            sq_11_arefs.append(aref)
        elif sq == 12:
            sq_12_arefs.append(aref)
        elif sq == 13:
            sq_13_arefs.append(aref)
        elif sq == 14:
            sq_14_arefs.append(aref)
        elif sq == 15:
            sq_15_arefs.append(aref)
        elif sq == 16:
            sq_16_arefs.append(aref)
    # print("6615 arefs and types are ", type(row_16_arefs), row_16_arefs)
    # print("6616 arefs and types are ", type(col_16_arefs), col_16_arefs)
    # print("6617 arefs and types are ", type(sq_16_arefs), sq_16_arefs)


def make_current_arefs():
    '''Make rcs references lists'''
    global row_1_arefs
    row_1_arefs = []
    row_2_arefs = []
    row_3_arefs = []
    row_4_arefs = []
    row_5_arefs = []
    row_6_arefs = []
    row_7_arefs = []
    row_8_arefs = []
    row_9_arefs = []
    row_10_arefs = []
    row_11_arefs = []
    row_12_arefs = []
    row_13_arefs = []
    row_14_arefs = []
    row_15_arefs = []
    row_16_arefs = []
    col_1_arefs = []
    col_2_arefs = []
    col_3_arefs = []
    col_4_arefs = []
    col_5_arefs = []
    col_6_arefs = []
    col_7_arefs = []
    col_8_arefs = []
    col_9_arefs = []
    col_10_arefs = []
    col_11_arefs = []
    col_12_arefs = []
    col_13_arefs = []
    col_14_arefs = []
    col_15_arefs = []
    col_16_arefs = []
    print("6510 type not_done_arefs is ", type(not_done_arefs))
    for aref in not_done_arefs:
        row = aref['row']
        col = aref['col']
        sq = aref['sq']
        if row == 1:
            row_1_arefs.append(aref)
        elif row == 2:
            row_2_arefs.append(aref)
        elif row == 3:
            row_3_arefs.append(aref)
        elif row == 4:
            row_4_arefs.append(aref)
        elif row == 5:
            row_5_arefs.append(aref)
        elif row == 6:
            row_6_arefs.append(aref)
        elif row == 7:
            row_7_arefs.append(aref)
        elif row == 8:
            row_8_arefs.append(aref)
        elif row == 9:
            row_9_arefs.append(aref)
        elif row == 10:
            row_10_arefs.append(aref)
        elif row == 11:
            row_11_arefs.append(aref)
        elif row == 12:
            row_12_arefs.append(aref)
        elif row == 13:
            row_13_arefs.append(aref)
        elif row == 14:
            row_14_arefs.append(aref)
        elif row == 15:
            row_15_arefs.append(aref)
        elif row == 16:
            row_16_arefs.append(aref)

        col = aref['col']
        if col == 1:
            col_1_arefs.append(aref)
        elif col == 2:
            col_2_arefs.append(aref)
        elif col == 3:
            col_3_arefs.append(aref)
        elif col == 4:
            col_4_arefs.append(aref)
        elif col == 5:
            col_5_arefs.append(aref)
        elif col == 6:
            col_6_arefs.append(aref)
        elif col == 7:
            col_7_arefs.append(aref)
        elif col == 8:
            col_8_arefs.append(aref)
        elif col == 9:
            col_9_arefs.append(aref)
        elif col == 10:
            col_10_arefs.append(aref)
        elif col == 11:
            col_11_arefs.append(aref)
        elif col == 12:
            col_12_arefs.append(aref)
        elif col == 13:
            col_13_arefs.append(aref)
        elif col == 14:
            col_14_arefs.append(aref)
        elif col == 15:
            col_15_arefs.append(aref)
        elif col == 16:
            col_16_arefs.append(aref)

        sq = aref['sq']
        if sq == 1:
            sq_1_arefs.append(aref)
        elif sq == 2:
            sq_2_arefs.append(aref)
        elif sq == 3:
            sq_3_arefs.append(aref)
        elif sq == 4:
            sq_4_arefs.append(aref)
        elif sq == 5:
            sq_5_arefs.append(aref)
        elif sq == 6:
            sq_6_arefs.append(aref)
        elif sq == 7:
            sq_7_arefs.append(aref)
        elif sq == 8:
            sq_8_arefs.append(aref)
        elif sq == 9:
            sq_9_arefs.append(aref)
        elif sq == 10:
            sq_10_arefs.append(aref)
        elif sq == 11:
            sq_11_arefs.append(aref)
        elif sq == 12:
            sq_12_arefs.append(aref)
        elif sq == 13:
            sq_13_arefs.append(aref)
        elif sq == 14:
            sq_14_arefs.append(aref)
        elif sq == 15:
            sq_15_arefs.append(aref)
        elif sq == 16:
            sq_16_arefs.append(aref)
    # print("6615 arefs and types are ", type(row_16_arefs), row_16_arefs)
    # print("6616 arefs and types are ", type(col_16_arefs), col_16_arefs)
    # print("6617 arefs and types are ", type(sq_16_arefs), sq_16_arefs)


def only_1_num_in_cell_1():
    num_in_row_col_of_sq()


def test_2():
    make_aref_RCS_lists()
    make_RCS_strings()
    make_done_arefs()
    make_RCS_sets_1()
    make_RCS_sets()
    make_row_dicts()
    make_col_dicts()
    num_in_row_col_of_sq()
    remove_num_in_row_sq()
    remove_num_in_col_sq()


def make_RCS_strings():
    """
    Makes lists of all the numbers in each row, column, and square.
    These lists update global variables and will be used to find
    when a number only occurs once in a row, column, or square.
    """
    for r in n_1_16:
        row_nums[r - 1][1] = ""
        col_nums[r - 1][1] = ""
    # row_nums = [[1, ""],
    # print("3885 row_nums are ", row_nums, row_nums[0])
    for cell in not_done_arefs:
        # if cell['sq'] == 5 and len(cell['nums']) != 1:
        row_num = cell['row']
        col_num = cell['col']
        sq_num = cell['sq']
        nums = cell['nums']
        # print("3909 cell['nums'] ", cell['btn_str'], row_num, col_num,
        #       sq_num, nums, row_nums, col_nums, sq_nums)
        row_nums[row_num - 1][1] += nums
        col_nums[col_num - 1][1] += nums
        sq_nums[sq_num - 1][1] += nums
    print("7648 row numbers are ", row_nums)
    print("7649 col numbers are ", col_nums)


def test_1a():
    for item in arrRefs_List:
        row = item['row']
        col = item['col']
        sq = item['sq']
        nums = item['nums']
        aref = item['aref']
        if row == 1:
            # print("3912 aref is ", item)
            # print("3913 aref is ", item['aref'], nums)
            row_1_arefs.append(item)
            # row_1_arefs.append(nums)
            # row_1_arefs.append(aref)
        elif row == 2:
            row_2_arefs.append(item)
        elif row == 3:
            row_3_arefs.append(item)
        elif row == 4:
            row_4_arefs.append(item)
        elif row == 5:
            row_5_arefs.append(item)
        elif row == 6:
            row_6_arefs.append(item)
        elif row == 7:
            row_7_arefs.append(item)
        elif row == 8:
            row_8_arefs.append(item)
        elif row == 9:
            row_9_arefs.append(item)
        elif row == 10:
            row_10_arefs.append(item)
        elif row == 11:
            row_11_arefs.append(item)
        elif row == 12:
            row_12_arefs.append(item)
        elif row == 13:
            row_13_arefs.append(item)
        elif row == 14:
            row_14_arefs.append(item)
        elif row == 15:
            row_15_arefs.append(item)
        elif row == 16:
            row_16_arefs.append(item)
        if col == 1:
            col_1_arefs.append(item)
        elif col == 2:
            col_2_arefs.append(item)
        elif col == 3:
            col_3_arefs.append(item)
        elif col == 4:
            col_3_arefs.append(item)
        elif col == 5:
            col_5_arefs.append(item)
        elif col == 6:
            col_6_arefs.append(item)
        elif col == 7:
            col_6_arefs.append(item)
        elif col == 8:
            col_8_arefs.append(item)
        elif col == 9:
            col_9_arefs.append(item)
        elif col == 10:
            col_10_arefs.append(item)
        elif col == 11:
            col_11_arefs.append(item)
        elif col == 12:
            col_12_arefs.append(item)
        elif col == 13:
            col_13_arefs.append(item)
        elif col == 14:
            col_14_arefs.append(item)
        elif col == 15:
            col_15_arefs.append(item)
        elif col == 16:
            col_16_arefs.append(item)
        if sq == 1:
            sq_1_arefs.append(item)
        elif sq == 2:
            sq_2_arefs.append(item)
        elif sq == 3:
            sq_3_arefs.append(item)
        elif sq == 4:
            sq_4_arefs.append(item)
        elif sq == 5:
            sq_5_arefs.append(item)
        elif sq == 6:
            sq_6_arefs.append(item)
        elif sq == 7:
            sq_7_arefs.append(item)
        elif sq == 8:
            sq_8_arefs.append(item)
        elif sq == 9:
            sq_9_arefs.append(item)
        elif sq == 10:
            sq_10_arefs.append(item)
        elif sq == 11:
            sq_11_arefs.append(item)
        elif sq == 12:
            sq_12_arefs.append(item)
        elif sq == 13:
            sq_13_arefs.append(item)
        elif sq == 14:
            sq_14_arefs.append(item)
        elif sq == 15:
            sq_15_arefs.append(item)
        elif sq == 16:
            sq_16_arefs.append(item)
    print("4644 row_1_arefs ", row_1_arefs)
    print("4645 aref_sq_9 ", sq_9_arefs)

    test_4()


def test_4():
    for aref_list in row_arefs:
        print("4644 ", aref_list)
        for item in aref_list:
            print("4646 item in aref_list is ", item)
            # if item['done'] == False:
            #     print("4023 item is ", item['aref'],
            #           item['btn_str'], item['nums'])


def temp_Test():
    global currentNumber
    currentNumber = 'D'
    for aref in not_done_arefs:
        temp_btn = aref['btn']  # ''' This works '''
        temp_aref = eval(
            aref['aref'])  # ''' This works when aref is a string'''
        update_cell(temp_btn, temp_aref, temp_btn, temp_aref)
        # temp_btn = arrRef0['btn']  # ''' This works when aref is a string'''
        # temp_btn = eval(arrRef0['btn']) # TypeError: eval() arg 1 must be a string, bytes or code object
        print("1900 aref ", aref)
        print("1901 temp_aref ", temp_aref)
        print("1902 temp_aref ", type(temp_btn), temp_btn)
        break


def btn_ShowAref():
    aref_text = 'aref=arrRef0, btn=btn_R1C1, \n' \
        'row=1, col=1, sq=1, done=False,\n' \
        'nums=0123456789ABCDEF,\n' \
        'width=6, height=hit, font=labelfont, \n' \
        'fg=black'
    txt_Other.insert(END, aref_text)


def clear_current_history_file():
    print("current_solution_file")
    with open('C:\PythonProjects\MonsterSudoku\MS_Current_Solution.txt', 'w') as outFile:
        outFile.write('')


def save_current_to_history(history):
    with open('C:\PythonProjects\MonsterSudoku\MS_Current_Solution.txt', 'a') as outFile:
        outFile.write(f'{history}')


def auto():
    print("5148 Auto set")
    only_1_num_in_cell()
    # CheckForOnlyOneNumber()
    # solve_rcs_singles()
    # CheckForOnlyOneNumber()
    # solve_rcs_singles()
    # only_1_num_in_cell()
    # CheckForOnlyOneNumber()
    # only_1_num_in_cell()
    # CheckForOnlyOneNumber()
    # only_1_num_in_cell()
    # find_Duples()
    # fix_duples()
    # CheckForOnlyOneNumber()
    # only_1_num_in_cell()
    # find_Duples()
    # fix_duples()
    # find_Triples()
    # fix_triples()
    # num_in_only_RC_in_Sq()


def reloadPuzzle(btn='btn_R1C2', aref='arrRef1'):
    print("3667 Reload puzzle")
    for item in arrRefs_List:
        if item == 'arrRef1':
            print(item)
            print("3683 aref ", item['btn'])
    cells_done()
    cells_remaining()


def load_currentSolution():
    print("3669 Entered load_currentSolution")
    with open('C:\PythonProjects\MonsterSudoku\MS_Current_Solution.txt', 'r') as outFile:
        for line in outFile:
            print("3671 line is ", line)


def save_currentSolution():
    print("2764 Entered save_currentSolution")
    global currentNumber
    global currentSolution
    currentSolution = ""
    for cell in arrRefs_List:
        if cell['done'] == True:
            currentNumber = cell['nums']
            print(f"2255 currentNumber = '{currentNumber}'")
            aref = cell['aref']
            btn = cell['btn']
            currentSolution += f"currentNumber = '{currentNumber}'"
            print(f"2263 update_cell({btn} , {aref})")
            currentSolution += f"update_cell({btn} , {aref})"


def load_solution_1a():
    print("3755 Entered load_solution_1")
    # enlarge_puzzle()
    # 'C:\PythonProjects\MonsterSudoku\MS_5Star_9.txt'
    global currentNumber
    file = open("C:\MonsterSudoku\MS_5Star_1.txt", "r")
    print("File opened")
    for line in file:
        print("line is ", line)
        eval(line)
    file.close()
    print("File closed.")
    cells_done()
    cells_remaining()


lbl_Title = Label(main_canvas, text="Monster Sudoku Solver Helper")
lbl_Title.grid(row=0, sticky='n')
lbl_Title.config(font=titlefont)

btn_R1C1 = tk.Button(F1_frame, wraplength=48, justify=LEFT, text=startingString,
                     command=update_R1C1, width=6, height=hit)
btn_R1C1.grid(row=1, column=0, sticky='w')
btn_R1C1.config(font=labelfont)

btn_R1C2 = Button(F1_frame, wraplength=48, justify=LEFT, text=startingString,
                  command=update_R1C2, width=6, height=hit)
btn_R1C2.grid(row=1, column=1, sticky='w')
btn_R1C2.config(font=labelfont)

btn_R1C3 = Button(F1_frame, wraplength=48, justify=LEFT, text=startingString,
                  command=update_R1C3, width=6, height=hit)
btn_R1C3.grid(row=1, column=2, sticky='w')
btn_R1C3.config(font=labelfont)

btn_R1C4 = Button(F1_frame, wraplength=48, justify=LEFT, text=startingString,
                  command=update_R1C4, width=6, height=hit)
btn_R1C4.grid(row=1, column=3, sticky='w')
btn_R1C4.config(font=labelfont)

btn_R1C5 = Button(F2_frame, wraplength=48, justify=LEFT, text=startingString,
                  command=update_R1C5, width=6, height=hit)
btn_R1C5.grid(row=1, column=0, sticky='w')
btn_R1C5.config(font=labelfont)

btn_R1C6 = Button(F2_frame, wraplength=48, justify=LEFT, text=startingString,
                  command=update_R1C6, width=6, height=hit)
btn_R1C6.grid(row=1, column=1, sticky='w')
btn_R1C6.config(font=labelfont)

btn_R1C7 = Button(F2_frame, wraplength=48, justify=LEFT, text=startingString,
                  command=update_R1C7, width=6, height=hit)
btn_R1C7.grid(row=1, column=2, sticky='w')
btn_R1C7.config(font=labelfont)

btn_R1C8 = Button(F2_frame, wraplength=48, justify=LEFT, text=startingString,
                  command=update_R1C8, width=6, height=hit)
btn_R1C8.grid(row=1, column=3, sticky='w')
btn_R1C8.config(font=labelfont)

btn_R1C9 = Button(F3_frame, wraplength=48, justify=LEFT, text=startingString,
                  command=update_R1C9, width=6, height=hit)
btn_R1C9.grid(row=1, column=0, sticky='w')
btn_R1C9.config(font=labelfont)

btn_R1C10 = Button(F3_frame, wraplength=48, justify=LEFT, text=startingString,
                   command=update_R1C10, width=6, height=hit)
btn_R1C10.grid(row=1, column=1, sticky='w')
btn_R1C10.config(font=labelfont)

btn_R1C11 = Button(F3_frame, wraplength=48, justify=LEFT, text=startingString,
                   command=update_R1C11, width=6, height=hit)
btn_R1C11.grid(row=1, column=2, sticky='w')
btn_R1C11.config(font=labelfont)
btn_R1C12 = Button(F3_frame, wraplength=48, justify=LEFT, text=startingString,
                   command=update_R1C12, width=6, height=hit)
btn_R1C12.grid(row=1, column=3, sticky='w')
btn_R1C12.config(font=labelfont)

btn_R1C13 = Button(F4_frame, wraplength=48, justify=LEFT, text=startingString,
                   command=update_R1C13, width=6, height=hit)
btn_R1C13.grid(row=1, column=0, sticky='w')
btn_R1C13.config(font=labelfont)

btn_R1C14 = Button(F4_frame, wraplength=48, justify=LEFT, text=startingString,
                   command=update_R1C14, width=6, height=hit)
btn_R1C14.grid(row=1, column=1, sticky='w')
btn_R1C14.config(font=labelfont)

btn_R1C15 = Button(F4_frame, wraplength=48, justify=LEFT, text=startingString,
                   command=update_R1C15, width=6, height=hit)
btn_R1C15.grid(row=1, column=2, sticky='w')
btn_R1C15.config(font=labelfont)
btn_R1C16 = Button(F4_frame, wraplength=48, justify=LEFT, text=startingString,
                   command=update_R1C16, width=6, height=hit)
btn_R1C16.grid(row=1, column=3, sticky='w')
btn_R1C16.config(font=labelfont)

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

btn_R2C2 = Button(F1_frame, wraplength=48, justify=LEFT, text=startingString,
                  command=update_R2C2, width=6, height=hit)
btn_R2C2.grid(row=2, column=1, sticky='w')
btn_R2C2.config(font=labelfont)

btn_R2C3 = Button(F1_frame, wraplength=48, justify=LEFT, text=startingString,
                  command=update_R2C3, width=6, height=hit)
btn_R2C3.grid(row=2, column=2, sticky='w')
btn_R2C3.config(font=labelfont)

btn_R2C4 = Button(F1_frame, wraplength=48, justify=LEFT, text=startingString,
                  command=update_R2C4, width=6, height=hit)
btn_R2C4.grid(row=2, column=3, sticky='w')
btn_R2C4.config(font=labelfont)

btn_R2C5 = Button(F2_frame, wraplength=48, justify=LEFT, text=startingString,
                  command=update_R2C5, width=6, height=hit)
btn_R2C5.grid(row=2, column=0, sticky='w')
btn_R2C5.config(font=labelfont)

btn_R2C6 = Button(F2_frame, wraplength=48, justify=LEFT, text=startingString,
                  command=update_R2C6, width=6, height=hit)
btn_R2C6.grid(row=2, column=1, sticky='w')
btn_R2C6.config(font=labelfont)

btn_R2C7 = Button(F2_frame, wraplength=48, justify=LEFT, text=startingString,
                  command=update_R2C7, width=6, height=hit)
btn_R2C7.grid(row=2, column=2, sticky='w')
btn_R2C7.config(font=labelfont)

btn_R2C8 = Button(F2_frame, wraplength=48, justify=LEFT, text=startingString,
                  command=update_R2C8, width=6, height=hit)
btn_R2C8.grid(row=2, column=3, sticky='w')
btn_R2C8.config(font=labelfont)

btn_R2C9 = Button(F3_frame, wraplength=48, justify=LEFT, text=startingString,
                  command=update_R2C9, width=6, height=hit)
btn_R2C9.grid(row=2, column=0, sticky='w')
btn_R2C9.config(font=labelfont)

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

btn_R2C13 = Button(F4_frame, wraplength=48, justify=LEFT, text=startingString,
                   command=update_R2C13, width=6, height=hit)
btn_R2C13.grid(row=2, column=0, sticky='w')
btn_R2C13.config(font=labelfont)

btn_R2C14 = Button(F4_frame, wraplength=48, justify=LEFT, text=startingString,
                   command=update_R2C14, width=6, height=hit)
btn_R2C14.grid(row=2, column=1, sticky='w')
btn_R2C14.config(font=labelfont)

btn_R2C15 = Button(F4_frame, wraplength=48, justify=LEFT, text=startingString,
                   command=update_R2C15, width=6, height=hit)
btn_R2C15.grid(row=2, column=2, sticky='w')
btn_R2C15.config(font=labelfont)
btn_R2C16 = Button(F4_frame, wraplength=48, justify=LEFT, text=startingString,
                   command=update_R2C16, width=6, height=hit)
btn_R2C16.grid(row=2, column=3, sticky='w')
btn_R2C16.config(font=labelfont)

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

btn_R3C1 = Button(F1_frame, wraplength=48, justify=LEFT, text=startingString,
                  command=update_R3C1, width=6, height=hit)
btn_R3C1.grid(row=3, column=0, sticky='w')
btn_R3C1.config(font=labelfont)

btn_R3C2 = Button(F1_frame, wraplength=48, justify=LEFT, text=startingString,
                  command=update_R3C2, width=6, height=hit)
btn_R3C2.grid(row=3, column=1, sticky='w')
btn_R3C2.config(font=labelfont)

btn_R3C3 = Button(F1_frame, wraplength=48, justify=LEFT, text=startingString,
                  command=update_R3C3, width=6, height=hit)
btn_R3C3.grid(row=3, column=2, sticky='w')
btn_R3C3.config(font=labelfont)

btn_R3C4 = Button(F1_frame, wraplength=48, justify=LEFT, text=startingString,
                  command=update_R3C4, width=6, height=hit)
btn_R3C4.grid(row=3, column=3, sticky='w')
btn_R3C4.config(font=labelfont)

btn_R3C5 = Button(F2_frame, wraplength=48, justify=LEFT, text=startingString,
                  command=update_R3C5, width=6, height=hit)
btn_R3C5.grid(row=3, column=0, sticky='w')
btn_R3C5.config(font=labelfont)

btn_R3C6 = Button(F2_frame, wraplength=48, justify=LEFT, text=startingString,
                  command=update_R3C6, width=6, height=hit)
btn_R3C6.grid(row=3, column=1, sticky='w')
btn_R3C6.config(font=labelfont)

btn_R3C7 = Button(F2_frame, wraplength=48, justify=LEFT, text=startingString,
                  command=update_R3C7, width=6, height=hit)
btn_R3C7.grid(row=3, column=2, sticky='w')
btn_R3C7.config(font=labelfont)

btn_R3C8 = Button(F2_frame, wraplength=48, justify=LEFT, text=startingString,
                  command=update_R3C8, width=6, height=hit)
btn_R3C8.grid(row=3, column=3, sticky='w')
btn_R3C8.config(font=labelfont)

btn_R3C9 = Button(F3_frame, wraplength=48, justify=LEFT, text=startingString,
                  command=update_R3C9, width=6, height=hit)
btn_R3C9.grid(row=3, column=0, sticky='w')
btn_R3C9.config(font=labelfont)

btn_R3C10 = Button(F3_frame, wraplength=48, justify=LEFT, text=startingString,
                   command=update_R3C10, width=6, height=hit)
btn_R3C10.grid(row=3, column=1, sticky='w')
btn_R3C10.config(font=labelfont)

btn_R3C11 = Button(F3_frame, wraplength=48, justify=LEFT, text=startingString,
                   command=update_R3C11, width=6, height=hit)
btn_R3C11.grid(row=3, column=2, sticky='w')
btn_R3C11.config(font=labelfont)
btn_R3C12 = Button(F3_frame, wraplength=48, justify=LEFT, text=startingString,
                   command=update_R3C12, width=6, height=hit)
btn_R3C12.grid(row=3, column=3, sticky='w')
btn_R3C12.config(font=labelfont)

btn_R3C13 = Button(F4_frame, wraplength=48, justify=LEFT, text=startingString,
                   command=update_R3C13, width=6, height=hit)
btn_R3C13.grid(row=3, column=0, sticky='w')
btn_R3C13.config(font=labelfont)

btn_R3C14 = Button(F4_frame, wraplength=48, justify=LEFT, text=startingString,
                   command=update_R3C14, width=6, height=hit)
btn_R3C14.grid(row=3, column=1, sticky='w')
btn_R3C14.config(font=labelfont)

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

btn_R4C2 = Button(F1_frame, wraplength=48, justify=LEFT, text=startingString,
                  command=update_R4C2, width=6, height=hit)
btn_R4C2.grid(row=4, column=1, sticky='w')
btn_R4C2.config(font=labelfont)

btn_R4C3 = Button(F1_frame, wraplength=48, justify=LEFT, text=startingString,
                  command=update_R4C3, width=6, height=hit)
btn_R4C3.grid(row=4, column=2, sticky='w')
btn_R4C3.config(font=labelfont)

btn_R4C4 = Button(F1_frame, wraplength=48, justify=LEFT, text=startingString,
                  command=update_R4C4, width=6, height=hit)
btn_R4C4.grid(row=4, column=3, sticky='w')
btn_R4C4.config(font=labelfont)

btn_R4C5 = Button(F2_frame, wraplength=48, justify=LEFT, text=startingString,
                  command=update_R4C5, width=6, height=hit)
btn_R4C5.grid(row=4, column=0, sticky='w')
btn_R4C5.config(font=labelfont)

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

btn_R5C2 = Button(F5_frame, wraplength=48, justify=LEFT, text=startingString,
                  command=update_R5C2, width=6, height=hit)
btn_R5C2.grid(row=1, column=1, sticky='w')
btn_R5C2.config(font=labelfont)

btn_R5C3 = Button(F5_frame, wraplength=48, justify=LEFT, text=startingString,
                  command=update_R5C3, width=6, height=hit)
btn_R5C3.grid(row=1, column=2, sticky='w')
btn_R5C3.config(font=labelfont)

btn_R5C4 = Button(F5_frame, wraplength=48, justify=LEFT, text=startingString,
                  command=update_R5C4, width=6, height=hit)
btn_R5C4.grid(row=1, column=3, sticky='w')
btn_R5C4.config(font=labelfont)

btn_R5C5 = Button(F6_frame, wraplength=48, justify=LEFT, text=startingString,
                  command=update_R5C5, width=6, height=hit)
btn_R5C5.grid(row=1, column=0, sticky='w')
btn_R5C5.config(font=labelfont)

btn_R5C6 = Button(F6_frame, wraplength=48, justify=LEFT, text=startingString,
                  command=update_R5C6, width=6, height=hit)
btn_R5C6.grid(row=1, column=1, sticky='w')
btn_R5C6.config(font=labelfont)

btn_R5C7 = Button(F6_frame, wraplength=48, justify=LEFT, text=startingString,
                  command=update_R5C7, width=6, height=hit)
btn_R5C7.grid(row=1, column=2, sticky='w')
btn_R5C7.config(font=labelfont)

btn_R5C8 = Button(F6_frame, wraplength=48, justify=LEFT, text=startingString,
                  command=update_R5C8, width=6, height=hit)
btn_R5C8.grid(row=1, column=3, sticky='w')
btn_R5C8.config(font=labelfont)

btn_R5C9 = Button(F7_frame, wraplength=48, justify=LEFT, text=startingString,
                  command=update_R5C9, width=6, height=hit)
btn_R5C9.grid(row=1, column=0, sticky='w')
btn_R5C9.config(font=labelfont)

btn_R5C10 = Button(F7_frame, wraplength=48, justify=LEFT, text=startingString,
                   command=update_R5C10, width=6, height=hit)
btn_R5C10.grid(row=1, column=1, sticky='w')
btn_R5C10.config(font=labelfont)

btn_R5C11 = Button(F7_frame, wraplength=48, justify=LEFT, text=startingString,
                   command=update_R5C11, width=6, height=hit)
btn_R5C11.grid(row=1, column=2, sticky='w')
btn_R5C11.config(font=labelfont)
btn_R5C12 = Button(F7_frame, wraplength=48, justify=LEFT, text=startingString,
                   command=update_R5C12, width=6, height=hit)
btn_R5C12.grid(row=1, column=3, sticky='w')
btn_R5C12.config(font=labelfont)

btn_R5C13 = Button(F8_frame, wraplength=48, justify=LEFT, text=startingString,
                   command=update_R5C13, width=6, height=hit)
btn_R5C13.grid(row=1, column=0, sticky='w')
btn_R5C13.config(font=labelfont)

btn_R5C14 = Button(F8_frame, wraplength=48, justify=LEFT, text=startingString,
                   command=update_R5C14, width=6, height=hit)
btn_R5C14.grid(row=1, column=1, sticky='w')
btn_R5C14.config(font=labelfont)

btn_R5C15 = Button(F8_frame, wraplength=48, justify=LEFT, text=startingString,
                   command=update_R5C15, width=6, height=hit)
btn_R5C15.grid(row=1, column=2, sticky='w')
btn_R5C15.config(font=labelfont)
btn_R5C16 = Button(F8_frame, wraplength=48, justify=LEFT, text=startingString,
                   command=update_R5C16, width=6, height=hit)
btn_R5C16.grid(row=1, column=3, sticky='w')
btn_R5C16.config(font=labelfont)

btn_R6C1 = tk.Button(F5_frame, wraplength=48, justify=LEFT, text=startingString,
                     command=update_R6C1, width=6, height=hit)
btn_R6C1.grid(row=2, column=0, sticky='w')
btn_R6C1.config(font=labelfont)

btn_R6C2 = Button(F5_frame, wraplength=48, justify=LEFT, text=startingString,
                  command=update_R6C2, width=6, height=hit)
btn_R6C2.grid(row=2, column=1, sticky='w')
btn_R6C2.config(font=labelfont)

btn_R6C3 = Button(F5_frame, wraplength=48, justify=LEFT, text=startingString,
                  command=update_R6C3, width=6, height=hit)
btn_R6C3.grid(row=2, column=2, sticky='w')
btn_R6C3.config(font=labelfont)

btn_R6C4 = Button(F5_frame, wraplength=48, justify=LEFT, text=startingString,
                  command=update_R6C4, width=6, height=hit)
btn_R6C4.grid(row=2, column=3, sticky='w')
btn_R6C4.config(font=labelfont)

btn_R6C5 = Button(F6_frame, wraplength=48, justify=LEFT, text=startingString,
                  command=update_R6C5, width=6, height=hit)
btn_R6C5.grid(row=2, column=0, sticky='w')
btn_R6C5.config(font=labelfont)

btn_R6C6 = Button(F6_frame, wraplength=48, justify=LEFT, text=startingString,
                  command=update_R6C6, width=6, height=hit)
btn_R6C6.grid(row=2, column=1, sticky='w')
btn_R6C6.config(font=labelfont)

btn_R6C7 = Button(F6_frame, wraplength=48, justify=LEFT, text=startingString,
                  command=update_R6C7, width=6, height=hit)
btn_R6C7.grid(row=2, column=2, sticky='w')
btn_R6C7.config(font=labelfont)

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
btn_R7C15 = Button(F8_frame, wraplength=48, justify=LEFT, text=startingString,
                   command=update_R7C15, width=6, height=hit)
btn_R7C15.grid(row=3, column=2, sticky='w')
btn_R7C15.config(font=labelfont)
btn_R7C16 = Button(F8_frame, wraplength=48, justify=LEFT, text=startingString,
                   command=update_R7C16, width=6, height=hit)
btn_R7C16.grid(row=3, column=3, sticky='w')
btn_R7C16.config(font=labelfont)

btn_only_one_num = Button(fn_frame, wraplength=40, justify=LEFT, text='Find\nSingle',
                          command=CheckForOnlyOneNumber, width=6, height=3)
btn_only_one_num.grid(row=0, column=0, sticky='nw')
btn_only_one_num.config(font=labelfont)
btn_find_duple = Button(fn_frame, wraplength=40, justify=LEFT, text='Find\nDuples',
                        command=find_Duples, width=6, height=hit)
btn_find_duple.grid(row=0, column=1, sticky='nw')
btn_find_duple.config(font=entryfont)
btn_find_triple = Button(fn_frame, wraplength=40, justify=LEFT, text='Find\nTriple',
                         command=find_Triples, width=6, height=hit)
btn_find_triple.grid(row=0, column=2, sticky='nw')
btn_find_triple.config(font=entryfont)
btn_find_quad = Button(fn_frame, wraplength=40, justify=LEFT, text='Find\nQuads',
                       command=find_Quads, width=6, height=hit)
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

btn_R8C3 = Button(F5_frame, wraplength=48, justify=LEFT, text=startingString,
                  command=update_R8C3, width=6, height=hit)
btn_R8C3.grid(row=4, column=2, sticky='w')
btn_R8C3.config(font=labelfont)

btn_R8C4 = Button(F5_frame, wraplength=48, justify=LEFT, text=startingString,
                  command=update_R8C4, width=6, height=hit)
btn_R8C4.grid(row=4, column=3, sticky='w')
btn_R8C4.config(font=labelfont)

btn_R8C5 = Button(F6_frame, wraplength=48, justify=LEFT, text=startingString,
                  command=update_R8C5, width=6, height=hit)
btn_R8C5.grid(row=4, column=0, sticky='w')
btn_R8C5.config(font=labelfont)

btn_R8C6 = Button(F6_frame, wraplength=48, justify=LEFT, text=startingString,
                  command=update_R8C6, width=6, height=hit)
btn_R8C6.grid(row=4, column=1, sticky='w')
btn_R8C6.config(font=labelfont)

btn_R8C7 = Button(F6_frame, wraplength=48, justify=LEFT, text=startingString,
                  command=update_R8C7, width=6, height=hit)
btn_R8C7.grid(row=4, column=2, sticky='w')
btn_R8C7.config(font=labelfont)

btn_R8C8 = Button(F6_frame, wraplength=48, justify=LEFT, text=startingString,
                  command=update_R8C8, width=6, height=hit)
btn_R8C8.grid(row=4, column=3, sticky='w')
btn_R8C8.config(font=labelfont)

btn_R8C9 = Button(F7_frame, wraplength=48, justify=LEFT, text=startingString,
                  command=update_R8C9, width=6, height=hit)
btn_R8C9.grid(row=4, column=0, sticky='w')
btn_R8C9.config(font=labelfont)

btn_R8C10 = Button(F7_frame, wraplength=48, justify=LEFT, text=startingString,
                   command=update_R8C10, width=6, height=hit)
btn_R8C10.grid(row=4, column=1, sticky='w')
btn_R8C10.config(font=labelfont)

btn_R8C11 = Button(F7_frame, wraplength=48, justify=LEFT, text=startingString,
                   command=update_R8C11, width=6, height=hit)
btn_R8C11.grid(row=4, column=2, sticky='w')
btn_R8C11.config(font=labelfont)
btn_R8C12 = Button(F7_frame, wraplength=48, justify=LEFT, text=startingString,
                   command=update_R8C12, width=6, height=hit)
btn_R8C12.grid(row=4, column=3, sticky='w')
btn_R8C12.config(font=labelfont)

btn_R8C13 = Button(F8_frame, wraplength=48, justify=LEFT, text=startingString,
                   command=update_R8C13, width=6, height=hit)
btn_R8C13.grid(row=4, column=0, sticky='w')
btn_R8C13.config(font=labelfont)

btn_R8C14 = Button(F8_frame, wraplength=48, justify=LEFT, text=startingString,
                   command=update_R8C14, width=6, height=hit)
btn_R8C14.grid(row=4, column=1, sticky='w')
btn_R8C14.config(font=labelfont)

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

btn_R9C2 = Button(F9_frame, wraplength=48, justify=LEFT, text=startingString,
                  command=update_R9C2, width=6, height=hit)
btn_R9C2.grid(row=1, column=1, sticky='w')
btn_R9C2.config(font=labelfont)

btn_R9C3 = Button(F9_frame, wraplength=48, justify=LEFT, text=startingString,
                  command=update_R9C3, width=6, height=hit)
btn_R9C3.grid(row=1, column=2, sticky='w')
btn_R9C3.config(font=labelfont)

btn_R9C4 = Button(F9_frame, wraplength=48, justify=LEFT, text=startingString,
                  command=update_R9C4, width=6, height=hit)
btn_R9C4.grid(row=1, column=3, sticky='w')
btn_R9C4.config(font=labelfont)

btn_R9C5 = Button(F10_frame, wraplength=48, justify=LEFT, text=startingString,
                  command=update_R9C5, width=6, height=hit)
btn_R9C5.grid(row=1, column=0, sticky='w')
btn_R9C5.config(font=labelfont)

btn_R9C6 = Button(F10_frame, wraplength=48, justify=LEFT, text=startingString,
                  command=update_R9C6, width=6, height=hit)
btn_R9C6.grid(row=1, column=1, sticky='w')
btn_R9C6.config(font=labelfont)

btn_R9C7 = Button(F10_frame, wraplength=48, justify=LEFT, text=startingString,
                  command=update_R9C7, width=6, height=hit)
btn_R9C7.grid(row=1, column=2, sticky='w')
btn_R9C7.config(font=labelfont)

btn_R9C8 = Button(F10_frame, wraplength=48, justify=LEFT, text=startingString,
                  command=update_R9C8, width=6, height=hit)
btn_R9C8.grid(row=1, column=3, sticky='w')
btn_R9C8.config(font=labelfont)

btn_R9C9 = Button(F11_frame, wraplength=48, justify=LEFT, text=startingString,
                  command=update_R9C9, width=6, height=hit)
btn_R9C9.grid(row=1, column=0, sticky='w')
btn_R9C9.config(font=labelfont)

btn_R9C10 = Button(F11_frame, wraplength=48, justify=LEFT, text=startingString,
                   command=update_R9C10, width=6, height=hit)
btn_R9C10.grid(row=1, column=1, sticky='w')
btn_R9C10.config(font=labelfont)

btn_R9C11 = Button(F11_frame, wraplength=48, justify=LEFT, text=startingString,
                   command=update_R9C11, width=6, height=hit)
btn_R9C11.grid(row=1, column=2, sticky='w')
btn_R9C11.config(font=labelfont)
btn_R9C12 = Button(F11_frame, wraplength=48, justify=LEFT, text=startingString,
                   command=update_R9C12, width=6, height=hit)
btn_R9C12.grid(row=1, column=3, sticky='w')
btn_R9C12.config(font=labelfont)

btn_R9C13 = Button(F12_frame, wraplength=48, justify=LEFT, text=startingString,
                   command=update_R9C13, width=6, height=hit)
btn_R9C13.grid(row=1, column=0, sticky='w')
btn_R9C13.config(font=labelfont)

btn_R9C14 = Button(F12_frame, wraplength=48, justify=LEFT, text=startingString,
                   command=update_R9C14, width=6, height=hit)
btn_R9C14.grid(row=1, column=1, sticky='w')
btn_R9C14.config(font=labelfont)

btn_R9C15 = Button(F12_frame, wraplength=48, justify=LEFT, text=startingString,
                   command=update_R9C15, width=6, height=hit)
btn_R9C15.grid(row=1, column=2, sticky='w')
btn_R9C15.config(font=labelfont)
btn_R9C16 = Button(F12_frame, wraplength=48, justify=LEFT, text=startingString,
                   command=update_R9C16, width=6, height=hit)
btn_R9C16.grid(row=1, column=3, sticky='w')
btn_R9C16.config(font=labelfont)
# btn_R2C16.bind("<<ComboboxSelected>>", create_record())
btn_solve_singles = Button(fn_frame, wraplength=40, justify=LEFT, text='Solve\nsingles',
                           command=solve_rcs_singles, width=6, height=hit)
btn_solve_singles.grid(row=2, column=0, sticky='nw')
btn_solve_singles.config(font=entryfont)
btn_Fix_Duples = Button(fn_frame, wraplength=40, justify=LEFT, text='Fix\nduples',
                        command=fix_duples, width=6, height=hit)
btn_Fix_Duples.grid(row=2, column=1, sticky='nw')
btn_Fix_Duples.config(font=entryfont)
btn_IDTriples = Button(fn_frame, wraplength=40, justify=LEFT, text='Fix\ntriples',
                       command=fix_triples, width=6, height=hit)
btn_IDTriples.grid(row=2, column=2, sticky='nw')
btn_IDTriples.config(font=entryfont)

btn_FixQuads = Button(fn_frame, wraplength=48, justify=LEFT, text='Fix\nquads',
                      command=fix_quads, width=6, height=hit)
btn_FixQuads.grid(row=2, column=3, sticky='nw')
btn_FixQuads.config(font=entryfont)  #

btn_del_num = Button(fn_frame, wraplength=40, justify=LEFT, text='Del\nnum\nfrom\ncell',
                     command=set_bRemoveANumberFromACell, width=6, height=hit)
btn_del_num.grid(row=3, column=0, sticky='nw')
btn_del_num.config(font=entryfont)

btn_Reload = Button(fn_frame, wraplength=40, justify=LEFT, text='Reload\nSolutn',
                    command=reloadPuzzle, width=6, height=hit)
btn_Reload.grid(row=3, column=1, sticky='nw')
btn_Reload.config(font=entryfont)
btn_done = Button(fn_frame, wraplength=40, justify=LEFT, text='Cells\nDone',
                  command=cells_done, width=6, height=hit)
btn_done.grid(row=3, column=2, sticky='nw')
btn_done.config(font=entryfont)
btn_remaining = Button(fn_frame, wraplength=48, justify=LEFT, text='Cells\nRemain',
                       command=cells_remaining, width=6, height=hit)
btn_remaining.grid(row=3, column=3, sticky='nw')
btn_remaining.config(font=entryfont)

btn_e = Button(fn_frame, wraplength=40, justify=LEFT, text='Num\nin 1\nr or c \n in sq',
               command=test_2, width=6, height=hit)
btn_e.grid(row=4, column=0, sticky='nw')
btn_e.config(font=entryfont)
btn_load = Button(fn_frame, wraplength=40, justify=LEFT, text='Load\nsoln',
                  command=load_solution_1, width=6, height=hit)
btn_load.grid(row=4, column=1, sticky='nw')
btn_load.config(font=entryfont)
btn_auto = Button(fn_frame, wraplength=40, justify=LEFT, text='Auto\nMode',
                  command=auto, width=6, height=hit)
btn_auto.grid(row=4, column=2, sticky='nw')
btn_auto.config(font=entryfont)
btn_clear_text = Button(fn_frame, wraplength=48, justify=LEFT, text='Clear\ntext\n',
                        command=clear_text, width=6, height=hit)
btn_clear_text.grid(row=4, column=3, sticky='nw')
btn_clear_text.config(font=entryfont)


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
# , columnspan=4, sticky='nw'
txt_Explain.grid(row=0, column=0, rowspan=4, sticky='w')
txt_Explain.config(font=labelfont)
txt_Explain.insert(END, 'Explanatory text goes below.\n')
# txt_Explain.insert(END, startingString)

txt_Other = Text(txt_frame, width=32, height=15)
# , columnspan=4, sticky='nw'
txt_Other.grid(row=0, column=0, rowspan=4, sticky='w')
txt_Other.config(font=labelfont)
txt_Other.insert(END, "Hints\n")
txt_Other.insert(END, "Note: There are numerous errors in the program! ")
txt_Other.insert(END, "Deleting numbers until there is only one number ")
txt_Other.insert(
    END, "in a cell does not correctly update the cell contents. ")
txt_Other.insert(END, "So Find Single doesn't find that single number cell.\n")
txt_Other.insert(END, "The fllowing hints are for one program \n")
txt_Other.insert(END, "and don't apply to other programs. \n")
txt_Other.insert(END, "Cells Done = 123 \n")
txt_Other.insert(END, "Duple C14\n")
# = 59C : 14,16 = 6; 2,16 D 9; 3,16 D 9; 12,16 Del C
txt_Other.insert(END, "Triple C16\n")
txt_Other.insert(END, "Triple can help identify a triple, but doesn't ")
txt_Other.insert(END, "remove numbers from cells the way Duples does.\n")
txt_Other.insert(END, "Cells Done = 142\n")
txt_Other.insert(END, "Duple S3\n")
txt_Other.insert(END, "Look for duples, triples.\n")
# txt_Other.insert(END, "Check S7 for 5s.\n")
txt_Other.insert(END, "S7 R6 has only 5s in row\n")
txt_Other.insert(END, "S9 C1 has only 7s in Col and Sq.\n")
txt_Other.insert(END, "Note Duple only solved the first duple found.\n")
txt_Other.insert(END, "So Duple will ID duples, but not simplify puzzle.\n")
txt_Other.insert(
    END, "You need to simplify the puzzle manually from here on.\n")
txt_Other.insert(
    END, "Duple S8 = BF : 8,13 Del F  Duple S8 = 9C Del Cs from row\n")
# Quad S14 39AD : 16,5 = 5; D = 143 15,5 Del 3; 15,8 Del AD
txt_Other.insert(END, "Quad S14\n")
txt_Other.insert(END, "Duple S13\n")  # S13 Duple 7C
# triple S15  359 : 15,11 = 1; 13,12 Del 5; 14,5 Del 5
txt_Other.insert(END, "Triple S15\n")
# triple S15 triple ACD : 16,13 = 5; D = 145
txt_Other.insert(END, "Triple S15\n")
# S15, C12 has only Cs in S, 6,112 Del C
txt_Other.insert(END, "S15, C12 has only Cs\n")
# Triple R9  14A : Del 1,4,A from other cells
txt_Other.insert(END, "Triple R9\n")
txt_Other.insert(END, "Triple S15\n")
# S7 R6 has only 5s in row, so 5,11 Del 5  8

txt_Other.insert(END, "Cells Done = 165\n")
# Duple S15 R14 AD : 14,4 = 0, 14,1 Del 1; 14,2 Del AD
txt_Other.insert(END, "Duple S15\n")
txt_Other.insert(END, "Duple S12\n")  # Duple S12 C15 Duple 14 : 4,15 Del 4
# 5,6 = 0 no auto complete with find and solve
txt_Other.insert(END, "5,6 = 0 no auto complete\n")
txt_Other.insert(END, "Duple S15\n")  # S15 Duple 39 : 6,10 Del 3, 7,10, Del 3
# S14 C7 has only 9A in square : duple : del from col, also, 13,6 = 3
txt_Other.insert(END, "S14 C7 has only 9A\n")
# txt_Other.insert(END, "4,2 = 4 no auto complete\n")
# txt_Other.insert(END, "5,2 = 2 no auto complete\n")

# S1 C4 has the only 7s in the column, so 3,1 del 7 and 3,3 del 7
txt_Other.insert(END, "S1 C4 has the only 7s\n")
txt_Other.insert(END, "S9 C1 has the only 7s\n")
txt_Other.insert(END, "S1 R3 has the only As\n")
txt_Other.insert(END, "5, 2 = 2 no auto complete\n")
txt_Other.insert(END, "Triple S2\n")
txt_Other.insert(END, "Quad S1\n")
# 13AD  ?Wrong Quad S1 39AE so 2,4 del 3 ; 12,4 del 8
txt_Other.insert(END, "Quad C3\n")
# Duple 7C so 5,1 = 1 Triple C3 13A, del 1,3A,  duple 7C  5,1 = 1
txt_Other.insert(END, "Duple S5\n")

txt_Other.insert(END, "11,2 = 0 no auto complete\n")
txt_Other.insert(END, "5,2 = 2 no auto complete\n")
txt_Other.insert(END, "6,7 = E no auto complete\n")
txt_Other.insert(END, "S14 C7 has the only 9s\n")
txt_Other.insert(END, "Duple S5\n")  # Duple 3D
# 349A  ?Wrong Quad S1 39AE so 2,4 del 3 ; 12,4 del 8
txt_Other.insert(END, "Quad S1\n")
txt_Other.insert(END, "Duple S1\n")  # Duple 78
# Find and solve * ?  finished!.\n")
txt_Other.insert(END, "Find and solve\n")

# EventText=tk.Text(root, height=10, width=50)
EventScrollBar = tk.Scrollbar(
    ex_frame, command=txt_Explain.yview, orient="vertical")
EventScrollBar.grid(row=0, column=1, sticky="ns")
# txt_Explain.grid(row=0,column=0)
txt_Explain.configure(yscrollcommand=EventScrollBar.set)
# Quote=("""Suck\ne\ne\ne\ne\ne\ne\ne\ne\ne\nee\ne\ne\ne\ne\ne\ne\ne\nee\ned\ne\ne\nde\nd\ne\nded\nc\nc\nx\nc\nx\nc\nzc\ns\nds\nx\nwd\ns\nd\nwd""")
# txt_Explain.insert(tk.END, Quote)


# arrRef0 = dict(btn=btn_R1C1)

btn_dict = {}
arrRef0 = dict(aref='arrRef0', btn=btn_R1C1, btn_str='btn_R1C1', row=1, col=1, sq=1,
               done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef1 = dict(aref='arrRef1', btn=btn_R1C2, btn_str='btn_R1C2', row=1, col=2, sq=1,
               done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef2 = dict(aref='arrRef2', btn=btn_R1C3, btn_str='btn_R1C3', row=1, col=3, sq=1,
               done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef3 = dict(aref='arrRef3', btn=btn_R1C4, btn_str='btn_R1C4', row=1, col=4, sq=1,
               done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef4 = dict(aref='arrRef4', btn=btn_R1C5, btn_str='btn_R1C5', row=1, col=5, sq=2,
               done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef5 = dict(aref='arrRef5', btn=btn_R1C6, btn_str='btn_R1C6', row=1, col=6, sq=2,
               done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef6 = dict(aref='arrRef6', btn=btn_R1C7, btn_str='btn_R1C7', row=1, col=7, sq=2,
               done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef7 = dict(aref='arrRef7', btn=btn_R1C8, btn_str='btn_R1C8', row=1, col=8, sq=2,
               done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef8 = dict(aref='arrRef8', btn=btn_R1C9, btn_str='btn_R1C8', row=1, col=9, sq=3,
               done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef9 = dict(aref='arrRef9', btn=btn_R1C10, btn_str='btn_R1C10', row=1, col=10, sq=3,
               done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef10 = dict(aref='arrRef10', btn=btn_R1C11, btn_str='btn_R1C11', row=1, col=11, sq=3,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef11 = dict(aref='arrRef11', btn=btn_R1C12, btn_str='btn_R1C12', row=1, col=12, sq=3,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef12 = dict(aref='arrRef12', btn=btn_R1C13, btn_str='btn_R1C13', row=1, col=13, sq=4,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef13 = dict(aref='arrRef13', btn=btn_R1C14, btn_str='btn_R1C14', row=1, col=14, sq=4,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef14 = dict(aref='arrRef14', btn=btn_R1C15, btn_str='btn_R1C15', row=1, col=15, sq=4,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef15 = dict(aref='arrRef15', btn=btn_R1C16, btn_str='btn_R1C16', row=1, col=16, sq=4,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef16 = dict(aref='arrRef16', btn=btn_R2C1, btn_str='btn_R2C1', row=2, col=1, sq=1,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef17 = dict(aref='arrRef17', btn=btn_R2C2, btn_str='btn_R2C2', row=2, col=2, sq=1,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef18 = dict(aref='arrRef18', btn=btn_R2C3, btn_str='btn_R2C3', row=2, col=3, sq=1,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef19 = dict(aref='arrRef19', btn=btn_R2C4, btn_str='btn_R2C4', row=2, col=4, sq=1,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef20 = dict(aref='arrRef20', btn=btn_R2C5, btn_str='btn_R2C5', row=2, col=5, sq=2,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef21 = dict(aref='arrRef21', btn=btn_R2C6, btn_str='btn_R2C6', row=2, col=6, sq=2,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef22 = dict(aref='arrRef22', btn=btn_R2C7, btn_str='btn_R2C7', row=2, col=7, sq=2,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef23 = dict(aref='arrRef23', btn=btn_R2C8, btn_str='btn_R2C8', row=2, col=8, sq=2,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef24 = dict(aref='arrRef24', btn=btn_R2C9, btn_str='btn_R2C9', row=2, col=9, sq=3,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef25 = dict(aref='arrRef25', btn=btn_R2C10, btn_str='btn_R2C10', row=2, col=10, sq=3,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef26 = dict(aref='arrRef26', btn=btn_R2C11, btn_str='btn_R2C11', row=2, col=11, sq=3,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef27 = dict(aref='arrRef27', btn=btn_R2C12, btn_str='btn_R2C12', row=2, col=12, sq=3,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef28 = dict(aref='arrRef28', btn=btn_R2C13, btn_str='btn_R2C13', row=2, col=13, sq=4,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef29 = dict(aref='arrRef29', btn=btn_R2C14, btn_str='btn_R2C14', row=2, col=14, sq=4,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef30 = dict(aref='arrRef30', btn=btn_R2C15, btn_str='btn_R2C15', row=2, col=15, sq=4,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef31 = dict(aref='arrRef31', btn=btn_R2C16, btn_str='btn_R2C16', row=2, col=16, sq=4,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef32 = dict(aref='arrRef32', btn=btn_R3C1, btn_str='btn_R3C1', row=3, col=1, sq=1,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef33 = dict(aref='arrRef33', btn=btn_R3C2, btn_str='btn_R3C2', row=3, col=2, sq=1,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef34 = dict(aref='arrRef34', btn=btn_R3C3, btn_str='btn_R3C3', row=3, col=3, sq=1,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef35 = dict(aref='arrRef35', btn=btn_R3C4, btn_str='btn_R3C4', row=3, col=4, sq=1,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef36 = dict(aref='arrRef36', btn=btn_R3C5, btn_str='btn_R3C5', row=3, col=5, sq=2,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef37 = dict(aref='arrRef37', btn=btn_R3C6, btn_str='btn_R3C6', row=3, col=6, sq=2,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef38 = dict(aref='arrRef38', btn=btn_R3C7, btn_str='btn_R3C7', row=3, col=7, sq=2,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef39 = dict(aref='arrRef39', btn=btn_R3C8, btn_str='btn_R3C8', row=3, col=8, sq=2,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef40 = dict(aref='arrRef40', btn=btn_R3C9, btn_str='btn_R3C9', row=3, col=9, sq=3,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef41 = dict(aref='arrRef41', btn=btn_R3C10, btn_str='btn_R3C10', row=3, col=10, sq=3,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef42 = dict(aref='arrRef41', btn=btn_R3C11, btn_str='btn_R3C11', row=3, col=11, sq=3,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef43 = dict(aref='arrRef43', btn=btn_R3C12, btn_str='btn_R3C12', row=3, col=12, sq=3,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef44 = dict(aref='arrRef44', btn=btn_R3C13, btn_str='btn_R3C13', row=3, col=13, sq=4,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef45 = dict(aref='arrRef45', btn=btn_R3C14, btn_str='btn_R3C14', row=3, col=14, sq=4,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef46 = dict(aref='arrRef46', btn=btn_R3C15, btn_str='btn_R3C15', row=3, col=15, sq=4,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef47 = dict(aref='arrRef47', btn=btn_R3C16, btn_str='btn_R3C16', row=3, col=16, sq=4,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef48 = dict(aref='arrRef48', btn=btn_R4C1, btn_str='btn_R4C1', row=4, col=1, sq=1,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef49 = dict(aref='arrRef49', btn=btn_R4C2, btn_str='btn_R4C2', row=4, col=2, sq=1,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef50 = dict(aref='arrRef50', btn=btn_R4C3, btn_str='btn_R4C3', row=4, col=3, sq=1,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef51 = dict(aref='arrRef51', btn=btn_R4C4, btn_str='btn_R4C4', row=4, col=4, sq=1,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef52 = dict(aref='arrRef52', btn=btn_R4C5, btn_str='btn_R4C5', row=4, col=5, sq=2,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef53 = dict(aref='arrRef53', btn=btn_R4C6, btn_str='btn_R4C6', row=4, col=6, sq=2,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef54 = dict(aref='arrRef54', btn=btn_R4C7, btn_str='btn_R4C7', row=4, col=7, sq=2,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef55 = dict(aref='arrRef55', btn=btn_R4C8, btn_str='btn_R4C8', row=4, col=8, sq=2,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef56 = dict(aref='arrRef56', btn=btn_R4C9, btn_str='btn_R4C9', row=4, col=9, sq=3,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef57 = dict(aref='arrRef57', btn=btn_R4C10, btn_str='btn_R4C10', row=4, col=10, sq=3,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef58 = dict(aref='arrRef58', btn=btn_R4C11, btn_str='btn_R4C11', row=4, col=11, sq=3,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef59 = dict(aref='arrRef59', btn=btn_R4C12, btn_str='btn_R4C12', row=4, col=12, sq=3,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef60 = dict(aref='arrRef60', btn=btn_R4C13, btn_str='btn_R4C13', row=4, col=13, sq=4,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef61 = dict(aref='arrRef61', btn=btn_R4C14, btn_str='btn_R4C14', row=4, col=14, sq=4,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef62 = dict(aref='arrRef62', btn=btn_R4C15, btn_str='btn_R4C15', row=4, col=15, sq=4,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef63 = dict(aref='arrRef63', btn=btn_R4C16, btn_str='btn_R4C16', row=4, col=16, sq=4,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef64 = dict(aref='arrRef64', btn=btn_R5C1, btn_str='btn_R5C1', row=5, col=1, sq=5,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef65 = dict(aref='arrRef65', btn=btn_R5C2, btn_str='btn_R5C2', row=5, col=2, sq=5,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef66 = dict(aref='arrRef66', btn=btn_R5C3, btn_str='btn_R5C3', row=5, col=3, sq=5,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef67 = dict(aref='arrRef67', btn=btn_R5C4, btn_str='btn_R5C4', row=5, col=4, sq=5,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef68 = dict(aref='arrRef68', btn=btn_R5C5, btn_str='btn_R5C5', row=5, col=5, sq=6,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef69 = dict(aref='arrRef69', btn=btn_R5C6, btn_str='btn_R5C6', row=5, col=6, sq=6,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef70 = dict(aref='arrRef70', btn=btn_R5C7, btn_str='btn_R5C7', row=5, col=7, sq=6,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef71 = dict(aref='arrRef71', btn=btn_R5C8, btn_str='btn_R5C8', row=5, col=8, sq=6,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef72 = dict(aref='arrRef72', btn=btn_R5C9, btn_str='btn_R5C9', row=5, col=9, sq=7,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef73 = dict(aref='arrRef73', btn=btn_R5C10, btn_str='btn_R5C10', row=5, col=10, sq=7,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef74 = dict(aref='arrRef74', btn=btn_R5C11, btn_str='btn_R5C11', row=5, col=11, sq=7,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef75 = dict(aref='arrRef75', btn=btn_R5C12, btn_str='btn_R5C12', row=5, col=12, sq=7,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef76 = dict(aref='arrRef76', btn=btn_R5C13, btn_str='btn_R5C13', row=5, col=13, sq=8,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef77 = dict(aref='arrRef77', btn=btn_R5C14, btn_str='btn_R5C14', row=5, col=14, sq=8,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef78 = dict(aref='arrRef78', btn=btn_R5C15, btn_str='btn_R5C15', row=5, col=15, sq=8,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef79 = dict(aref='arrRef79', btn=btn_R5C16, btn_str='btn_R5C16', row=5, col=16, sq=8,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef80 = dict(aref='arrRef80', btn=btn_R6C1, btn_str='btn_R6C1', row=6, col=1, sq=5,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef81 = dict(aref='arrRef81', btn=btn_R6C2, btn_str='btn_R6C2', row=6, col=2, sq=5,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef82 = dict(aref='arrRef82', btn=btn_R6C3, btn_str='btn_R6C3', row=6, col=3, sq=5,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef83 = dict(aref='arrRef83', btn=btn_R6C4, btn_str='btn_R6C4', row=6, col=4, sq=5,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef84 = dict(aref='arrRef84', btn=btn_R6C5, btn_str='btn_R6C5', row=6, col=5, sq=6,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef85 = dict(aref='arrRef85', btn=btn_R6C6, btn_str='btn_R6C6', row=6, col=6, sq=6,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef86 = dict(aref='arrRef86', btn=btn_R6C7, btn_str='btn_R6C7', row=6, col=7, sq=6,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef87 = dict(aref='arrRef87', btn=btn_R6C8, btn_str='btn_R6C8', row=6, col=8, sq=6,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef88 = dict(aref='arrRef88', btn=btn_R6C9, btn_str='btn_R6C9', row=6, col=9, sq=7,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef89 = dict(aref='arrRef89', btn=btn_R6C10, btn_str='btn_R6C10', row=6, col=10, sq=7,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef90 = dict(aref='arrRef90', btn=btn_R6C11, btn_str='btn_R6C11', row=6, col=11, sq=7,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef91 = dict(aref='arrRef91', btn=btn_R6C12, btn_str='btn_R6C12', row=6, col=12, sq=7,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef92 = dict(aref='arrRef92', btn=btn_R6C13, btn_str='btn_R6C13', row=6, col=13, sq=8,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef93 = dict(aref='arrRef93', btn=btn_R6C14, btn_str='btn_R6C14', row=6, col=14, sq=8,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef94 = dict(aref='arrRef94', btn=btn_R6C15, btn_str='btn_R6C15', row=6, col=15, sq=8,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef95 = dict(aref='arrRef95', btn=btn_R6C16, btn_str='btn_R6C16', row=6, col=16, sq=8,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef96 = dict(aref='arrRef96', btn=btn_R7C1, btn_str='btn_R7C1', row=7, col=1, sq=5,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef97 = dict(aref='arrRef97', btn=btn_R7C2, btn_str='btn_R7C2', row=7, col=2, sq=5,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef98 = dict(aref='arrRef98', btn=btn_R7C3, btn_str='btn_R7C3', row=7, col=3, sq=5,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef99 = dict(aref='arrRef99', btn=btn_R7C4, btn_str='btn_R7C4', row=7, col=4, sq=5,
                done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef100 = dict(aref='arrRef100', btn=btn_R7C5, btn_str='btn_R7C5', row=7, col=5, sq=6,
                 done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef101 = dict(aref='arrRef101', btn=btn_R7C6, btn_str='btn_R7C6', row=7, col=6, sq=6,
                 done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef102 = dict(aref='arrRef102', btn=btn_R7C7, btn_str='btn_R7C7', row=7, col=7, sq=6,
                 done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef103 = dict(aref='arrRef103', btn=btn_R7C8, btn_str='btn_R7C8', row=7, col=8, sq=6,
                 done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef104 = dict(aref='arrRef104', btn=btn_R7C9, btn_str='btn_R7C9', row=7, col=9, sq=7,
                 done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef105 = dict(aref='arrRef105', btn=btn_R7C10, btn_str='btn_R7C10', row=7, col=10,
                 sq=7, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef106 = dict(aref='arrRef106', btn=btn_R7C11, btn_str='btn_R7C11', row=7, col=11,
                 sq=7, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef107 = dict(aref='arrRef107', btn=btn_R7C12, btn_str='btn_R7C12', row=7, col=12,
                 sq=7, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef108 = dict(aref='arrRef108', btn=btn_R7C13, btn_str='btn_R7C13', row=7, col=13,
                 sq=8, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef109 = dict(aref='arrRef109', btn=btn_R7C14, btn_str='btn_R7C14', row=7, col=14,
                 sq=8, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef110 = dict(aref='arrRef110', btn=btn_R7C15, btn_str='btn_R7C15', row=7, col=15,
                 sq=8, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef111 = dict(aref='arrRef111', btn=btn_R7C16, btn_str='btn_R7C16', row=7, col=16,
                 sq=8, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef112 = dict(aref='arrRef112', btn=btn_R8C1, btn_str='btn_R8C1', row=8, col=1, sq=5,
                 done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef113 = dict(aref='arrRef113', btn=btn_R8C2, btn_str='btn_R8C2', row=8, col=2, sq=5,
                 done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef114 = dict(aref='arrRef114', btn=btn_R8C3, btn_str='btn_R8C3', row=8, col=3, sq=5,
                 done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef115 = dict(aref='arrRef115', btn=btn_R8C4, btn_str='btn_R8C4', row=8, col=4, sq=5,
                 done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef116 = dict(aref='arrRef116', btn=btn_R8C5, btn_str='btn_R8C5', row=8, col=5, sq=6,
                 done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef117 = dict(aref='arrRef117', btn=btn_R8C6, btn_str='btn_R8C6', row=8, col=6, sq=6,
                 done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef118 = dict(aref='arrRef118', btn=btn_R8C7, btn_str='btn_R8C7', row=8, col=7, sq=6,
                 done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef119 = dict(aref='arrRef119', btn=btn_R8C8, btn_str='btn_R8C8', row=8, col=8, sq=6,
                 done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef120 = dict(aref='arrRef120', btn=btn_R8C9, btn_str='btn_R8C9', row=8, col=9, sq=7,
                 done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef121 = dict(aref='arrRef121', btn=btn_R8C10, btn_str='btn_R8C10', row=8, col=10,
                 sq=7, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef122 = dict(aref='arrRef122', btn=btn_R8C11, btn_str='btn_R8C11', row=8, col=11,
                 sq=7, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef123 = dict(aref='arrRef123', btn=btn_R8C12, btn_str='btn_R8C12', row=8, col=12,
                 sq=7, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef124 = dict(aref='arrRef124', btn=btn_R8C13, btn_str='btn_R8C13', row=8, col=13,
                 sq=8, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef125 = dict(aref='arrRef125', btn=btn_R8C14, btn_str='btn_R8C14', row=8, col=14,
                 sq=8, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef126 = dict(aref='arrRef126', btn=btn_R8C15, btn_str='btn_R8C15', row=8, col=15,
                 sq=8, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef127 = dict(aref='arrRef127', btn=btn_R8C16, btn_str='btn_R8C16', row=8, col=16,
                 sq=8, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef128 = dict(aref='arrRef128', btn=btn_R9C1, btn_str='btn_R9C1', row=9, col=1, sq=9,
                 done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef129 = dict(aref='arrRef129', btn=btn_R9C2, btn_str='btn_R9C2', row=9, col=2, sq=9,
                 done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef130 = dict(aref='arrRef130', btn=btn_R9C3, btn_str='btn_R9C3', row=9, col=3, sq=9,
                 done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef131 = dict(aref='arrRef131', btn=btn_R9C4, btn_str='btn_R9C4', row=9, col=4, sq=9,
                 done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef132 = dict(aref='arrRef132', btn=btn_R9C5, btn_str='btn_R9C5', row=9, col=5, sq=10,
                 done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef133 = dict(aref='arrRef133', btn=btn_R9C6, btn_str='btn_R9C6', row=9, col=6, sq=10,
                 done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef134 = dict(aref='arrRef134', btn=btn_R9C7, btn_str='btn_R9C7', row=9, col=7, sq=10,
                 done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef135 = dict(aref='arrRef135', btn=btn_R9C8, btn_str='btn_R9C8', row=9, col=8, sq=10,
                 done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef136 = dict(aref='arrRef136', btn=btn_R9C9, btn_str='btn_R9C9', row=9, col=9, sq=11,
                 done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef137 = dict(aref='arrRef137', btn=btn_R9C10, btn_str='btn_R9C10', row=9, col=10,
                 sq=11, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef138 = dict(aref='arrRef138', btn=btn_R9C11, btn_str='btn_R9C11', row=9, col=11,
                 sq=11, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef139 = dict(aref='arrRef139', btn=btn_R9C12, btn_str='btn_R9C12', row=9, col=12,
                 sq=11, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef140 = dict(aref='arrRef140', btn=btn_R9C13, btn_str='btn_R9C13', row=9, col=13,
                 sq=12, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef141 = dict(aref='arrRef141', btn=btn_R9C14, btn_str='btn_R9C14', row=9, col=14,
                 sq=12, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef142 = dict(aref='arrRef142', btn=btn_R9C15, btn_str='btn_R9C15', row=9, col=15,
                 sq=12, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef143 = dict(aref='arrRef143', btn=btn_R9C16, btn_str='btn_R9C16', row=9, col=16,
                 sq=12, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef144 = dict(aref='arrRef144', btn=btn_R10C1, btn_str='btn_R10C1', row=10, col=1, sq=9, done=False,
                 nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef145 = dict(aref='arrRef145', btn=btn_R10C2, btn_str='btn_R10C2', row=10, col=2, sq=9, done=False,
                 nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef146 = dict(aref='arrRef146', btn=btn_R10C3, btn_str='btn_R10C3', row=10, col=3, sq=9, done=False,
                 nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef147 = dict(aref='arrRef147', btn=btn_R10C4, btn_str='btn_R10C4', row=10, col=4, sq=9, done=False,
                 nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef148 = dict(aref='arrRef148', btn=btn_R10C5, btn_str='btn_R10C5', row=10, col=5,
                 sq=10, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef149 = dict(aref='arrRef149', btn=btn_R10C6, btn_str='btn_R10C6', row=10, col=6,
                 sq=10, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef150 = dict(aref='arrRef150', btn=btn_R10C7, btn_str='btn_R10C7', row=10, col=7,
                 sq=10, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef151 = dict(aref='arrRef151', btn=btn_R10C8, btn_str='btn_R10C8', row=10, col=8,
                 sq=10, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef152 = dict(aref='arrRef152', btn=btn_R10C9, btn_str='btn_R10C9', row=10, col=9,
                 sq=11, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef153 = dict(aref='arrRef153', btn=btn_R10C10, btn_str='btn_R10C10', row=10, col=10,
                 sq=11, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef154 = dict(aref='arrRef154', btn=btn_R10C11, btn_str='btn_R10C11', row=10, col=11,
                 sq=11, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef155 = dict(aref='arrRef155', btn=btn_R10C12, btn_str='btn_R10C12', row=10, col=12,
                 sq=11, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef156 = dict(aref='arrRef156', btn=btn_R10C13, btn_str='btn_R10C13', row=10, col=13,
                 sq=12, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef157 = dict(aref='arrRef157', btn=btn_R10C14, btn_str='btn_R10C14', row=10, col=14,
                 sq=12, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef158 = dict(aref='arrRef158', btn=btn_R10C15, btn_str='btn_R10C15', row=10, col=15,
                 sq=12, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef159 = dict(aref='arrRef159', btn=btn_R10C16, btn_str='btn_R10C16', row=10, col=16,
                 sq=12, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef160 = dict(aref='arrRef160', btn=btn_R11C1, btn_str='btn_R11C1', row=11, col=1, sq=9, done=False,
                 nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef161 = dict(aref='arrRef161', btn=btn_R11C2, btn_str='btn_R11C2', row=11, col=2, sq=9, done=False,
                 nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef162 = dict(aref='arrRef162', btn=btn_R11C3, btn_str='btn_R11C3', row=11, col=3, sq=9, done=False,
                 nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef163 = dict(aref='arrRef163', btn=btn_R11C4, btn_str='btn_R11C4', row=11, col=4,
                 sq=9, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef164 = dict(aref='arrRef164', btn=btn_R11C5, btn_str='btn_R11C5', row=11, col=5,
                 sq=10, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef165 = dict(aref='arrRef165', btn=btn_R11C6, btn_str='btn_R11C6', row=11, col=6,
                 sq=10, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef166 = dict(aref='arrRef166', btn=btn_R11C7, btn_str='btn_R11C7', row=11, col=7,
                 sq=10, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef167 = dict(aref='arrRef167', btn=btn_R11C8, btn_str='btn_R11C8', row=11, col=8,
                 sq=10, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef168 = dict(aref='arrRef168', btn=btn_R11C9, btn_str='btn_R11C9', row=11, col=9,
                 sq=11, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef169 = dict(aref='arrRef169', btn=btn_R11C10, btn_str='btn_R11C10', row=11, col=10,
                 sq=11, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef170 = dict(aref='arrRef170', btn=btn_R11C11, btn_str='btn_R11C11', row=11, col=11,
                 sq=11, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef171 = dict(aref='arrRef171', btn=btn_R11C12, btn_str='btn_R11C12', row=11, col=12,
                 sq=11, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef172 = dict(aref='arrRef172', btn=btn_R11C13, btn_str='btn_R11C13', row=11, col=13,
                 sq=12, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef173 = dict(aref='arrRef173', btn=btn_R11C14, btn_str='btn_R11C14', row=11, col=14,
                 sq=12, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef174 = dict(aref='arrRef174', btn=btn_R11C15, btn_str='btn_R11C15', row=11, col=15,
                 sq=12, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef175 = dict(aref='arrRef175', btn=btn_R11C16, btn_str='btn_R11C16', row=11, col=16,
                 sq=12, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef176 = dict(aref='arrRef176', btn=btn_R12C1, btn_str='btn_R12C1', row=12, col=1,
                 sq=9, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef177 = dict(aref='arrRef177', btn=btn_R12C2, btn_str='btn_R12C2', row=12, col=2, sq=9, done=False,
                 nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef178 = dict(aref='arrRef178', btn=btn_R12C3, btn_str='btn_R12C3', row=12, col=3, sq=9, done=False,
                 nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef179 = dict(aref='arrRef179', btn=btn_R12C4, btn_str='btn_R12C4', row=12, col=4,
                 sq=9, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef180 = dict(aref='arrRef180', btn=btn_R12C5, btn_str='btn_R12C5', row=12, col=5,
                 sq=10, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef181 = dict(aref='arrRef181', btn=btn_R12C6, btn_str='btn_R12C6', row=12, col=6,
                 sq=10, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef182 = dict(aref='arrRef182', btn=btn_R12C7, btn_str='btn_R12C7', row=12, col=7,
                 sq=10, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef183 = dict(aref='arrRef183', btn=btn_R12C8, btn_str='btn_R12C8', row=12, col=8,
                 sq=10, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef184 = dict(aref='arrRef184', btn=btn_R12C9, btn_str='btn_R12C9', row=12, col=9,
                 sq=11, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef185 = dict(aref='arrRef185', btn=btn_R12C10, btn_str='btn_R12C10', row=12, col=10,
                 sq=11, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef186 = dict(aref='arrRef186', btn=btn_R12C11, btn_str='btn_R12C11', row=12, col=11,
                 sq=11, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef187 = dict(aref='arrRef187', btn=btn_R12C12, btn_str='btn_R12C12', row=12, col=12,
                 sq=11, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef188 = dict(aref='arrRef188', btn=btn_R12C13, btn_str='btn_R12C13', row=12, col=13,
                 sq=12, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef189 = dict(aref='arrRef189', btn=btn_R12C14, btn_str='btn_R12C14', row=12, col=14,
                 sq=12, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef190 = dict(aref='arrRef190', btn=btn_R12C15, btn_str='btn_R12C15', row=12, col=15,
                 sq=12, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef191 = dict(aref='arrRef191', btn=btn_R12C16, btn_str='btn_R12C16', row=12, col=16,
                 sq=12, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef192 = dict(aref='arrRef192', btn=btn_R13C1, btn_str='btn_R13C1', row=13, col=1,
                 sq=13, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef193 = dict(aref='arrRef193', btn=btn_R13C2, btn_str='btn_R13C2', row=13, col=2,
                 sq=13, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef194 = dict(aref='arrRef194', btn=btn_R13C3, btn_str='btn_R13C3', row=13, col=3,
                 sq=13, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef195 = dict(aref='arrRef195', btn=btn_R13C4, btn_str='btn_R13C4', row=13, col=4,
                 sq=13, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef196 = dict(aref='arrRef196', btn=btn_R13C5, btn_str='btn_R13C5', row=13, col=5,
                 sq=14, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef197 = dict(aref='arrRef197', btn=btn_R13C6, btn_str='btn_R13C6', row=13, col=6,
                 sq=14, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef198 = dict(aref='arrRef198', btn=btn_R13C7, btn_str='btn_R13C7', row=13, col=7,
                 sq=14, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef199 = dict(aref='arrRef199', btn=btn_R13C8, btn_str='btn_R13C8', row=13, col=8,
                 sq=14, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef200 = dict(aref='arrRef200', btn=btn_R13C9, btn_str='btn_R13C9', row=13, col=9,
                 sq=15, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef201 = dict(aref='arrRef201', btn=btn_R13C10, btn_str='btn_R13C10', row=13, col=10,
                 sq=15, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef202 = dict(aref='arrRef202', btn=btn_R13C11, btn_str='btn_R13C11', row=13, col=11,
                 sq=15, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef203 = dict(aref='arrRef203', btn=btn_R13C12, btn_str='btn_R13C12', row=13, col=12,
                 sq=15, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef204 = dict(aref='arrRef204', btn=btn_R13C13, btn_str='btn_R13C13', row=13, col=13,
                 sq=16, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef205 = dict(aref='arrRef205', btn=btn_R13C14, btn_str='btn_R13C14', row=13, col=14,
                 sq=16, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef206 = dict(aref='arrRef206', btn=btn_R13C15, btn_str='btn_R13C15', row=13, col=15,
                 sq=16, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef207 = dict(aref='arrRef207', btn=btn_R13C16, btn_str='btn_R13C16', row=13, col=16,
                 sq=16, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef208 = dict(aref='arrRef208', btn=btn_R14C1, btn_str='btn_R14C1', row=14, col=1,
                 sq=13, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef209 = dict(aref='arrRef209', btn=btn_R14C2, btn_str='btn_R14C2', row=14, col=2,
                 sq=13, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef210 = dict(aref='arrRef210', btn=btn_R14C3, btn_str='btn_R14C3', row=14, col=3,
                 sq=13, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef211 = dict(aref='arrRef211', btn=btn_R14C4, btn_str='btn_R14C4', row=14, col=4,
                 sq=13, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef212 = dict(aref='arrRef212', btn=btn_R14C5, btn_str='btn_R14C5', row=14, col=5,
                 sq=14, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef213 = dict(aref='arrRef213', btn=btn_R14C6, btn_str='btn_R14C6', row=14, col=6,
                 sq=14, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef214 = dict(aref='arrRef214', btn=btn_R14C7, btn_str='btn_R14C7', row=14, col=7,
                 sq=14, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef215 = dict(aref='arrRef215', btn=btn_R14C8, btn_str='btn_R14C8', row=14, col=8,
                 sq=14, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef216 = dict(aref='arrRef216', btn=btn_R14C9, btn_str='btn_R14C9', row=14, col=9,
                 sq=15, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef217 = dict(aref='arrRef217', btn=btn_R14C10, btn_str='btn_R14C10', row=14, col=10,
                 sq=15, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef218 = dict(aref='arrRef218', btn=btn_R14C11, btn_str='btn_R14C11', row=14, col=11,
                 sq=15, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef219 = dict(aref='arrRef219', btn=btn_R14C12, btn_str='btn_R14C12', row=14, col=12,
                 sq=15, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef220 = dict(aref='arrRef220', btn=btn_R14C13, btn_str='btn_R14C13', row=14, col=13,
                 sq=16, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef221 = dict(aref='arrRef221', btn=btn_R14C14, btn_str='btn_R14C14', row=14, col=14,
                 sq=16, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef222 = dict(aref='arrRef222', btn=btn_R14C15, btn_str='btn_R14C15', row=14, col=15,
                 sq=16, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef223 = dict(aref='arrRef223', btn=btn_R14C16, btn_str='btn_R14C16', row=14, col=16,
                 sq=16, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef224 = dict(aref='arrRef224', btn=btn_R15C1, btn_str='btn_R15C1', row=15, col=1,
                 sq=13, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef225 = dict(aref='arrRef225', btn=btn_R15C2, btn_str='btn_R15C2', row=15, col=2,
                 sq=13, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef226 = dict(aref='arrRef226', btn=btn_R15C3, btn_str='btn_R15C3', row=15, col=3,
                 sq=13, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef227 = dict(aref='arrRef227', btn=btn_R15C4, btn_str='btn_R15C4', row=15, col=4,
                 sq=13, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef228 = dict(aref='arrRef228', btn=btn_R15C5, btn_str='btn_R15C5', row=15, col=5,
                 sq=14, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef229 = dict(aref='arrRef229', btn=btn_R15C6, btn_str='btn_R15C6', row=15, col=6,
                 sq=14, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef230 = dict(aref='arrRef230', btn=btn_R15C7, btn_str='btn_R15C7', row=15, col=7,
                 sq=14, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef231 = dict(aref='arrRef231', btn=btn_R15C8, btn_str='btn_R15C8', row=15, col=8,
                 sq=14, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef232 = dict(aref='arrRef232', btn=btn_R15C9, btn_str='btn_R15C9', row=15, col=9,
                 sq=15, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef233 = dict(aref='arrRef233', btn=btn_R15C10, btn_str='btn_R15C10', row=15, col=10,
                 sq=15, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef234 = dict(aref='arrRef234', btn=btn_R15C11, btn_str='btn_R15C11', row=15, col=11,
                 sq=15, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef235 = dict(aref='arrRef235', btn=btn_R15C12, btn_str='btn_R15C12', row=15, col=12,
                 sq=15, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef236 = dict(aref='arrRef236', btn=btn_R15C13, btn_str='btn_R15C13', row=15, col=13,
                 sq=16, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef237 = dict(aref='arrRef237', btn=btn_R15C14, btn_str='btn_R15C14', row=15, col=14,
                 sq=16, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef238 = dict(aref='arrRef238', btn=btn_R15C15, btn_str='btn_R15C15', row=15, col=15,
                 sq=16, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef239 = dict(aref='arrRef239', btn=btn_R15C16, btn_str='btn_R15C16', row=15, col=16,
                 sq=16, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef240 = dict(aref='arrRef240', btn=btn_R16C1, btn_str='btn_R16C1', row=16, col=1,
                 sq=13, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef241 = dict(aref='arrRef241', btn=btn_R16C2, btn_str='btn_R16C2', row=16, col=2,
                 sq=13, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef242 = dict(aref='arrRef242', btn=btn_R16C3, btn_str='btn_R16C3', row=16, col=3,
                 sq=13, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef243 = dict(aref='arrRef243', btn=btn_R16C4, btn_str='btn_R16C4', row=16, col=4,
                 sq=13, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef244 = dict(aref='arrRef244', btn=btn_R16C5, btn_str='btn_R16C5', row=16, col=5,
                 sq=14, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef245 = dict(aref='arrRef245', btn=btn_R16C6, btn_str='btn_R16C6', row=16, col=6,
                 sq=14, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef246 = dict(aref='arrRef246', btn=btn_R16C7, btn_str='btn_R16C7', row=16, col=7,
                 sq=14, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef247 = dict(aref='arrRef247', btn=btn_R16C8, btn_str='btn_R16C8', row=16, col=8,
                 sq=14, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef248 = dict(aref='arrRef248', btn=btn_R16C9, btn_str='btn_R16C9', row=16, col=9,
                 sq=15, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef249 = dict(aref='arrRef249', btn=btn_R16C10, btn_str='btn_R16C10', row=16, col=10,
                 sq=15, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef250 = dict(aref='arrRef250', btn=btn_R16C11, btn_str='btn_R16C11', row=16, col=11,
                 sq=15, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef251 = dict(aref='arrRef251', btn=btn_R16C12, btn_str='btn_R16C12', row=16, col=12,
                 sq=15, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef252 = dict(aref='arrRef252', btn=btn_R16C13, btn_str='btn_R16C13', row=16, col=13,
                 sq=16, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef253 = dict(aref='arrRef253', btn=btn_R16C14, btn_str='btn_R16C14', row=16, col=14,
                 sq=16, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef254 = dict(aref='arrRef254', btn=btn_R16C15, btn_str='btn_R16C15', row=16, col=15,
                 sq=16, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")
arrRef255 = dict(aref='arrRef255', btn=btn_R16C16, btn_str='btn_R16C16', row=16, col=16,
                 sq=16, done=False, nums=startingString, width=6, height=hit, font=labelfont, fg="black")

# arrRefs_set = set([arrRef0, arrRef1, arrRef2, arrRef3,
#                   arrRef4, arrRef5, arrRef6, arrRef7])
arrRefs_setq = set(['arrRef0', 'arrRef1', 'arrRef2', 'arrRef3',
                    'arrRef4', 'arrRef5', 'arrRef6', 'arrRef7'])
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

if __name__ == '__main__':
    make_arefs()
    root.mainloop()

    # clear_current_history_file()
