class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        ans = 0;

        for i in range(0, len(startTime)):
            if (queryTime > startTime[i] - 1 and queryTime < endTime[i] + 1):
                ans += 1;

        return ans;
