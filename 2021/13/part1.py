#!/usr/bin/env python3

import numpy as np

def filter_data():
	with open('input', 'r') as fp:
		data = fp.read().splitlines()
		poi, folds = data[:799], data[800:]
		poi = np.asarray([ eval(i) for i in poi ], dtype=int)
		return poi, folds

def fold(poi_, axis, line):
    poi = poi_.copy()
    for i in poi:
        if i[axis]>line:
            i[axis] = 2*line-i[axis]
    return poi

def main():
	poi, folds = filter_data()

	a = poi.copy()
	axis=0
	if 'y' in folds[0]:
		axis=1
	line = int(folds[0].split('=')[1])
	a = fold(a, axis, line)

	k = set([tuple(i) for i in fold(a, 0, 655)])

	return len(k)

if __name__ == '__main__':
	print(main())
