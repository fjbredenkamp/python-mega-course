date = input("Enter today's date(ex 2024-05-31): ")
mood = input("Rate your mood today from 1 to 10: ")
thoughts = input("Let your thoughts flow:\n")

with open(f"journal/{date}.txt", "w") as file:
    file.write(f"Mood rating: {mood}" + 2 * "\n")
    file.write(thoughts)
