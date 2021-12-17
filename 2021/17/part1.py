#!/usr/bin/env python3

import numpy as np

def filter_data():
	with open('input', 'r') as fp:
		# data = "target area: x=20..30, y=-10..-5"
		data = fp.read().strip()
		import re
		return [ int(i) for i in re.findall('([-0-9]+)', data) ]

def solve(vel, data):
	pos = [0,0]
	height = 0
	while pos[0]<=data[1] and pos[1]>=data[2]:
		prevpos = pos.copy()
		prevvel = vel.copy()
		pos[0]+= vel[0]
		if pos[1]>height:
			height = pos[1]
		pos[1]+= vel[1]
		vel[0] = vel[0]-1 if vel[0] else 0
		vel[1]-= 1
	if data[0]<=prevpos[0]<=data[1] and data[2]<=prevpos[1]<=data[3]:
		return height

def main():
	data = filter_data()
	x_range = []
	for i in range(data[1]):
		k = solve([i,0],data)
		if k is not None:
			x_range.append(i)
	
	height = 0
	for i in x_range:
		for j in range(1,1000):
			k = solve([i,j],data)
			if k is not None:
				if k>height:
					height = k
	return height




if __name__ == '__main__':
	print(main())

