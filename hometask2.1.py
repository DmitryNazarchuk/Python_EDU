a=int(input("Введите сторану а:"))
b=int(input("Введите сторану b:"))
k = 1
while a != b:
    if a > b:
        a -= b
        #print(n)
        print("длины ребер ",b)
        print("---")
    else:
        b -= a
        #print(n)
        print("длины ребер ",a)
        print("---")
    k += 1
print('МОЖНО РАЗДЕЛИТЬ ПРЯМОУГОЛЬНИК НА', k,'КВАДРАТОВ')