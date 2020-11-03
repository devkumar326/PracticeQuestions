import math
def circularSubarraySum(a, n):
    if (n == 1):
        return a[0]

    sum = 0
    for i in range (n):
        sum += a[i]

    curr_max = a[0]
    max_so_far = a[0]
    curr_min = a[0]
    min_so_far = a[0]

    for i in range (1,n):
        curr_max = max(curr_max + a[i], a[i])
        max_so_far = max(max_so_far, curr_max)

        curr_min = min(curr_min + a[i], a[i])
        min_so_far = min(min_so_far, curr_min)

    if (min_so_far == sum):
        return max_so_far

    return max(max_so_far, sum - min_so_far)

T=int(input())
while(T>0):
    n=int(input())
    arr=[int(i) for i in input().split()]
    print(circularSubarraySum(arr,n))
    T-=1