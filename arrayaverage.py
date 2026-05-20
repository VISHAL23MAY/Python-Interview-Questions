# Print Average of all elements from array.
def average_of_all(arr):
    total=0
    for i in range(len(arr)):
        total+=arr[i]
    
    avg=total/len(arr)
    
nums=[10,20,30,40,50]
average_of_all(nums)






# or
# def average_of_all(arr):

#     total = 0

#     for i in arr:
#         total += i

#     avg = total / len(arr)

#     print(avg)