#!/usr/bin/env python3

import numpy as np

def filter_data():
	with open('input', 'r') as fp:
		data = np.asarray([list(i) for i in fp.read().splitlines()], dtype=np.uint8)
		return data

def bti(a):
	return int(''.join(str(int(i)) for i in a),2)

def main():
	data = filter_data()
	su = data.sum(0)
	le = data.shape[0]/2
	return bti(su>le)*bti(su<le)

if __name__ == '__main__':
	print(main())
