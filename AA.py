import sys
sys.stdin=open("input.txt", "rt")

n=int(input())
py=[]
for i in range(n):
    h,w=map(int,input().split())
    py.append((h,w))
py.sort(reverse=True)
aw=0
cnt=0
for h,w in py:
    if w>aw:
        aw=w
        cnt+=1
print(cnt)