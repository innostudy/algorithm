# 수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

# 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
# 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
# 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

# 1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.
def solution2(answers):
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    count = {'1' : 0,'2' : 0,'3':0}
    for i in range(len(answers)):
        if(answers[i] == first[i%5]):
            count['1'] += 1
        if(answers[i] == second[i%8]):
            count['2'] += 1
        if(answers[i] == third[i%10]):
            count['3'] += 1
    max_count = max(count.values())
    
    answer = []
    for k,v in count.items():
        if(max_count == v):
            answer.append(int(k))
            
    
    return answer

def solution(answers):
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    st = 0
    en = 0
    rd = 0
    for i in range(len(answers)):
        if(answers[i] == first[i%5]):
            st += 1
        if(answers[i] == second[i%8]):
            en += 1
        if(answers[i] == third[i%10]):
            rd += 1
    max_count = max(st,en,rd)
    
    answer = []
    if(max_count == st):
        answer.append(1)
    if(max_count == en):
        answer.append(2)
    if(max_count == rd):
        answer.append(3)
    
    return answer