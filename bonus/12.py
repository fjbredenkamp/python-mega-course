# Decoupling
feet_inches = input("Enter feet in inches: ")

def convert(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])

    meters = feet * 0.3048 + inches * 0.0254
    # too many things returned to re-use in another area of a program. ideally return only 1 thing
    # see decoupled below
    return f"{feet} feet and {inches} inches is equal to {meters} meters."


print(convert(feet_inches))

def convert_to_meters(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])

    meters = feet * 0.3048 + inches * 0.0254
    #decoupled:
    return meters


result = convert_to_meters(feet_inches)

if result < 1.6:
    print("Minimum height is 1.6m. Kid is too small.")
else:
    print("Kid can use the slide.")
