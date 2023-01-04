from collections import Counter
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        tasks_counter = Counter(tasks)
        answer = 0
        for task in tasks_counter:
            if tasks_counter[task] == 1:
                return -1
            if tasks_counter[task] == 2:
                answer += 1
                continue
            answer += (tasks_counter[task] // 3)
            if tasks_counter[task] % 3:
                answer += 1
        return answer
                