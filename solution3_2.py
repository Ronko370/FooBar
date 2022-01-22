import math

# Let's assume access codes have to be unique
def solution(l):
    l.reverse()
    count = 0
    dividers = {}

    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            n = l[j]
            if l[i] % n == 0:
                if j not in dividers:
                    dividers[j] = 0
                    _i = len(l) - 1
                    while _i > j:
                        if(n % l[_i] == 0):
                            dividers[j] += 1
                        _i -= 1

                count += dividers[j]
    return count


print solution([1, 2, 3, 11, 4, 5, 6])
print solution([1, 1, 1])
print solution([n for n in range(1, 2001)])
