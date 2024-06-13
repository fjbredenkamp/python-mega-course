ranking = ['John', 'Sen', 'Lisa']  # Prompt the user to input a rank number and assign it to the variable 'rank'.

name = input("Enter person's name: ")

# Access the element in the ranking list based on the given rank and assign it to the variable 'name'.
rank = ranking.index(name) +1

# Print the name of the person who has the given rank.
print(rank)