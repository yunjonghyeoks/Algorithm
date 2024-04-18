import math


factorial = int(input())
arr = []
for i in range (1, factorial + 1):
    arr.append(i)
    

    print(math.prod(arr))
# 만약 10!면
# 1x2x3x4x5x6x7x8x9x10을 해야함