#!/usr/bin/env python3
import numpy as np

def count_turns(board, calls):
    mask = np.zeros((5,5))
    for turn,i in enumerate(calls):
        for n,j in enumerate(board):
            if i in j:
                mask[n,j.index(i)]=1
        if 5 in mask.sum(axis=0) or 5 in mask.sum(axis=1):
            return turn, mask

def filter_data():
	with open('input', 'r') as fp:
		data = fp.read().splitlines()
		calls = eval(data.pop(0))
		boards=[]
		for i in data:
			if i == '':
				boards.append([])
			else:
				boards[-1].append([int(i) for i in i.split(' ') if i!=''])
		return calls, boards


def main():
	calls, boards = filter_data()
	counts = [count_turns(i, calls)[0] for i in boards]
	min_index = np.argmin(counts)
	count, mask = count_turns(boards[min_index], calls)
	return calls[count] * np.sum(np.asarray(boards[min_index]) * (1 - count_turns(boards[min_index], calls)[1]))


if __name__ == '__main__':
	print(main())
