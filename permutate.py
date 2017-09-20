from itertools import permutations
from random import sample, shuffle

N = 10 #amount of members
GROUPS = (5, 5) #quantities of members per group
PERMUTATIONS_RANGE = 100000

PARTS = list('0123456789abdefghijklmnopqrstuvwxyz')[:N]
COUNT_GR = len(GROUPS)

разница
def rep_list():
    #return spreadsheet of repeating meetings
    reps = [[0] * N for _ in range(N)]
    for block in blocks:
        for line in block:
            for elem in line:
                for part in PARTS:
                    if part != elem and part in line:
                        reps[PARTS.index(elem)][PARTS.index(part)] += 1
    for i in range(N):
        reps[i][i] = reps[2][1] 
    return reps


def delta_reps():
    #return difference between max and min number of repeating meetings
    reps  = rep_list()
    min_rep = min([min(line) for line in reps])
    max_rep = max([max(line) for line in reps])
    delta = max_rep - min_rep
    return delta


def print_reps_table():
    #print spreadsheet of repeating meetings
    reps  = rep_list()
    print(('   ' + '{:>3}' * N).format(*PARTS))
    for i in range(N):
        reps[i][i] = ''
    for i, line in enumerate(reps):
        print(('{:>3}' * (N + 1)).format(PARTS[i], *line))
    for i in range(N):
        reps[i][i] = reps[2][1]
    min_rep = min([min(line) for line in reps])
    max_rep = max([max(line) for line in reps])
    delta = max_rep - min_rep
    print('MIN =', min_rep)
    print('MAX =', max_rep)
    print('DELTA =', delta)


def main():
    blocks = []
    rand_box = PARTS[:]
    if COUNT_GR == 3:
        blocks.append([rand_box[:GROUPS[0]], rand_box[GROUPS[0]:-GROUPS[2]], rand_box[-GROUPS[2]:]])
    else:
        blocks.append([rand_box[:GROUPS[0]], rand_box[GROUPS[0]:]])
    for i in range(7):
        min_delta = 100
        for _ in range(PERMUTATIONS_RANGE):
            shuffle(rand_box)
            if COUNT_GR == 3:
                blocks.append([rand_box[:GROUPS[0]], rand_box[GROUPS[0]:-GROUPS[2]], rand_box[-GROUPS[2]:]])
            else:
                blocks.append([rand_box[:GROUPS[0]], rand_box[GROUPS[0]:]])
            cur_delta = delta_reps()
            if cur_delta < min_delta:
                best_box = rand_box[:]
                min_delta = cur_delta
            blocks.pop()
        if COUNT_GR == 3:
            blocks.append([best_box[:GROUPS[0]], best_box[GROUPS[0]:-GROUPS[2]], best_box[-GROUPS[2]:]])
        else:
            blocks.append([best_box[:GROUPS[0]], best_box[GROUPS[0]:]])
    for block in blocks:
        for line in block:
            [print(elem, end='') for elem in line]
            print()
        print()
    print_reps_table()


if __name__ == '__main__':
    main()
