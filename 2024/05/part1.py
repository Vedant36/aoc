#!/usr/bin/env python3

import numpy as np

def filter_data():
    qwe, wer = open('input', 'r').read().split('\n\n')
    qwe = list(map(lambda a: a.split('|'), qwe.split('\n')))
    wer = list(map(lambda a: a.split(','), wer.split('\n')))
    return qwe, wer

qwe, wer = filter_data()
qwe = np.asarray(qwe)
wer = [[int(j) for j in i] for i in wer]

answer = 0
for update in wer:
    correct_order = True
    for n, page in enumerate(update):
        before = []
        after = []
        for a,b in qwe:
            if a == page:
                after.append(b)
            if b == page:
                before.append(a)
        if set(after).intersection(set(update[:n])):
            correct_order = False
            break
        if set(before).intersection(set(update[n+1:])):
            correct_order = False
            break
    if not correct_order:
        print(after, before, update)
        break
        answer += update[(len(update) + 1) // 2]
