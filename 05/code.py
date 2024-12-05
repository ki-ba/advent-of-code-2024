import re, math, functools

def create_lines():
    with open('input.txt') as file:
        lines = [line.rstrip() for line in file]
    return(lines)

def create_updates_array(lines):
    updates = []
    for line in lines:
        updates_sequence = []
        a = re.search('([0-9]{2},?){3,}', line) 
        if a:
            updates_sequence = re.findall('[0-9]{2}', line) 
        if updates_sequence:
            updates.append(updates_sequence)
    return (updates)

def create_rules_array(lines):
    rules = []
    for line in lines:
        rule = []
        a = re.search('[0-9]{2}\\|[0-9]{2}', line)
        if a:
            rule.append(a[0][:2])
            rule.append(a[0][3:])
            rules.append(rule)
    return (rules)



def create_rules_dict(rules):
    _dict = {}
    for rule in rules:
        if rule[1] not in _dict:
            _dict[rule[1]] = []
        _dict[rule[1]].append(rule[0])
    return (_dict)


lines = create_lines()
rules = create_rules_array(lines)
_dict = create_rules_dict(rules)
updates = create_updates_array(lines)


def is_update_sequence_correct(seq,_dict):
    for update in seq:
        i = seq.index(update)    
        for up2 in seq[i+1:]:
            if update in _dict:
                if up2 in _dict[update]:
                    return False
    return True


def sum_middle_correct_updates(updates, _dict):
    _sum = 0
    for u in updates:
        if(is_update_sequence_correct(u, _dict)):
            _sum += int(u[math.floor(len(u)/2)])
    return (_sum)

def create_incorrect_updates(updates):
    incorrect_updates = []
    for seq in updates:
        if is_update_sequence_correct(seq, _dict) == False:
            incorrect_updates.append(seq)
    return incorrect_updates

def comp_two_updates(a, b):
    if (b in _dict):
        if (a in _dict[b]):
            return -1
    if (a in _dict):
        if (b in _dict[b]):
            return 1
    return 0


_sum = sum_middle_correct_updates(updates, _dict)
print(_sum) # solution to part 1

incorrect_updates = create_incorrect_updates(updates)

for u in incorrect_updates:
    u.sort(key=functools.cmp_to_key(comp_two_updates))

_sum = 0
for u in incorrect_updates:
    _sum += int(u[math.floor(len(u)/2)])
print(_sum) # solution to part 2
