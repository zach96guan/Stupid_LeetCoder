class Solution {
    public int validSubarrays(int[] nums) {
        // O(N^2)
        // int ret = 0;
        // for (int i = 0; i < nums.length; i++) {
        //     int tmp = 1;
        //     for (int j = i+1; j < nums.length; j++) {
        //         if (nums[i] <= nums[j]) {
        //             tmp++;
        //         }
        //         else {
        //             break;
        //         }
        //     }
        //     ret += tmp;
        // }
        // return ret;
        
        // O(N)
        int ret = 0;
        Stack<Integer> stack = new Stack<>();
        
        for (int num: nums) {
            while (!stack.isEmpty() && num < stack.peek()) {
                stack.pop();
            }
            
            stack.push(num);
            ret += stack.size();
        }
        return ret;
    }
}