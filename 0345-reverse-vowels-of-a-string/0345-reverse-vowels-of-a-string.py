class Solution:
    def reverseVowels(self, s: str) -> str:
        def isVowel(c):
            if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
                return True
            if c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U':
                return True
            return False
        
        n = len(s)
        answer = ""
        j = n-1
        for i in range(n):
            if isVowel(s[i]):
                while not isVowel(s[j]):
                    j -= 1
                answer += s[j]
                j -= 1
            else:
                answer += s[i]
        
        return answer