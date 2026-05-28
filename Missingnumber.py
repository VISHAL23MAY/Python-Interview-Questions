'''Given an array nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array.
input:
nums = [9,6,4,2,3,5,7,0,1]
Output: 8'''


def missingNumber( nums):
    n = len(nums)

    total = n * (n + 1) // 2

    arr_sum = sum(nums)

    return total - arr_sum


nums = [9,6,4,2,3,5,7,0,1]



print(missingNumber(nums))