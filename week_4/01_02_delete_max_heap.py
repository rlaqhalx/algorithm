# O(log(N))

class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        self.items.append(value)
        cur_index = len(self.items) - 1

        while cur_index > 1:  # cur_index 가 1이 되면 정상을 찍은거라 다른 것과 비교 안하셔도 됩니다!
            parent_index = cur_index // 2
            if self.items[parent_index] < self.items[cur_index]:
                self.items[parent_index], self.items[cur_index] = self.items[cur_index], self.items[parent_index]
                cur_index = parent_index
            else:
                break

    # 최대힙에서 원소를 삭제하는방법은 최댓값, 루트노드를 삭제하는것입니다. (Stack Like)
    # 맨 위에 있는 원소만 제거 가능하고 다른 위치의 노드는 삭제할수없습니다.
    # 추가와 마찬가지로 삭제도 힙의 규칙이 지켜져야합니다. Heapfify

    # 1. 루트 노드와 맨 끝에 있는 원소를 교체한다.
    # 2. 맨 뒤에 있는 원소를 (원래 루트 노드) 를 삭제합니다. 이때, 끝에 반환해줘야 하니까 저장해둡니다.
    # 3. 변경된 노드와 자식 노드를 비교합니다. 두 자식 중 더 큰 자식과 비교해서 자신보다 자식이 더 크다면 자리를 바꿔준다.
    # 4. 자식 노드 둘보다 부모노드가 더 크거나 가장 바닥에 도달하지 않을때까지 3. 을 반복합니다.
    # 5. 2에서 제거한 원래 루트 노드를 반환합니다.

    def delete(self):
        # 구현해보세요!
        self.items[1] , self.items[-1] = self.items[-1], self.items[1]
        # list.pop() -> removes last node list.pop(3) -> removes index 3
        prev_max = self.items.pop()
        cur_index = 1

        while cur_index <= len(self.items) - 1:
            left_child_index = cur_index * 2
            right_child_index = cur_index * 2 + 1
            max_index = cur_index

            if left_child_index <= len(self.items) - 1 and self.items[left_child_index] > self.items[max_index]:
                max_index = left_child_index

            if right_child_index <= len(self.items) - 1 and self.items[right_child_index] > self.items[max_index]:
                max_index = right_child_index

            if max_index == cur_index:
                break

            self.items[cur_index], self.items[max_index] =   self.items[max_index], self.items[cur_index]
            cur_index = max_index

        return prev_max

max_heap = MaxHeap()
max_heap.insert(8)
max_heap.insert(6)
max_heap.insert(7)
max_heap.insert(2)
max_heap.insert(5)
max_heap.insert(4)
print(max_heap.items)  # [None, 8, 6, 7, 2, 5, 4]
print(max_heap.delete())  # 8 을 반환해야 합니다!
print(max_heap.items)  # [None, 7, 6, 4, 2, 5]

# 이 맥스 힙에서 원소를 제거해보겠습니다! (항상 맨 위의 루트 노드가 제거 됩니다.)
#       8      Level 0
#     6   7    Level 1
#    2 5 4 3   Level 2
#
# 1. 루트 노드와 맨 끝에 있는 원소를 교체한다.
#
#       8      Level 0
#     6   7    Level 1
#    2 5 4 3   Level 2
#
#       3      Level 0
#     7   6    Level 1
#    2 5 4 8   Level 2
#
# 2. 맨 뒤에 있는 원소를 (원래 루트 노드)를 삭제합니다.
# 이 값이 기존 맥스힙에 있던 가장 큰 값입니다. 따라서 이 값을 마지막에는 반환해줘야 합니다!
#
#       3      Level 0
#     6   7    Level 1
#    2 5 4 X   Level 2
#
# 3-1. 변경된 노드를 더 큰 자식 노드와 비교해야 합니다.
# 우선 부모와 왼쪽 자식을 비교합니다. 그리고 부모와 오른쪽 자식을 비교합니다.
# 그리고 부모 보다 큰 자식 중, 더 큰 자식과 변경해야 합니다.
# 왼쪽 자식인 6과 오른쪽 자식인 7 중에서 7이 더 크고, 부모인 3보다 크니까 둘의 자리를 변경합니다.
#
#       3      Level 0
#     6   7    Level 1
#    2 5 4     Level 2
#
#       7      Level 0
#     6   3    Level 1
#    2 5 4     Level 2
#
# 3-2. 다시 자식 노드와 비교합니다.
# 우선 부모와 왼쪽 자식을 비교합니다.
# 왼쪽 자식인 4는 부모인 3보다 더 크니까 둘의 자리를 변경합니다.
#
#       7      Level 0
#     6   3    Level 1
#    2 5 4     Level 2
#
#       7      Level 0
#     6   4    Level 1
#    2 5 3     Level 2
#
#
# 4. 가장 아래 레벨에 도달했으므로 멈춥니다. 힙의 특성을 그대로 유지해 데이터를 삭제했습니다!
#
#       7      Level 0
#     6   4    Level 1
#    2 5 3     Level 2
#
# 5. 그리고, 아까 제거한 원래 루트 노드, 8을 반환하면 됩니다!