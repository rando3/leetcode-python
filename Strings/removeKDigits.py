import sys


class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str

        Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
        """
        stack = []  # will be the remaining digits
        for i, v in enumerate(num):
            while stack and k > 0:
                if v < stack[-1]:
                    k -= 1
                    stack.pop()  # remove if end of stack is higher than next v
                else:
                    break
            stack.append(v)

        while k != 0:
            stack.pop()  # just pop until we have k = 0
            k -= 1

        while stack:
            if stack[0] == "0":  # remove leading zeroes
                stack = stack[1:]
            else:
                break
        return "".join(stack) or "0"
