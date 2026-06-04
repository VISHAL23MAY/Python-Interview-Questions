def solution(nums):
    i=0
    for j in range(1,len(nums)):
        if (nums[j]!=nums[i]):
            i+=1
            nums[i]=nums[j]
a=[2,3,3,4,5,5,5,6]
solution(a)7