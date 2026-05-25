'''Check if a given string is strictly increasing or not '''

def Strictly_increasing(a):
    for i in range(1,len(a)):
        if a[i-1]>=a[i]:
            return False
        return True
strs=["vishal","Anuj","kundan","Kuldeep","Abhinav"]
print(Strictly_increasing(strs))