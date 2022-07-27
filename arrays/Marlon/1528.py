class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        order = [None] * len(indices)
        for i in range(0, len(indices)):
            order[indices[i]] = s[i]
        newstring = ''.join(str(x) for x in order)
        return newstring
