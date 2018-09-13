import re


def isPalindrome(self, s):
    """
    :type s: str
    :rtype: bool
    """
    alphanumeric = re.sub("[^A-Za-z0-9]+", "", s).lower()
    return alphanumeric == alphanumeric[::-1]


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        str1 = "abcdefghijklmnopqrstuvwxyz0123456789"
        lower = s.lower()
        validList = [w for w in lower if w in str1]
        reversedList = validList[::-1]
        if reversedList == validList:
            return True
        return False
