def areIsomorphic(s,p):
    dict1={}
    dict2={}
    for i,value in enumerate(s):
        dict1[value]=dict1.get(value,[])+[i]
    for j,value in enumerate(p):
        dict2[value]=dict2.get(value,[])+[j]
    if sorted(dict1.values())==sorted(dict2.values()):
        return True
    else:
        return False


t=int(input())
for i in range (t):
    s=str(input())
    p=str(input())
    if(areIsomorphic(s, p)):
        print(1)
    else:
        print(0)