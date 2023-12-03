# 자연수 n이 주어졌을 때, n의 다음 큰 숫자는 다음과 같이 정의 합니다.

# 조건 1. n의 다음 큰 숫자는 n보다 큰 자연수 입니다.
# 조건 2. n의 다음 큰 숫자와 n은 2진수로 변환했을 때 1의 갯수가 같습니다.
# 조건 3. n의 다음 큰 숫자는 조건 1, 2를 만족하는 수 중 가장 작은 수 입니다.
# 예를 들어서 78(1001110)의 다음 큰 숫자는 83(1010011)입니다.

# 자연수 n이 매개변수로 주어질 때, n의 다음 큰 숫자를 return 하는 solution 함수를 완성해주세요.
def solution(n):
    before = format(n, 'b')
    before_one_cnt = before.count('1')
    
    last_one = before[::-1].index("1")
    n = n + 2**int(last_one)

    after = format(n ,'b')
    after_one_cnt = after.count('1')


    for i in range(before_one_cnt - after_one_cnt):        
        n += 2**i

    return n