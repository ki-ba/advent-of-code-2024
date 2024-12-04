def max(a, b):
    if (a < b):
        return b
    else:
        return a

def min(a, b):
    if (a < b):
        return a
    else:
        return b


left = [] 
right = []
duo = []
with open("input.txt") as file:
    diff = 0
    lines = [line.rstrip() for line in file]
    for l in lines:
        t = l.split("   ")
        left.append(int(t[0]))
        right.append(int(t[1]))

left.sort()
right.sort()
for i in range(len(left)):
    diff += max(left[i], right[i]) - min(left[i], right[i]) 
print("DIFF = ",diff)

sim = 0;
for l in left:
    for r in right:
        if (r == l):
            print(l, " = ", r ," : ", sim + 1)
            sim += l
print("SIM = ",sim)
