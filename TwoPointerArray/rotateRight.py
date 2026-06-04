'''WAJP to rotate each element of an array by one
position in right side.

Original array:[10, 20 ,30 ,40, 50, 60 ,70]
Rotated array:[70, 10, 20, 30, 40, 50 ,60] '''


def rotateRightByOne(arr):
    last=arr[len(arr)-1]
    
    for i in range(len(arr)-1,0,-1):
        arr[i]=arr[i-1]
        
    arr[0]=last
    return arr
nums = [10, 20, 30, 40, 50, 60, 70]

print("Original array:", nums)
print("Rotated array :", rotateRightByOne(nums))
    
    
    


