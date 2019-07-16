class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        // O(N^2)
        ArrayList res = new ArrayList<>();
        Arrays.sort(nums);
        
        for (int i = 0; i < nums.length; i++) {
            if (i > 0 && nums[i] == nums[i-1]) {
                continue;
            }
            
            int l = i+1, r = nums.length-1;
            int target = nums[i];
            while (l < r) {
                if (target + nums[l] + nums[r] == 0) {
                    res.add(Arrays.asList(target, nums[l], nums[r]));
                    l++;
                    while (l < r && nums[l] == nums[l-1]) {
                        l++;
                    }
                }
                else if (target + nums[l] + nums[r] < 0) {
                    l++;
                }
                else {
                    r--;
                }
             }
        }
        return res;
    }
}