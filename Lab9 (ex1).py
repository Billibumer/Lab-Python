with open('matrix.txt','r') as f:
    lines=f.readlines()

matrix=[list(map(int,line.strip().split(','))) for line in lines]

elements=[elem for row in matrix for elem in row]

s=sum(elements)
max_elem=max(elements)
min_elem=min(elements)

print('Сумма:',s)
print('Максимум:',max_elem)
print('Минимум:',min_elem)
