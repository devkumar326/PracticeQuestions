import itertools as it
t=int(input())
for x in range(t):
    k=str(input())
    k="".join(sorted(k))
    l=list(it.permutations(k))
    for i in l:
        print(''.join(i), end=" ")
    print()