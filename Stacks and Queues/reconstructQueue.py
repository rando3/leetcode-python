class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        406. Queue Reconstruction by Height
        Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

        My try: failed because of runtime.
        """
        # if people is None:
        #     return None
        # if len(people) == 0:
        #     return []
        # zeros = sorted([x for x in people if x[1] == 0])
        # p = people[:]
        # q = {0: zeros[0]}
        # p.remove(zeros[0])
        # while len(q) < len(people):
        #     new = []
        #     for x in p:
        #         back = x[1]
        #         if len(q) < back:
        #             continue
        #         cntCheck = 0
        #         good = True
        #         for key in q:
        #             if q.get(key)[0] >= x[0]:
        #                 cntCheck += 1
        #                 if cntCheck > back:
        #                     good = False
        #                     break
        #         if good is False:
        #             continue
        #         if cntCheck != back:
        #             continue
        #         new.append(x)
        #     new = sorted(new)
        #     q[len(q)] = new[0]
        #     p.remove(new[0])
        # return q

        # Solution:
        # sort by descending order of x[0] and then ascending order of x[1]

        people.sort(key=lambda x: (-x[0], x[1]))

        result = []
        for p in people:
            result.insert(p[1], p)  # insert person at p[1] position (kth)
        return result

        '''
        [[7, 0], [7, 1], [6, 1], [5, 0], [5, 2], [4, 4]] # ordered by -x[0] then x[1]
        0 [7, 0]  # matters most (taller than everyone,lower ppl in front), insert at k
        1 [7, 1]
        1 [6, 1]
        0 [5, 0]  # can add to zero position, because shorter than [7,0]
        2 [5, 2]
        4 [4, 4]  # matters least, insert at k after all others inserted
        [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]
        '''


if __name__ == '__main__':
    sol = Solution()
    test1 = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    sol.reconstructQueue(test1)
