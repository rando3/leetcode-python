class Solution:

    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        """
        input = ()
        output = [()]

        #this can generate a duplicate in the input
        input = ())
        output = [()]

        #same
        input = (()
        output = [()]

        #empty case
        input = ""
        output = [""]

        #this one removed minimum of 2 to make it valid
        input = ())(
        output = [()]

        #example given
        input = ()())()
        output = ["()()()", "(())()"]
        """
        def isvalid(s):  # O(s)
            ctr = 0
            for c in s:
                ctr += (c == '(') - (c == ')')
                if ctr < 0:
                    return False
            return ctr == 0
        level = {s}  # set
        while True:
            valid = list(filter(isvalid, level))  # filter(func, iter) = [i for i in iter if func(i)]
            if valid:
                return valid
            level = {s[:i] + s[i + 1:] for s in level for i in range(len(s)) if s[i] in ('(', ')')}  # add all possible brackets into store

    def removeInvalidParentheses2(self, s):
        """
        :type s: str
        :rtype: List[str]
        Scan from left to right, make sure count["("]>=count[")"].
        Then scan from right to left, make sure count["("]<=count[")"].
        """
        removed = 0
        results = {s}
        count = {"(": 0, ")": 0}
        for i, c in enumerate(s):
            if c == ")" and count["("] == count[")"]:
                new_results = set()
                while results:
                    result = results.pop()
                    for j in range(i - removed + 1):
                        if result[j] == ")":
                            new_results.add(result[:j] + result[j + 1:])
                results = new_results
                removed += 1
            else:
                if c in count:
                    count[c] += 1

        count = {"(": 0, ")": 0}
        i = len(s)
        ll = len(s) - removed  # removed unnecessary ")"
        for ii in range(ll - 1, -1, -1):
            i -= 1
            c = s[i]
            if c == "(" and count["("] == count[")"]:
                new_results = set()
                while results:
                    result = results.pop()
                    for j in range(ii, ll):
                        if result[j] == "(":
                            new_results.add(result[:j] + result[j + 1:])
                results = new_results
                ll -= 1
            else:
                if c in count:
                    count[c] += 1
        return list(results)


''' DP ''' 
def minDrop(s, si, oc, cache, pseq):
    N = len(s)

    if oc < 0:
        return N - si + 1

    if si == N :
        if oc == 0:
            pseq[si][oc] = {''}
        return oc

    if cache[si][oc] != -1:
        return cache[si][oc]

    
    if s[si] in '()':
        dc0 = 1 + minDrop(s, si + 1, oc, cache, pseq)
        pseq0 = pseq[si + 1][oc]

        if s[si] == '(':
            dc1 = minDrop(s, si + 1, oc + 1, cache, pseq)
            pseq1 = ['(' + x for x in pseq[si + 1][oc + 1]]
        else:
            dc1 = minDrop(s, si + 1, oc - 1, cache, pseq)
            pseq1 = [')' + x for x in pseq[si + 1][oc - 1]]

        cache[si][oc] = min(dc0, dc1)

        # note '=' - in case of eqaulity we keep both combination sets
        if dc0 >= dc1 :
            pseq[si][oc] = pseq[si][oc].union(pseq1)

        if dc0 <= dc1 :
            pseq[si][oc] = pseq[si][oc].union(pseq0) 

    else:
        cache[si][oc] = minDrop(s, si + 1, oc, cache, pseq)
        pseq[si][oc] = [s[si] + x for x in pseq[si + 1][oc]]

    return cache[si][oc]

class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        N = len(s)
        cache = [[-1 for x in range(N)] for x in range(N)]
        pseq = [[set() for x in range(N + 1)] for x in range(N + 1)]

        c = minDrop(s, 0, 0, cache, pseq)

        return list(pseq[0][0])
