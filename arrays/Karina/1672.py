# 1672. Richest Customer Wealth
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = 0
        for i in range(0, len(accounts)):
            tempWealth = 0
            for j in range(0, len(accounts[i])):
                tempWealth = tempWealth + accounts[i][j]
            if tempWealth > wealth:
                wealth = tempWealth

        return wealth

#    rows = len(matrix)
# columns = len(matrix[0]) 