import atexit
import io
import sys

def fractionalknapsack(W,Items,n):
    '''
    :param W: max weight which can be stored
    :param Items: List contianing Item class objects as defined in driver code, with value and weight
    :param n: size of Items
    :return: Float value of max possible value, two decimal place accuracy is expected by driver code
    
    {
        class Item:
        def __init__(self,val,w):
            self.value = val
            self.weight = w
    }
    '''
    pR = [0]*n
    
    for i in range(n):
        pR[i] = (Items[i].value/Items[i].weight)
    for i in range(n):
        for j in range(n-1-i):
            if pR[j] < pR[j+1]:
                Items[j], Items[j+1] = Items[j+1], Items[j]
                pR[j], pR[j+1] = pR[j+1], pR[j]
    k = 0
    s = 0
    while k < n:
        if W > 0 and Items[k].weight <= W:
            s += Items[k].value
            W -= Items[k].weight
            k += 1
        else:
            break
    if W > 0 and k < n:
        s += pR[k]*W
        
    return s


class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,W = map(int,input().strip().split())
        info = list(map(int,input().strip().split()))
        Items = [Item(0,0) for i in range(n)]
        for i in range(n):
            Items[i].value = info[2*i]
            Items[i].weight = info[2*i+1]

        print("%.2f" %fractionalknapsack(W,Items,n))
