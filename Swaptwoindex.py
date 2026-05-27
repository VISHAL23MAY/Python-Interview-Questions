'''wapp to swap two index value of the array
original array: [10,20,30,40,50,60,70]
swapped array:[10,60,30,40,50,20,70]'''


def swap(arr, i, j):

    arr[i], arr[j] = arr[j], arr[i]

    return arr


arr = [10,20,30,40,50,60,70]

print("Original Array:", arr)

swap(arr, 1, 5)

print("Swapped Array:", arr)