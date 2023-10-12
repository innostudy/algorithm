# 지뢰가 있는 지역과 지뢰에 인접한 위, 아래, 좌, 우 대각선 칸을 모두 위험지역으로 분류합니다.
# 지뢰는 2차원 배열 board에 1로 표시되어 있고 board에는 지뢰가 매설 된 지역 1과, 지뢰가 없는 지역 0만 존재합니다.
# 지뢰가 매설된 지역의 지도 board가 매개변수로 주어질 때, 안전한 지역의 칸 수를 return하도록 solution 함수를 완성해주세요.
import collections

def solution(board):
    col = len(board);
    row = len(board[0]);
    def change(x,y):
        if(x < 0 or y < 0 or x >= row or y >= col):
            return;
        if(board[x][y] == 0):
            board[x][y] = 2
            return;
    xList = [-1,0,1,-1,1,-1,0,1]
    yList = [-1,-1,-1,0,0,1,1,1]
    for i in range(col):
        for j in range(row):
            if(board[i][j] == 1):
                for k in range(8):
                    change(i+xList[k],j+yList[k])
                

    # print(board)
    answer = 0
    for i in range(col):
        for j in range(row):
            if(board[i][j] == 0):
                answer = answer + 1
    return answer