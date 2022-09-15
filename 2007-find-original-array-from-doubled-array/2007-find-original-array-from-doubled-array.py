from collections import Counter
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        answer = []
        cnt = Counter(changed)
        changed.sort()
        
        for num in changed:
            if num * 2 == num:
                if cnt[num] % 2 == 0 and cnt[num]:
                    answer.append(num)
                    cnt[num] -= 2
            else:
                if cnt[num*2] and cnt[num] and cnt[num * 2] >= cnt[num]:
                    cnt[num] -= 1
                    cnt[num*2] -= 1
                    answer.append(num)
                    
        return answer if sum(cnt.values()) == 0 else []