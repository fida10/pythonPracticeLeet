# 2114. Maximum Number of Words Found in Sentences
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:

        maxVal = 0

        for sentence in sentences:
            val = len(sentence.split(" "))
            if val > maxVal:
                maxVal = val
        return maxVal

