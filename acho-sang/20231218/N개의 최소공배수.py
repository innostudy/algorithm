# 두 수의 최소공배수(Least Common Multiple)란 입력된 두 수의 배수 중 공통이 되는 가장 작은 숫자를 의미합니다. 예를 들어 2와 7의 최소공배수는 14가 됩니다. 정의를 확장해서, n개의 수의 최소공배수는 n 개의 수들의 배수 중 공통이 되는 가장 작은 숫자가 됩니다. n개의 숫자를 담은 배열 arr이 입력되었을 때 이 수들의 최소공배수를 반환하는 함수, solution을 완성해 주세요.


from collections import defaultdict,Counter

def solution(arr):
    answer = 1
    div_list = defaultdict(list)
    arr = set(arr)
    for i in arr:
        num = i
        while i > 1:
            for j in range(2,i+1):
                if(i % j == 0):
                    div_list[num].append(j)
                    i = i // j
                    break;     
    cnt = Counter([1])
    for i in div_list:
        cnt = Counter(div_list[i]) | cnt
    
    cnt_merge = list(cnt.elements())
    
    for i in cnt_merge:
        answer = answer * i
    return answer