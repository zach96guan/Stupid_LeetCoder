class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        
        for i in range(n):
            if nums[i] == 0:
                continue
            
            # slow/fast pointers
            j = i
            k = self.next_loc(nums, n, i)
            
            while nums[k] * nums[i] > 0 and nums[self.next_loc(nums, n, k)] * nums[i] > 0:
                if j == k:
                    if j == self.next_loc(nums, n, j):  # cycle length > 1
                        break
                    return True
                else:
                    j = self.next_loc(nums, n, j)
                    k = self.next_loc(nums, n, self.next_loc(nums, n, k))
        
            # set to zero when we find different direction (search fail)
            pos = i
            while nums[pos] * nums[i] > 0:
                nxt_pos = self.next_loc(nums, n, pos)
                nums[pos] = 0
                pos = nxt_pos
        
        return False
            
        
    def next_loc(self, nums, n, i):
        return (nums[i] + i + n) % n
        
    