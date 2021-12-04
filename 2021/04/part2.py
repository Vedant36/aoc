from part1 import *

def main():
	calls, boards = filter_data()
	counts = [count_turns(i, calls)[0] for i in boards]
	min_index = np.argmax(counts)
	count, mask = count_turns(boards[min_index], calls)
	return calls[count] * np.sum(np.asarray(boards[min_index]) * (1 - count_turns(boards[min_index], calls)[1]))

if __name__ == '__main__':
	print(main())
