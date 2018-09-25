import collections
class Solution(object):
    # O(nlogn) greedy to place most popular and distinct tasks first
    # We always place different tasks in a cycle which will minimize steps
    # If not different tasks can be placed in a cycle, place an `idle`.
    
    def _leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        n += 1
        ans = 0
        d = collections.Counter(tasks)
        heap = [-c for c in d.values()]  # max heap
        heapq.heapify(heap)
        while heap:
            stack = []
            cnt = 0
            for _ in range(n):
                if heap:
                    c = heapq.heappop(heap)
                    cnt += 1
                    if c < -1:
                        stack.append(c + 1)
            for item in stack:
                heapq.heappush(heap, item)
            ans += n if heap else cnt  # == if heap then n else cnt
        return ans


    # O(n) # of the most frequent tasks, say longest, will determine the legnth
    # to void counting idle intervals, we count (longest - 1) * (n + 1)
    # then count how many will in the last cycle which means finding ties
    # if counted number is less than # of tasks which means 
    # less frequent tasks can be always placed in such cycle
    # and it won't cause any conflicts with requirement since even most frequent can be settle
    # finally, return max(# of task, total counted number)
    
    def leastInterval2(self, tasks, n):
        d = collections.Counter(tasks)
        counts = d.values()
        longest = max(counts)
        ans = (longest - 1) * (n + 1)
        for count in counts:
            ans += count == longest and 1 or 0
        return max(len(tasks), ans)

    def leastInterval3(self, tasks, N):
        '''
        https://leetcode.com/problems/task-scheduler/discuss/104507/Python-Straightforward-with-Explanation
        '''
        task_counts = collections.Counter(tasks).values()
        M = max(task_counts)
        Mct = task_counts.count(M)
        return max(len(tasks), (M - 1) * (N + 1) + Mct)

    def leastInterval4(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        Here is my solution , to generate schedule along with length of schedule. Generating schedule could be an optional extension of this question

        Tasks alternate between run queue and wait queue. Wait queue task moves to run queue when its cooling period has passed. A run queue task gets scheduled and then put on wait queue if it has still some chunks to run.
        """
        class Task(object):
            """
                Task class to encapsulate notion of task
            """
            def __init__(self, name, count):
                self.name = name       # name of task
                self.count = -count     # number of instances
                self.time = -1         # time at which it last ran

            def __repr__(self):
                return self.name +':' +str(self.count)

            def schedule(self, time):
                self.time = time      # task is scheduled, update time at which it last ran
                self.count += 1        # decrease count

            #def __cmp__(self, other):
            #    cmp(self.count, other.count)

            def __lt__(self, other):
                # if two have same count, use the one with lexicographically smaller
                return self.count < other.count or self.count == other.count and self.name < other.name

        if n == 0:
            # if no cooling period, simply return as many tasks as there are
            return len(tasks)

        task_collection = collections.Counter(tasks) # count task occurrences
        cpu_slots = []      # a sequence depicting which task runs when
        runq = []          # a run queue,  a priority queue
        waitq = collections.deque([])   # a wait queue, a simple queue

        # push all tasks in a run que
        for name, count in task_collection.items():
            heapq.heappush(runq, Task(name, count))  # higher the instances, higher the priority

        idle_task = Task("idle", 0) # an idle task
        time = 0                    # clock
        while runq or waitq:        # if at least one of the queue has some tasks to run
            
            if waitq and ( time - waitq[0].time ) > n:  # if wait queue has task whose cooling period has come
                heapq.heappush(runq,waitq.popleft())    # put that task in run queue

            if runq:     # schdule highest priority task, if one is ready
                task = heapq.heappop(runq)
                task.schedule(time)  # consume one instance
            else:       # no task is ready, so schedule idle task
                task = idle_task

            cpu_slots.append(task.name) # task scheduled on CPU
            if task is not idle_task and task.count != 0:
                waitq.append(task)      # if task is not idle task and has at least some instances to run
            time += 1

        return len(cpu_slots)   # cpu slots will also print task schedule

import collections
class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        dic = collections.defaultdict(int)
        for t in tasks:
            dic[t] += 1
        prev = None
        res = 0
        count = []
        for key in dic:
            count.append((key, dic[key]))
        count.sort(reverse=True, key = lambda x: x[1])
        c = 0
        for i in count:
            if i[1] == count[0][1]:
                c += 1
        return max(len(tasks), (count[0][1] - 1)*(n+1)+c)


class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        dic = {}
        count = []
        for i in tasks:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        large = 0
        
        for i in dic:
            count.append(dic[i])
        for i in count:
            if i == max(count):
                large += 1
        print(large)
        
        ans = (max(count) - 1) * (n + 1) + large
        return max(ans, len(tasks))