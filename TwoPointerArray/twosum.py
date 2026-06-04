def solution(number,target):
    left,right,=0,len(number)-1
    while(left<right):
        if (number[left]+number[right]==target):
            return left+1,right+1
        elif number[left]+1,[right]+1
        