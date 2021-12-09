#!/usr/bin/env python3

import numpy as np

def filter_data():
	with open('input', 'r') as fp:
		data = np.asarray([list(i) for i in fp.read().splitlines()], dtype=int)
		return data

def solve(data):
	risk = 0
	for n1,i in enumerate(data):
		for n2,j in enumerate(i):
			temp = []
			if n1!=0: temp.append(data[n1-1,n2])
			if n2!=0: temp.append(data[n1,n2-1])
			if n1!=data.shape[0]-1: temp.append(data[n1+1,n2])
			if n2!=data.shape[1]-1: temp.append(data[n1,n2+1])
			if np.sum(j>=np.asarray(temp))==0:
				risk+=j+1
	return risk

def main():
	data = filter_data()
	return solve(data)

if __name__=='__main__':
	print(main())
