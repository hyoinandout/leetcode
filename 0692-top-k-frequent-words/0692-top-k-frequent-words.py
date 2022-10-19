from collections import defaultdict
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        answer = []
        
        dictionary = defaultdict(int)
        for word in words:
            dictionary[word] += 1
        
        cnt = 0
        
        sorted_dict = sorted(dictionary.items(),key=lambda x:(-x[1],x[0]))
        
        for item in sorted_dict:
            answer.append(item[0])
            cnt += 1
            if cnt == k:
                break
        return answer