# The following get_maximum function is designed to return the maximum
# value of the celsius list, while the last two lines of the code will
# convert the Celsius value to Fahrenheit and print it out.

# def get_maximum():
#     celsius = [14, 15.1, 12.3]
#     maximum = max(celsius)
#     print(maximum)
#
#
# celsius = get_maximum()
# fahrenheit = celsius * 1.8 + 32
#
# print(fahrenheit)

def get_maximum():
    celsius = [14, 15.1, 12.3]
    maximum = max(celsius)
    return maximum


celsius = get_maximum()
fahrenheit = celsius * 1.8 + 32

print(fahrenheit)
