if n==1:
    return [0]
if n==2:
    return[-1, 1]
output = []
sub = 0
if (n % 2) != 0:
    output.append(0)
while (len(output) < n - 1):
    number = n - sub
    output.append(number)
    output.append(number * -1)
    sub += 1
return output