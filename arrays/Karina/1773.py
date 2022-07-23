#1773. Count Items Matching a Rule
#New pythin file
class Solution:
def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
    counter = 0
    for i in range(0, len(items)):

        if ruleKey == "type" and items[i][0] == ruleValue:
            counter = counter + 1
        elif ruleKey == "color" and items[i][1] == ruleValue:
            counter = counter + 1
        elif ruleKey == "name" and items[i][2] == ruleValue:
            counter = counter + 1
    return counter
