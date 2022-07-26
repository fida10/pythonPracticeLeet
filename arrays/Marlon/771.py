class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        num_of_jewels = 0
        for stone in stones:
            for jewel in jewels:
                if stone == jewel:
                    num_of_jewels += 1
        return num_of_jewels
