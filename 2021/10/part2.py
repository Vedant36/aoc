#!/usr/bin/env python3

from part1 import *

def main():
	data = filter_data()
	check = { '(':')', '[':']', '{':'}', '<':'>' }
	score = { '(':1, '[':2, '{':3, '<':4 }
	ans = []
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
				corrupted = 1
				break
		if not corrupted:
			temp = 0
			for i in stack[-1::-1]:
				temp*=5
				temp+=score[i]
			ans.append(temp)
	return sorted(ans)[(len(ans)-1)//2]

if __name__ == '__main__':
	print(main())
