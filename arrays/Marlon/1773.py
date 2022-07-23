#1773. Count Items Matching a Rule
#
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
output = 0
value = 0
if ruleKey == "type":
    value = 0
elif ruleKey == "color":
    value = 1
elif ruleKey == "name":
    value = 2

for item in items:
    if item[value] == ruleValue:
        output += 1
return output

