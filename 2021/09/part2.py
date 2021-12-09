#!/usr/bin/env python3

from part1 import *

def solve(data):
	locations = []
	for n1,i in enumerate(data):
		for n2,j in enumerate(i):
			temp = []
			if n1!=0: temp.append(data[n1-1,n2])
			if n2!=0: temp.append(data[n1,n2-1])
			if n1!=data.shape[0]-1: temp.append(data[n1+1,n2])
			if n2!=data.shape[1]-1: temp.append(data[n1,n2+1])
			temp = np.asarray(temp)
			temp2 = j>=temp
			if np.sum(temp2)==0:
				locations.append((n1,n2))
	return locations

def flow(z, data, low_points):
	z = tuple(z)
	while z not in low_points:
		temp = {}
		if z[0]!=0:               temp[data[z[0]-1,z[1]]] = (z[0]-1,z[1])
		if z[1]!=0:               temp[data[z[0],z[1]-1]] = (z[0],z[1]-1)
		if z[0]!=data.shape[0]-1: temp[data[z[0]+1,z[1]]] = (z[0]+1,z[1])
		if z[1]!=data.shape[1]-1: temp[data[z[0],z[1]+1]] = (z[0],z[1]+1)
		z = temp[min(temp)]
	return z

def main():
	data = filter_data()
	low_points = solve(data)
	basin_size = {tuple(i):0 for i in low_points}
	for n1,i in enumerate(data):
		for n2,j in enumerate(i):
			if j==9: continue
			else: basin_size[flow((n1,n2), data, low_points)]+=1
	a,b,c = [basin_size[i] for i in sorted(basin_size, key=lambda a: basin_size[a])][-3:]
	return a*b*c


if __name__=='__main__':
	print(main())
