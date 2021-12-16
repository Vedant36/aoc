#!/usr/bin/env python3
# tried until:14:03

from part1 import *
from math import prod

class Packet:
	def __init__(self, data):
		self.V, self.T = int(data[0:3],2), int(data[3:6],2)
		self.data = data

	def setup(self):
		self.funcs = {
				0: lambda n: sum(n),
				1: lambda n: prod(n),
				2: lambda n: min(n),
				3: lambda n: max(n),
				5: lambda n: int(n[0]>n[1]),
				6: lambda n: int(n[0]<n[1]),
				7: lambda n: int(n[0]==n[1])
			}
		data = self.data
		if self.T==4:
			offset = 6
			temp = []
			temp.append(data[offset+1:offset+5])
			while data[offset]!='0':
				offset+=5
				temp.append(data[offset+1:offset+5])
			self.value = int("".join(temp), 2)
			return offset+5, self.value
		else:
			values = []
			self.I = int(data[6],2)
			if self.I:
				self.num = int(data[7:18],2)
				offset=0
				for i in range(self.num):
					offset_, value = Packet(data[18+offset:]).setup()
					offset+=offset_
					values.append(value)
				return 18+offset, self.funcs[self.T](values)
			else:
				self.length = int(data[7:22],2)
				offset=0
				while True:
					section = data[22+offset:22+self.length]
					if section=='':
						break
					offset_, value = Packet(section).setup()
					offset+=offset_
					values.append(value)
				return 22+self.length, self.funcs[self.T](values)

def parse_packet(data):
	return Packet(data).setup()[1]

def main():
	data = filter_data()
	# check = {
	# 	'C200B40A82': 3,
	# 	'04005AC33890':54,
	# 	'880086C3E88112': 7,
	# 	'CE00C43D881120': 9,
	# 	'D8005AC2A8F0': 1,
	# 	'F600BC2D8F': 0,
	# 	'9C005AC2F8F0': 0,
	# 	'9C0141080250320F1802104A08': 1,
	# }
	# for i in check:
	# 	ans = parse_packet(bin(eval('0xF'+i))[6:])
	# 	print(f"Works for {i}: {ans==check[i]}")
	return parse_packet(data)

if __name__=='__main__':
	print(main())

