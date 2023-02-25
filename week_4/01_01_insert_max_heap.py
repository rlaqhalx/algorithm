# 완전이진트리
# 가장 크거나 작은 값을 구할때 유용하게 쓰인다.

# Tree 구조를 표현하는 방법 1. 직접 클래스를 구현해서 사용하는 방법 2. 배열로 표현하는방법 (완전이진트리) -> list
# [None]
# 1. 현재 인덱스 * 2 -> 왼쪽 자식의 인덱스
# 2. 현재 인덱스 * 2 + 1 -> 오른쪽 자식의 인덱스
# 3. 현재 인덱스 // 2 -> 부모의 인덱스

# 완전이진트리의 nodes:
# 각레벨에 k -> 2^k 개
# 최대노드의 개수: 2(h+1) - 1 개
# 완전이진트리의 height: h = log2(N+1)-1

# O(log(N))

class MaxHeap:
    def __init__(self):
        self.items = [None]

    # 1. 새노드를 맨 끝에 추가한다.
    # 2. 지금 넣은 새노드를 부모와 비교한다. 만약 부모보다 크다면 교체한다.
    # 3. 이 과정을 꼭대기까지 반복한다.

    def insert(self, value):
        # 구현해보세요!
        self.items.append(value)
        cur_index = len(self.items) - 1

        while cur_index > 1:
            parent_index = cur_index // 2
            if self.items[cur_index] > self.items[parent_index]:
                self.items[cur_index], self.items[parent_index] = self.items[parent_index],  self.items[cur_index]
                cur_index = parent_index
            else:
                break

        return


max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!