# based on nitekat1124 's solution : https://github.com/nitekat1124/advent-of-code-2024/blob/main/solutions/day04.py

import regex as re

def create_lists():
    with open("input") as file:
        lines = [line.rstrip() for line in file]
    return (lines)

lst = create_lists()

lst2 = lst[:]
for col in range(len(lst2[0])):
    column = [] 
    for row in lst:
        column.append(row[col])
    lst2.append("".join(column))

rows, cols = len(lst), len(lst[0])
main_diagonals = {}
anti_diagonals = {}

for r in range(rows):
    for c in range(cols):
        main_key = r - c
        if main_key not in main_diagonals:
            main_diagonals[main_key] = []
        main_diagonals[main_key].append(lst[r][c])

        anti_key = r + c
        if anti_key not in anti_diagonals:
            anti_diagonals[anti_key] = []
        anti_diagonals[anti_key].append(lst[r][c])


lst2.extend(["".join(i) for i in main_diagonals.values()])
lst2.extend(["".join(i) for i in anti_diagonals.values()])



#print(lst2)
nb = 0
for line in lst2:
    sub = re.findall("XMAS",line, overlapped=True)
    nb += len(sub) 
    sub = re.findall("SAMX",line, overlapped=True)
    nb += len(sub) 
print(nb)

count = 0
_set = {"M","S"}
for r in range(1, len(lst) - 1):
    for c in range(1, len(lst[0]) - 1):
        if (lst[r][c] == 'A'):
            if ({lst[r-1][c-1], lst[r+1][c+1]} == _set and {lst[r+1][c-1], lst[r-1][c+1]} == _set):
                 count += 1
print(count)
