class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        n = len(s1)
        
        parent = [i for i in range(26)]
        def findParent(s: str):
            idx = ord(s)-97
            while parent[idx] != idx:
                idx = parent[idx]
            return parent[idx]
        
        for i in range(n):
            idx_s1 = findParent(s1[i])
            idx_s2 = findParent(s2[i])
            if parent[idx_s1] < parent[idx_s2]:
                parent[idx_s2] = parent[idx_s1]
            else:
                parent[idx_s1] = parent[idx_s2]
            
        answer = ""
        for i in range(len(baseStr)):
            idx = findParent(baseStr[i])
            answer += chr(idx+97)
        return answer