class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        
        n1=len(nums1)
        n2=len(nums2)
        
        dp = [[0 for _ in range(n2+1)] for _ in range(n1+1)]
        
        nums1 = [0] + nums1
        nums2 = [0] + nums2
        
        ans = 0
        for i in range(1,n1+1):
            for j in range(1,n2+1):
                if nums1[i] == nums2[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
            ans = max(ans,max(dp[i]))
        return ans
                