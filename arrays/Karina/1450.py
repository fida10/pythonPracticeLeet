#1450. Number of Students Doing Homework at a Given Time
class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        count = 0
        for i in range(0, len(endTime)):
            if queryTime >= startTime[i] and queryTime <= endTime[i]:
                count += 1
        return count
