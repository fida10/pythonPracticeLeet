s = "abccbaacz";

lowestIndexOfSecond = len(s);

for i in range(0, len(s)):
    currentVal = s[i];
    currentIndexOfSecond = len(s);
    for j in range(i + 1, len(s)):
        if (s[j] == currentVal):
            currentIndexOfSecond = j;
            break;
    if (currentIndexOfSecond < lowestIndexOfSecond):
        lowestIndexOfSecond = currentIndexOfSecond;

print(s[lowestIndexOfSecond]);