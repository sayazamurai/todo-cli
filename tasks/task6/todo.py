print("Welcome to your todo list!")

todo_list = []

todos_txt = open("todos.txt")

while True:
    todos_readline = todos_txt.readline()

    if todos_readline:
        todos_readline_strip = todos_readline.strip()
        todo_list.append(todos_readline_strip)
    else:
        break

todos_txt.close()

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