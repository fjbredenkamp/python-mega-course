def liters_to_m3(liters):
    cubic_meters = float(liters) * float(0.001)
    return cubic_meters


liters = input("Enter the number of liters: ")
result = liters_to_m3(liters)
print(result)
