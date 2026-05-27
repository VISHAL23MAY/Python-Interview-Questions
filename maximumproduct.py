'''Given the array of integers nums, you will choose two different indices i and j of that array. 
Return the maximum value of (nums[i]-1)*(nums[j]-1).
 Example 1:
Input: nums = [3,4,5,2]
Output: 12 
Explanation: If you choose the indices i=1 and j=2 (indexed from 0), 
you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12. '''

  
def maxProduct(nums):
    firstMax = 0
    secondMax = 0

    for n in nums:
        if n > firstMax:
            secondMax = firstMax
            firstMax = n

        elif n > secondMax:
            secondMax = n

    return (firstMax - 1) * (secondMax - 1)


nums = [3, 4, 5, 2]

print("Maximum Product:", (maxProduct(nums)))