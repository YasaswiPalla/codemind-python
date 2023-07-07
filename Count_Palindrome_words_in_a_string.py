s=input()
r=s.lower()
p=r.split()
count=0
for i in p:
    o=i[::-1]
    if o==i:
        count+=1
print(count)
