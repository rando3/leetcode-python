from collections import defaultdict
import sys


class Graph:
    def __init__(self, num):
        self.adj_list = defaultdict(list)  # dictionary containing adjacency list
        self.modules = num  # number of modules

    def addDependency(self, dep, mod):
        ''' Add dependency to module, (edge to DAG) '''
        if mod in self.adj_list[dep]:
            print("No valid ordering exists")
            sys.exit()
        self.adj_list[mod].append(dep)

    def top_sort(self):
        # Find number of incoming edges for each vertex
        in_degree = {}
        for x, neighbors in self.adj_list.items():
            in_degree.setdefault(x, 0)
            for n in neighbors:
                in_degree[n] = in_degree.get(n, 0) + 1

        # Iterate over edges to find vertices with no incoming edges
        empty = {v for v, count in in_degree.items() if count == 0}

        result = []
        while empty:
            # Take random vertex from empty set
            v = empty.pop()
            result.append(v)

            # Remove edges originating from it, if vertex not present
            # in adjacency list use empty list as neighbors
            for neighbor in self.adj_list.get(v, []):
                in_degree[neighbor] -= 1

                # If neighbor has no more incoming edges add it to empty set
                if in_degree[neighbor] == 0:
                    empty.add(neighbor)

        if len(result) != len(in_degree):
            print("No valid ordering exists")
            sys.exit()
        else:
            return result


if __name__ == "__main__":
    g = Graph(3)
    g.addDependency(1, 3)
    g.addDependency(1, 2)
    order = g.top_sort()
    for num in order:
        print(num, end=" ")
