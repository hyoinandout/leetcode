class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        answer = []
        
        sum_evens = 0
        for num in nums:
            if num % 2 == 0:
                sum_evens += num
                
        for query in queries:
            value, index = query[0], query[1]
            if value % 2 == 0:
                if nums[index] % 2 == 0:
                    sum_evens += value
                else:
                    pass
            else:
                if nums[index] % 2 == 0:
                    sum_evens -= nums[index]
                else:
                    sum_evens += (nums[index] + value)
            nums[index] += value
            answer.append(sum_evens)
        return answer
            