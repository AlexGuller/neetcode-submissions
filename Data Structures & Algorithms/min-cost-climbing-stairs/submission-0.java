class Solution {
    public int minCostClimbingStairs(int[] cost) {
        int cost1 = cost[0];
        int cost2 = cost[1];

        int[] dp = new int[cost.length];
        dp[0] = cost1;
        dp[1] = cost2;

        for(int i = 2; i < cost.length; i++){
            dp[i] = Math.min(dp[i-1], dp[i-2]) + cost[i];
        }
        return Math.min(dp[cost.length - 1], dp[cost.length - 2]);
    }
}
