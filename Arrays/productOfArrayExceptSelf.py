class Solution:
    def productExceptSelf(self, nums):
        '''
        Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

        Note: Please solve it without division and in O(n).
        Could you solve it with constant space complexity? The output array does not count as extra space.
        '''

        # products = []  # list to return, does not count towards space

        # # O(n)
        # leftproduct = 1
        # for num in nums:  # think about fibonacci sequence but multiplication O(n)
        #     products.append(leftproduct)
        #     leftproduct += nums

        # # O(n)
        # rightproduct = 1  # fibonacci backwards now, skip last num because that's total
        # for i in range(len(nums) - 1, -1, -1):
        #     products[i] *= rightproduct
        #     rightproduct *= nums[i]
        # return products
        p = 1  # offset by 1
        n = len(nums)
        output = []
        for i in range(0, n):
            print(p)
            output.append(p)
            p = p * nums[i]  # multiply forward
        print(output)
        p = 1
        for i in range(n - 1, -1, -1):
            print(p)
            output[i] = output[i] * p  # multiple backward
            p = p * nums[i]
        return output


if __name__ == "__main__":
    run = Solution()
    print(run.productExceptSelf([1,2,3,4,5,6]))
    # After first run: [1, 1, 2, 6, 24, 120]
    # After second run: [720, 360, 240, 180, 144, 120]
