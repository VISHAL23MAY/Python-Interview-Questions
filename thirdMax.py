'''Given an integer array nums, return the third distinct maximum number in this array. 
If the third maximum does not exist, return the maximum number.
Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.'''

def thirdMax(nums):

    fMax = float('-inf')
    sMax = float('-inf')
    tMax = float('-inf')

    for n in nums:

        if n > fMax:
            tMax = sMax
            sMax = fMax
            fMax = n

        elif n > sMax and n != fMax:
            tMax = sMax
            sMax = n

        elif n > tMax and n != fMax and n != sMax:
            tMax = n

    return fMax if tMax == float('-inf') else tMax


nums = [20,18,17,16,20]

result = thirdMax(nums)

print("Third Maximum Number:", result)