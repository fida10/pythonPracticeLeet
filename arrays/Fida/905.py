nums = [3, 1, 2, 4];
odd = []
even = [];

while(len(nums) > 0):
    if(nums[0] % 2 != 0):
        odd.append(nums[0]);
    else:
        even.append(nums[0]);
    nums.remove(nums[0])

print(even + odd);