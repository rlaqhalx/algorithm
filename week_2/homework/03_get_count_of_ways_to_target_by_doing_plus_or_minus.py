numbers = [2, 3, 1]
target_number = 0
# result = [] # 모든 경우의 수를 담기 위한 배열
result_count = 0  # target 을 달성할 수 있는 모든 방법의 수를 담기 위한 변수


def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index, current_sum):
    if current_index == len(array): # 탈출조건
        # all_ways.append(current_sum) # 마지막 index 에 다다랐을 때 합계를 추가해준다
        if current_sum == target:
            global result_count
            result_count += 1 # 마지막 다다랐을 때 합계를 추가해준다
        return
    get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index + 1, current_sum + array[current_index])
    get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index + 1, current_sum - array[current_index])

# get_all_ways_to_by_doing_plus_or_minus(numbers, 0, 0, result)
# print (result)

get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number, 0 ,0)
# current_index 와 current_sum 에 0, 0을 넣은 이유는 시작하는 총액이 0, 시작 인덱스도 0이니까 그렇습니다!
print (result_count)

# Call by Object Reference
# if you pass array as parameter to function, you can add element to that array
# Yet, if you pass int, str type of variable as parameter to function, the value gets copied and creates new value
# Thus, if you pass result_count as parameter, only value in (all_ways_count) function gets changed, not result_count, which is outside of fucntion scope
# To use outside of function variable, use 'GLOBAL'
# 'GLOBAL' to use variable that is defined outside of variable