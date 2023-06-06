def fib_series(num):
    a=0
    b=1
    c=a+b
    for x in range(num):
        if x <= 1:
            print(x, end=" ")
        else:
            c = a + b
            a, b = b, c
            print(c, end=" ")
fib_series(10000)
