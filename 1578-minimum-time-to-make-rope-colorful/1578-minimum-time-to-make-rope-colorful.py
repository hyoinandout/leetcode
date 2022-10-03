class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        answer = 0
        minTime = 0
        initialColor = ""
        
        for i in range(len(colors)):
            if initialColor == colors[i]:
                if minTime > neededTime[i]:
                    answer += neededTime[i]
                    initialColor = colors[i]
                    continue
                else:
                    answer += minTime
            minTime = neededTime[i]
            initialColor = colors[i]
            
        return answer