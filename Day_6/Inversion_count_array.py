#User function Template for python3

# arr[]: Input Array
# N : Size of the Array arr[]

def merge(arr, temp_arr, left, mid, right):
    i = left     # Starting index of left subarray
    j = mid + 1 # Starting index of right subarray
    k = left     # Starting index of to be sorted subarray
    inv_count = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            k += 1
            i += 1
        else:
            temp_arr[k] = arr[j]
            inv_count += (mid-i + 1)
            k += 1
            j += 1
    while i <= mid:
        temp_arr[k] = arr[i]
        k += 1
        i += 1
    while j <= right:
        temp_arr[k] = arr[j]
        k += 1
        j += 1
    for loop_var in range(left, right + 1):
        arr[loop_var] = temp_arr[loop_var]
        
    return inv_count
    
def mergeSort(arr,temp_arr, left, right):
    inv_count = 0

    if left < right:
        mid = (left + right)//2
        inv_count += mergeSort(arr, temp_arr, left, mid)
        inv_count += mergeSort(arr, temp_arr, mid + 1, right)
        inv_count += merge(arr, temp_arr, left, mid, right)
    return inv_count
    
    
def inversionCount(a,n):
    temp_arr=[0]*n
    return mergeSort(a, temp_arr, 0, n-1)

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=="__main__":
    t=int(input())
    for tt in range (t):
        n=list(input())
        a=list(map(int, input().strip().split()))
        print(inversionCount(a,n))