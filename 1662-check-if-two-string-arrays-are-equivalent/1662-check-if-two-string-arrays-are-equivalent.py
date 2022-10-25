class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        concatenated_word1 = ""
        for word in word1:
            concatenated_word1 += word
        concatenated_word2 = ""
        for word in word2:
            concatenated_word2 += word
        if concatenated_word1 == concatenated_word2:
            return True
        return False