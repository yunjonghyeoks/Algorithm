num_of_sub = int(input())

sub_score = list(map(int, input().split()))    
max_value = max(sub_score)

result_list = [(x / max_value) * 100 for x in sub_score]

print(sum(result_list) / num_of_sub)
# 최댓값을 M
# 모든점수 score / M * 100 후 평균 구하기