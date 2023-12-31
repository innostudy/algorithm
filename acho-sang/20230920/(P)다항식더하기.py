# 한 개 이상의 항의 합으로 이루어진 식을 다항식이라고 합니다.
# 다항식을 계산할 때는 동류항끼리 계산해 정리합니다. 
# 덧셈으로 이루어진 다항식 polynomial이 매개변수로 주어질 때,
# 동류항끼리 더한 결괏값을 문자열로 return 하도록 solution 함수를 완성해보세요. 
# 같은 식이라면 가장 짧은 수식을 return 합니다.
def solution(polynomial):
    totailList = polynomial.split('+');
    if ('x' not in polynomial):
        return str(sum(map(int, totailList)))
    
    numCnt = 0;
    formulaCnt = 0;
    
    for i in totailList:
        math = i.strip();
        if('x' in math):
            if(len(math) ==1):
                formulaCnt = formulaCnt + 1;
            else:
                formulaCnt = formulaCnt + int(math[:-1]);
        else:
            numCnt = numCnt + int(math);
    answer = ''
    if(formulaCnt !=0):
        if(formulaCnt ==1):
            answer = 'x';
        else:
            answer = str(formulaCnt)+'x';
        
    if(numCnt !=0):
        answer = answer + ' + '+str(numCnt)
    
    return answer