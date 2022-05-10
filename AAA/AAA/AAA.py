import sys
sys.stdin=open("input.txt", "r")
def DFS(x):
    if x>0:        
        DFS(x-1)
        print(x, end=" ")


n=int(input())
DFS(n)