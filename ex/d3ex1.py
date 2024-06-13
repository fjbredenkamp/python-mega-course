country = "India"

while True:
    user_action = input("Type your country: ")
    user_action = user_action.strip()

    match user_action:
        case 'India':
            print("Namaste")
        case 'USA':
            print('Hello')
        case 'Germany':
            print("Hallo")
        case 'exit':
            break
