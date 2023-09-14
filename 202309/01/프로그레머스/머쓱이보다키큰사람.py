# 머쓱이는 학교에서 키 순으로 줄을 설 때 몇 번째로 서야 하는지 궁금해졌습니다. 
# 머쓱이네 반 친구들의 키가 담긴 정수 배열 array와 머쓱이의 키 height가 
# 매개변수로 주어질 때, 머쓱이보다 키 큰 사람 수를 return 하도록 solution
# 함수를 완성해보세요.

def solution(array, height):
    sortedArray = sorted(array);
    lenth = len(array)
    i = 0;
    while height >= sortedArray[i]:
        i=i+1;
        if i == lenth:
            break;
    answer = lenth - i;
    return answer

# with search
def solution2(array, height):
    sortedArray = sorted(array);
    length = len(sortedArray);
    left, right = 0, length - 1
    result = length  # 초기값 설정

    while left <= right:
        mid = (left + right) // 2  # 중간 인덱스 계산
        if sortedArray[mid] > height:
            result = mid  # 현재 인덱스를 저장하고
            right = mid - 1  # 왼쪽 반을 탐색
        else:
            left = mid + 1  # 오른쪽 반을 탐색
    return length - result;