# 771. Jewels and Stones
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for jewel in jewels:
            for stone in stones:
                if jewel == stone:
                    count = count + 1
        return count
