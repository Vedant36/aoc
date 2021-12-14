#!/usr/bin/env python3

from part1 import *
from collections import defaultdict

def step(template, pir, step=1):
	ret = defaultdict(lambda: 0, { ''.join([i,j]):1 for i,j in zip(template[:-1],template[1:]) })
	ret_ = ret.copy()

	for i in range(step):
		ret = ret_.copy()
		for j in ret:
			if j in pir and ret[j]>0:
				temp = pir[j]
				temp2 = ret[j]
				ret_[j[0]+temp]+=temp2
				ret_[temp+j[1]]+=temp2
				ret_[j]-=temp2

	return ret_

def main():
	poly, pir = filter_data()
	a = step(poly, pir, 40)
	a[poly[0]+poly[-1]]+=1
	b = {sum([j.count(i)*a[j] for j in a])//2:i for i in set(''.join(a))}
	return max(b)-min(b)

if __name__ == '__main__':
	print(main())
