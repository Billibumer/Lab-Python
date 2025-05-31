with open('input.txt','r') as f:
    numbers=list(map(int,f.read().split()))
prod=1
for n in numbers:
    prod*=n
with open('output.txt','w') as f:
    f.write(str(prod))
