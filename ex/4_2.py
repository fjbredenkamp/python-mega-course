# The ranking list given in the coding area represents the ranking of three athletes,
# John, Sen, and Lisa. John won 1st place, Sen got 2nd, and Lisa 3rd.
#
# Your task is to create a program that:
# 1. Contains the above list.
# 2. Prompts the user to input a rank number.
# 3. Returns the person who has the given rank.
#
# For example:
# Enter rank number: 2
# Prints Sen

#Mine: :(
ranking = ['John', 'Sen', 'Lisa']

while True:
    user_rank = input("Enter rank number: ")

    match user_rank:
        case '1':
            user_rank = int('1')
            print(ranking[0])
        case '2':
            user_rank = int('2')
            print(ranking[1])
        case '3':
            user_rank = int('3')
            print(ranking[2])
        case 'exit':
            break

#Theirs:
# Prompt the user to input a rank number and assign it to the variable 'rank'.
rank = int(input("Enter rank number: ")) - 1

# Access the element in the ranking list based on the given rank and assign it to the variable 'name'.
name = ranking[rank]

# Print the name of the person who has the given rank.
print(name)