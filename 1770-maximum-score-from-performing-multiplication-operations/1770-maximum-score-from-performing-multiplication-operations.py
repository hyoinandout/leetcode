class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n = len(nums)
        m = len(multipliers)
        
        dp = [[0 for _ in range(m+1)] for _ in range(m+1)]
        
        for multi in range(m-1,-1,-1):
            for index in range(multi,-1,-1):
                left = multipliers[multi] * nums[index] + dp[multi+1][index+1]
                right = multipliers[multi] * nums[n-1-multi+index] + dp[multi+1][index]
                dp[multi][index] = max(left,right)
        return dp[0][0]
        