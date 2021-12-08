#!/usr/bin/env python3

from part1 import *

def solve(data):
	num = [ 'abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg' ]
	q,a = [ i.split() for i in data.split(' | ') ]
	u = np.unique(list(''.join(q)), return_counts=1)[1] + np.unique(list(''.join([i for i in q if len(i)!=4])), return_counts=1)[1]
	u_ = [16,11,15,13,8,17,14]
	o1 = { j:i for i,j in zip(u, 'abcdefg') }
	o2 = { i:j for i,j in zip(u_, 'abcdefg') }
	return int(''.join([str(([set(i) for i in num]).index(set(''.join([ o2[o1[i]] for i in j])))) for j in a]))

def main():
	data = filter_data()
	return sum([solve(i) for i in data])

if __name__ == '__main__':
	print(main())
