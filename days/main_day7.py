while True:
    # Get user input and strip space chars from it
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            file = open('files/todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open('files/todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case 'show':
            file = open('files/todos.txt', 'r')
            todos = file.readlines()
            file.close()
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
            file = open('files/todos.txt', 'w')
            todos = file.readlines()
            file.close()
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo
        case 'complete':
            file = open('files/todos.txt', 'w')
            todos = file.readlines()
            file.close()
            number = int(input("Number of the todo to complete: "))
            todos.pop(number -1)
        case 'exit':
            break

print("Bye!")
