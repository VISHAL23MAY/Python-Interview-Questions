'''WAJP to check whether a given array is in sorted in  increasing order
order or not.
i/p: [2, 7, 7, 8, 9]
o/p: Array is sorted'''


def sorted_array(arr):
    for i in range(len(arr)-1): # to check till last element 

        if arr[i] > arr[i+1]:
            print("Array is not sorted")
            return

    print("Array is sorted")


num = [2, 3, 7, 8, 9]

sorted_array(num)