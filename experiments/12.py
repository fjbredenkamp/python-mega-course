# Only functions with a return value need to be assigned to a variable, see get_todos below
def get_todos(filepath):
    # exp 2: this results in a file not found error:
    # filepath = 'todos1.txt'
    with (open(filepath, 'r') as file_local):
        todos_local = file_local.readlines()
    return todos_local
    # exp 1 - this results in a error
    # return filepath


# Functions that don't return anything don't need to be assigned to a variable, see write_todos below
def write_todos(filepath, todos_arg):
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


while True:
    # Get user input and strip space chars from it
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        # list slicing [4:] read from 4th char. [4:9]
        # for the string add clean the bag would produce clean so from char 4 to 9...char 9 NOT included!
        todo = user_action[4:]

        todos = get_todos('files/todos.txt')

        todos.append(todo + "\n")

        write_todos('files/todos.txt', todos)

    elif user_action.startswith("show"):
        # old way
        # file = open('files/todos.txt', 'r')
        # todos = file.readlines()
        # file.close()
        # new way using context manager:
        # with open('files/todos.txt', 'r') as file:
        #     todos = file.readlines()
        # second new way...call a function:
        todos = get_todos('files/todos.txt')

        # for loop vs:
                    # new_todos = []
                    #
                    # for item in todos:
                    #     new_item = item.strip('\n')
                    #     new_todos.append(new_item)
        # list comprehension:
        #             new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
         # simplest solution:
            item = item.strip('\n')
            item = item.title()
            row = f"{index + 1}.{item}"
            print(row)
        if not todos:
            print("You have 0 items")

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos('files/todos.txt')

            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo + '\n'

            write_todos('files/todos.txt', todos)
        except ValueError:
            print("Your command is not valid, please enter a number")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos('files/todos.txt')

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos('files/todos.txt', todos)

            message = f"Todo '{todo_to_remove}' was removed from the list"
            print(message)
        except IndexError:
            print("There is no item with that number")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid")

print("Bye!")
