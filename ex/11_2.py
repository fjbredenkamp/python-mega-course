# Coding Exercise 2
# The get_max function you created in the previous exercise returned 9.7.
#
# In this exercise, you should:
#
# 1. change the function so this time it returns the following string:
#
# "Max: 9.7, Min: 9.2"
#
# where 9.7 is the maximum, and 9.2 is the minimum.
#
# Note: For the exercise to be marked as correct by the system,
# you should return the exact string "Max: 9.7, Min: 9.2"

def get_max():
    grades = [9.6, 9.2, 9.7]
    highest = max(grades)
    lowest = min(grades)
    high_low = f"Max: {highest}, Min: {lowest}"
    return high_low


highest_val = get_max()
print(highest_val)