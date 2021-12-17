#!/usr/bin/env python3

from part1 import *

def main():
	data = filter_data()
	return sum([i<j for i,j in zip(data[:-3],data[3:])])

if __name__ == '__main__':
	print(main())
