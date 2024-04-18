cnt = 1
def fibonacci(n, a, b):
    if n == 0:
        return 0
    global cnt
    c = a + b
    
    cnt += 1
    if cnt < n:
        return fibonacci(n, b, c)
    else:
        print(c)

n = int(input())

default_value_0 = 0
default_value_1 = 1
fibonacci(n, default_value_0, default_value_1)