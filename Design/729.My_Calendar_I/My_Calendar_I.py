class Node:
    def __init__(self, start, end):
        self.s = start
        self.e = end
        self.left = None
        self.right = None

    def insert(self, start, end):
        if self.s >= end:
            if not self.left:
                self.left = Node(start, end)
                return True
            else:
                return self.left.insert(start, end)
        elif self.e <= start:
            if not self.right:
                self.right = Node(start, end)
                return True
            else:
                return self.right.insert(start, end)
        else:
            return False


class MyCalendar:
    # binary search
    # O(NlogN), O(N)
    def __init__(self):
        self.root = None
        
    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if not self.root:
            self.root = Node(start, end)
            return True
        else:
            return self.root.insert(start, end)


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)