class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = ["[", "(", "{"]
        stack = []
        bracketMap = {"]":"[", ")":"(", "}":"{"}
        if len(s) == 0:
            return True
        for b in s:
            if b in left:
                stack.append(b)
            else: 
                if len(stack) == 0:
                    return False
                other = stack.pop()
                if other == bracketMap[b]:
                    continue
                else:
                    return False
        if len(stack) > 0:
            return False
        return True
