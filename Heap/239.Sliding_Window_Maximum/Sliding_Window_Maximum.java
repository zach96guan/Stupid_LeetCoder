class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        Deque<Integer> q = new LinkedList<>();
        ArrayList<Integer> ret = new ArrayList<>();
        
        for (int i = 0; i < nums.length; i++) {
            while (!q.isEmpty() && nums[i] > nums[q.peekLast()]) {
                q.pollLast();
            }
            q.add(i);
            
            if (i == q.peekFirst() + k) {
                q.pollFirst();
            }
            
            if (i >= k - 1) {
                ret.add(nums[q.peekFirst()]);
            }
        }
        return ret.stream().mapToInt(i->i).toArray();
    }
}