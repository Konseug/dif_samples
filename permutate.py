from itertools import permutations
from random import sample, shuffle

N = 10 # Число участников
GROUPS = (5, 5) # Распределение участников по группам

N_GR = len(GROUPS)

def delta_reps():
    reps = [[0] * N for _ in range(N)]
    for block in blocks:
        for line in block:
            for elem in line:
                for part in parts:
                    if part != elem and part in line:
                        reps[parts.index(elem)][parts.index(part)] += 1
    for i in range(N):
        reps[i][i] = reps[2][3]        
    min_rep = min([min(line) for line in reps])
    max_rep = max([max(line) for line in reps])
    delta = max_rep - min_rep
    return delta


def print_reps_table():
    reps = [[0] * N for _ in range(N)]
    for block in blocks:
        for line in block:
            for elem in line:
                for part in parts:
                    if part != elem and part in line:
                        reps[parts.index(elem)][parts.index(part)] += 1
    print(('   ' + '{:>3}' * N).format(*parts))
    for i in range(N):
        reps[i][i] = ''
    for i, line in enumerate(reps):
        print(('{:>3}' * (N + 1)).format(parts[i], *line))
    for i in range(N):
        reps[i][i] = reps[2][3]
    min_rep = min([min(line) for line in reps])
    max_rep = max([max(line) for line in reps])
    delta = max_rep - min_rep       
    print('MIN =', min_rep)
    print('MAX =', max_rep)
    print('DELTA =', delta)   


blocks = []
parts = list('0123456789abdef')[:N]
rand_box = parts[:]
if N_GR == 3:
    blocks.append([rand_box[:GROUPS[0]], rand_box[GROUPS[0]:-GROUPS[2]], rand_box[-GROUPS[2]:]])
else:
    blocks.append([rand_box[:GROUPS[0]], rand_box[GROUPS[0]:]])
for i in range(7):
    min_delta = 100
    for _ in range(100000):
        shuffle(rand_box)
        if N_GR == 3: 
            blocks.append([rand_box[:GROUPS[0]], rand_box[GROUPS[0]:-GROUPS[2]], rand_box[-GROUPS[2]:]])
        else:
            blocks.append([rand_box[:GROUPS[0]], rand_box[GROUPS[0]:]])
        cur_delta = delta_reps()
        if cur_delta < min_delta:
            best_box = rand_box[:]
            min_delta = cur_delta
        blocks.pop()
    if N_GR == 3:
        blocks.append([best_box[:GROUPS[0]], best_box[GROUPS[0]:-GROUPS[2]], best_box[-GROUPS[2]:]])
    else:
        blocks.append([best_box[:GROUPS[0]], best_box[GROUPS[0]:]])
for b in blocks:
    for l in b:
        [print(el, end='') for el in l]
        print()
    print()
print_reps_table()
