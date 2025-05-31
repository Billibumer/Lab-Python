def sierpinski(n):
    size = 2 ** n
    triangle = [[' ' for _ in range(2 * size)] for _ in range(size)]
    def fill(x, y, size):
        if size == 1:
            triangle[x][y] = '*'
        else:
            half = size // 2
            fill(x, y, half)                     
            fill(x + half, y - half, half)       
            fill(x + half, y + half, half)       
    fill(0, size - 1, size)

    for row in triangle:
        print(''.join(row))
sierpinski(3)
