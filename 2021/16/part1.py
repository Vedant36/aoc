#!/usr/bin/env python3
# tried until:14:03

import numpy as np

def filter_data():
	with open('input', 'r') as fp:
		data = fp.read()[:-1]
		return bin(eval('0xF'+data))[6:]

class Packet:
	def __init__(self, data):
		self.V, self.T = int(data[0:3],2), int(data[3:6],2)
		self.data = data

	def setup(self):
		data = self.data
		if self.T==4:
			offset = 6
			while data[offset]!='0':
				offset+=5
			self.value = int(data[6:offset+5], 2)
			return self.V, offset+5
		else:
			self.I = int(data[6],2)
			if self.I:
				self.num = int(data[7:18],2)
				offset=0
				for i in range(self.num):
					ver, offset_ = Packet(data[18+offset:]).setup()
					self.V+=ver
					offset+=offset_
				return self.V, 18+offset
			else:
				self.length = int(data[7:22],2)
				offset=0
				while True:
					section = data[22+offset:22+self.length]
					if section=='':
						break
					ver, offset_ = Packet(section).setup()
					self.V+=ver
					offset+=offset_
				return self.V, 22+self.length


def parse_packet(data):
	return Packet(data).setup()[0]

def main():
	data = filter_data()
	# check = {
	# 	'D2FE28': 6,
	# 	'EE00D40C823060': 14,
	# 	'38006F45291200': 9,
	# 	'8A004A801A8002F478': 16,
	# 	'620080001611562C8802118E34': 12,
	# 	'C0015000016115A2E0802F182340': 23,
	# 	'A0016C880162017C3686B18A3D4780': 31
	# }
	# for i in check:
	# 	ans = parse_packet(bin(eval('0xF'+i))[6:])
	# 	print(f"Works for {i}: {ans==check[i]}")
	return parse_packet(data)

if __name__ == '__main__':
	print(main())

