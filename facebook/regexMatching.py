class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

        '.' Matches any single character.
        '*' Matches zero or more of the preceding element.
        The matching should cover the entire input string (not partial).

        Note:

        s could be empty and contains only lowercase letters a-z.
        p could be empty and contains only lowercase letters a-z, and characters like . or *.
        """


class Solution2(object):
    def isMatch(self, s, p):
        prev = [False, True]
        for j in range(len(p)):
            prev.append(p[j] == '*' and prev[j])

        for i in range(len(s)):
            curr = [False, False]
            for j in range(len(p)):
                if p[j] == '*':
                    curr.append(curr[j] or curr[j+1] or (prev[j+2] and p[j-1] in (s[i], '.')))
                else:
                    curr.append(prev[j+1] and p[j] in (s[i], '.'))
            prev = curr
        return prev[-1]