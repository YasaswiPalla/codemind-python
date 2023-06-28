n,m=map(int,input().split())
mat=[]
for i in range(n):
    a=list(map(int,input().split()))
    mat.append(a)
for j in range(m):
    s=0
    for i in range(n):
        s+=mat[i][j]
    print(s, end=" ")