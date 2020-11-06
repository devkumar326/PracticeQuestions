tc = int(input())
for i in range(tc):
    s = input()
    li=[]
    curl = 0
    comm = 0
    squa = 0
    for j in range(len(s)):
        if(s[j]=="{"):
            curl+=1
            li.append("{")
        elif(s[j]=="["):
            squa+=1
            li.append("[")
        elif(s[j]=="("):
            comm+=1
            li.append("(")
        elif(s[j]=="}"):
            curl-=1
            if(len(li)!=0 and li[-1]=="{"):
                li.pop()
        elif(s[j]=="]"):
            squa-=1
            if(len(li)!=0 and li[-1]=="["):
                li.pop()
        elif(s[j]==")"):
            comm-=1
            if(len(li)!=0 and li[-1]=="("):
                li.pop()
    if((curl==0 and squa==0 and comm==0 and len(li)==0)):
        print("balanced")
    else:
        print("not balanced")