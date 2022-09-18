from collections import deque
class Solution:
    def trap(self, height: List[int]) -> int:
        answer = 0
        stored = 0
        heap = []
        heapq.heappush(heap,-height[0])
        for i in range(len(height)):
            if height[i] >= -heap[0]:
                answer += stored
                stored = 0
                heap = []
                heapq.heappush(heap,-height[i])
            else:
                stored += (-heap[0]) - height[i]
        stored = 0
        heap = []
        heapq.heappush(heap,-height[-1])
        for i in range(len(height)-1,-1,-1):
            if height[i] > -heap[0]:
                answer += stored
                stored = 0
                heap = []
                heapq.heappush(heap,-height[i])
            else:
                stored += (-heap[0]) - height[i]
        return answer