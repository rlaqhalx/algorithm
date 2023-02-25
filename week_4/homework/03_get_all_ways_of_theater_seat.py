# vip 석은 고정
# 나머지는 한칸식 왼쪽 또는 오른쪽 이동 가능

# 4번 좌석과 7번 좌석이 VIP석인 경우에 <123456789>는 물론 가능한 배치이다.
# 또한 <213465789> 와 <132465798> 도 가능한 배치이다.
# 그러나 <312456789> 와 <123546789> 는 허용되지 않는 배치 방법이다.

# 오늘 공연은 입장권이 매진되어 1번 좌석부터 N번 좌석까지 모든 좌석이 다 팔렸다.
# 총 좌석의 개수와 VIP 회원들의 좌석 번호들이 주어졌을 때,
# 사람들이 좌석에 앉는 서로 다른 방법의 가짓수를 반환하시오.

# Solution
# 4, 7 은 고정 자리이므로,
# 123과 56과 89를 마음껏 변경할 수 있습니다
# 이 문제의 핵심은 변경 가능한 좌석들의 규칙을 발견하는 것입니다.

# 좌석 [1, 2] 를 옮겨본다고 해보겠습니다.
# 가능한 경우는 [1, 2] [2, 1] 총 2개 입니다.
#
# 좌석 [1, 2, 3] 를 옮겨본다고 해보겠습니다.
# 가능한 경우는 [1, 2, 3] [2, 1, 3] [1, 3, 2] 총 3개 입니다.
#
# 좌석 [1, 2, 3, 4] 를 옮겨본다고 해보겠습니다.
# 가능한 경우는 [1, 2, 3, 4] [1, 2, 4, 3] [1, 3, 2, 4] [2, 1, 3, 4] [2, 1, 4, 3] 총 5개 입니다.
# 좌석 [1, 2, 3, 4, 5] 를 옮겨본다고 해보겠습니다.
# 가능한 경우는 총 8개 입니다!

# [1, 2, 3, 4, 5] [1, 2, 3, 5, 4] [2, 1, 3, 4, 5] [2, 1, 3, 5, 4]
# [1, 2, 4, 3, 5] [2, 1, 4, 3, 5] [2, 1, 3, 4, 5] [1, 3, 2, 4, 5]

# 2, 3, 5, 8 -> fibonacci

# 원래 fibonacci 에서는 f(1) = 1, f(2) = 1 f(3) = 2 였는데 여기서는 f(1) = 1, f(2) = 2, f(3) = 3 (2개의 좌석을 옮기는 방법이 2개이므로)



seat_count = 9
vip_seat_array = [4, 7]

memo = {
    1: 1,
    2: 2
}

def fibo_dynamic_programming(n, fibo_memo):
    if n in fibo_memo:
        return fibo_memo[n]
    # recursion!
    nth_fibo = fibo_dynamic_programming(n - 1, fibo_memo) + fibo_dynamic_programming(n - 2, fibo_memo)
    fibo_memo[n] = nth_fibo
    return nth_fibo

def get_all_ways_of_theater_seat(total_count, fixed_seat_array):
    all_ways = 1
    current_index = 0
    for fixed_seat in fixed_seat_array:
        fixed_seat_index = fixed_seat - 1  # 3, 6
        # 3 - 0, memo -> memo[3] : 3
        # 6 - (3 + 1), memo -> memo[2]: 2
        count_of_ways = fibo_dynamic_programming(fixed_seat_index - current_index, memo)
        # need to multiply for union (prob)
        # 이제 이 자리들로 만들 수 있는 모든 경우의 수를 구하는 것이기 때문에
        # 곱의 법칙에 의해 모든 수를 곱하겠습니다.
        all_ways *= count_of_ways
        current_index = fixed_seat_index + 1

    # 9 - (6 + 1), memo -> memo[2]: 2
    count_of_ways = fibo_dynamic_programming(total_count - current_index, memo)
    all_ways *= count_of_ways
    return all_ways


# 12가 출력되어야 합니다! => 3 * 2 * 2
print(get_all_ways_of_theater_seat(seat_count, vip_seat_array))
print("정답 = 4 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(9,[2,4,7]))
print("정답 = 26 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(11,[2,5]))
print("정답 = 6 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(10,[2,6,9]))

# 그런데, 왜 피보나치 수열로 나올까요?
#
# 다음과 같이 생각해볼 수 있습니다.
# i번째 좌석에 있는 사람이 앉는 방법은 두 가지가 있습니다.
# i번째 좌석에 그대로 앉던지, i - 1 번째 좌석에 앉는 방법입니다.
#
# 1. i번째 좌석에 i번 티켓을 가진 사람이 그대로 앉게 된다면
# 나머지 i-1개만 배치하면 되기 때문에 i-1 개를 배치하는 방법의 개수가 됩니다.
#
#                          [결정됨]
# 0       ....     i-1       i
#
# 2. i번째 좌석에 i-1번 티켓을 가진 사람이 앉게 된다면
# i - 1번째 사람은 i 번째에 반드시 앉아야 합니다.
# 왜냐면 i 번째 좌석이 비는데, i - 1번째 사람이 앉지 않으면 어느 누구도 앉지 못하기 때문에
# i - 1 번 티켓 사람은 반드시 i 번째에 앉게 됩니다.
#
# 즉, 나머지 i-2 개만 배치하면 되기 때문에 i - 2 개를 배치하는 방법의 개수가 됩니다.
#
#                      [결정됨] [결정됨]
# 0       .... i-2      i-1            i
#
# 이걸 수식으로 표현하면,
# F(N) 을 N명의 사람들을 좌석에 배치하는 방법
# F(N) = F(N - 1) + F(N - 2) 라고 표시할 수 있기 때문에 피보나치 수열이 됩니다!
#
# 자 그러면, 이제 변경 가능한 좌석들의 개수에 따라 변경할 수 있는 수를 구했습니다!
#
# 그러면 아래 예시에서, 각 구역당 좌석을 배치할 수 있는 방법은 다음과 같습니다.
# 123 4 56 7 89
#
# 123 → 3자리 이므로 F(3) = 3
# 56 → 2자리 이므로 F(2) = 2
# 89 → 2자리 이므로 F(2) = 2
#
# 이제 이 자리들로 만들 수 있는 모든 경우의 수를 구하는 것이기 때문에
# 곱의 법칙에 의해 모든 수를 곱하겠습니다.
#
# 그러면 총 3 * 2 * 2 = 12가지의 경우가 나오게 됩니다!
