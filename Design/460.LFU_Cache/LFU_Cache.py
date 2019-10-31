from collections import OrderedDict, defaultdict
# OrderedDict == dict + double linked list, O(1)

class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.key2valfreq = {}  # key -> (val, freq)
        self.count2node = defaultdict(OrderedDict)  # freq -> key -> node
        self.capacity = capacity
        self.min_freq = 1


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.key2valfreq:
            return -1
        
        val, freq = self.key2valfreq.pop(key)
        self.count2node[freq].pop(key)
        
        if len(self.count2node[freq]) == 0 and freq == self.min_freq:
            self.min_freq = freq + 1

        self.count2node[freq + 1][key] = None
        self.key2valfreq[key] = (val, freq + 1)
        return val


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.capacity <= 0:
            return
        
        if key in self.key2valfreq:
            self.get(key)
            self.key2valfreq[key] = (value, self.key2valfreq[key][1])
            return
        
        if self.capacity <= len(self.key2valfreq):
            k, _ = self.count2node[self.min_freq].popitem(last=False)  # FIFO
            self.key2valfreq.pop(k)
        
        self.key2valfreq[key] = (value, 1)
        self.count2node[1][key] = None
        self.min_freq = 1
        

        
# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)