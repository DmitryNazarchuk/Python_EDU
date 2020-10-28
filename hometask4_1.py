# generator version
def fibonachi(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

for x in fibonachi(35):
    print(x)