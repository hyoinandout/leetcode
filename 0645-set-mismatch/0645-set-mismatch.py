class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        set_nums = set(nums)
        original_nums = [i for i in range(1,len(nums) + 1)]
        visited_nums = [False] * (len(nums) + 1)
        
        answer = []
        
        for num in nums:
            if not visited_nums[num]:
                visited_nums[num] = True
            else:
                answer.append(num)
        
        
        for num in original_nums:
            if num not in set_nums:
                answer.append(num)
        
        return answer