# 소수점 아래 숫자가 계속되지 않고 유한개인 소수를 유한소수라고 합니다. 분수를 소수로 고칠 때 유한소수로 나타낼 수 있는 분수인지 판별하려고 합니다. 유한소수가 되기 위한 분수의 조건은 다음과 같습니다.

# 기약분수로 나타내었을 때, 분모의 소인수가 2와 5만 존재해야 합니다.
# 두 정수 a와 b가 매개변수로 주어질 때, a/b가 유한소수이면 1을, 무한소수라면 2를 return하도록 solution 함수를 완성해주세요.




def solution(a, b):
    div = [];
    answer = 1;
    for i in range(1,a+1):
        if(a%i==0 and b%i==0):
            div.append(i)
    if(len(div) == 1):
        c = b;
    else:
        c = b / div.pop()
    while c%2 == 0:
        c = c/2
    while c%5 ==0:
        c = c/5
    if(c != 1):
        answer = 2;
        
    return answer