class MyCircularQueue:
    # FIFO
    # O(1), O(N)
    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.k = k
        self.q = [0] * self.k
        self.size = 0
        self.rear = self.front = -1
        

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        # insert at rear
        if self.size >= self.k:
            return False
        else:
            if self.rear == -1:
                self.rear = self.front = 0
            else:
                self.rear = (self.rear + 1) % self.k
            self.q[self.rear] = value
            self.size += 1
            return True
        

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        # delete at front
        if self.size == 0:
            return False
        else:
            self.q[self.front] = 0
            if self.front == self.rear:
                self.front = self.rear = -1
            else:
                self.front = (self.front + 1) % self.k
            self.size -= 1
            return True

        
    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        return self.q[self.front] if self.size > 0 else -1
        

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        return self.q[self.rear] if self.size > 0 else -1
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.size == 0
        

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.size == self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()