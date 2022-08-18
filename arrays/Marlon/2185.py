class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        output=0
        for i in words:
            if i[0:len(pref)]==pref:
                output+=1
        return output