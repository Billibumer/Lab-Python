a=list(map(int,input().split()))
imin=amax=0
for i in range(1,len(a)):
    if a[i]<a[imin]:imin=i
    if a[i]>a[amax]:amax=i
a[imin],a[amax]=a[amax],a[imin]
print(a)
