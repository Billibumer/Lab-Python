s=input()
d={}
for c in s:
    if c!=" ":
        if c in d:
            d[c]+=1
        else:
            d[c]=1
items=sorted(d.items(),key=lambda x:-x[1])
for i in range(min(3,len(items))):
    print(f"{items[i][0]}: {items[i][1]}")
