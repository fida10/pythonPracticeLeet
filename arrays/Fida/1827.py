nums = [1,5,2,4,1];

ops = 0;

for i in range(1, len(nums)):
    if(nums[i - 1] >= nums[i]):
        currentChange = nums[i - 1] - nums[i] + 1;
        ops += currentChange;
        nums[i] += currentChange;


print(ops);