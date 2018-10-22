from collections import defaultdict, deque
import sys


class ComputeGraph:
    def __init__(self, num):
        self.graph = defaultdict(list)  # dictionary containing adjacency list
        self.modules = num  # number of modules

    def addDependency(self, dep, mod):
        ''' Add dependency to module, (edge to DAG) '''
        self.graph[mod].append(dep)

    def computeOrdering(self):
        '''
        Perform topological sort to find numerically smallest ordering.
        '''
        indegree = [0] * (self.modules + 1)
        for i in self.graph:
            for j in self.graph[i]:  # O(V+E)
                indegree[j] += 1

        queue = deque()  # efficient enqueues and dequeues
        for i in range(1, self.modules + 1):
            if indegree[i] == 0:
                queue.append(i)

        visited = 0  # visited modules
        order = []  # store order

        while queue:
            mod = queue.popleft()
            order.append(mod)
            for adj in self.graph[mod]:
                indegree[adj] -= 1
                if indegree[adj] == 0:
                    queue.append(adj)  # enqueue adjacent module
            visited += 1

        if visited != self.modules:  # Check if valid DAG
            print("No valid ordering exists")
            sys.exit()
        else:
            for num in order:
                print(num, end=" ")

# if __name__ == "__main__":
#     num_args = input().split(" ")
#     g = ComputeGraph(int(num_args[0]))
#     for i in range(int(num_args[1])):
#         edge = input().split(" ")
#         g.addDependency(int(edge[0]), int(edge[1]))
#     g.computeOrdering()


if __name__ == "__main__":
    g = ComputeGraph(3)
    g.addDependency(1, 3)
    g.addDependency(1, 2)

    print("All topologicalSorts")
    g.computeOrdering()
