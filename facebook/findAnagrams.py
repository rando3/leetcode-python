from collections import Counter


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

        Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

        The order of output does not matter.
        Input:
        s: "cbaebabacd" p: "abc"

        Output:
        [0, 6]

        Explanation:
        The substring with start index = 0 is "cba", which is an anagram of "abc".
        The substring with start index = 6 is "bac", which is an anagram of "abc".
        """

    def findAnagrams2(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        pCounter = Counter(p)
        sCounter = Counter(s[:len(p) - 1])  # creates a dictionary which counts the occurence of elements in the substring of s starting from 0 to len(p)-2. it is for initializing the len(p)-1 elements of the sliding window
        for i in range(len(p) - 1, len(s)):
            sCounter[s[i]] += 1   # include a new char in the window
            if sCounter == pCounter:    # This step is O(1), since there are at most 26 English letters
                res.append(i - len(p) + 1)   # append the starting index
            sCounter[s[i - len(p) + 1]] -= 1   # decrease the count of oldest char in the window
            if sCounter[s[i - len(p) + 1]] == 0:
                del sCounter[s[i - len(p) + 1]]   # remove the count if it is 0
        return res
