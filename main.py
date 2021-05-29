# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def format_index_number(index):
    index += 1

    index_as_string = str(index)
    length_of_index = len(index_as_string)
    last_digit = index_as_string
    if length_of_index > 1:
        last_digit = index_as_string[len(index_as_string)-1:]
    print(f"The last digit is : {last_digit}")

    ending = "th"
    if last_digit == "1":
        ending = "st"
    elif last_digit == "2":
        ending = "nd"
    elif last_digit == "3":
        ending = "rd"

    return str(index) + ending


def print_broken_answer(index, wrong_name):
    print(f'In the {format_index_number(index)} time you gave : {wrong_name}')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    counter = 0
    broken_names = []
    while True:
        name = input("Give name : ")
        print(f"name given : {name}")
        if name == "Nobody":
            print(f"nice try...")
            continue
        elif name == "Alexandra":
            print(f"Hi {name}")
            break
        broken_names.append(name)
        counter += 1
    print(f"Times without a valid answer {counter}")
    print("I can print " + str(counter) + " messages")
    for i in range(counter):
        print_broken_answer(i, broken_names[i])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
