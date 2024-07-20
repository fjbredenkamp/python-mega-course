def ounces_to_millimeters(ounces):
    millimeters = float(ounces) * float(29.57353)
    return millimeters


ounces = input("Enter ounces: ")
foo = ounces_to_millimeters(ounces)
print(f"Number of ml: {foo}")
