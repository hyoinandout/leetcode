class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        cnt = 0
        n = len(dominoes)
        status = [0] * n
        failingDir = 0
        for i in range(n):
            if failingDir > 0:
                failingDir -= 1
            if dominoes[i] == "R":
                failingDir = n
            elif dominoes[i] == "L":
                failingDir = 0
            status[i] += failingDir

        failingDir = 0
        for i in range(n-1,-1,-1):
            if failingDir > 0:
                failingDir -= 1
            if dominoes[i] == "L":
                failingDir = n
            elif dominoes[i] == "R":
                failingDir = 0
            status[i] -= failingDir
            
        answer = ""
        for i in range(n):
            if status[i] > 0:
                answer += "R"
            elif status[i] < 0:
                answer += "L"
            else:
                answer += "."
        
        return answer
            