class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        return (getValueOfWord(firstWord) + getValueOfWord(secondWord)) == getValueOfWord(targetWord);


def getValueOfWord(word):
    val = 0;

    for i in range(0, len(word)):
        val += (ord(word[i]) - 97) * (10 ** ((len(word) - 1) - i));

    return (val);