#!/usr/bin/env python3

import numpy as np

def filter_data():
	with open('input', 'r') as fp:
		data = fp.read().splitlines()
		return [set(i.split('-')) for i in data]

class Graph:
	def __init__(self, connections):
		self.connections = connections
		a = []; [a.extend(list(i)) for i in self.connections]
		self.uniq = set(a)

	def connected(self, node:str):
		qwe = set()
		for i in self.connections:
			if node in i:
				qwe = qwe.union(i.difference({node}))
		return qwe

	def count(self):
		cache = { i:self.connected(i) for i in self.uniq }
		paths = []
		next = cache['start']
		for node in next:
			paths.append(['start', node])
		while not all([i[-1]=='end' for i in paths]):
			temp = []
			for path in paths:
				if path[-1]=='end':
					temp.append(path)
					continue
				next = cache[path[-1]]
				for node in next:
					if node.isupper() or node not in path:
						temp2 = path.copy()
						temp2.append(node)
						temp.append(temp2)
			paths = temp.copy()
		return paths

# [{'MN', 'yw'}, {'wn', 'XB'}, {'DG', 'dc'}, {'MN', 'wn'}, {'DG', 'yw'}, {'start', 'dc'}, {'start', 'ah'}, {'MN', 'start'}, {'fi', 'yw'}, {'fi', 'XB'}, {'wn', 'ah'}, {'MN', 'ah'}, {'MN', 'dc'}, {'yw', 'end'}, {'fi', 'end'}, {'th', 'fi'}, {'end', 'XB'}, {'dc', 'XB'}, {'yw', 'XN'}, {'yw', 'wn'}, {'dc', 'ah'}, {'MN', 'fi'}, {'DG', 'wn'}]
def main():
	data = filter_data()
	graph = Graph(data)
	return len(graph.count())

if __name__ == '__main__':
	print(main())
