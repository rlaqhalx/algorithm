class Dict:
    def __init__(self):
        self.items = [None] * 8

# Collisoin: What if hash value is the same ---> Overriding issue
# Chaining 과 Open Addressing 이라는 방법
# Chaining 은 linkedlist 를 이용한다.
    def put(self, key, value):
        index = hash(key) % len(self.items) # 0-7 사이
        # key -> ksdfksdf8 -> self.items[7] = [("ksdfksdf8", "test")]
        # key -> ksdfksdfk -> self.items[7] = [("ksdfksdf8", "test")] -> [("ksdfksdfk", "test33")]
        self.items[index] = value


    def get(self, key):
        index = hash(key) % len(self.items)
        return self.items[index]


my_dict = Dict()
my_dict.put("test", 3)
print(my_dict.get("test"))  # 3이 반환되어야 합니다!