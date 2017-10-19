from sys import argv

print("Welcome to your todo list!")

todo_list = []

open("todos.txt", "a").close()

with open("todos.txt") as todos_txt:
    for todos_readline in todos_txt:
        todos_readline_strip = todos_readline.strip()
        todo_list.append(todos_readline_strip)


def print_todos():
    if len(todo_list) == 1:
        print("You added 1 item:")
    else:
        print(f"You added {len(todo_list)} items:")

    for (number, next_todo) in enumerate(todo_list):
        print(f"{number + 1}. {next_todo}")


def write_todos(todo):
    todo_list.append(todo)

    with open("todos.txt", 'w') as todos_txt:
        todos_txt.write('\n'.join(todo_list))


def command_todos():
    todo_command = input("Enter a command (add/exit):\n")

    if todo_command != "add" and todo_command != "exit":
        print(f"Sorry, {todo_command} is not a valid command.")
        command_todos()

    elif todo_command == "exit":
        exit(0)


def todo():
    while True:
        print_todos()

        command_todos()

        todo = input("Add a todo:\n")

        write_todos(todo)


def todo2():
    todo = argv[2]

    write_todos(todo)

    print_todos()


def todo_argv():
    if len(argv) == 2 and argv[1] == "list":
        print_todos()

    elif len(argv) == 2 and argv[1] == "add":
        print('''Error: Name of a todo item missing.
Try: python3.6 todo.py add "Name of todo item"''')

    elif len(argv) == 3:
        todo2()

    else:
        todo()


todo_argv()


