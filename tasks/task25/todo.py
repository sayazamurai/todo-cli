# Hint1:
# メソッドの変数の頭に"*"をつけると、複数の値がタプルに入って出力される
# メソッドの中でその変数を使う時は"*"はつけない
#
# e.g.
# def add(self, todo_name, *subtasks):
#   print(subtasks)
# ターミナルで
# python3.6 todo.py "A" "a" "b" "c"
# を実行
# =>
#　("a", "b", "c")
#
#　print(list(subtasks))とすると、タプルがリストに変換される
# ["a", "b", "c"]

# Hint2:
# dictionaryを文字列変換する方法、文字列をdictionaryに戻す方法
#
# import json
# *dictionary → 文字列
# json.dumps(dictionary)
# *文字列（dictionary_string） → dictionary
# json.loads(dictionary_string)

import fire
import json


class Todo:
    def __init__(self, name, is_new, subtasks):
        self.name = name
        self.is_new = is_new
        self.subtasks = subtasks  # [a, b, c]

    def print_todo(self):
        print(self.name, end="")
        if self.is_new:
            print(" (NEW)", end="")
        print()
        if self.subtasks != "none":
            for subtask in self.subtasks:
                print(f"- {subtask}")


class TodoList:
    def __init__(self):
        self.todos = []

        open("todos.txt", "a").close()
        with open("todos.txt") as f:
            for line in f:
                todo_name = line.strip()
                dictionary_todo_name = json.loads(
                    todo_name)  # = {"A": "none"}, = {"C": ["a", "b", "c"]}...
                for todo, subtasks in dictionary_todo_name.items():
                    new_todo = Todo(
                        todo, False,
                        subtasks)  # new_todo = Todo("A", False, "none")
                    self.todos.append(new_todo)

    def list(self):
        for todo in self.todos:  # self.todos = [Todo("A", True, "none"),Todo("B", True, [a, b, c]),...)
            todo.print_todo()

    def add(self, todo_name, *subtasks):
        if subtasks:
            new_todo = Todo(todo_name, True, list(subtasks))
        else:
            new_todo = Todo(todo_name, True, "none")
        self.todos.append(new_todo)
        self.list()
        self._save()

    def _save(self):
        with open("todos.txt", "w") as f:
            todo_string_list = []

            for todo in self.todos:  # self.todos = [Todo("A", True, "none"),Todo("B", True, [a, b, c]),...)
                dictionary_todo_name = {}
                dictionary_todo_name[todo.name] = todo.subtasks
                str_dictionary_todo_name = json.dumps(dictionary_todo_name)
                todo_string_list.append(str_dictionary_todo_name)
            f.write("\n".join(todo_string_list))


if __name__ == "__main__":
    fire.Fire(TodoList)
