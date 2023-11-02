# 두 정수 left와 right가 매개변수로 주어집니다. left부터 right까지의 모든 수들 중에서, 약수의 개수가 짝수인 수는 더하고, 약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성해주세요.


def solution(left, right):
    def divSol(num):
        divList = []
        for i in range(1,int(num**0.5)+1):
            if (num % i == 0):
                divList.append(i)
                if (num // i) != i:
                    divList.append(num//i)
                
        return len(divList)
    
    answer = 0
    for i in range(left,right+1):
        if divSol(i) % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer