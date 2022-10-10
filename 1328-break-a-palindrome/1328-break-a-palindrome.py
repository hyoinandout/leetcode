class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        answer = ['z'] * 1000
        answer = ''.join(answer)
        flag = False
        for i in range(len(palindrome) // 2):
            for j in range(97,ord(palindrome[i])):
                temp = list(palindrome)
                temp[i] = chr(j)
                answer = min(answer,''.join(temp))
                flag = True
                break
            if flag:
                break
        
        if not flag:
            temp = list(palindrome)
            temp[-1] = 'b'
            answer =''.join(temp)
        
        if len(palindrome) == 1:
            answer = ""
        
        return answer
        