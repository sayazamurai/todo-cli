from sys import argv

print("Welcome to your todo list!")

todo_list = []

# completed_list = []

open("todos.txt", "a").close()

open("completed.txt", "a").close()

with open("todos.txt") as todos_txt:
    for todos_readline in todos_txt:
        todos_readline_strip = todos_readline.strip()
        todo_list.append(todos_readline_strip)


# with open("completed.txt") as completed_txt:
#     for completed_readline in completed_txt:
#         completed_readline_strip = completed_readline.strip()
#         completed_list.append(completed_readline_strip)


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
    # `open`のときに`a`を使う →
    # txtファイルの最後に文字列が追加されるので
    # いままでの completed.txt の中身を保持しておく必要がない
    with open("completed.txt", 'a') as completed_txt:
        completed_txt.write(f"{todo_list[remove_number - 1]}\n")

    # `open` のときに `w` を使う →
    # ファイルの中身が全部総入れ替えされるため、
    # removeする前に、いままでの completed.txt の中身を
    # 全部リストで保持しておき
    # removeする度に、リストに項目を追加していく必要がある
    # completed_list.append(todo_list[remove_number - 1])
    #
    # with open("completed.txt", 'w') as completed_txt:
    #     completed_txt.write('\n'.join(completed_list))

    todo_list.pop(remove_number - 1)

    with open("todos.txt", 'w') as todos_txt:
        todos_txt.write('\n'.join(todo_list))


def command_todos():
    todo_command = input("Enter a command (add/exit/check):\n")

    if todo_command != "add" and todo_command != "exit" and todo_command != "check":
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

        else: # argv[1] == "add"?
            todo2()

    else:
        todo()


todo_argv()