import sys
sys.stdin=open("input.txt", "rt")

n, k=map(int,input().split())
a=list(map(int, input().split()))
res=set() #중복을 제거한다
for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            res.add(a[i]+a[j]+a[m])
res=list(res)
res.sort(reverse=True)
print(res[k-1])