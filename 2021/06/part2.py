#!/usr/bin/env python3

from part1 import *

def simulate(data_, days):
	data = data_.copy()
	counts = [ data.count(i) for i in range(9) ]
	for i in range(days):
		temp = counts.pop(0)
		counts.append(temp)
		counts[6]+=temp
	return counts


def main():
	data = filter_data()
	return sum(simulate(data, 256))

if __name__ == '__main__':
	print(main())

