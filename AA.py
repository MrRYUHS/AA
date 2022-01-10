import sys
sys.stdin=open("input.txt", "rt")

n=int(input())
a=list(map(int,input().split()))
av=round(sum(a)/n)
min=2147000000
for idx, x in enumerate(a):
    tmp=abs(x-av)
    if tmp<min:
        min=tmp
        score=x
        r=idx
    elif tmp==min:
        if x>score:
            r=idx+1
print(av, r)