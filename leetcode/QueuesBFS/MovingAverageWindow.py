'''Using deque module from collections package'''
from collections import deque

class MovingAverage:

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.queue = deque()
        self.size = size
        self._sum = 0.0
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.queue.append(val)
        self._sum += val
        if len(self.queue) > self.size:
            self._sum -= self.queue.popleft()       
        
        return self._sum/len(self.queue)


# Your MovingAverage object will be instantiated and called as such:
# m = MovingAverage(3)
# print(m.next(1))
# print(m.next(10))
# print(m.next(3))
# print(m.next(5))

'''Using Queue module from queue package.'''
''' import queue as q

class MovingAverage:

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.queue = q.Queue(size)
        self.sum = 0.0
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if self.queue.full():
            self.sum -= self.queue.get()
        
        self.queue.put(val)
        self.sum += val
        
        return self.sum/self.queue.qsize() '''


# Your MovingAverage object will be instantiated and called as such:
# m = MovingAverage(3)
# print(m.next(1))
# print(m.next(10))
# print(m.next(3))
# print(m.next(5))