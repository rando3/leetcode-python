from collections import deque


class Stack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, data):
        self.q1.append(data)
        while len(self.q2) != 0:
            x = self.q2.popleft()
            self.q1.append(x)
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        return self.q2.popleft()


if __name__ == "__main__":
    s = Stack()
    s.push(2)
    s.push(4)
    print(s.pop())
