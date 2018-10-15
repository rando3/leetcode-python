def answer(n):
    # level 1
    # completed in 44 min
    primeString = get_prime()
    return primeString[n:n+5]


def get_prime():
    A = 25000  # took me a while to realize this wasn't big enough (started with 5000)
    primeList = [True for x in xrange(A+1)]
    p = 2
    while(p*p <= A):
        if primeList[p]:
            for i in xrange(p*2, A+1, p):
                primeList[i] = False
        p += 1
    primeStr = [str(i) for i,v in enumerate(primeList) if v]
    print(len(primeStr))
    return ''.join(primeStr)[2:]
        

if __name__ == "__main__":
    # print answer(3)
    # print answer(0)
    print answer(10000)
