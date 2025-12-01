import time

FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of to-do items
    :param filepath:
    :return:
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list in the text file.
    :param todos_arg:
    :param filepath:
    :return:
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


def get_day_time() -> str:
    hour = int(time.strftime("%H"))
    if 21 < hour < 4:
        return "night"
    elif hour < 12:
        return "morning"
    elif hour < 17:
        return "afternoon"
    else:
        return "evening"


now = time.strftime("%b %d, %Y %H:%M:%S")
day_time = get_day_time()
if __name__ == '__main__':
    print(f"Hello and good {day_time}. It's now {now}")
    print(get_todos())