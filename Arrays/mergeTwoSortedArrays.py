class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        Input:
        nums1 = [1,2,3,0,0,0], m = 3
        nums2 = [2,5,6],       n = 3

        Output: [1,2,2,3,5,6]
        """
        nums1[m:] = nums2
        nums1.sort()
        return nums1


if __name__ == "__main__":
    run = Solution()
    print(run.merge([3,4,5,6,7,8,9,0,0,0,0,0,0], 7, [1,3,4,5,6,7], 6))
