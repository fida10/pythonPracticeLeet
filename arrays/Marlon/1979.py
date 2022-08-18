nums = [7,5,6,8,3]
nums.sort()
minimum=min(nums)
maximum=max(nums)
output=[]
for i in range(1, minimum+1):
    if minimum%i==0 and maximum%i==0:
        output.append(i)
print(max(output))