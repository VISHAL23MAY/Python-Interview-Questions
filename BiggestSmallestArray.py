'''Print Biggest and Smallest Element of Array.'''


# Print Biggest and Smallest Element of Array

def Biggest_Smallest(arr):

    biggest = arr[0]
    smallest = arr[0]

    # Biggest
    for i in arr:

        if i > biggest:
            biggest = i

    # Smallest
    for i in arr:

        if i < smallest:
            smallest = i

    print("Biggest =", biggest)
    print("Smallest =", smallest)


nums = [1, 2, 3, 4, 5, 6]

Biggest_Smallest(nums)
            