from part1 import *

def main():
    data = np.asarray(filter_data())
    return np.sum(board>1)

if __name__=='__main__':
    print(main())

