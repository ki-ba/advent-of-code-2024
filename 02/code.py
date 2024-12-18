lst= []
def create_lists():
    with open("input.txt") as file:
        diff = 0
        lines = [line.rstrip() for line in file]
        for l in lines:
            lst.append(list(map(int, l.split())))
    return (lst)




def is_safe(line):
    safe = True
    sign = ((line[1] - line[0]) > 0)
    for i in range(len(line) - 1):
        if ((line[i+1] - line[i] > 0) != sign):
            safe = False
        if (abs(line[i+1] - line[i]) > 3):
            safe = False
        if (line[i+1] - line[i] == 0):
            safe = False
    return (safe)

safe_nb = 0
lst = create_lists()
for line in lst:
    safe = True
    if (is_safe(line) == False):
        safe = False
        for i in range(len(line)):
            line_popped = line.copy()
            line_popped.pop(i)
            if (is_safe(line_popped)):
                print("The list ", line, "is safe by removing ", line[i], "[", i, "] : ", safe_nb)
                safe = True
                break
    else:
        print("The list ", line, "is safe : ", safe_nb)
    if (safe):
        safe_nb+=1

print(safe_nb)
