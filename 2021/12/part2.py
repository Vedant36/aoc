#!/usr/bin/env python3

from part1 import *

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
				condition = not any([path.count(i)-1 for i in path if i.islower()])
				for node in next:
					if node=='start': continue
					if node.isupper() or (node not in path) or condition:
						temp2 = path.copy()
						temp2.append(node)
						temp.append(temp2)
			paths = temp.copy()
		return paths

def main():
	data = filter_data()
	graph = Graph(data)
	return len(graph.count())

if __name__ == '__main__':
	print(main())
