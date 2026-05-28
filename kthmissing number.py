'''Given an array arr of positive integers sorted in a strictly increasing order, 
and an integer k.
Return the kth positive integer that is missing from this array.

Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. 
The 5th missing positive integer is 9.'''



def MissingNumber(a):
    k=5
    for n in a:
        if n<=k:
            k+=1
        else:
            break
    return k
nums= [2,3,4,7,11]
print(MissingNumber(nums))
