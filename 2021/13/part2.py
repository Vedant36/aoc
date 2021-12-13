#!/usr/bin/env python3

from part1 import *

def main():
	poi, folds = filter_data()

	a = poi.copy()
	for i in folds[0:]:
		axis=0
		if 'y' in i:
			axis=1
		line = int(i.split('=')[1])
		a = fold(a, axis, line)

	ans = ''
	min, max = a.min(0), a.max(0)
	k = set([tuple(i) for i in fold(a, 0, 655)])
	for i in range(min[1], max[1]+1):
		for j in range(min[0], max[0]+1):
			if (j,i) in k:
				ans+='QQ'
			else:
				ans+='  '
		ans+='\n'

	return ans

if __name__ == '__main__':
	print(main())
