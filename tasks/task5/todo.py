print("Welcome to your todo list!")

todo_list = []

def todo():
    while True:
        todo = input("Add a todo:\n")
        todo_list.append(todo)

        if len(todo_list) == 1:
            print("You added 1 item:")
        else:
            print(f"You added {len(todo_list)} items:")

        for next_todo in todo_list:
            print(f"- {next_todo}")

todo()