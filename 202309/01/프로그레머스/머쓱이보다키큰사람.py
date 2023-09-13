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