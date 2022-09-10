#2011. Final Value of Variable After Performing Operations
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        Y=0
        for X in operations:
            if (X== "X++" or X== "++X"):
                Y = Y+1
            if (X== "X--" or X== "--X"):
                Y = Y-1
        return Y