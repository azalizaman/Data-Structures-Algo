from cmath import inf
from sympy import minimum


def minSubArrayLen(target, nums):
    left=0
    windowSum=0
    minWindowSize=float('inf')

    for right in range(len(nums)):
        windowSum+=nums[right]

        while windowSum>target:
            windowSum-=nums[left]
            left+=1

        if windowSum==target:
            minWindowSize=min(minWindowSize, right-left)

    if minWindowSize==float('inf'):
        return 0
    return minWindowSize+1

print(minSubArrayLen(13,[1,3,5,5,2,8,10]))