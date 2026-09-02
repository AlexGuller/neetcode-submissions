class Solution {
    public int[] productExceptSelf(int[] nums) {
        int prefix = 1;
        int postfix = 1;
        int[] res = new int[nums.length];
        Arrays.fill(res, 1);
        for(int i = 0; i < nums.length; i++){
            res[i] = prefix;
            prefix *= nums[i];
        }
        for(int i = nums.length - 1; i >= 0; i--){
            res[i] *= postfix;
            postfix *= nums[i];
        }
        return res;

    }
}  
