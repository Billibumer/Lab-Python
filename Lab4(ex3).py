a=input().split()
d={}
res=[]
for s in a:
    if s in d:
        d[s]+=1
    else:
        d[s]=1
    res.append(d[s])
print(*res)
