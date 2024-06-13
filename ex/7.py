# Comments
#
# Use a # in front of a line to explain code or add notes
#
# Crtl / is for block commenting multiple lines
# 1.
# Extend the given code (in the exercise area) so the code capitalizes all the names and surnames of the list and then prints the new list.
# The output of your code should be as below:
#
# ['John Smith', 'Jay Santi', 'Eva Kuki']
names = ["john smith", "jay santi", "eva kuki"]
new_name = [name.title() for name in names]
print(new_name)
# 2.
# Extend the given code so the code prints out a list containing the number of characters for each username.
#
# The output of your code should be as below:
#
# [9, 11, 11]
usernames = ["john 1990", "alberta1970", "magnola2000"]
num_chars = [len(username) for username in usernames]
print(num_chars)
# 3.
# Extend the given code so the code prints out a list containing the same items as floats.
#
# The output of your code should be as below:
#
# [10.0, 19.1, 20.0]
user_entries = ['10', '19.1', '20']
floats = [float(user_entry) for user_entry in user_entries]
print(floats)
# 4.
# Extend the given code so it prints out the sum of the numbers.
#
# The output of your code should be as below:
#
# 49.1
user_entries = ['10', '19.1', '20']
floats = [float(user_entry) for user_entry in user_entries]
print(sum(floats))
