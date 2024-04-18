num = int(input())

test = [int(x) for x in str(num)]

test.sort(reverse=True)
print(*test, sep="")