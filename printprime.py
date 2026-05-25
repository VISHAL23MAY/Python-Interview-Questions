'''WAJP to print all prime numbers available in array.'''


# def print_prime(num):
#     if num==0 or num==1:
#         return num
#     for i in range(2,num):
#         if num%i==0:
#             return False
#         return True
# num=[1,2,3,4,5,6,7,8,9]
# for i in num:
#     if print_prime(i):
#         print(i)
        
        
"WAJP to count all prime numbers available inarray."

def print_prime_count(num):
    if num==0 or num==1:
        return num
    for i in range(2,num):
        if num%i==0:
            return False
        return True
num=[1,2,3,4,5,6,7,8,9]
count=0

for i in num:
    
    if print_prime_count(i):
        count+=1
        print(i,end=" ")
print("the count is :",count)
        
        
        