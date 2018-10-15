class Solution:
    ''' NAIVE O(2^n) '''
    def num_ways(self, s):
        return helper(s, len(s))

    def helper(self, s, k):
        if k == 0:
            return 1
        i = len(s) - k
        if s[i] == '0':
            return 0
        result = self.helper(s, k - 1)
        if k >= 2 and int(s[i:i + 2]) <= 26:
            result += self.helper(s, k - 2)
        return result


class SolutionOptimized:
    ''' O(n) but not NEARLY as efficient as below solutions'''
    def num_ways(self, s, memo):
        memo = [0] * (len(s) + 1)
        return self.helper(s, len(s), memo)

    def helper(self, s, k, memo):
        if k == 0:
            return 1
        i = len(s) - k
        if s[i] == '0':
            return 0
        if memo[k] != 0:
            return memo[k]
        result = self.helper(s, k - 1, memo)
        if k >= 2 and int(s[i:i + 2]) <= 26:
            result += self.helper(s, k - 2, memo)
        memo[k] = result
        return result


class Solution2:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        A message containing letters from A-Z is being encoded to numbers using the following mapping:
        'A' -> 1
        'B' -> 2
        ...
        'Z' -> 26
        Given a non-empty string containing only digits, determine the total number of ways to decode it.

        Input: "12"
        Output: 2
        Explanation: It could be decoded as "AB" (1 2) or "L" (12).
        '''
        numDecodings('3') = 1
        numDecodings('') = 1

        numDecodings('12345') = "a" + numDecodings("2345") OR "l" + decode("345")  # call twice
        numDecodings('12345') = numDecodings("2345") + numdecodings("345")

        numDecodings('27345') = "b" + numdecodings("7345")  # call once
        numDecodings('27345') = numDecodings("7345")

        numDecodings("011") = 0  # starts with 0, no message

        Base case = String empty or given string starts with 0
        Recursive case = call func twice or call func once
        '''
        """
    '''USE THE TWO BELOW, GO FROM O(N) SPACE TO O(1) SPACE'''

    # DP O(N) space
    # bottom up approach
    # dp[i] means the number of ways to decode s[:i]
    # dp[i] = dp[i-1] if s[i] != '0'
    #       + dp[i-2] if '9' < s[i-2:i] < '27'
    def numDecodings3(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        for i in range(1, len(dp)):
            if s[i - 1] != '0':
                dp[i] = dp[i - 1]
            if i != 1 and '09' < s[i - 2:i] < '27':
                dp[i] += dp[i - 2]
        return dp[-1]

    # Due to dp[i] only depends on dp[i-1] and dp[i-2], we can use two variables to reduce the
    # space to O(1).
    # ways is the number of ways to decode s[:i];
    # oneBefore is the number of ways to decode s[:i-1];
    # twoBefore is the number of ways to decode s[:i-2]
    def numDecodings4(self, s):
        ways, oneBefore, twoBefore = 0, 1, 0
        for i in range(1, len(s) + 1):
            if s[i - 1] != '0':
                ways = oneBefore
            if i != 1 and '09' < s[i - 2:i] < '27':
                ways += twoBefore
            ways, oneBefore, twoBefore = 0, ways, oneBefore
        return oneBefore
