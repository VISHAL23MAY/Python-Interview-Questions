'''For the given array of Strings, print the largest
string.'''

def largest_string(arr):
    largest=arr[0]
    for i in range(len(arr)):
        if len(arr[i])> len(largest):
            largest=arr[i]
    print(largest)
    
names = ["hi", "hello", "python", "java"]

largest_string(names)