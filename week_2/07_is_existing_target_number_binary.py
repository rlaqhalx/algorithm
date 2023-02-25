finding_target = 2
finding_numbers = [0, 3, 5, 6, 1, 2, 4]

def is_exist_target_number_binary(target, numbers, min, max):
    # 이 부분을 채워보세요!
    numbers.sort()
    current_mid = 0
    # check base case
    if min <= max:
        current_mid = (max + min) // 2
        if numbers[current_mid] == target:
            return True
        # if target is smaller than mid
        elif numbers[current_mid] > target:
            return is_exist_target_number_binary(target, numbers, min, current_mid -1)
        # if target is bigger than mid
        else:
            return is_exist_target_number_binary(target, numbers, current_mid + 1, max)

    else:
        return False


# result = is_exist_target_number_binary(finding_target, finding_numbers)
result = is_exist_target_number_binary(finding_target, finding_numbers, 0, 6)

print(result)