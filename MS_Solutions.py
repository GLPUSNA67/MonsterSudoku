
# import MS_Solutions_data as solution
solution = [["F", 1, 2, 1], ["A", 1, 5, 2], ["9", 8, 9, 8]]
solutionText = ""
entryNums = 0
for entry in solution:
    # print(entry)
    num = solution[entryNums][0]
    row = solution[entryNums][1]
    col = solution[entryNums][2]
    sq = solution[entryNums][3]
    btn = f"btnR{row}C{col}"
    print("currentNumber = ", num)
    print("btn is ", btn)
    solutionText = solutionText + f"currentNumber = {num}\nupdateCell(btnR{row}C{col})\n"
    entryNums += 1

print("Number of entries is ", entryNums)
print("19 solutionText is:")
print(solutionText)
''' I couldn't get file reading and parsing to work.'''
solution = []
# print("22 ", solution)
file = open("MS_Solutions.txt", "r")
# To parse a solution from a file, do the below and convert the output to 
# puzzle update commands. 
# The following will parse the first list into num, row, col, and sq
# this can be duplicated up through RCS = 9, but above that, the index 
# needs to be changes from -1 to -2
print("30")
for line in file:
    # for item in line:
    # solution = solution +  line
    print(line)
    # # l = solution
    # l = solution[1:-1]
    
    # print("31 ", l)
    # # print("32 ", new_l)
    # text = l[1:-1]
    # # results = l.split(',')
    # # print("35 results are ", results)
    # i = text.index(',')
    # # print("40 index i is ", i)
    # num = text[i -2]
    # print("42 num is ", num)
    # text = text[i+1:]
    # i = text.index(',')
    # # print("44 index i is ", i)
    # row = text[i-1]
    # # print("47 text is ", text)
    # print("48 row is ", row)
    # text = text[i+1:]
    # i = text.index(',')
    # col = text[i -1]
    # text = text[i+1:]
    # i = text.index(',')
    # sq = text[i -2]
    # print("55 sq is ", sq)
    # print("36 text is ", text)
    # print("text[0:]", text[0:])
    # print("text[1:]", text[1:])
    # print("text[2:]", text[2:])
    # print("text[1:][1:2]", text[1:][0:1])
    # print(text[1:][4:5])
    # print(text[1:][8:9])
    # print(text[1:][11:12])