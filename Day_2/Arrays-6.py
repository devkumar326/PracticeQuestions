from sys import maxsize
def kadaneAlgo(a,size):
    max_so_far=-maxsize-1
    max_ending_here=0
    for i in range (0,size):
        max_ending_here +=a[i]
        if (max_so_far<max_ending_here):
            max_so_far=max_ending_here
        if (max_ending_here<0):
            max_ending_here=0
    return max_so_far

T=int(input())
while(T>0):
    n=int(input())
    arr=[int(i) for i in input().split()]
    print(kadaneAlgo(arr, n))
    T-=1