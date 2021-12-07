#!/usr/bin/env python3

import numpy as np

def filter_data():
	with open('input', 'r') as fp:
		data = np.asarray(eval(fp.read()))
		return data

def main():
	data = filter_data()
	qwe = np.asarray([(np.abs(data-i)*(np.abs(data-i)+1)/2).sum() for i in range(data.min(), data.max()+1)])
	return min(qwe)

if __name__ == '__main__':
	print(main())


