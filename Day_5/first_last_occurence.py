def binarySearch(arr,target,flag):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start+end)//2
        if (arr[mid] == target and flag) or arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return start if flag else end
    
for _ in range(int(input())):
    n,target = map(int,input().split())
    arr = list(map(int,input().split()))
    leftIndex = binarySearch(arr,target,1)
    if leftIndex == len(arr) or arr[leftIndex] != target:
        print(-1)
    else:
        print(leftIndex,binarySearch(arr,target,0))