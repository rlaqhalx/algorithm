class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def get_kth_node_from_last(self, k):
        # implement this part
        length = 1
        cur = self.head
        while cur.next is not None:
            cur = cur.next
            length +=1
        length_to_k = length - k
        cur = self.head
        for i in range(length_to_k):
            cur = cur.next
        return cur

        # Or You can use two pointers with k distance between them
        # slow = self.head
        # fast = self.head
        # for i in range (k):
        #    fast = fast.next
        # while fast is not None:
        #    slow = slow.next
        #    fast = fast.next
        # return slow

linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

# [6] -> [7] -> [8] length: 3 length_from_last: 1 (len - k)
print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!