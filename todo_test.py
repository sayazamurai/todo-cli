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

# list = ["a", "b", "c", "d", "e", "f"]

# for (number, i) in enumerate(list):
#     print(number + 1, i)

# number_completed = int(input("> "))
# list.pop(number_completed - 1)

# for (number, i) in enumerate(list):
#     print(number + 1, i)

# task20
# test_string = "a b c a b c d e f"

# # ['a b ', ' a b c d e f']
# # 1回目の'c'にだけsplitを適用する
# # →'c'を境界として文字列を分割し、リストにして返す
# print(test_string.split('c', 1))

# # a b c d e f
# #　↑で作ったリストの[1]にある要素を返す
# print(test_string.split('c', 1)[1])

# # a b
# print(test_string.split('c', 1)[0])

# # ['a b ', ' a b ', ' d e f']
# # 3回目の'c'までsplitを適用する
# print(test_string.split('c', 3))

# # ['a b ', ' a b ', ' d e f']
# # 4回目の'c'までsplitを適用する
# print(test_string.split('c', 4))

# # a b c d e f
# print(test_string.split('c', 1)[-1])

# # ['a b ', ' a b ', ' d e f']
# print(test_string.split('c'))

test_string = "1 a b c"

# ['', ' a b c']
print(test_string.split('1'))

# a b c
print(test_string.split('1')[1])

# ['1', 'a', 'b', 'c']
print(test_string.split(' '))

# a
print(test_string.split(' ')[1])


members = ["shori", "fuma", "kento", "sho", "marius"]
members[3] = "so"
print(members)
# ['shori', 'fuma', 'kento', 'so', 'marius']









