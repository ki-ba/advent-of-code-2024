import re

numbers = []
summ = 0
do = True
with open('input.txt', 'r') as file:
    f = file.read()
x = re.findall("do\(\)|don't\(\)|mul\([0-9]{1,3},[0-9]{1,3}\)", f)
for mul in x:
    if (mul == "do()"):
        do = True
    elif (mul == "don't()"):
        do = False
    elif (do):
        numbers.append(re.findall("[0-9]{1,3}",mul))
for tup in numbers:
    summ += int(tup[0]) * int(tup[1])
print(summ)
