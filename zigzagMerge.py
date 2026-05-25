def zigzag_merge(a,b):
    c=[0]*(len(a)+len(b))
    i, j, k=0,0,0
    while i<len(a) and j<len(b):
        c[k]=a[i]
        k+=1
        i+=1
        c[k]=b[j]
        k+=1
        j+=1
    while(i<len(a)):
        c[k]=a[i]
        k+=1
        i+=1
    while(j<len(b )):
        c[k]=b[j]
        k+=1
        j+=1
    return c
a=[10,20,30]
b=[6,5,4,3,2,1]
c=zigzag_merge(a,b)
print(c)