class Person:
    def __init__(self, param_name):
        print("I am created! ", self)
        self.name = param_name

    def talk(self):
        print("Hi, my name is", self.name, "!")

person_1 = Person("A")
print(person_1.name)
person_1.talk()
person_2 = Person("B")
print(person_2)