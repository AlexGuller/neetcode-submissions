class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> seen = new HashMap<>();
        for(int i = 0; i < nums.length; i++){
            if(seen.containsKey(target - nums[i])){
                int[] arr = new int[2];
                arr[0] = seen.get(target - nums[i]);
                arr[1] = i;
                return arr;
            }else{
                seen.put(nums[i], i);
            }
        }
        return new int[2];
    }
}
