def answer(n):
    if n <= 0:
        return 0
    if n <= 4:
        return 1

    math_list = [[0 for _ in xrange(n + 1)] for _ in xrange(n + 1)]  # n + 1 so that I can just call math_list[n][n] instead of math_list[n-1][n-1]
    math_list[0][0] = 1  # all operations based on this assumption

    for x in xrange(1, n + 1):
        for y in xrange(n + 1):
            math_list[x][y] = math_list[x - 1][y]
            if y >= x:
                math_list[x][y] += math_list[x - 1][y - x]

    combos = math_list[n][n] - 1
    return combos

if __name__ == '__main__':
    print answer(4)
    print answer(5)
    print answer(6)
    print answer(200)
