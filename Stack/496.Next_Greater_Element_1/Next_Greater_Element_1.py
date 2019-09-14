class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # O(M + N), O(M + N)
        stack = []
        dic = collections.defaultdict(lambda:-1)
        
        for num in nums2:
            while stack and num > stack[0]:
                dic[stack.pop(0)] = num
            stack.insert(0, num)
        
        return [dic[num] for num in nums1]
        