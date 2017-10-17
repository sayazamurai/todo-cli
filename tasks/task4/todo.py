print("Welcome to your todo list!")

todo_list = []

def todo():
    while True:
        todo = input("Add a todo:\n")
        todo_list.append(todo)
        print("You added:")

        for next_todo in todo_list:
            print(f"- {next_todo}")

todo()