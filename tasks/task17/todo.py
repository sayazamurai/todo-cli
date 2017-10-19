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
        print("You have 1 item:")
    else:
        print(f"You have {len(todo_list)} items:")

    for (number, next_todo) in enumerate(todo_list):
        print(f"{number + 1}. {next_todo}")


def write_todos(todo):
    todo_list.append(todo)

    with open("todos.txt", 'w') as todos_txt:
        todos_txt.write('\n'.join(todo_list))


def remove_completed_todos(remove_number):
    todo_list.pop(remove_number - 1)

    with open("todos.txt", 'w') as todos_txt:
        todos_txt.write('\n'.join(todo_list))


def command_todos():
    todo_command = input("Enter a command (add/exit/check):\n")

    if todo_command != "add" and todo_command != "exit" and todo_command != "check":
        print(f"Sorry, {todo_command} is not a valid command.")
        command_todos()

    elif todo_command == "exit":
        exit(0)

    elif todo_command == "check":
        todo_number_completed = int(input("Which item to mark as completed?\n"))

        remove_completed_todos(todo_number_completed)
        # todo_list.pop(todo_number_completed - 1)

        # with open("todos.txt", 'w') as todos_txt:
        #     todos_txt.write('\n'.join(todo_list))

        todo()


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


def todo3():
    todo_number_completed = int(argv[2])

    remove_completed_todos(todo_number_completed)
    # todo_list.pop(todo_number_completed - 1)

    # with open("todos.txt", 'w') as todos_txt:
    #         todos_txt.write('\n'.join(todo_list))

    print_todos()


def todo_argv():
    if len(argv) == 2:
        if argv[1] == "list":
            print_todos()

        elif argv[1] == "add":
            print('''Error: Name of a todo item missing.
Try: python3.6 todo.py add "Name of todo item"''')

        elif argv[1] == "check":
            print('''Error: Item number missing.
Try: python3.6 todo.py check item_number"''')

    elif len(argv) == 3:
        if argv[1] == "check":
            todo3()

        else:
            todo2()

    else:
        todo()


todo_argv()


