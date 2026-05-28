
'''Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]'''


def validMountainArray(arr):

        n = len(arr)

        # length check
        if n < 3:
            return False

        i = 0

        # increasing part
        while i + 1 < n and arr[i] < arr[i + 1]:
            i += 1

        # peak first ya last nahi hona chahiye
        if i == 0 or i == n - 1:
            return False

        # decreasing part
        while i + 1 < n and arr[i] > arr[i + 1]:
            i += 1

        return i == n - 1
nums=[0,3,2,1]
print(validMountainArray(nums))