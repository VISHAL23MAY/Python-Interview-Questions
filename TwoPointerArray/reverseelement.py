'''WAJP to reverse each element of the array.
Original array:10 20 30 40 50 60 70
Reversed array:70 60 50 40 30 20 10'''



def reverseElement(a):
    start = 0
    end = len(a) - 1

    while start < end:
        a[start], a[end] = a[end], a[start]
        start += 1
        end -= 1

    return a

nums = [10, 20, 30, 40, 50, 60, 70]

print("Original array:", nums)
print("Reversed array:", reverseElement(nums))