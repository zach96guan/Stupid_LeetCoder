class Solution {
    public int[][] indexPairs(String text, String[] words) {
        ArrayList<int[]> ret = new ArrayList<>();
        
        for (int i = 0; i < text.length(); i++) {
            for (String word: words) {
                if (text.startsWith(word, i)) {
                    ret.add(new int[]{i, i + word.length() - 1});
                }
            }
        }
        
        Collections.sort(ret, new Comparator<int[]>() {
            @Override
            public int compare(int[] x, int[] y) {
                int cmp = x[0] - y[0];
                if (cmp == 0) {
                    cmp = x[1] - y[1];
                } 
                return cmp;
            }
        });
        
        return ret.toArray(new int[0][]);
    }
}