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

    for next_todo in todo_list:
        print(f"- {next_todo}")


def write_todos(todo):
    todo_list.append(todo)

    with open("todos.txt", 'w') as todos_txt:
        todos_txt.write('\n'.join(todo_list))


def todo():
    while True:
        print_todos()

        todo = input("Add a todo:\n")

        write_todos(todo)


def todo2():
    todo = argv[2]

    write_todos(todo)

    print_todos()


def todo_argv():
    if len(argv) == 2 and argv[1] == "list":
        print_todos()
    elif len(argv) == 3:
        todo2()
    else:
        todo()


todo_argv()


