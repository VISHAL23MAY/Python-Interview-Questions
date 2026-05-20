'''WAJP to check if an array is strictly increasing.
i/p: [2, 3, 7, 8, 9]
o/p: Array is strictly increasing'''


# WAJP to check if array is strictly increasing

def strictly_increasing(arr):

    for i in range(len(arr)-1):

        if arr[i] >= arr[i+1]:
            print("Array is not strictly increasing")
            return

    print("Array is strictly increasing")


num = [2, 3, 7, 8, 9]

strictly_increasing(num)



# def strictly_increasing(arr):

#     previous = arr[0]

#     for i in range(1, len(arr)):

#         current = arr[i]

#         if current > previous:
#             previous = current

#         else:
#             print("Not increasing")
#             return

#     print("Strictly increasing")


# num = [2, 3, 7, 8, 9]

# strictly_increasing(num)



# 

    
        