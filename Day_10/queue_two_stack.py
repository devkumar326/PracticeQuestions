def Push(x,stack1,stack2):
    '''
    x: value to push
    stack1: list
    stack2: list
    '''
    stack1.append(x)
    stack2.insert(0, x)
    

def Pop(stack1,stack2):
    
    '''
    stack1: list
    stack2: list
    '''
    if not stack2:
        return -1
    popped = stack2.pop()
    stack1.pop(0)
    return popped

if __name__=='__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        qry=int(input())
        qtyp_qry=list(map(int, input().strip().split()))
        
        i=0
        stack1=[]
        stack2=[]
        while i <len(qtyp_qry):
            #print(i)
            if qtyp_qry[i]==1:
                Push(qtyp_qry[i+1],stack1,stack2)
                #print(i)
                i+=2
            else:
                print(Pop(stack1,stack2),end=' ')
                i+=1
                
        print()