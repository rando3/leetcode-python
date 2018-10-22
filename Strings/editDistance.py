
# Time:  O(n * m)
# Space: O(n + m)
#
# Given two words word1 and word2, find the minimum number of steps
# required to convert word1 to word2. (each operation is counted as 1 step.)
#
# You have the following 3 operations permitted on a word:
#
# a) Insert a character
# b) Delete a character
# c) Replace a character
#


class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
        if len(word1) < len(word2):
            return self.minDistance(word2, word1)

        distance = [i for i in range(len(word2) + 1)]

        for i in range(1, len(word1) + 1):
            pre_distance_i_j = distance[0]
            distance[0] = i
            for j in range(1, len(word2) + 1):
                insert = distance[j - 1] + 1
                delete = distance[j] + 1
                replace = pre_distance_i_j
                if word1[i - 1] != word2[j - 1]:
                    replace += 1
                pre_distance_i_j = distance[j]
                distance[j] = min(insert, delete, replace)

        return distance[-1]

# Time:  O(n * m)
# Space: O(n * m)


class Solution2:
    # @return an integer
    def minDistance(self, word1, word2):
        distance = [[i] for i in range(len(word1) + 1)]
        distance[0] = [j for j in range(len(word2) + 1)]

        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                insert = distance[i][j - 1] + 1
                delete = distance[i - 1][j] + 1
                replace = distance[i - 1][j - 1]
                if word1[i - 1] != word2[j - 1]:
                    replace += 1
                distance[i].append(min(insert, delete, replace))

        return distance[-1][-1]


class Solution3:
    dp = {}

    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if (word1, word2) in self.dp:
            return self.dp[(word1, word2)]
        size1 = len(word1)
        size2 = len(word2)
        if not word1 or not word2:
            return size1 + size2
        if word1[0] == word2[0]:
            ans = self.minDistance(word1[1:], word2[1:])
            self.dp[(word1, word2)] = ans
            return ans
        else:
            delete = 1 + self.minDistance(word1[1:], word2)
            insert = 1 + self.minDistance(word1, word2[1:])
            replace = 1 + self.minDistance(word1[1:], word2[1:])
            ans = min(delete, insert, replace)
            self.dp[(word1, word2)] = ans
            return ans
        
if __name__ == "__main__":
    print(Solution().minDistance("Rabbit", "Racket"))
    print(Solution2().minDistance("Rabbit", "Rabket"))
    print(Solution().minDistance("Rabbit", "Rabbitt"))
