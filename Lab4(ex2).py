a=list(map(int,input("Первый список: ").split()))
b=list(map(int,input("Второй список: ").split()))
c=set(a)&set(b)
print("Кол-во общих чисел:",len(c))
