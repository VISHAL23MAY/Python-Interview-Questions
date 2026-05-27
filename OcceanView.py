'''OceanView Problem:
In right side we have Ocean and array contains
height of buildings. How many buildings will
get Ocean view?
i/p:[4, 2, 6, 18, 5, 7, 12, 6]
o/p: 3'''

def OcceanView(a):
    count=1
    Max_height=len(a)-1                #or a[-1]
    for i in range(len(a)-2,-1,-1):
        if a[i]>Max_height:
            count+=1
            Max_height=a[i]
    return count
nums=[4, 2, 6, 18, 5, 7, 12, 6]
print( OcceanView(nums))
        