class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxNo = 0;

        for sentence in sentences:
            currentLen = len(sentence.split(" "));
            if (currentLen) > maxNo:
                maxNo = currentLen;

        return maxNo;