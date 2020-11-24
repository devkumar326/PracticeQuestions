def go(i,temp):
    if(i==len(arr)):
        if(temp[-1]==' '):
            ans_f.append(temp[:len(temp)-1])
            return 
        ans_f.append(temp)
        return
    go(i+1,temp+arr[i]+' ')
    go(i+1,temp+arr[i])
for _ in range(int(input())):
    arr=list(input())
    ans_f=list()
    ch=dict()
    go(0,'')
    for i in ans_f:
        if(i not in ch):
            print('('+i+')',end='')
            ch[i]=1
    print()