#!/usr/bin/env python3

import numpy as np

def filter_data():
	with open('input', 'r') as fp:
		data = fp.read().splitlines()
		return data

def main():
	data = filter_data()
	x,y=0,0
	for i in data:
		if i[0]=='f':
			x+=int(i.split()[1])
		elif i[0]=='u':
			y-=int(i.split()[1])
		elif i[0]=='d':
			y+=int(i.split()[1])
	return x*y

if __name__ == '__main__':
	print(main())
