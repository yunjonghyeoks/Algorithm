def solution(s):

    return s.lower().count("p") == s.lower().count("y")

word = input()
result = solution(word)
print(result)

