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
        print(f"I am an {self.type} and my name is : {self.name}")

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
    whiskey, rose , snakey = animals
    print("Hello I am " + whiskey.get_name())
    print("Hello I am " + rose.get_name())
    for i in range(len(animals)):
        animal = animals[i]
        animal.what_am_i()
        print(f"do I have legs : {animal.i_have_legs()}")


if __name__ == '__main__':
    main()
