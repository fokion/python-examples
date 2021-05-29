import random


class Animal:
    name = ""
    type = "animal"
    has_legs = False

    def __init__(self, name, has_legs=True):
        self.name = name
        self.has_legs = has_legs

    def get_name(self):
        return self.name

    def what_am_i(self):
        return f"I am an {self.type} and my name is : {self.name}"

    def i_have_legs(self):
        return self.has_legs


class Cat(Animal):
    type = "cat"


class Snake(Animal):
    type = "snake"

    def __init__(self, name):
        super().__init__(name, False)


def main():
    animals = [Cat("whiskey"), Cat("rose"), Snake("shh")]
    whiskey, rose, snake = animals
    print("Hello I am " + whiskey.get_name())
    print("Hello I am " + rose.get_name())
    print("---------------------")
    print(f"the index of snake is {animals.index(snake)}")
    print("---------------------")
    for i in range(len(animals)):
        animal = animals[i]
        has_legs = "do"
        if not animal.i_have_legs():
            has_legs += " not"
        print(f'{animal.what_am_i()}, {has_legs} have legs')
    print("---------------------")
    for i in range(len(animals)):
        random.choice(animals).what_am_i()


if __name__ == '__main__':
    main()
