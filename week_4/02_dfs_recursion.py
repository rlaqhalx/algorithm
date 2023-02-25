# 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!

graph = {
    1: [2, 5, 9],
    2: [1, 3],
    3: [2, 4],
    4: [3],
    5: [1, 6, 8],
    6: [5, 7],
    7: [6],
    8: [5],
    9: [1, 10],
    10: [9]
}
visited = []

# - 노드를 방문하고 깊이 우선으로 인접한 노드를 방문한다.
# - 또 그 노드를 방문해서 깊이 우선으로 인접한 노드를 방문한다.
# - 만약 끝에 도달했다면 리턴한다.
# 반복하다... 갈수없으면... 탈출조건... => recursion

# 1. 시작 노드 (루트 노드) 인 1부터 탐색한다
# 2. 현재 방문한 노드를 visited_array 에 추가한다
# 3. 현재 방문한 노드와 인접하지 않은 노드 중 방문하지 않은 노드에 방문한다.

def dfs_recursion(adjacent_graph, cur_node, visited_array):
    # 구현해보세요!
    visited_array.append(cur_node)
    # object = {a: 1, b: 2, c: 3}
    # for property in object
    # property = a,b,c 이고 object[property] = 1,2,3
    for adjacent_node in adjacent_graph[cur_node]: # to find adjacent nodes (values) of curr_node (key)
        print("adjacent_node:", adjacent_node)
        if adjacent_node not in visited_array: # 만약 다 방문했다면 (4번 처럼 3 을 이미 방문하고 남은게 없다면) 옛날 함수로 돌아간다 (1 의 두번째인 5)
            dfs_recursion(adjacent_graph, adjacent_node, visited_array)


dfs_recursion(graph, 1, visited)  # 1 이 시작노드입니다!
print(visited)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 이 출력되어야 합니다!