n=int(input())
p=list(map(int,input().split()))
l=[]
for i in p:
    if i%2==0:
        l.append(i)
k=l[::-1]
for o in k:
    print(o)
    break