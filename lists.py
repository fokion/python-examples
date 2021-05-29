from copy import copy


def main():
    elements = [324, 2342, 22, 1231, 5467, 23, 63, 34]
    elements.sort()
    print(f"{elements}")
    elements.reverse()
    print("---------------")
    print(f"{elements}")
    print("-----------ids-----------")
    print(f"id : {id(elements)}")
    new_elements = elements
    print(f"id : {id(new_elements)}")
    copy_elements = copy(elements)
    print(f"id : {id(copy_elements)}")
    print("---------------")
    test = "1234"
    print(id(test))
    new_test = "1234"
    print(id(new_test))
    print(id('1234'))
    print("---------------")



if __name__ == "__main__":
    main()
