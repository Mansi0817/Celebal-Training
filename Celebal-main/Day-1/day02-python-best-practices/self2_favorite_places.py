# Self Practice 2: Favorite Places

places = []
for place_number in range(1, 6):
    place = input(f"Enter favorite place {place_number}: ").strip()
    places.append(place)

print("My Favorite Places are", end=" ")
print(*places, sep=", ")

print("\nMy Favorite Places are")
print(*places, sep="\n\n")
