def tour(lis, n):
    i = 0
    index = 0
    petrol = 0
    flag = 0
    pre = 0

    for i in range(n):
        petrol += lis[i][0] - lis[i][1]
        if(petrol < 0):
            index = i+1
            pre += petrol
            petrol = 0
    
    if(petrol + pre >= 0):
        return index
    else:
        return -1

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr=list(map(int, input().strip().split()))
        lis=[]
        for i in range(1, 2*n, 2):
            lis.append([ arr[i-1], arr[i] ])
        print(tour(lis, n))