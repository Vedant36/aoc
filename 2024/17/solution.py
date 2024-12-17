A = 25986278
main = [2,4,1,4,7,5,4,1,1,4,5,5,0,3,3,0]

# fast version of the input program
def f(A):
    qwe = []
    while (A):
        B = (A&7)^4
        B = B^((A&(2**10-1))>>B)^4
        qwe.append(B&7)
        A = A>>3
    return qwe

def trydowithindex(main, count=0, prefix=0):
    #print(main, count, prefix)
    if f(prefix)[-len(main):] == main:
        # print(prefix)
        if f(prefix) == main:
            return prefix
    chi = min(len(main)%3 + 3*count, len(main))
    qwe = []
    for i in range(8**3):
        result = f(prefix * 8**3 + i)
        #print(chi, oct(i), result[-chi:], main[-chi:])
        if result[-chi:] == main[-chi:]:
            qwe.append(prefix * 8**3 + i)
    #print(qwe, count, prefix)
    for i in qwe:
        result = trydowithindex(main, count+1, prefix=i)
        if result > 0:
            return result
    return -1

def part1():
    return ','.join(map(str, f(A)))

def part2():
    return trydowithindex(main)

print(f"Solution to part 1: {part1()}")
print(f"Solution to part 2: {part2()}")
