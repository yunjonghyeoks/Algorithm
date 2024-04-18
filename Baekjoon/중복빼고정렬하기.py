import sys

n = int(sys.stdin.readline())

a = list(map(int, sys.stdin.readline().split()))

a.sort()

print(*list(set(a)))

    