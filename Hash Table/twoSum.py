class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        Given an array of integers, return indices of the two numbers such that they add up to a specific target.
        Given nums = [2, 7, 11, 15], target = 9,

        Because nums[0] + nums[1] = 2 + 7 = 9,
        return [0, 1].
        You may assume that each input would have exactly one solution, and you may not use the same element twice.

        Beats 46% of python3 submissions.
        Implemented array in key value because there were duplicates.
        """
        d = {}
        for i, x in enumerate(nums):
            if x not in d:
                d[x] = [i]
            else:
                d[x].append(i)
        for key in d:
            value = target - key
            if value in d:
                if value == key:
                    return [d.get(key)[0], d.get(key)[1]]
                return [d.get(key)[0], d.get(value)[0]]

        '''Better: because simpler and you eliminate need to handle duplicates'''

        numDict = {}

        for i, x in enumerate(nums):
            if (target - x) in numDict:
                return [i, numDict[target - x]]
            numDict[x] = i
        return []
