class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = [];
        subtract = 0;
        while (len(ans) < n - 1):
            numToAdd = n - subtract;
            ans.append(numToAdd)
            ans.append(numToAdd * -1)
            subtract += 1;

        if (n % 2 != 0):
            ans.append(0);

        return ans;