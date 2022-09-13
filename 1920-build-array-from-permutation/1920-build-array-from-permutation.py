class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        answer = [nums[nums[i]] for i in range(len(nums))]
        return answer