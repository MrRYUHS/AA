import sys
sys.stdin=open("input.txt", "rt")

num,m=map(int,input().split())
num=list(map(int,str(num)))
stack=[]
for x in num:
    while stack and m>0 and x>stack[-1]:
        stack.pop()
        m-=1
    stack.append(x)
if m!=0:
    stack=stack[:-m]
res=''.join(map(str, stack))
print(res)