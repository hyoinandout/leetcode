class Solution:
    def concatenatedBinary(self, n: int) -> int:
        answer = 0
        for i in range(1,n+1):
            left = len(bin(i)[2:])
            answer = ((answer << left) + i) % (10 ** 9 + 7)
        return answer