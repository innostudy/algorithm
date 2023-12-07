def solution(n, words):
    stack = [words[0]]
    answer = [0,0]
    before = words[0][-1]
    for i in range(1,len(words)):
        if(before == words[i][0] and words[i] not in stack):
            stack.append(words[i])
            before = words[i][-1]
        else:
            answer =  [(i%n)+1, (i//n)+1]
            break
            
    



    return answer