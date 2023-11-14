# 네오와 프로도가 숫자놀이를 하고 있습니다. 네오가 프로도에게 숫자를 건넬 때 일부 자릿수를 영단어로 바꾼 카드를 건네주면 프로도는 원래 숫자를 찾는 게임입니다.

# 다음은 숫자의 일부 자릿수를 영단어로 바꾸는 예시입니다.

# 1478 → "one4seveneight"
# 234567 → "23four5six7"
# 10203 → "1zerotwozero3"
# 이렇게 숫자의 일부 자릿수가 영단어로 바뀌어졌거나, 혹은 바뀌지 않고 그대로인 문자열 s가 매개변수로 주어집니다. s가 의미하는 원래 숫자를 return 하도록 solution 함수를 완성해주세요.

def solution(s):
    answer = ''
    tempString = ''
    checklist = ['zero',
         'one',
         'two',
         'three',
         'four',
         'five',
         'six',
         'seven',
         'eight',
         'nine']
    num_dict = {'zero' : '0',
         'one' : '1',
         'two' : '2',
         'three' : '3',
         'four' : '4',
         'five':'5',
         'six':'6',
         'seven':'7',
         'eight':'8',
         'nine':'9'}
    
    for i in s:
        if(i.isdigit()):
            answer += i
        else:
            tempString += i
            if(tempString in checklist):
                answer += num_dict[tempString]
                tempString = ''
    return int(answer)

def solution2(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)