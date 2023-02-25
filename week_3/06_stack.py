#FILO

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_head = Node(value)
        new_head.next = self.head
        self.head = new_head
        return

    # pop 기능 구현
    def pop(self):
        if self.is_empty():
            return "Stack is Empty"
        delete_head = self.head
        self.head = self.head.next
        return delete_head

    def peek(self):
        if self.is_empty():
            return "Stack is Empty"
        return self.head.data


    # isEmpty 기능 구현
    def is_empty(self):
        return self.head is None

stack = Stack()
stack.push(3)
print(stack.peek())
stack.push(4)
print(stack.peek())
print(stack.pop().data)
print(stack.peek())
print(stack.is_empty())

# 여기서 linked list 의 Concept 인 node 를 이용하여 스택을 구현해봤지만
# 실제 코드에서는 파이썬의 list 를 이용해서 스택으로 사용합니다.