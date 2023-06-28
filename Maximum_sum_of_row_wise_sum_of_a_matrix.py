n,m=map(int,input().split())
mat=[]
max=0
for i in range(n):
    a=list(map(int,input().split()))
    mat.append(a)
for i in range(n):
    s=0
    for j in range(m):
        s+=mat[i][j]
    if max<s:
        max=s
print(max)
        
    