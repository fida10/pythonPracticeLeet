# 1528. Shuffle String
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        empty = [0] * len(s)
        for i in range(0, len(s)):
            empty[indices[i]] = s[i]

        result = "".join(empty)
        return result
