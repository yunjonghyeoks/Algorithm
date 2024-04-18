# 1 ~ 30까지 출석번호 있음
# 이때 고정으로 28명은 과제 제출했고 2명은 안함 <- 2명을 찾는거임


stdn = set([int(i) for i in range(1, 31)]) # 총 학생 번호
sub_stdn = set([int(input()) for _ in range(28)]) # 제출한 학생 번호
 
sub = stdn & sub_stdn # 교집합 구하기

stdn -= sub # 총 학생 번호에서 공통된 학생 번호 빼기

print(*stdn, sep="\n")

# 1 3 4 5 6 7 8 10

# 답 : 2 9

