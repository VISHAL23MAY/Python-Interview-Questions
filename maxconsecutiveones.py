'''Find Max consecutive ones'''

def findMaxConsecutiveOnes(nums):

    tempCount,maxCount=0,0
    for n in nums:
        if n==1:
            tempCount+=1
        else:
            if tempCount > maxCount:
                maxCount=tempCount
            tempCount=0
    return tempCount if tempCount>maxCount else maxCount
        


nums = [0,1,1,0,0,1,1,1]

print(findMaxConsecutiveOnes(nums))