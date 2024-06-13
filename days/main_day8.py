while True:
    # Get user input and strip space chars from it
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)
        case 'show':
            # old way
            # file = open('files/todos.txt', 'r')
            # todos = file.readlines()
            # file.close()
# new way using context manager:
            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

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
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number - 1

            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo + '\n'

            with open('files/todos.txt', 'w') as file:
                todos = file.writelines(todos)

        case 'complete':
            number = int(input("Number of the todo to complete: "))

            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open('files/todos.txt', 'w') as file:
                todos = file.writelines(todos)

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)

        case 'exit':
            break

print("Bye!")
