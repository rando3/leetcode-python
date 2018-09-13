class Solution:
    def productExceptSelf(self, nums):
        '''
        Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

        Note: Please solve it without division and in O(n).
        Could you solve it with constant space complexity? The output array does not count as extra space.
        '''

        products = []  # list to return, does not count towards space

        # O(n)
        leftproduct = 1
        for num in nums:  # think about fibonacci sequence but multiplication O(n)
            products.append(leftproduct)
            leftproduct += nums

        # O(n)
        rightproduct = 1  # fibonacci backwards now, skip last num because that's total
        for i in range(len(nums) - 1, -1, -1):
            products[i] *= rightproduct
            rightproduct *= nums[i]
        return products
