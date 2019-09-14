class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:        
        if not intervals or len(intervals) < 2:
            return True
        
        intervals.sort(key=lambda x:x[0])
        for i in range(1, len(intervals)):
            if intervals[i-1][-1] > intervals[i][0]:
                return False     
        return True
        