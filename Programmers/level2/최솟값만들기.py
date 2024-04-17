def solution(A, B):
    answer = 0
    A.sort()
    B.sort(reverse = True)

    for i in range(len(A)):
        answer += A[i] * B[i]

    return answer

A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = solution(A, B)
print(result)
# A.sort()
# B.sort()

#제일 작은 수를 만들기 위해서는
#무조건 제일 큰수랑 제일 작은수랑 곱해야한다
