s=input("Введите строку: ")
r= ""
i=0
while i<len(s):
    count = 1  
    while i+1< len(s) and s[i]==s[i+1]:
        count+=1
        i+=1
    r+=s[i]
    if count > 1:
        r+=str(count)
    i+=1
print("Сжатая строка:", r)
