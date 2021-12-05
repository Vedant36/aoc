#!/usr/bin/env python3

import numpy as np

def filter_data():
	with open('input', 'r') as fp:
		data = fp.read().splitlines()
		qwe = []
		for i in data:
			k = i.split(' -> ')
			qwe.append([eval(k[0]),eval(k[1])])
		return qwe

def main():
	data = np.asarray(filter_data())
	board = np.zeros((1000,1000))

	for i in data:
		inc = [ 1 if i[0][0]<i[1][0] else -1, 1 if i[0][1]<i[1][1] else -1 ]
		if i[0][0]==i[1][0]:
			for j in range(i[0][1],i[1][1]+inc[1],inc[1]):
				board[i[0][0], j]+=1
		elif i[0][1]==i[1][1]:
			for j in range(i[0][0],i[1][0]+inc[0],inc[0]):
				board[j, i[0][1]]+=1

	return np.sum(board>1)

if __name__=='__main__':
	print(main())

