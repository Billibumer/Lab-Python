with open('input.txt','r') as f:
    numbers=[int(line) for line in f.readlines()]
numbers.sort()
with open('output.txt','w') as f:
    for n in numbers:
        f.write(str(n)+'\n')

