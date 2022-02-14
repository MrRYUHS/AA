import sys
sys.stdin=open("input.txt", "rt")

n=int(input())
mt=[]
for i in range(n):
    s,e=map(int,input().split())
    mt.append((s,e))
mt.sort(key=lambda i:(i[1], i[0]))
et=0
cnt=0
for s,e in mt:
    if s>=et:
        et=e
        cnt+=1
print(cnt)