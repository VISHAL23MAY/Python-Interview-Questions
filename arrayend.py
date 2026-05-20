# Access all elements of array from end.

def acess_from_end(arr):
    for i in range(len(arr)-1, -1, -1):
        print(arr[i])

numbers = [10, 20, 30, 40, 50,77]

acess_from_end(numbers)