#!/usr/bin/env python3

def filter_data():
	with open('input', 'r') as fp:
		data = list(eval(fp.read()))
		return data

def simulate(data_, days):
	data = data_.copy()
	for i in range(days):
		n = len(data)
		print(i,n)
		for j in range(n):
			if data[j]>0:
				data[j]-=1
			else:
				data[j] = 6
				data.append(8)
	return data

def main():
	data = filter_data()
	return len(simulate(data, 80))

if __name__ == '__main__':
	print(main())

