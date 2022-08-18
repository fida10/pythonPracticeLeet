#1979. Find Greatest Common Divisor of Array
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        GCD = (nums[0]*nums[len(nums)-1])/math.lcm(nums[0], nums[len(nums)-1]) #From the formula GCD = (a*b)/(lcd(a,b))
        return(int(GCD))

###################2######################
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()

        x = nums[0]
        y = nums[len(nums) - 1]
        z = (x * y) / math.lcm(x, y)  # From the formula GCD = (a*b)/(lcd(a,b))
        return (int(z))

##################################3######################################################
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()

        x = nums[0]  # Original Low Value
        y = nums[len(nums) - 1]  # Original High Value

        while (y):  # Y starts as the highest value
            x, y = y, x % y  # x = to y, and y is equal to the remainder of x % y i.e 5%12 = 0, R =5, 15%4 = 3, r=5
        # This will essentially flip y to the lower value if y is larger than x, if not then this proces repeats and X is the quotient and y decreases and is the remainder and stops until the remainder = 0, thus x is returned which is the GCD
        return abs(x)