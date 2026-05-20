'''Print sum of all elements divisible by 3.'''

def sum_of_all_divisible_by_3(arr):
    
    total=0
    for i in arr:
        if i%3==0:
            total+=i
    print(total)
nums=[10,20,30,40]
sum_of_all_divisible_by_3(nums)