#!/usr/bin/env python3

import numpy as np

def filter_data():
	with open('input', 'r') as fp:
		data = np.asarray([list(i) for i in fp.read().splitlines()], dtype=int)
		return data

def Dijkstra(dataset, source, destination):
	U = {} # unvisited
	T = {}
	for i in dataset:
		U[i] = np.inf
		T[i] = np.inf
	U[source] = 0
	T[source] = 0
	I = {source} # intermediate
	while U:
		min = np.inf
		for i in I:
			if U[i]<min:
				min = U[i]
				C = i
		for i in [(C[0]-1,C[1]),(C[0],C[1]-1),(C[0]+1,C[1]),(C[0],C[1]+1)]:
			if i in U:
				I.add(i)
				temp = U[C] + dataset[i]
				if U[i]>temp:
					U[i] = temp
					T[i] = temp
		U.pop(C)
		I.discard(C)
	return T

def main():
	data = filter_data()
	
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

