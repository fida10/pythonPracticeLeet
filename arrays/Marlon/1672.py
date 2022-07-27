class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = 0
        for i in accounts:
            currentwealth = 0
            for j in i:
                currentwealth += j
            if currentwealth > wealth:
                wealth = currentwealth

        return wealth