class Solution:
    def reverseWords(self, s: str) -> str:
        answer = ""
        chunks = s.split()
        for chunk in chunks:
            answer += chunk[::-1]
            answer += " "
        return answer[:-1]