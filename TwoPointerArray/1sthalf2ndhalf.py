'''WAJP to reverse 1st half and 2nd half elements of array.

Original array:10 20 30 40 50 60 70
Reversed array:40 30 20 10 70 60 50 
'''
'''this method is applicable when the length of array is odd'''


def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

arr = [10, 20, 30, 40, 50, 60, 70]

mid = len(arr) // 2

reverse(arr, 0, mid)              # first half
reverse(arr, mid + 1, len(arr)-1) # second half

print(arr)




'''this method is applicable when the length of array is even


def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

arr = [10, 20, 30, 40, 50, 60]

mid = len(arr) // 2

# First half: 0 to mid-1
reverse(arr, 0, mid - 1)

# Second half: mid to n-1
reverse(arr, mid, len(arr) - 1)

print(arr)
'''