FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    with open(filepath, "r") as file:
        todos_local = file.readlines()
    return todos_local


def show_todos(todos_list):
    for (ind, tod) in enumerate(todos_list):
        print(f"{ind + 1}. {tod}".strip())


def save_file(todos_arg, filepath=FILEPATH):
    with open(filepath, "w") as new_file:
        new_file.writelines(todos_arg)


