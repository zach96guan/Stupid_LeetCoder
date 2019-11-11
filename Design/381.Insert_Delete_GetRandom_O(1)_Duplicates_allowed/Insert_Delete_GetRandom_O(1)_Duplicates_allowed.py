class RandomizedCollection:
    # O(1), follow-up using Set
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = []
        self.dic = collections.defaultdict(set)
        

    def insert(self, val: 'int') -> 'bool':
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.q.append(val)
        idx = len(self.q) - 1
        self.dic[val].add(idx)
        return len(self.dic[val]) == 1
        

    def remove(self, val: 'int') -> 'bool':
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if len(self.dic[val]) < 1:
            return False
        
        idx = self.dic[val].pop()
        last = self.q[-1]
        self.dic[last].add(idx)
        self.q[idx] = last
        
        self.dic[last].discard(len(self.q) - 1)
        self.q.pop()
        return True
            

    def getRandom(self) -> 'int':
        """
        Get a random element from the collection.
        """
        return random.choice(self.q)
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()