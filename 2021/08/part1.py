#!/usr/bin/env python3

import numpy as np

def filter_data():
	with open('input', 'r') as fp:
		data = fp.read().splitlines()
		return data

def main():
	data = filter_data()
	appear = 0
	for i in data:
		qwe = i.split(' | ')[1].split()
		appear += len([i for i in qwe if len(i) in {2,3,4,7} ])
	return appear

if __name__ == '__main__':
	print(main())

