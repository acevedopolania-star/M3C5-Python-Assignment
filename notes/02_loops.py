# --- Introduction to Python Loops ---
# Understanding the difference between 'for-in' and 'while' loops.

# 1. FOR-IN LOOP
# Best used when you have a collection of items (List, Tuple, Set).
# It iterates a specific number of times based on the collection size.
players = ['Altuve', 'Bregman', 'Correa']

print("--- For-In Loop Output ---")
for player in players:
    print(f"Current player: {player}")


# 2. WHILE LOOP
# Best used when the number of iterations is unknown and depends on a condition.
# WARNING: Always ensure the condition eventually becomes False to avoid infinite loops.
count = 0
print("\n--- While Loop Output ---")
while count < 3:
    print(f"Iteration count: {count}")
    count += 1  # Crucial: This updates the condition so the loop can end.

# Tip: In Python, prefer 'for-in' loops whenever possible 
# as they are more readable and less prone to errors (Infinite Loops).

# --- Iterating through Collections ---

# 1. Iterating over a List
# Best practice: Singular 'player' for plural 'players' list
players_list = ['Altuve', 'Bregman', 'Correa', 'Gattis']

print("\n--- List Iteration ---")
for player in players_list:
    print(f"Player name: {player}")

# 2. Iterating over a Tuple
# Works exactly the same as a list
players_tuple = ('Altuve', 'Bregman', 'Correa', 'Gattis')

print("\n--- Tuple Iteration ---")
for player in players_tuple:
    print(f"Player name (from tuple): {player}")

# 3. Iterating over a Dictionary
# We use .items() to unpack both the key (position) and the value (player)
players_dict = {
    '2b': 'Altuve',
    '3b': 'Bregman',
    'ss': 'Correa',
    'dh': 'Gattis'
}

print("\n--- Dictionary Iteration ---")
for position, player in players_dict.items():
    print(f"Position: {position}")
    print(f"Player: {player}")

# 4. Coding Exercise
def loop_over_list():
    my_list = ['football', 'soccer', 'baseball', 'basket', 'volley']
    for sport in my_list:
        print(sport)
    
    
    return my_list

# --- String Iteration ---
# Demonstrating that strings are treated as collections of characters.

alphabet = 'abcdef'

print("\n--- String Iteration ---")
for letter in alphabet:
    print(letter)

# This confirms that in Python, a string is an iterable object, 
# just like a list or a tuple.

# 1. Coding Exercise
def loop_over_string():
    name = "Manuela"
    for letters in name:
        print(letters)
        
    return name

# --- Looping Over Ranges ---
# Using the range() function to generate number sequences.

# 1. Basic Range (Stop is exclusive)
# This will print 1 to 9
print("\n--- Basic Range (1 to 10) ---")
for num in range(1, 10):
    print(f"Number: {num}")

# 2. Including the last number
# To include 10, we must set the stop at 11
print("\n--- Range including 10 ---")
for num in range(1, 11):
    print(f"Number: {num}")

# 3. Range with Step (Intervals)
# This will print every second value: 1, 3, 5, 7, 9
print("\n--- Range with Step (2) ---")
for num in range(1, 11, 2):
    print(f"Odd number: {num}")

# Practical Tip: range(5) is shorthand for range(0, 5)

# 4. Coding Exercise

def loop_over_range():
    # Write your code here
    for number in range(1, 11):
        print(number)