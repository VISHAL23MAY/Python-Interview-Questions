'''Print sum of all even elements from array.'''

# def sum_of_all(arr):
#     total=0
#     for i in range(len(arr)):
#         if i%2==0:
#             total+=arr[i]
#     print(total)
# nums=[10,20,30,40,50]
# sum_of_all(nums)

'''Print sum of all odd elements from array.'''


def sum_of_all(arr):
    total=0
    for i in range(len(arr)):
        if i%2!=0:
            total+=arr[i]
    print(total)
nums=[10,20,30,40,50]
sum_of_all(nums)
