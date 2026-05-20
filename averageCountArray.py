'''WAJP to print and count all the elements of array which are bigger than average value.'''

# WAJP to print and count all the elements
# of array which are bigger than average value

def Average_count_Bigger(arr):

    total = 0

    for i in range(len(arr)):
        total += arr[i]

    avg = total / len(arr)

    count = 0

    for i in range(len(arr)):

        if arr[i] > avg:
            print(arr[i])
            count += 1

    print("Count =", count)


nums = [10, 20, 30, 40]

Average_count_Bigger(nums) 





# or    
# WAJP to print and count all the elements
# of array which are bigger than average value

# def Average_count_Bigger(arr):

#     total = 0

#     for i in arr:
#         total += i

#     avg = total / len(arr)

#     count = 0

#     for i in arr:

#         if i > avg:
#             print(i)
#             count += 1

#     print("Count =", count)


# nums = [10, 20, 30, 40]

# Average_count_Bigger(nums)