class Solution:
    # @param A : integer
    # @return a list of integers
    '''
    https://www.geeksforgeeks.org/sieve-of-eratosthenes/
    Get all prime numbers less than or equal to int
    All numbers up to A, modulus by 2->A and keep remaining
    '''
    '''
    Works, but not well optimized for memory
    '''
    def primeSum(self, A):
        primeList = self._generate_primes(A)
        for i, v in enumerate(primeList):
            if primeList[i] and primeList[A - i] and i >= 2:
                return [i, A - i]
        return None

    def _generate_primes(self, A):
        # Create a boolean array "prime[0..n]" and initialize
        #  all entries it as true. A value in prime[i] will
        # finally be false if i is Not a prime, else true.
        primeList = [True for x in range(A + 1)]
        p = 2
        while(p * p <= A):
            # p*p because if 20*20 = 400, once you get to 21, you're multiplying by a number you've been to already i.e. 21*18 or something
            if primeList[p]:
                for i in range(p * 2, A + 1, p):
                # multiples of p are not prime, make False
                    primeList[i] = False
            p += 1
        return primeList

    '''
    BETTER
    '''
    def primesum(self, A):
        for i in range(2, A // 2 + 1):  # only need to go halfway, ur going from both sides
            if self._is_prime(i) and self._is_prime(A - i):
                return i, A - i

    def _is_prime(self, n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
