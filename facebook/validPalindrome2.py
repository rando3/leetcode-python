class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

        Example 1:
        Input: "aba"
        Output: True
        Example 2:
        Input: "abca"
        Output: True
        Explanation: You could delete the character 'c'.
        """

    def validPalindrome2(self, s):
        """
        :type s: str
        :rtype: bool
        We can use the standard two-pointer approach that starts at the left and right of the string and move inwards. Whenever there is a mismatch, we can either exclude the character at the left or the right pointer. We then take the two remaining substrings and compare against its reversed and see if either one is a palindrome.
        """
        # Time: O(n)
        # Space: O(n)
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                one, two = s[left:right], s[left + 1:right + 1]
                return one == one[::-1] or two == two[::-1]
            left, right = left + 1, right - 1
        return True

    def validPalindrome3(self, s):  # TIME LIMIT EXCEEDED FOR THIS
        """
        :type s: str
        :rtype: bool
        """
        if s == s[::-1]:
            return True
        b = s[::-1]
        for i in range(0, len(s)):
            if s[i] != b[i]:
                temp = s[:i] + s[i + 1:]
                temp1 = b[:i] + b[i + 1:]
        return temp == temp[::-1] or temp1 == temp1[::-1]
