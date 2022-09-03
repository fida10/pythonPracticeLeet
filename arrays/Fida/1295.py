class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0;

        for indivNum in nums:
            digitsInIndivNum = 0;
            while (indivNum != 0):
                indivNum = int(indivNum / 10);
                digitsInIndivNum += 1;
            if (digitsInIndivNum % 2 == 0):
                ans += 1;

        return ans;