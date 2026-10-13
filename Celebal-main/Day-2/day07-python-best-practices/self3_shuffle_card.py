# Self Practice 3: Shuffle Card
import random

card_points = ['A', 'K', 'Q', 'J', '2', '3', '4',
               '5', '6', '7', '8', '9', '10']

card_signs = ['HEART', 'CLUB', 'DIAMOND', 'SPADE']

# Create the deck of 52 cards
cards = []

for sign in card_signs:
    for point in card_points:
        cards.append(f"{sign}-{point}")

# Display the initial deck
print("Initial Deck:")
for position, card in enumerate(cards, start=1):
    print(f"Position {position}: {card}")

# Find the initial positions of all Kings
king_positions = [
    position
    for position, card in enumerate(cards, start=1)
    if card.endswith("-K")
]

print("\nInitial positions of all Kings:")
print(king_positions)

# Shuffle the deck
random.shuffle(cards)

# Display the shuffled deck
print("\nShuffled Deck:")
for position, card in enumerate(cards, start=1):
    print(f"Position {position}: {card}")

# Find the new positions of all Kings
king_positions = [
    position
    for position, card in enumerate(cards, start=1)
    if card.endswith("-K")
]

print("\nShuffled positions of all Kings:")
print(king_positions)