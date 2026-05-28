'''OceanView Problem:
In right side we have Ocean and array contains
height of buildings. Get all the index of
buildings which will get Ocean view?
i/p:[4, 2, 6, 18, 5, 7, 12, 6]
o/p: [3,6,7]'''


def Sunview(a):

    max_height = 0
    result = []

    # right -> left
    for i in range(len(a)-1, -1, -1):

        if a[i] > max_height:
            result.append(i)
            max_height = a[i]

    result.reverse()

    return result


nums = [4, 2, 6, 18, 5, 7, 12, 6]

print(Sunview(nums))





'''Right to left '''


def Sunview(a):

    max_height = 0
    result = []

    # left -> right
    for i in range(len(a)):

        if a[i] > max_height:
            result.append(i)
            max_height = a[i]

    print(result)


nums = [4, 2, 6, 18, 5, 7, 12, 6]

Sunview(nums)

