import fire


class TodoList:
    def __init__(self):
        self.todos = []

        # "todos.txt"ファイルがあればそのままにしておき
        # 無ければ"todos.txt"ファイル（空のファイル）を作る
        open("todos.txt", "a").close()
        # "todos.txt"を開いて行ごとに読み込み
        # 余分なスペースなどを除いたものを(= .strip())
        # リストにappendする
        with open("todos.txt") as f:
            for line in f:
                self.todos.append(line.strip())

        # self.todos = ["watch sexy zone channel", "listen to qrzone", "eat"]

    def list(self):
        for todo in self.todos:
            print(todo)

    def add(self, new_todo):
        self.todos.append(new_todo)
        self.list()


if __name__ == "__main__":
    # fireでclassの中のメソッドを呼びたい時は
    # ()の中にclassの名前を指定する
    fire.Fire(TodoList)

# terminalで
# python3.6 list
# =>
# todolist = TodoList()
# todolist.list()
# =>
# watch sexy zone channel
# listen to qrzone
# eat

# python3.6 todo.py add "Listen to Victory Roads"
# watch sexy zone channel
# listen to qrzone
# eat
# Listen to Victory Roads
