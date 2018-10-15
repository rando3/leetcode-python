def answer(l, t):
    # Level 2, challenge 2
    # Finished in 15 min, 36 sec
    if len(l) == 1:
        if l[0] != t:
            return [-1, -1]
        return [0, 0]
    start = 0
    end = 0
    for i in xrange(len(l)):
        start = i
        total = l[i]
        if l[i] == t:
            return [start, i]
        for j in xrange(i+1, len(l)):
            total += l[j]
            if total == t:
                end = j
                return [start, end]
            elif total > t:
                break
    return [-1, -1]


if __name__ == '__main__':
    print answer([4, 3, 10, 2, 8], 12)
    print answer([1, 2, 3, 4], 15)
