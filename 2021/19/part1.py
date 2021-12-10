#!/usr/bin/env python3

import numpy as np

def filter_data():
	with open('input', 'r') as fp:
		data = fp.read().splitlines()
		return data

def main():
	data = filter_data()

if __name__ == '__main__':
	print(main())
