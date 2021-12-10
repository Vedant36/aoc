#!/usr/bin/env python3

def filter_data():
	with open('input', 'r') as fp:
		data = fp.read().splitlines()
		return data

def main():
	data = filter_data()
	check = { '(':')', '[':']', '{':'}', '<':'>' }
	score = { ')':3, ']':57, '}':1197, '>':25137 }
	ans = 0
	for i in data:
		stack = []
		corrupted = 0
		for n,j in enumerate(i):
			if j in check:
				stack.append(j)
				continue
			elif check[stack[-1]]==j:
				stack.pop()
				continue
			else:
				ans += score[j]
				corrupted = 1
				break
	return ans

if __name__ == '__main__':
	print(main())
