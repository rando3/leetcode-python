#!/usr/bin/env python
class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = node()

    def add(self, data):
        new = node(data)
        if self.head is None:
            self.head = new
        else:
            node.next = self.head
            self.head = node

    def length(self):
        cur = self.head
        cnt = 0
        while cur.next is not None:
            cnt += 1
            cur = cur.next
        return cnt

    def display(self):
        nodes = []
        cur = self.head
        while cur.next is not None:
            cur = cur.next
            nodes.append(cur.data)
        print(nodes)

    def get(self, index):
        if index >= self.length():
            raise ValueError("Index out of range. ")
            return None
        curIndex = 0
        cur = self.head
        while curIndex != index:
            cur = cur.next
            curIndex += 1
        return cur.data

    def remove(self, data):
        cur = self.head
        prev = None
        found = False
        while cur and found is False:
            if cur.data == data:
                found = True
            else:
                prev = cur
                cur = cur.next
        if cur is None:
            raise ValueError("Data not in list")
        if prev is None:
            self.head = cur.next
        else:
            prev.next = cur.next


if __name__ == '__main__':
    test = linkedList()
    test.add(1)
    test.add(3)
    test.add(5)
    test.add(7)
    print("Len: " + str(test.length()))
    test.display()
