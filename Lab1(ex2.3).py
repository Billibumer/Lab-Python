n = int(input("Введите число n: "))
a = len(str(n))

# Задание 2.1 с выравниванием
for i in range(n, 0, -1):
    line = "".join(f"{j:>{a}}" for j in range(1, i + 1))
    print(line)

print()  

# Задание 2.2 с выравниванием
for i in range(n, 0, -1):
    spaces = " " * a * (n - i)
    left = "".join(f"{j:>{a}}" for j in range(i, 0, -1))
    right = "".join(f"{j:>{a}}" for j in range(2, i + 1))
    print(spaces + left + right)
