'''
class Pair(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
'''
def maxchain(parr,n,dp):
    if n==-1:
        return 0
    if dp[n]!=-1:
        return dp[n]
    ret=1
    for i in range(n):
        if parr[i].b<parr[n].a:
            temp=1+maxchain(parr,i,dp)
            ret=max(ret,temp)
    dp[n]=ret 
    return dp[n]
    
def maxChainLen(Parr, n):
    ans=0
    dp=[-1]*(n)
    for i in range(n):
        for j in range(n):
            if Parr[i].a<Parr[j].a:
                temp=Parr[i]
                Parr[i]=Parr[j]
                Parr[j]=temp
    for i in range(n):
        ans=max(ans,maxchain(Parr,i,dp))
    return ans

class Pair(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

if __name__ =='__main__':
    tcs = int(input())

    for _ in range(tcs):
        n=int(input())

        arr=[int(x) for x in input().split()]

        Parr=[]

        i=0
        while n*2>i:

            Parr.append(Pair(arr[i],arr[i+1]))

            i+=2

        #print(Parr,len(Parr))

        print(maxChainLen(Parr, n))
