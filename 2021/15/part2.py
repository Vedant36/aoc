#!/usr/bin/env python3

from part1 import *

def main():
	data = filter_data()
	a = data.copy()
	a = np.r_[a,(a)%9+1,(a+1)%9+1,(a+2)%9+1,(a+3)%9+1]
	a = np.c_[a,(a)%9+1,(a+1)%9+1,(a+2)%9+1,(a+3)%9+1]
	data = a.copy()
	
	dataset = {}
	for n1,i in enumerate(data):
		for n2,j in enumerate(i):
			dataset[(n1,n2)] = j
	destination = (data.shape[0]-1,data.shape[1]-1)
	del data
	a = Dijkstra(dataset, (0,0), destination)
	return a[destination]

if __name__ == '__main__':
	print(main())

