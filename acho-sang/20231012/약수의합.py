# 약수의 합
# 문제 설명
# 정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.

# 제한 사항
# n은 0 이상 3000이하인 정수입니다.
def solution(n):
    if (n==1):
        return 1
    if (n==0):
        return 0
    answer = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            answer.append(i)
            if n // i != i:
                answer.append(n // i)
    answer.append(n)
    return sum(answer)+1