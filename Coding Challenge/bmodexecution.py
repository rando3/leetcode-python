# Python program to print topological sorting of a DAG
from collections import defaultdict
import sys


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # dictionary containing adjacency List
        self.V = vertices  # No. of vertices

    def addEdge(self, u, v):
        ''' Function to add an edge to graph '''
        if v in self.graph[u]:
            print("No valid ordering exists")
            sys.exit()
        self.graph[v].append(u)

    def topologicalSortUtil(self, visited, indegree, stack):
        ''' A recursive function used by topologicalSort '''
        combos_found = False  # are all topological orderings found

        for i in range(1, self.V + 1):
            if not visited[i] and indegree[i] == 0:
                visited[i] = True  # include in result
                stack.append(i)
                for node in self.graph[i]:
                    indegree[node] -= 1
                self.topologicalSortUtil(visited, indegree, stack)
                # reset visited res and indegree for backtracking
                visited[i] = False
                stack.pop()
                for node in self.graph[i]:
                    indegree[node] += 1
                combos_found = True

        if not combos_found:
            if len(stack) < self.V:
                print("No valid ordering exists")
                sys.exit()
            for x in stack:
                print(x, end=" ")
            sys.exit()

    def topologicalSort(self):
        '''
         The function to do Topological Sort.
         It uses recursive topologicalSortUtil()
        '''
        visited = [False] * (self.V + 1)  # base case not visited
        stack = []
        indegree = [0] * (self.V + 1)
        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for i in range(1, self.V + 1):
            for node in self.graph[i]:
                indegree[node] += 1

        self.topologicalSortUtil(visited, indegree, stack)


if __name__ == "__main__":
    g = Graph(3)
    g.addEdge(1, 3)
    g.addEdge(1, 2)

    print("All topologicalSorts")
    g.topologicalSort()
