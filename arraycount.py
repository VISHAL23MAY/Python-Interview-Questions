# print and count all three-digit numbers from array.

# Print and count all three-digit numbers from array

def count_all_array(arr):
    count = 0

    for i in range(len(arr)):                                      #for i in arr:                             
        if arr[i] >= 100 and arr[i] <= 999:                         #if 100 <= i <= 999:
            print(arr[i])                                              #print(i)
            count += 1

    print("Count =", count)


nums = [10, 120, 30, 456, 50, 999, 1000]

count_all_array(nums)




# or
# for i in arr:
#     if 100 <= i <= 999:
#         print(i)