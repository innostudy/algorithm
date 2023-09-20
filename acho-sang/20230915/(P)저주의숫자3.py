# 3x 마을 사람들은 3을 저주의 숫자라고 생각하기 때문에 
# 3의 배수와 숫자 3을 사용하지 않습니다. 3x 마을 사람들의 숫자는 다음과 같습니다.

def solution(n):
    if( n % 10 >=3):
        answer = n + n//3 + n//10;
    else:
        answer = n + n//3;
        
    i = 1;
    answer = 1;
    while i <= n:
        if(('3' not in str(answer)) and ((answer % 3) != 0)):
            i = i +1;
        
        answer = answer +1;
    return answer - 1