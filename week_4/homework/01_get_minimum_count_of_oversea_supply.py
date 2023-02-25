import heapq

ramen_stock = 4
supply_dates = [4, 10, 15]
supply_supplies = [20, 5, 10]
supply_recover_k = 30
# 다음과 같이 입력값이 들어온다면,
# 현재 재고가 4개 있습니다. 그리고 정상적으로 돌아오는 날은 30일까지입니다.
# 즉, 26개의 공급량을 사와야 합니다!
# 그러면 제일 최소한으로 26개를 가져오려면? supplies 에서 20, 10 을 가져오면 되겠죠?
# 그래서 이 경우의 최소 공급 횟수는 2 입니다!

# 원할때 언제든지 최소값과 최댓값을 뽑을수 있게 만든 자료구조: HEAP
# 하지만 항상 힙 자료구조를 써줘야지 쓸수있는것은 아니다. 미리 만들어둔 라이브러리를 쓸수 있다.
# heapq module using import heapq
# heap = []
# heapq.heappush(heap, 4)
# heapq.heappop(heap)
# print(heap)
# 위는 최소값이 top 이다. 만약 최댓값을 넣고 빼고 싶다면 음수를 이용한다
# -1 를 곱해서 넣고, -1 을 곱해서 뺀다.
# heapq.heappush(heap, 4 * -1)
# print(heapq.heappop(heap) * -1) // 최댓값을 빼는 방법

#  현재 재고가 바닥나는 시점 이전까지 받을 수 있는 밀가루 중 제일 많은 밀가루를 받는 게 목표

# 1. 현재 재고의 상태에 따라 최곳값을 받아야 된다. (동적 변경 상황)
# 2. 제일 많은 값만 가져가면 된다.

# 1. 데이터를 넣을 때마다 최댓값을 동적으로 변경시키며
# 2. 최솟/최댓값을 바로 꺼낼 수 있는
# Heap 구조를 사용하면 된다


def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    answer = 0
    last_added_date_index = 0
    max_heap = []

    # 우리의 목표는 현재 재고, stock 이 k보다 많게 하는 것입니다!
    # stock 이 k 보다 많아야 k날까지 버틸 수 있기 때문입니다.
    # 따라서 그 전까지 while 문을 이용해서 밀가루들을 추가해보겠습니다.

    # supplies 의 값들을 꺼내서 heap 에 넣어 줄 예정
    # 그렇게 되면 Heap 의 성질을 이용해서 가장 큰 값들을 쉽게 빼서 stock 에 추가할 수 있기 때문
    # 조건: stock 이 비면 공장이 멈추기 때문에 stock 이 떨어지기 전까지의 공급량들 중에서 가장 큰 값
    # ->  현재 stock 의 양이 date 보다 높아야함 stock 이 10이면 8일까지는 가능, 하지만 11일은 불가능
    # -> 따라서 dates[last_added_date_index] <= stock: 라는 조건

    # 그러면, 이제 heap 에 있는 값을 빼서 stock 에 추가해주기만 하면 됩니다.
    # 들어가 있는 값들 중 가장 최고로 높은 공급량을 stock 에 추가해주겠습니다.
    # 그러면 한 번씩 공급량을 추가했으니 answer 가 하나 증가됩니다. <- 최소한의 밀가루 공급수

    while stock <= k:
        while last_added_date_index < len(dates) and dates[last_added_date_index] <= stock:
            heapq.heappush(max_heap, -supplies[last_added_date_index])
            last_added_date_index += 1

        answer += 1
        heappop = heapq.heappop(max_heap)
        stock += -heappop

    return answer

# heap 에 추가할때 조건에 맞춰서 추가한다. 그래서 그냥 꺼내기만 한다.
print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))
print("정답 = 2 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(4, [4, 10, 15], [20, 5, 10], 30))
print("정답 = 4 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(4, [4, 10, 15, 20], [20, 5, 10, 5], 40))
print("정답 = 1 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(2, [1, 10], [10, 100], 11))