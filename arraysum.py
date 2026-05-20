# Print sum of all elements from array.

def sum_of_array(arr):
    sum=0
    for i in range(len(arr)):
        
        sum+=arr[i]
    print(sum)
nums=[10,20,30,40,50]
sum_of_array(nums)


# or 
# def sum_of_array(arr):

#     sum = 0

#     for i in arr:
#         sum += i

#     print(sum)