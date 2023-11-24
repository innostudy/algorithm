# 각 칸마다 색이 칠해진 2차원 격자 보드판이 있습니다. 그중 한 칸을 골랐을 때, 위, 아래, 왼쪽, 오른쪽 칸 중 같은 색깔로 칠해진 칸의 개수를 구하려고 합니다.

# 보드의 각 칸에 칠해진 색깔 이름이 담긴 이차원 문자열 리스트 board와 고른 칸의 위치를 나타내는 두 정수 h, w가 주어질 때 board[h][w]와 이웃한 칸들 중 같은 색으로 칠해져 있는 칸의 개수를 return 하도록 solution 함수를 완성해 주세요.

# 이웃한 칸들 중 몇 개의 칸이 같은 색으로 색칠되어 있는지 확인하는 과정은 다음과 같습니다.
def solution(board, h, w):
    answer = 0
    max_x = len(board[0])
    max_y = len(board)
    dx = [0,1,-1,0]
    dy = [1,0,0,-1]
    for i in range(4):
        if(0<=w+dx[i]<=(max_x-1) and 0<= h+dy[i] <= (max_y-1)):
            if(board[h][w] == board[h+dy[i]][w+dx[i]]):
                answer += 1
        
    return answer