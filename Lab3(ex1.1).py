s=input("Введите сжатую строку: ")
result=""
i=0
while i<len(s):
    char=s[i]
    i+=1
    count=""
    while i < len(s) and s[i].isdigit():
        count+=s[i]
        i+=1
    if count=="":
        result+=char
    else:
        result+=char*int(count)
print("Восстановленная строка:", result)
