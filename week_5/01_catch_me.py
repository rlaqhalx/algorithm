# 코니의 위치 변화
# 코니는 처음 위치에서 1초후 1만큼, 매초마다  이전 이동거리 + 1 만큼 움직인다
# 즉 증각하는 속도가 1초마다 1씩 증가한다
# 속도 1, 2, 3, 4, 5,6
# 위치 3, 4, 6, 9, 13, 18
# 시간에 따라 더해준다

# 브라운의 위치 변화는
# B - 1, B + 1, 2 * B
# 위치 2
# 1-1. 2-1 = 1
# 1-2. 2 + 1 = 3
# 2 * 2 = 4
# 1-1-1. 1 - 1 = 0
# 1-1-2. 1 + 1 =2
# 1-1-3. 1 * 2 = 2
# ... 무수한 갈래로 선택지가 나눠진다

# 모든 경우의 수를 다 나열해야된다 -> bfs

# 잡았다! 라는 의미는 똑같은 시간에 똑같은 위치에 존재해야한다.
# 시간은 + 1
# 위치 코니도 브라운도 값이 자유자재로 바뀝니다.

# 규칙적 : 배열, 자유자재 -> 딕셔너리

# 각 시간마다 브라운이 갈수 있는 위치를 저장하고 싶다. [{}]






from collections import deque

c = 11
b = 2


def catch_me(cony_loc, brown_loc):
    time = 0
    queue = deque()
    queue.append((brown_loc, 0)) # 위치와 시간을 담아준다.
    visited = [{} for _ in range(200001)] # [{}, {}, {},]
    # visited[0] = {
    #   2: True
    # }
    # visited[1] ={
    #   1: True
    #   3: True
    #   4: True
    # }
    # 그 시간에 갈수 있는 코니의 위치
    # visited[위치][시간]
    # visited[3] 에 5 라는 키가 있냐? = 3 위치에 5 초에 간적이 있냐?



    while cony_loc < 200000:
        cony_loc += time # 시간만큼 +1, _2, +3, +4

        if time in visited[cony_loc]:
            return time

        for i in range(0, len(queue)):
            current_position, current_time = queue.popleft()
            new_time = current_time + 1

# 모든 경우의 수를 구하기 위해 각각의 갈래길들을 만들어준다.
            new_position = current_position - 1
            if 0 <= new_position <= 200000:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))

            new_position = current_position + 1
            if 0 <= new_position <= 200000:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))

            new_position = current_position * 2
            if 0 <= new_position <= 200000:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))

        time += 1
    return -1


print(catch_me(c, b))  # 5가 나와야 합니다!