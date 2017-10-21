from sys import argv

print("Welcome to your todo list!")

todo_list = []


open("todos.txt", "a").close()

open("completed.txt", "a").close()

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
    with open("completed.txt", 'a') as completed_txt:
        completed_txt.write(f"{todo_list[remove_number - 1]}\n")

    todo_list.pop(remove_number - 1)

    with open("todos.txt", 'w') as todos_txt:
        todos_txt.write('\n'.join(todo_list))


def edit_todos(number_edited, todo_edited):
    # list[x] = y ...
    # リストのxの要素をyに置き換える
    todo_list[number_edited - 1] = todo_edited

    with open("todos.txt", 'w') as todos_txt:
        todos_txt.write('\n'.join(todo_list))


def command_todos():
    todo_command = input("Enter a command (add/exit/check/edit):\n")

    if todo_command != "add" and todo_command != "exit" and \
    todo_command != "check" and todo_command != "edit":
        print(f"Sorry, {todo_command} is not a valid command.")

        command_todos()

    elif todo_command == "add":
        todo = input("Add a todo:\n")

        write_todos(todo)

    elif todo_command == "exit":
        exit(0)

    elif todo_command == "check":
        todo_number_completed = int(input("Which item to mark as completed?\n"))

        if todo_number_completed > len(todo_list):
            print("Invalid item number.")

            command_todos()

        else:
            remove_completed_todos(todo_number_completed)

    elif todo_command == "edit":
        todo_edited_input = input("Enter item number, followed by a space and the new item name.\n")

        str_todo_number_edited = todo_edited_input.split(' ', 1)[0]
        str_todo_edited = todo_edited_input.split(' ', 1)[1]

        int_todo_number_edited = int(str_todo_number_edited)

        if int_todo_number_edited > len(todo_list):
            print("Invalid item number.")

            command_todos()

        else:
            edit_todos(int_todo_number_edited, str_todo_edited)


def todo():
    while True:
        print_todos()

        command_todos()


def todo2():
    todo = argv[2]

    write_todos(todo)

    print_todos()


def todo3():
    todo_number_completed = int(argv[2])

    if todo_number_completed > len(todo_list):
        print("Invalid item number.")

    else:
        remove_completed_todos(todo_number_completed)

        print_todos()

def todo4():
    int_todo_number_edited = int(argv[2])
    str_todo_edited = argv[3]

    if int_todo_number_edited > len(todo_list):
        print("Invalid item number.")

    else:
        edit_todos(int_todo_number_edited, str_todo_edited)

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

        elif argv[1] == "edit":
            print('''Error: Item number or new name missing.
Try: python3.6 todo.py edit item_number "Name of todo item"''')

        else:
            print(f"Sorry, {argv[1]} is not a valid command.")

    elif len(argv) == 3:
        if argv[1] == "add":
            todo2()

        elif argv[1] == "check":
            todo3()

        elif argv[1] == "edit":
            print('''Error: Item number or new name missing.
Try: python3.6 todo.py edit item_number "Name of todo item"''')

        else:
            print(f"Sorry, {argv[1]} is not a valid command.")

    elif len(argv) == 4:
        if argv[1] == "edit":
            todo4()

        else:
            print(f"Sorry, {argv[1]} is not a valid command.")

    else:
        todo()
todo_argv()