class Solution:
    def digitCount(self, num: str) -> bool:

        for i in range(0, len(num)):
            currentNum = num[i];
            currentCount = 0;
            expectedCounter = int(currentNum);
            for j in num:
                if (j == str(i)):
                    currentCount += 1;

            if (currentCount != expectedCounter):
                return False;

        return True;