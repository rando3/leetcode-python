class Solution:
    def threeSum(self, nums):
        '''
        :type nums: List[int]
        :rtype: List[List[int]]
        Use three pointers: left, right, curr
        This is O(nLogn + nn) = O(n^2)
        '''
        res = []
        nums.sort()  # O(n log n)
        for i in range(len(nums) - 2):  # need at least 3 nums to continue
            if i > 0 and nums[i] == nums[i - 1]:  # when i = 0, no prev
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
        return res


class Solution2:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        re = []
        dic = {}

        for num in nums:
            if num not in dic.keys():
                dic[num] = 0
            dic[num] += 1

        keys = dic.keys()

        if 0 in keys and dic[0] > 2:
            re.append([0, 0, 0])

        pos = [key for key in keys if key > 0]
        neg = [key for key in keys if key < 0]

        for p in pos:
            for n in neg:
                rem = - (p + n)
                if rem not in keys:
                    continue

                if rem == p and dic[p] > 1:
                    re.append([n, p, rem])
                elif rem == n and dic[n] > 1:
                    re.append([n, rem, p])
                elif rem < p and rem > n:
                    re.append([n, rem, p])

        return re
