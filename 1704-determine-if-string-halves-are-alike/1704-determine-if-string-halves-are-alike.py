class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        def isVowel(letter: str) -> bool:
            if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u' or letter == 'A' or letter == 'E' or letter == 'I' or letter == 'O' or letter == 'U':
                return True
            return False
        cnt = 0
        for i in range(len(s)//2):
            if isVowel(s[i]):
                cnt += 1
        for i in range(len(s)//2,len(s)):
            if isVowel(s[i]):
                cnt -= 1
        
        return True if cnt == 0 else False