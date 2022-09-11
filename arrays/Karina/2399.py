# 2399. Check Distances Between Same Letters, courtesy of Marlon, :]
class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        # refLetter = list(string.ascii_lowercase)
        # asci a = 97
        # print(distance)
        # uniqueNum = []*(int(len(s)/2))
        ans = True
        Dist = 0;
        Letter = 0

        for i in range(0, len(s)):
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    if (j - i - 1) != distance[ord(s[i]) - 97]:
                        return False
                    else:
                        break

        return (True)

