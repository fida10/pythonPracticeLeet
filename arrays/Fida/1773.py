# 1773. Count Items Matching a Rule

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:

        keyIndex = 0;
        if (ruleKey == 'color'):
            keyIndex = 1;
        elif (ruleKey == 'name'):
            keyIndex = 2;

        counter = 0;
        for indivItem in items:
            if (indivItem[keyIndex] == ruleValue):
                counter += 1;

        return counter;