class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # O(n), O(1)
        # Voting Algorithm
        cnt1 = cnt2 = 0
        cand1 = cand2 = None
        
        for num in nums:
            if num == cand1:
                cnt1 += 1
            elif num == cand2:
                cnt2 += 1
            
            elif cnt1 == 0:
                cand1, cnt1 = num, 1
            elif cnt2 == 0:
                cand2, cnt2 = num, 1
            
            else:
                cnt1 -= 1
                cnt2 -= 1
        
        return [x for x in (cand1, cand2) if nums.count(x) > len(nums) // 3]
        