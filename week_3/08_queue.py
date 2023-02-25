# FIFO

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    # head   tail
    # [4] -> [2]
    # new_node = Node(3)
    # head         tail
    # [4] -> [2] -> [3]

    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    # head         tail
    # [4] -> [2] -> [3]
    # delete_head = self.head
    # head   tail
    # [2] -> [3] return [4]

    def dequeue(self):

        if self.is_empty():
            return "Queue is Empty"
        delete_head = self.head
        self.head = self.head.next
        return delete_head.data

    def peek(self):
        if self.is_empty():
            return "Queue is Empty"
        return self.head.data

    def is_empty(self):
        return self.head is None

# Queue 또한 Stack 과 마찬가지로 linked list 와 유사하게 구현할수있습니다.
# Stack 과는 다르게 Queue 는 끝과 시작의 노드를 전부 가지고 있어야 하므로
# self.head 와 self.tail 을 가지고 시작합니다.

queue = Queue()
queue.enqueue((3))
print(queue.peek())
queue.enqueue((4))
print(queue.peek())
queue.enqueue((5))
print(queue.peek())
print(queue.dequeue())
print(queue.peek())
print(queue.is_empty())