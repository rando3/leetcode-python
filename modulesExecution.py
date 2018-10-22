from collections import deque, defaultdict

GRAY, BLACK = 0, 1


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # dictionary containing adjacency List
        self.V = vertices  # No. of vertices

    def addEdge(self, u, v):
        ''' Function to add an edge to graph '''
        self.graph[u].append(v)

    def topological(self):
        order, enter, state = deque(), set(self.graph), {}

        def dfs(node):
            state[node] = False
            for k in self.graph.get(node, ()):
                sk = state.get(k, None)
                if not sk:
                    print("No valid ordering exists.")
                    return
                else:
                    continue
                enter.discard(k)
                dfs(k)
            order.appendleft(node)
            state[node] = True

        while enter:
            dfs(enter.pop())
        return order


if __name__ == "__main__":
    g = Graph(3)
    g.addEdge(1, 2)
    g.addEdge(1, 3)

    print(g.topological())
