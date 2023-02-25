# Q. 수평 직선에 탑 N대를 세웠습니다. 모든 탑의 꼭대기에는 신호를 송/수신하는 장치를 설치했습니다. 발사한 신호는 신호를 보낸 탑보다 높은 탑에서만 수신합니다. 또한 ,한 번 수신된 신호는 다른 탑으로 송신되지 않습니다.
#
# 예를 들어 높이가 6, 9, 5, 7, 4 인 다섯 탑이 왼쪽으로 동시에 레이저 신호를 발사합니다.
# 그러면, 탑은 다음과 같이 신호를 주고 받습니다.
#
# 높이가 4인 다섯 번째 탑에서 발사한 신호는 높이가 7인 네 번째 탑에서 수신하고,
# 높이가 7인 네 번째 탑의 신호는 높이가 9인 두 번째 탑이,
# 높이가 5인 세 번째 탑의 신호도 높이가 9인 두 번째 탑이 수신합니다.
#
# 높이가 9인 두 번째 탑과 높이가 6인 첫 번째 탑이 보낸 레이저 신호는
# 어떤 탑에서도 수신할 수 없습니다.
#
# 이 때, 맨 왼쪽부터 순서대로 탑의 높이를 담은 배열 heights가 매개변수로 주어질 때 각 탑이 쏜 신호를 어느 탑에서 받았는지 기록한 배열을 반환하시오.

# [6, 9, 5, 7, 4] # 라고 입력된다면,
#
# # 아래 그림처럼 탑이 있다고 보시면 됩니다!
# <- <- <- <- <- 레이저의 방향
#    I
#    I
#    I     I
# I  I     I
# I  I  I  I
# I  I  I  I  I
# I  I  I  I  I
# I  I  I  I  I
# I  I  I  I  I
#
# [0, 0, 2, 2, 4] # 다음과 같이 반환하시면 됩니다!

top_heights = [6, 9, 5, 7, 4]

# [0, 0, 2, 2, 4]
# [0, 0, 0, 0, 0]

# <- <- <- <- <-
# 6  9  5  7  4
# [0, 0, 0, 0, 4] # 5번째의 레이저를 4번째가 맞음

# <- <- <- <-
# 6  9  5  7
# [0, 0, 0, 2, 4] # 4번째의 레이저를 2번째가 맞음 (3번째 5 는 skip since 5 < 7)

# <- <- <-
# 6  9  5
# [0, 0, 2, 2, 4] # 5번째의 레이저를 2번째 (9) 가 또 맞음

# <- <-
# 6  9
# [0, 0, 2, 2, 4] # 6 < 9 그래서 맞지않음 0

# <-
# 6
# [0, 0, 2, 2, 4] # 마지막은 왼쪽에 더이상 없기에 no update

# 맨 뒤 variable 이 없어진다 -> STACK!

# for idx in range (5 - 1, 0, -1)
# start, end, how to count from start to end (4, 3, 2, 1)

# O(N)
def get_receiver_top_orders(heights):
    answer = [0] * len(heights) #[0, 0, 0, 0, 0]
    while heights: #O(N)
        height = heights.pop()
        # [6, 9, 5, 7]  popped {4}
        # here len(heights) is after popped so 4 so referring to idx 3
        for idx in range(len(heights) - 1, 0, -1): #O(N)
            # print(idx) 3, 2, 1
            if heights[idx] > height:
                # heights[3]: 7 > height:4
                answer[len(heights)] = idx + 1
                # answer[len(heights)] => len(heights) after pop is 4 so popped item's index
                # idx + 1 is 'blocking (tall)'s order (order = index + 1)
                break
    return answer


print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!