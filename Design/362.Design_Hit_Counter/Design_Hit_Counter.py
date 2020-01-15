class HitCounter:
    # scalable solution
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hits = [[0, i + 1] for i in range(300)]
        

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        idx = (timestamp - 1) % 300
        if self.hits[idx][1] == timestamp:
            self.hits[idx][0] += 1
        else:
            self.hits[idx][1] = timestamp 
            self.hits[idx][0] = 1            
                 

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        cnt = 0
        for freq, t in self.hits:
            if timestamp - t < 300:
                cnt += freq
        
        return cnt


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)