import heapq
from collections import deque

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        answer = []
        
        # write index in each of task
        for i in range(len(tasks)):
            tasks[i].append(i)
            
        # make deque to make pop in O(1)    
        sorted_task = sorted(tasks)
        deque_sorted_task = deque(sorted_task)
        
        # to start make current time equal with head of sorted tasks
        current_time = deque_sorted_task[0][0]
        heap = []
        
        # while tasks are present push each task into pq regarding time
        while deque_sorted_task:
            if current_time < deque_sorted_task[0][0] and not heap:
                current_time = deque_sorted_task[0][0]
            while current_time >= deque_sorted_task[0][0]:
                enqueue_time, processing_time, index = deque_sorted_task.popleft()
                heapq.heappush(heap,[processing_time,index])
                if not deque_sorted_task:
                    break
            processing_time,index = heapq.heappop(heap)
            current_time += processing_time
            answer.append(index)
        
        while heap:
            processing_time,index = heapq.heappop(heap)
            answer.append(index)
            
        return answer