s1=input().lower()
s2=input().lower()
p=s1.split()
o=s2.split()
count=0
for i in p:
    for j in o:
        if i==j:
            count+=1
print(count)