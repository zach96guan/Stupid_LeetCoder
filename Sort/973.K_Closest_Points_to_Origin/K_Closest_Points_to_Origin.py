class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        # O(N)
        dist = lambda i : points[i][0] ** 2 + points[i][1] ** 2
        
        def sort(i, j, K):
            if i >= j:
                return
            
            k = random.randint(i, j)
            points[i], points[k] = points[k], points[i]
            
            m = partition(i, j)
            if K < m - i + 1:
                sort(i, m - 1, K)
            elif K > m - i + 1:
                sort(m + 1, j, K - (m - i + 1))
    
    
        def partition(i, j):
            pre_i = i
            pivot = dist(i)
            i += 1
            
            while i <= j:
                while i < j and dist(i) < pivot:
                    i += 1
                while i <= j and dist(j) >= pivot:
                    j -= 1
                
                if i >= j:
                    break
                points[i], points[j] = points[j], points[i]
            
            points[pre_i], points[j] = points[j], points[pre_i]
            return j
        
        
        sort(0, len(points) - 1, K)
        return points[:K]
      
        