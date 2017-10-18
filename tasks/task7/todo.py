print("Welcome to your todo list!")

todo_list = []

# with open(...) as を使うと、closeする必要がなくなる
with open("todos.txt") as todos_txt:
    # for ... in (オープンしたファイル) を使うと、
    # while True
    #   ... = ...readline()
    #   if ...
    #   else:
    #       break
    # を一行でできるようになる
    #
    # todos_txtはリストではなくopenしたファイルだが、
    # オープンしたファイルにfor inを使うと、一行ずつ
    # そのファイルの内容を読み込むことができる
    for todos_readline in todos_txt:
        todos_readline_strip = todos_readline.strip()
        todo_list.append(todos_readline_strip)

def todo():
    while True:
        if len(todo_list) == 1:
            print("You added 1 item:")
        else:
            print(f"You added {len(todo_list)} items:")

        for next_todo in todo_list:
            print(f"- {next_todo}")

        todo = input("Add a todo:\n")
        todo_list.append(todo)

todo()