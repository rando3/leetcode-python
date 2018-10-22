import sys
from collections import defaultdict, deque


class ComputeGraph:
    def __init__(self, num):
        self.graph = defaultdict(list)  # dictionary containing adjacency list
        self.modules = num  # number of modules

    def addDependency(self, dep, mod):
        ''' Add dependency to module, (edge to DAG) '''
        if mod in self.graph[dep]:
            print("No valid ordering exists")
            sys.exit()
        self.graph[mod].append(dep)

    def computeOrdering(self):
        '''
        Perform topological sort to find numerically smallest ordering.
        '''
        visited = [False] * (self.modules + 1)
        indegree = [0] * (self.modules + 1)
        stack = []

        for i in self.graph:
            for j in self.graph[i]:  # O(V+E)
                indegree[j] += 1

        def topologicalSortUtil(visited, indegree, stack):
            ''' A recursive function used by topologicalSort '''
            combos_found = False  # are all topological orderings found

            for i in range(1, self.modules + 1):
                if not visited[i] and indegree[i] == 0:
                    visited[i] = True  # include in result
                    stack.append(i)
                    for node in self.graph[i]:
                        indegree[node] -= 1
                    topologicalSortUtil(visited, indegree, stack)
                    # reset visited res and indegree for backtracking
                    visited[i] = False
                    stack.pop()
                    for node in self.graph[i]:
                        indegree[node] += 1
                    combos_found = True

            if not combos_found:
                if len(stack) < self.modules:
                    print("No valid ordering exists")
                    sys.exit()
                for x in stack:
                    print(x, end=" ")
                sys.exit()

        topologicalSortUtil(visited, indegree, stack)
        # queue = deque()  # efficient enqueues and dequeues
        # for i in range(1, self.modules + 1):
        #     if indegree[i] == 0:
        #         queue.append(i)
        # # visited = 0  # visited modules
        # order = []  # store order

        # while queue:
        #     mod = queue.popleft()
        #     order.append(mod)
        #     for adj in self.graph[mod]:
        #         indegree[adj] -= 1
        #         if indegree[adj] == 0:
        #             queue.append(adj)  # enqueue adjacent module
        #     visited[mod]

        # if len(order) != self.modules:  # Check if valid DAG
        #     print("No valid ordering exists")
        # else:
        #     for num in order:
        #         print(num, end=" ")

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
