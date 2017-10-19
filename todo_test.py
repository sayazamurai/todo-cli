# task10
# from sys import argv
#
# print(argv)
# print(len(argv))
# print(argv[1])

# task15
# 0 a
# 1 b
# 2 c
# 3 d
# 4 e
# 5 f
# list = ["a", "b", "c", "d", "e", "f"]

# for (number, i) in enumerate(list):
#     print(number, i)

#task16

list = ["a", "b", "c", "d", "e", "f"]

for (number, i) in enumerate(list):
    print(number + 1, i)

number_completed = int(input("> "))
list.pop(number_completed - 1)

for (number, i) in enumerate(list):
    print(number + 1, i)