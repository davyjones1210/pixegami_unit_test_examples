# d = {}
# while True:
#     course = input("Please enter your courses: ")
#     teacher = input("Please enter your teacher: ")
#     if course=='done' or teacher=='done':
#         break
#     d[course]=teacher
#     print(d)
#     print(type(d))
# import math
#
# x = (1, 2, 3)
# print(math.sqrt(sum(i**2 for i in x)))
# tuples = []
# while True:
#
#     user_input = input("Enter a tuple (or 'q' to quit): ")
#
#     if user_input.lower() == "q":
#
#         break
#
#     values = user_input.split(" ")
#     print("Values: ", values)
#
#     tuple_values = [int(value) for value in values]
#
#     tuple = tuple(tuple_values)
#
#     tuples.append(tuple)
#
#     print(tuples)

# x = (1,4)
# y = (2,5)
# z = (3,6)
#
# # cross_product = ((y[0] * z[1]) - (z[0] * y[1]),
# #                          (z[0] * x[1]) - (x[0] * z[1]),
# #                          (x[0] * y[1]) - (z[0] * x[1]))
# #
# # print(cross_product)
#
# input = "1 2 3"
#
# split_input = input.strip(" ")
# print(split_input.isdigit())

# mynewlist = [s for s in split_input if s.isdigit()]

#int_list = [int(i) for i in split_input]

# int_list = []
#
# try:
#     int_list = [int(i) for i in split_input]
# except ValueError:
#     print("That's not an int!")
#
# print("Split input: ", int_list)
# t = tuple(input)
#print(t)

# get_user_input = input("Please enter the coordinates of the first vector: ")
# print("User input", get_user_input)

# while True:
#
#     try:
#         get_user_input = input("Please enter the coordinates of the first vector: ")
#     except ValueError:
#         print('Please enter valid numbers separate by space, please')

#

class Foo():
    def __init__(self, a: int):
        self.a = a


    def input(self):
        user_input = input("Please enter the coordinates of the first vector: ")

        return user_input

    def set(self, a):
        self.a = a
        pass

    #returns the dot product of itself with another vector

    def add(self, b):

        sum = int(self.a) + int(b)

        return sum


def main():
    first_instance = Foo(None)
    second_instance = Foo(None)

    first_input = first_instance.input()  # asking the user to enter two vectors

    second_input = second_instance.input()  # asking the user to enter two vectors

    first_instance.set(first_input)
    second_instance.set(second_input)

    total = first_instance.add(second_input)

    print("Total is: ", total)




#main entry point to the program
if __name__ == "__main__":
    main()


