'''Sunlight Problem:
In left side we have sun and array contains
height of buildings. How many buildings will
get sun light?
i/p:[4, 2, 6, 8, 5, 7, 12, 6]
o/p: 4'''

def Sunlight(a):
    count=1
    max_Height=a[0]
    for i in range(1,len(a)):
        if a[i]>max_Height:
            count+=1
            max_Height=a[i]
    return count
nums=[4, 2, 6, 8, 5, 7, 12, 6]
print(Sunlight(nums))