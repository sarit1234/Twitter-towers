# This is a sample Python script.
import math


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def check_height(height):
    new_height = int(input("the height must be more than 2 cm, enter height again: "))
    while new_height < 2:
        new_height = int(input("the height must be more than 2 cm, enter height again: "))
    return new_height


def rectangle_tower():
    height = int(input("set height: "))
    if height < 2:
        height = check_height(height)
    width = int(input("set width: "))
    if height == width or abs(height - width) > 5:
        print("the area of the rectangle is " + str(height * width) + "\n")
    else:
        print("the Scope of the rectangle is " + str(2 * height + 2 * width))


def is_even(width):
    if width % 2 == 0:
        return True
    else:
        return False


def check_width_height(height, width):
    if width / height > 2:
        return True
    return False


def print1(height, width):
    middle_section = height - 2  # how many lines in the middle section
    num_groups = (width - 3) // 2  # how many groups we have, group is all the lines with the same number of stars.
    num_lines_each_equal_group = middle_section // num_groups  # how many lines the equal groups have.
    num_lines_first_group = middle_section - num_lines_each_equal_group * (num_groups - 1)
    num_spaces = width // 2
    num_stars = 1
    print(num_spaces * ' ' + num_stars * "*" + num_spaces * ' ' + "\n")
    num_spaces -= 1
    num_stars += 2
    for i in range(num_lines_first_group):
        print(num_spaces * ' ' + num_stars * "*" + num_spaces * ' ' + "\n")
    for j in range(num_groups - 1):
        num_spaces -= 1
        num_stars += 2
        for i in range(num_lines_each_equal_group):
            print(num_spaces * ' ' + num_stars * "*" + num_spaces * ' ' + "\n")
    print(width * "*" + "\n")


def print_triangle(height, width):
    if is_even(width) or check_width_height(height, width):
        print("The triangle cannot be printed\n")
    else:
        print1(height, width)


def triangular_tower():
    height = int(input("set height: "))
    if height < 2:
        height = check_height(height)
    width = int(input("set width: "))
    triangle_side = math.sqrt((width / 2) ** 2 + height ** 2)
    choose = int(input("choose 1 for scope of the triangle or 2 for print the triangle: "))
    if choose == 1:
        print("the scope of the triangle is: " + str(triangle_side * 2 + width) + "\n")
    if choose == 2:
        print_triangle(height, width)


def main():
    while True:
        choose = int(input("Choose 1 for a rectangle tower, choose 2 for a triangular tower, choose 3 for an exit\n"))
        if choose == 1:
            rectangle_tower()
        if choose == 2:
            triangular_tower()
        if choose == 3:
            break


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
