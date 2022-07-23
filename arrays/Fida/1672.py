class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:

        maxVal = 0;
        for person in accounts:
            currentVal = 0;
            for account in person:
                currentVal += account;

            if currentVal > maxVal:
                maxVal = currentVal;

        return maxVal;