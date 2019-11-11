class RandomizedSet:
    # O(1), list pop() + dictionary access
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}
        self.q = []
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.dic:
            return False
        else:
            self.q.append(val)
            idx = len(self.q) - 1
            self.dic[val] = idx
            return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.dic:
            return False
        else:
            last = self.q[-1]
            idx = self.dic[val]
            self.dic[last] = idx
            self.q[idx] = last
             
            del self.dic[val]
            self.q.pop()
            return True
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.q)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()