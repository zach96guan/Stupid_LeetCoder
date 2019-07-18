class Solution {
    public int heightChecker(int[] heights) {
        int[] right = Arrays.copyOf(heights, heights.length);
        // int[] right = heights.clone();
        Arrays.sort(right);
        
        int n = heights.length, cnt = 0;
        
        for (int i = 0; i < n; i++) {
            if (heights[i] != right[i]) {
                cnt++;
            }
        }
        return cnt;
    }
}