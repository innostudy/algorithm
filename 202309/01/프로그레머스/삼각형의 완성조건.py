def solution(sides):
    maxNum = -1;
    totalNum = 0;
    for i in sides:
        maxNum = max(i,maxNum);
        totalNum = totalNum + i;
    
    totalNum = totalNum - maxNum;
    if(totalNum <= maxNum):
        return 2;
    else:
        return 1;
    