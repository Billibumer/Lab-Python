with open('input.txt','r',encoding='utf-8') as f:
    lines=[line.strip() for line in f if line.strip()]

data=[line.split() for line in lines]

ages=[int(d[2]) for d in data]
min_age=min(ages)
max_age=max(ages)

youngest=[d for d in data if int(d[2])==min_age]
oldest=[d for d in data if int(d[2])==max_age]

with open('youngest.txt','w',encoding='utf-8') as f:
    for d in youngest:
        f.write(' '.join(d)+'\n')

with open('oldest.txt','w',encoding='utf-8') as f:
    for d in oldest:
        f.write(' '.join(d)+'\n')
