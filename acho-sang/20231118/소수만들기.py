# 주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다. 숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.
def solution(nums):
    answer = 0
    def check_prime(n):
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False

        return True
    length = len(nums)
    sum_list = []
    
    for i in range(length):
        for j in range(1,length-i):
            for k in range(1,length-i-j):
                sum_list.append(nums[i]+nums[i+j]+nums[i+j+k])


    set_num_list = set(sum_list)
    for m in sum_list:
        if(check_prime(m)):
            answer += 1
    return answer