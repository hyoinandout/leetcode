from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        answer = []
        p_counter = Counter(p)
        for i in range(len(s)-len(p)+1):
            if Counter(s[i:i+len(p)]) == p_counter:
                answer.append(i)
        return answer