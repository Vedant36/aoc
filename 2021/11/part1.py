#!/usr/bin/env python3

import numpy as np

def filter_data():
	with open('input', 'r') as fp:
		data = np.asarray([ list(i) for i in fp.read().splitlines() ], dtype=int)
		return data

def step(data_):
    data = data_.copy()
    data+=1
    flashed = []
    while np.sum(data>9)>len(flashed):
        for n1,i in enumerate(data):
            for n2,j in enumerate(i):
                if j>9 and (n1,n2) not in flashed:
                    data[n1-1 if n1 else 0:n1+2,n2-1 if n2 else 0:n2+2]+=1
                    flashed.append((n1,n2))
    for i in flashed:
        data[i]=0
    return data,len(flashed)

def main():
	data = filter_data()
	a,temp = step(data)
	flashes = temp
	for i in range(99):
		a,temp = step(a)
		flashes+= temp
	return flashes

if __name__ == '__main__':
	print(main())
