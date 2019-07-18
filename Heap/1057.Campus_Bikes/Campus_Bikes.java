class Solution {
    public int[] assignBikes(int[][] workers, int[][] bikes) {
        // index order
        PriorityQueue<int[]> q = new PriorityQueue<>((a, b) -> {
            int comp = Integer.compare(a[0], b[0]);
            if (comp == 0) {
                if (a[1] == b[1]) {
                    return Integer.compare(a[2], b[2]);
                }
                else {
                    return Integer.compare(a[1], b[1]);
                }
            }
            return comp;
        });
            
        for (int i = 0; i < workers.length; i++) {
            int[] worker = workers[i];
            for (int j = 0; j < bikes.length; j++) {
                int[] bike = bikes[j];
                int d = Math.abs(worker[0] - bike[0]) + Math.abs(worker[1] - bike[1]);
                q.add(new int[]{d, i, j});
            }
        }
        
        int[] ret = new int[workers.length];
        Arrays.fill(ret, -1);
        Set<Integer> set = new HashSet<>();
        while (set.size() < workers.length) {
            int[] tmp = q.poll();
            int wid = tmp[1], bid = tmp[2];
            if (ret[wid] == -1 && !set.contains(bid)) {
                ret[wid] = bid;
                set.add(bid);
            }
        }
        return ret;
    }
}