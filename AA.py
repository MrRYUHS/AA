import sys
sys.stdin=open("input.txt", "rt")
def Count(capa):
    cnt=1
    sum=0
    for i in Music:
        if sum+i>capa:
            cnt+=1
            sum=i
        else:
            sum+=i
    return cnt

n, m=map(int,input().split())
Music=list(map(int,input().split()))
lt=1
rt=sum(Music)
res=0
while lt<=rt:
    mid=(lt+rt)//2
    if Count(mid)<=m:
        res=mid
        rt=mid-1
    else:
        lt=mid+1
print(res)