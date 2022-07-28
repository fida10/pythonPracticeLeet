nums = [1,5,4,5];

biggest = 0;
secondBig = 0;

for num in nums:
    if (num > biggest):
        biggest = num;

nums.remove(biggest);

for num in nums:
    if (num > secondBig):
        secondBig = num;


print((biggest - 1) * (secondBig - 1));