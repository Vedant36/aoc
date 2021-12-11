#!/usr/bin/env python3

from part1 import *

def main():
	data = filter_data()
	a = step(data)[0]
	i=1
	while True:
		a = step(a)[0]
		i+=1
		if np.sum(a)==0:
			return i

if __name__ == '__main__':
	print(main())
