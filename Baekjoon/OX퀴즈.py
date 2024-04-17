loop_num = int(input())

point = 0
c = 1

for i in range(loop_num):
    ox = list(input())
    for j in ox:
        if j == "O":
            point += c
            c += 1
        else:
            c = 1
print(point)
        