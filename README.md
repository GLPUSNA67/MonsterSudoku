The objective is to have a program that will initialize (fill in the starting values of) a published Monster Sudoku (16x16x16) puzzle and 
use functions to either solve individual cells or to simplify the puzzle so that other functions can solve individual cells.
For those not familiar with Monster Sudoku: a standard Sudoku has 9 rows, 9 columns, and 9 3X3 squares; the numbers 1 through 9 must be
present in every row, column, and square. In Monster Sudoku there are 16 rows, 16 columns, and 16 squares and the hexadecimal numbers 
0 through 9 and A through F are used. (There are some puzzles that use 1-9 and A-G.)
Note: The developer is not a professional programmer. This will be obvious when you look at the code. I just want to set the bar low. 
A set of functions to save and load the initial puzzle is needed, but not yet developed. Currently, the puzzle must be saved by manually copying 
the current values and reloading those values -- ugly! (First, make it work, then improve on it.)
The program uses Tkinter for the GUI and many variable structures to both update and maintain the puzzle cell value -- the numbers that remain
in each cell, and each row, column, and square (RCS), the number and identity of cells that have been completed and remain to be completed, and
various housekeeping and control structures that control the program flow.
Key concepts: Maintain the values of each cell in dictionary structures with keys that allow easy access to those values. Identify patterns that
will either solve an individual cell or simplify the puzzle by reducing the number of potential numbers in cells and implement structures and functions that
will update the puzzle values, store the current values in a data structure, call a function that will update the puzzle with the current values, 
notify the user of the current status of the puzzle so he/she can choose a function that will further solve or simplify the puzzle.
When I say select, I mean click on the item. That could be a number in the number pad on the top right corner of the form, or a cell in the puzzle.
For example, start with a list of all cells. When initializing the puzzle, (from a published source) select a number from the number pad, then select a cell to set its value. 
When that cell is updated, the value in the cell structure is updated, the font size is increased, the color is changed (both make solved cells highly visible), 
the cell is marked "Done," the cell is removed from a "list of cells not done," the number of cells "Done" and "Not Done" is updated, for each cell in the 
same row, column, and square, the number solved for is removed from the list of numbers remaining, and, after all the cells have been updated, the puzzle display is refreshed.
After the puzzle has been initialized, it is manually saved. 
Next, a sequence of known patterns is used to solve the puzzle or simplify it. The first and easiest function to select is: "Only one number" (in a cell). 
If there is only one number remaining in a cell, it must be the correct number. So, update that cell with that number, update the rest of the related RCS cells,
refresh the puzzle, and repeat the process for every other cell that isn't done. (Python psudocode: For every cell in "Not Done List", if the number of "numbers"
in the cell == 1, set the value of the cell to the cell value, update all the structure variables, and refresh the puzzle.
A second function is similar, but more complicated. For every row, column, and square, make a list of all the values of every cell in that RCS. For every one of those
lists, check to see if any number only occurs once. For example, a row might have the following numbers reamining (123451341245567678AB3ABCDACD). The number 8 only 
appears once in that list. Therefore, it must be the value of the cell it is in. So, find the cell that has an 8 in it, make the value of that cell 8, and update the 
puzzle. 
Sometimes, you can't find a solution, but you can simplify the puzzle my removing some of the remaining numbers. One pattern that occurs regularly is where two cells
in a row have the same two numbers. So, cells 5 and 13 may both have the values (7, B). Since one cell must have one number and the other cell must have the other number,
we can remove those numbers from all other cells in that row. Use a similar procedure for every RCS. Also, use a similar function for 3, 4 and 5 numbers. 
However, there is a problem with 3 and larger matches! A triple can consist of 3 numbers in 3 different cells, but those numbers can be consist of 2 or 3 numbers in each cell.
For example, a valid triple might be (0, 1) (1, 2) and (0, 2), or one of the cells might have (0, 1, 2). It gets more complicated with quads (4 numbers) and quints (5 numbers). 
After each variaton of this process has been completed, go back the the find "Only one number" functions and try them again. 
Continue cycling through these functions/procedures until there are no more updates -- until the number of cells done doesn't increase. 
There are other patterns that can be applied and are being developed, but with a low priority.
An additional feature of the program is that it is not a black box. Every time a runction finds a solution or simplifys the puzzle, there should be a print out of 
what the program did. In the bottom right corner, there are two text boxes that have potentially helpful information for the user. The top box lists potential solutions
for only one number, duples, etc. The bottom box lists "hints" for potential actions to take. For example, the bottom right text box may have "Triple S15." That means
the user should look for a possible triple in Square 15. (Row, Column and Square numbers start with number 1 and go through 16. This numbering system is easier to keep
track of than a 0 based system and is only used for the user interface.)
There are several unresolved issues with the program. One issue is that sometimes there is only one number in a cell and clicking on the "Solve RCS" button doesn't solve
the cell. In these cases, select the number to be updated, then select the cell. This will cause a manual update of the cell and the puzzle.  
Please feel free to provide suggestions for improving this document.
More to come.
