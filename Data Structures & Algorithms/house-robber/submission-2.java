// EITHER USE THE PREVIOUS HOUSE BECAUSE MORE OR THE CURRENT BECAUSE PREVIOUSLY GOT MORE

// nums[i] + best from nums[i - 2]
//OR
// nums[i - 1]
class Solution {
    public int rob(int[] nums) {
        int rob1 = nums[0];
        if(nums.length == 1){
            return rob1;
        }
        int rob2 = nums[1];

        int[] dp = new int[nums.length];
        dp[0] = rob1;
        dp[1] = Math.max(rob1, rob2);
        for(int i = 2; i < nums.length; i++){
            if(nums[i] + dp[i - 2] > dp[i-1]){
                dp[i] = nums[i] + dp[i - 2];
            }else{
                dp[i] = dp[i-1];
            }
        }
        return dp[nums.length - 1];
    }
}
