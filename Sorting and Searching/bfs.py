from collections import deque


def bfs(root):
    seen, q = set(), deque()  # add root to seen and q
    seen.add(root)  # can optionally add root to initializing but this is for visual
    q.append(root)

    while q:
        node = q.popleft()  # remove from front of q O(1)
        visit(node)
        for n in node.neighbors:
            if n not in seen:
                seen.add(node)
                q.append(node)


def visit(n):
    print(n)
