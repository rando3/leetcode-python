# Python program to print topological sorting of a DAG
from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # dictionary containing adjacency List
        self.V = vertices  # No. of vertices

    def addEdge(self, u, v):
        ''' Function to add an edge to graph '''
        self.graph[u].append(v)

    def topologicalSortUtil(self, v, visited, stack):
        ''' A recursive function used by topologicalSort '''
        visited[v] = True  # curr node visited

        for i in self.graph[v]:  # Recur for all the vertices adjacent to this vertex
            if not visited[i]:
                self.topologicalSortUtil(i, visited, stack)
        stack.insert(0, v)  # Push current vertex to stack which stores result

    def topologicalSort(self):
        '''
         The function to do Topological Sort.
         It uses recursive topologicalSortUtil()
        '''
        visited = [False] * self.V  # base case not visited
        stack = []

        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for i in range(self.V):
            if not visited[i]:
                self.topologicalSortUtil(i, visited, stack)

        print(stack)  # Print contents of the stack


if __name__ == "__main__":
    g = Graph(3)
    g.addEdge(1, 3)
    g.addEdge(1, 2)

    print("Following is a Topological Sort of the given graph")
    g.topologicalSort()
