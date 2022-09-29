class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        arr = [-30001] + arr + [30001]
        index = 0
        for i in range(len(arr)):
            index = i
            if arr[i] >= x:
                break
        
        cnt = 0
        left_index = index - 1
        right_index = index
        
        answer = []
        
        while cnt < k:
            if abs(arr[left_index] - x) <= abs(arr[right_index] - x):
                answer.append(arr[left_index])
                left_index -= 1
                cnt += 1
            
            if cnt == k:
                break
                
            if abs(arr[left_index] - x) > abs(arr[right_index] - x):
                answer.append(arr[right_index])
                right_index += 1
                cnt += 1   
            
        
        answer.sort()
        return answer