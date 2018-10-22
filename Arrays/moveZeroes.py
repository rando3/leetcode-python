class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
        """
        pos = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[pos] = nums[i]
                pos += 1
        for i in range(pos, len(nums)):
            nums[i] = 0

        ''' or, but not sure if this counts as in place '''

        for num in nums:
            if num == 0:
                nums.remove(num)
                nums.append(0)
