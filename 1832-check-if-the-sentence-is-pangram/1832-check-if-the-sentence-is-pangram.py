class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        visited = [False] * 26
        for alphabet in sentence:
            visited[ord(alphabet) - 97] = True
        return all(visited)