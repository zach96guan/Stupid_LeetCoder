class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # greedy, O(NlogN), O(1)
        n = len(costs) // 2
        costs.sort(key=lambda x:x[0] - x[1])
        return sum(a if i < n else b for i, (a, b) in enumerate(costs))