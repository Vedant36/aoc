#!/usr/bin/env python3

from part1 import *

def main():
	data = filter_data()
	x,y,aim=0,0,0
	for i in data:
		X = int(i.split()[1])
		if i[0]=='f':
			x+=X
			y+=aim*X
		elif i[0]=='u':
			aim-=X
		elif i[0]=='d':
			aim+=X
	return x*y

if __name__ == '__main__':
	print(main())
