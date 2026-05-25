def isPrime(n):
    if(n<1):
        return False
    for i in range(2,n):
        if n%i==0:
            return False
        return True
def printandCount(arr):
    count=0
    for i in arr:
        if(isPrime(i)):
            print(i)
            count+=1
    print("Total Prime Numbers=",count)
    
numbers=[1,2,3,4,5,6,7,8,9,10,11]
printandCount(numbers)