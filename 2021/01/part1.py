#!/usr/bin/env python3

def filter_data():
	with open('input', 'r') as fp:
		data = list(map(int,fp.read().splitlines()))
		return data

def main():
	data = filter_data()
	return sum([i<j for i,j in zip(data[:-1],data[1:])])

if __name__ == '__main__':
	print(main())
