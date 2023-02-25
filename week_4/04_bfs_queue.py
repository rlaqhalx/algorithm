# dfs = stack
# bfs = queue
# WHY?
# dfs 는 탐색하는 원소를 최대한 깊게 따라가야한다.
# 이를 구현하기 위해 인접한 노드중 방문하지 않은 모든 노드들을 저장해두고,
# 가장 마지막에 놓은 노드를 꺼내서 탐색한다. -> stack

# bfs 는 현재 인접한 노드 먼저 방문해야 한다.
# 즉 인접한 노드 중 방문하지 않은 모든 노드들을 저장해두고,
# 가장 처름에 넣은 노드를 꺼내서 탐색하면 된다. -> queue

# 즉 value 를 넣는 방식은 같지만 빼는 방식이 다르다
# 둘다 class 를 따로 만들어서 instance 를 만든후 => stack = new Stack 쓸수도 있지만
# 간단히 [] list 를 통하여 만들수도 있다.
# stack 에서는 pop() 과 append(value) 를 쓰고
# queue 에서는 pop(0) 와 append(value) 를 쓴다.

# 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!
graph = {
    1: [2, 3, 4],
    2: [1, 5],
    3: [1, 6, 7],
    4: [1, 8],
    5: [2, 9],
    6: [3, 10],
    7: [3],
    8: [4],
    9: [5],
    10: [6]
}

# 1. 시작 노드를 큐에 넣습니다.
# 2. 현재 큐의 노드를 빼서 visited 에 추가합니다.
# 3. 현재 방문한 노드와 인접한 노드 중 방문하지 않은 노드를 큐에 추가합니다.

def bfs_queue(adj_graph, start_node):
    queue = [start_node]
    visited = []

    while queue:
        current_node = queue.pop(0)
        visited.append(current_node)
        for adj_node in adj_graph[current_node]:
            if adj_node not in visited:
                queue.append(adj_node)

    return visited


print(bfs_queue(graph, 1))  # 1 이 시작노드입니다!
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 이 출력되어야 합니다!