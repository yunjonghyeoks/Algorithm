def solution(n):
    answer = ''
    for i in range(n):
        if i % 2 == 0:
            answer += "수"
        else:
            answer += "박"


    return answer

num = int(input())

result = solution(num)
print(result)