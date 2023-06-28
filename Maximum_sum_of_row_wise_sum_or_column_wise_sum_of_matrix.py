n,m=map(int,input().split())
mat=[]
max1=0
max2=0
for i in range(n):
    a=list(map(int,input().split()))
    mat.append(a)
for i in range(n):
    s=0
    for j in range(m):
        s+=mat[i][j]
    if max1<s:
        max1=s
for j in range(m):
    k=0
    for i in range(n):
        k+=mat[i][j]
    if max2<k:
        max2=k
if max1>max2:
    print(max1)
else:
    print(max2)
    