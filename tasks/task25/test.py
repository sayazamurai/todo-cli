# ターミナルで*yを指定してない時に*yつかうとどうなるか
# import fire
#
# def test(x, *y):
#     if y:
#         print(x)
#         print(y)
#     else:
#         print(x)
#
# if __name__ == "__main__":
#     fire.Fire()

# "-"をつけてappendするとき
# some_list = [
#     "shori",
#     "fuma",
#     "marius",
#     "kento",
#     "so",
# ]
#
# new_list = []
#
# for something in some_list:
#     new_list.append(f"- {something}")
# print(new_list)

# リストの一部にディクショナリがあり、そのvalueを拾ってきたいとき
# some_list = ["A", "B", {"C": ["a", "b"]}, "D"]
#
# for i in some_list:
#     if "C" in i:
#         print(i["C"])
#     else:
#         print(i)

# 文字列をディクショナリに直すとき
# import json
#
# dictionary_string = '{"A": "a", "B": "b"}'
# dictionary = json.loads(dictionary_string)
# print(dictionary["A"])

# リストの中の文字列をディクショナリに戻す
# import json
#
# some_list = ['{"A": "False"}', '{"C": ["a", "b", "c"]}']
# #
# #↓これだとAがディクショナリじゃないのでできない
# #some_list = ['A', '{"C": ["a", "b", "c"]}']
# # some_list = ["A", "B", '{"C": ["a", "b", "c"]}', "D"]
# #
# for i in some_list:
#     todo_name = i.strip()
#     todo_name_transformed = json.loads(todo_name)
#     print(todo_name_transformed)
