nums = [6,2,6,5,1,2]
nums.sort()
output=0
for i in range(0,len(nums),2):
    output+=min(nums[i], nums[i+1])
print(output)