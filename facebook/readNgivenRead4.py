# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):
"""
:type buf: Destination buffer (List[str])
:type n: Maximum number of characters to read (int)
:rtype: The number of characters read (int)
The API: int read4(char *buf) reads 4 characters at a time from a file.

The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.

By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.

Note:
The read function may be called multiple times.
"""
import collections


class Solution(object):
    def __init__(self):
        self.queue = collections.deque()

    def read(self, buf, n):
        i = 0
        while i < n:
            buf4 = [''] * 4
            _ = read4(buf4)
            self.queue.extend(buf4)
            count = min(len(self.queue), n-i)
            if not count:
                break
            buf[i:] = [self.queue.popleft() for _ in range(count)]
            i += count
        return i

    def read4(self, buf):
        pass


class Solution2(object):
    def __init__(self):
        self.queue = []  # global "buffer"

    def read(self, buf, n):
        ind = 0

        # if queue is large enough, read from queue
        while self.queue and n > 0:
            buf[ind] = self.queue.pop(0)
            ind += 1
            n -= 1
        
        while n > 0:
            # read file to buf4
            buf4 = [""]*4
            l = read4(buf4)

            # if no more char in file, return
            if not l:
                return ind

            # if buf can not contain buf4, save to queue
            if l > n:
                self.queue += buf4[n:l]

            # write buf4 into buf directly
            for i in range(min(l, n)):
                buf[ind] = buf4[i]
                ind += 1
                n -= 1
        return ind
