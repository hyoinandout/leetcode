import copy
class Solution:
    path = []
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(graph, node, n, answer_list):
            Solution.path.append(node)
            if node == (n - 1):
                answer_list.append(copy.deepcopy(Solution.path))
            for next_node in graph[node]:
                dfs(graph, next_node, n, answer_list)
            del Solution.path[-1]
        my_answer = []
        n = len(graph)
        dfs(graph, 0, n, my_answer)
        return my_answer