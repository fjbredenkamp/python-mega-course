# ex 1 & 2
password = input("Enter a new password: ")

if len(password) > 7:
    print("Great password there!")
elif len(password) == 7:
    print("Password is OK, but not too strong")
else:
    print("Your password is weak.")

# ex 3 - dict:
day_temperatures = {"morning": 9.0, "noon": 15.1, "evening": 18.2}
print(day_temperatures)

# ex 4 dict + tuple:
# Create a dictionary with temperature data
day_temperatures = {
    'morning': (10.5, 12.3, 11.0),
    'noon': (15.2, 16.8, 15.5),
    'evening': (8.7, 9.5, 8.9)
}

# Print the day_temperatures dictionary
print(day_temperatures)

# ex 5 & 6 & 7 - slices
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters[1:4])

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters[:3])

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters[4:])
