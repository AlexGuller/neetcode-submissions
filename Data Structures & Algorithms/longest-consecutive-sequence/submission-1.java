class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> quick = new HashSet<>();
        for(int n : nums){
            quick.add(n);
        }
        int max = 0;
        int curr = 0;
        for(int i = 0; i < nums.length; i++){
            if(!quick.contains(nums[i] - 1)){
                int val = nums[i];
                while(quick.contains(val)){
                    val++;
                    curr++;
                }
                max = Math.max(curr, max);
                curr = 0;
            }
        }
        return max;
    }
}
