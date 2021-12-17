#!/usr/bin/env python3

from part1 import *

def main():
	data = filter_data()
	vels = []
	for i in range(0,data[1]+1):
		for j in range(data[2],-data[2]):
			k = solve([i,j],data)
			if k is not None:
				vels.append((i,j))
	return len(vels)

if __name__ == '__main__':
	print(main())
