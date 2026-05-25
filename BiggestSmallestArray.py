'''Print Biggest and Smallest Element of Array.'''


# Print Biggest and Smallest Element of Array

# def Biggest_Smallest(arr):

#     biggest = arr[0]
#     smallest = arr[0]

#     # Biggest
#     for i in arr:

#         if i > biggest:
#             biggest = i

#     # Smallest
#     for i in arr:

#         if i < smallest:
#             smallest = i

#     print("Biggest =", biggest)
#     print("Smallest =", smallest)


# nums = [1, 2, 3, 4, 5, 6]

# Biggest_Smallest(nums)


'''OR'''

def printBiggestSmallest(a):
    big=a[0]
    small=a[0]
    for n in a :
        if n>big:
            big=n
        elif n<small:
            small=n
    print(f"biggest is :{big}")
    print(f"smallest is :{small}")

a=[12,34,96,78,10,90]
printBiggestSmallest(a)
            

            