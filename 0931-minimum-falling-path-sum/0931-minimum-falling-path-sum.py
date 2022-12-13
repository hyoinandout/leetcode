class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        
        dp = [[0 for _ in range(n+2)]] + [[10001 for _ in range(n+2)] for _ in range(n+1)]
        
        for i in range(1,n+1):
            for j in range(1,n+1):
                dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i-1][j+1]) + matrix[i-1][j-1]
                
        answer = 10001
        for i in range(1,n+1):
            answer = min(answer, dp[n][i])
            
        return answer