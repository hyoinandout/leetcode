import heapq
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        max_heap = []
        for i in range(len(piles)):
            heapq.heappush(max_heap,-piles[i])
        
        for i in range(k):
            max_pile = heapq.heappop(max_heap)
            heapq.heappush(max_heap, max_pile // 2)
        
        return -sum(max_heap)
        