class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // Freq map <number, count>
        HashMap<Integer, Integer> map = new HashMap<>();
        for(int n : nums){
            map.put(n, map.getOrDefault(n, 0) + 1);
        }

        // Buckets
        List<List<Integer>> bucks = new ArrayList<>();
        for(int i = 0; i < nums.length + 1; i++){
            List<Integer> temp = new ArrayList<>();
            bucks.add(temp);
        }

        // Fill buckets
        for(int n : map.keySet()){
            int index = map.get(n);
            bucks.get(index).add(n);
        }

        // Loop
        int[] res = new int[k];
        int cntr = k - 1;
        int buckCntr = bucks.size() - 1;
        while(cntr >= 0){
            if(bucks.get(buckCntr).size() != 0){
                int bucksCntrCntr = bucks.get(buckCntr).size() - 1;
                while(cntr >= 0 && bucksCntrCntr >= 0){
                    res[cntr] = bucks.get(buckCntr).get(bucksCntrCntr);
                    bucksCntrCntr--;
                    cntr--;
                }
            }
            buckCntr--;
        }
        return res;
    }
}
