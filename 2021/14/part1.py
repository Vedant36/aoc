#!/usr/bin/env python3

import numpy as np

def filter_data():
	with open('input', 'r') as fp:
		data = fp.read().splitlines()
		return data[0], dict([tuple(i.split(' -> ')) for i in data[2:]])

def step(template, pir, step=1):
	ret = list(template)
	ret_ = ret.copy()
	for i in range(step):
		ret = ret_.copy()
		count = 0
		for j in range(len(ret)-1):
			temp = pir.get(''.join(ret[j:j+2]), '')
			if temp:
				ret_.insert(j+1+count, temp)
				count+=1
	return ''.join(ret_)

def main():
	poly, pir = filter_data()
	a = step(poly, pir, 10)
	b = {a.count(i):i for i in set(a)}
	return max(b)-min(b)

if __name__ == '__main__':
	print(main())
