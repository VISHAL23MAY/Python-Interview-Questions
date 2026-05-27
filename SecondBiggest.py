'''WAP to print Second Distinct biggest element of the array.
int[] a= {80, 80, 43, 50, 38, 63, 58, 80};
o/p
63'''
def SecondBiggest(a):
    max=float('-inf')
    Second_max=float('-inf')
    for n in a:
        if n > max:
            Second_max=max
            max = n
        if n > Second_max and n!=max:
            Second_max = n
        
    print("Max:",max)
    print("second Max:",Second_max)
                
                
    
nums=[80, 80, 43, 50, 38, 63, 58, 80]
SecondBiggest(nums)