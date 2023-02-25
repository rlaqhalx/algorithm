# [(key1, value1) -> (key2, value2) -> (key3, value3)]
# so how its used in dic -> some key gets assigned to the same index of list
# so we make linkedlist for each index to resolve collision
class LinkedTuple:
    def __init__(self):
        # self.items = [] OR
         self.items = list()

    def add(self, key, value):
        self.items.append((key, value))

    def get(self, key):
        # k = key, v = value
        for k, v in self.items:
            if k == key:
                return v

# this is linkedDic using linkedTuple above
# Collection of linkedTuple
# [
# [(key1, value) -> (key2, value2) -> (key3, value3)],
# [(key11, value) -> (key22, value2) -> (key33, value3)],
# [(key111, value) -> (key222, value2) -> (key333, value3)]
# ]
class LinkedDict:
    def __init__(self):
        self.items = [] #[LinkedTuple(), LinkedTuple(), LinkedTuple()... ]
        for i in range(8):
            self.items.append(LinkedTuple())

    def put(self, key, value):
        # 구현해보세요!
        index = hash(key) % len(self.items)
        self.items[index].add(key, value) # using method from linkedTuple
        # self.items[index] = value
        # Now empty list [] will become [(key, value)], tuple added in empty list
        return

    def get(self, key):
        # 구현해보세요!
        index = hash(key) % len(self.items)
        # LinkedTuple
        # return self.items[index]
        # [(key1, value1), (key2, value2)]
        return self.items[index].get(key) # using 'get' method from linkedTuple

#Tuple 이란 list 와 다르게 ( ) 을 쓰고 used to store multiple items in a single variable
# Its ordered and unchangeable