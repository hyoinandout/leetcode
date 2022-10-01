class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * len(s)
        if s[0] != "0":
            dp[0] = 1
            for i in range(1,len(s)):
                if 10 <= int(s[i-1:i+1]) <= 26:
                    if i == 1:
                        dp[i] += 1
                    else:
                        dp[i] += dp[i-2]
                if s[i] != "0":
                    dp[i] += dp[i-1]
        print(dp)
        return dp[len(s)-1]