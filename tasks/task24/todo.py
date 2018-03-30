import fire


class Todo:
    def __init__(self, name, is_new):
        self.name = name
        self.is_new = is_new

    def print_todo(self):
        # todoの項目ひとつをprintする/改行しない
        print(self.name, end="")
        # もしis_newがTrueならば
        if self.is_new:
            # ↑の後に" (NEW)"をprintする/改行しない
            print(" (NEW)", end="")
        # 改行する
        print()


class TodoList:
    def __init__(self):
        self.todos = []

        open("todos.txt", "a").close()
        with open("todos.txt") as f:
            # todos.txtを一行ずつ読み込む
            for line in f:
                # 余分なスペースをなくしてtodo_nameに代入する
                todo_name = line.strip()
                # ??? Todoオブジェクトを作る
                # 変数nameはtodo_name、
                # 今は既存のtodoを読み込んでいるのでis_newはFalse
                # ???? new_todoは文字列ではなくオブジェクトTodo(...)
                new_todo = Todo(todo_name, False)
                # リストself.todosにTodo(...)を追加する
                self.todos.append(new_todo)

    def list(self):
        for todo in self.todos:
            # ??? todoはTodoのオブジェクト
            todo.print_todo()

    def add(self, new_todo):
        new_todo = Todo(todo_name, True)
        self.todos.append(new_todo)
        self.list()
        self._save()

    # addしたあとのself.todosをtodos.txtに保存する
    # コマンドラインではなく、
    # 入っているclassの中だけで使うメソッドは
    # メソッド名の前に"_"をつける
    # "_"がついているメソッドはclassの外から呼んではいけない
    def _save(self):
        with open("todos.txt", "w") as f:
            todo_string_list = []
            for todo in self.todos:
                # ??? todoはTodoのオブジェクト
                todo_string_list.append(todo.name)
            f.write("\n".join(todo_string_list))


if __name__ == "__main__":
    fire.Fire(TodoList)
