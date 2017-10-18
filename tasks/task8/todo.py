print("Welcome to your todo list!")

todo_list = []

# ファイルtodos.txtが存在しない場合にtodos.txtを作り、
# すぐに閉じる
# →
# ファイルtodos.txtが存在しない状態で実行してもエラーとならない
open("todos.txt", "a").close()
# with open("todo.txt", "a") as todos_txt:
#     pass
# でもOK

with open("todos.txt") as todos_txt:
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