nums = [12,345,2,6,7896]
output=0
for num in nums:
    if len(str(num))%2==0:
        output+=1
print(output)