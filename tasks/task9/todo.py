print("Welcome to your todo list!")

todo_list = []

open("todos.txt", "a").close()

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

        with open("todos.txt", 'w') as todos_txt:
            todos_txt.write('\n'.join(todo_list))

todo()