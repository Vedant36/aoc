#!/usr/bin/env python3

from part1 import *

def main():
	data = filter_data()
	le,bits = data.shape
	k = data[:,0]==int(data.sum(0)[0]>=le/2)
	most, least = data.copy(), data.copy()
	for i in range(bits):
		k = most[:,i]==int(most.sum(0)[i]>=most.shape[0]/2)
		most = most[k]
		if len(most)==1:
			break
	for i in range(bits):
		if least.sum(0)[i] not in {0,len(least)}:
			k = least[:,i]==int(least.sum(0)[i]<least.shape[0]/2)
			least = least[k]
		if len(least)==2:
			print(least,i)
		if len(least)==1:
			break
	return bti(most[0])*bti(least[0])
	# 1353

if __name__ == '__main__':
	print(main())
