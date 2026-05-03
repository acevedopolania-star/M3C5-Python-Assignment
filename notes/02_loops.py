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

# --- Loop Control Flow: Continue and Break ---

usernames = ['jon', 'tyrion', 'theon', 'cersei', 'sansa']

# 1. Example of CONTINUE
# It skips 'cersei' but keeps going with 'sansa'
print("\n--- Testing CONTINUE ---")
for username in usernames:
    if username == 'cersei':
        print(f"Sorry {username}, you are not allowed")
        continue
    print(f"{username} is allowed")

# 2. Example of BREAK
# It stops the entire loop once it finds 'cersei'
print("\n--- Testing BREAK ---")
for username in usernames:
    if username == 'cersei':
        idx = usernames.index(username)
        print(f"{username} was found at index {idx}. Stopping search.")
        break
    print(f"Checking: {username}")

# Note: Use 'break' to optimize performance when searching 
# through large datasets.

# 3. Coding Excersice
def loop_and_break():
    vegetables = ["onion", "broccoli", "apple", "spinach"]
    
    for veg in vegetables:
        if veg == 'apple':
            print(f'apple is not a vegetable')
            break
        print(veg)


# --- While Loops & Iterator (Sentinel) Values ---

# 1. Basic while loop using list length as sentinel
# We create a list from 1 to 99
numbers_list = list(range(1, 100))

print("\n--- Popping elements with while ---")
while len(numbers_list) > 0: #len comes from length, it counts the number of elements 
    # .pop() removes and returns the last element, decreasing the list length
    print(f"Removing: {numbers_list.pop()}")

# 2. Infinite-style while loop for a game
# This continues until the user provides the correct answer (the sentinel event)
def guessing_game():
    while True:
        print('What is your guess?')
        # input() pauses the program and waits for user text in the terminal
        guess = input()

        if guess == '42':
            print('You correctly guessed it!')
            # 'return False' or 'break' exits the loop and the function
            return False
        else:
            print(f"No, {guess} isn't the answer, please try again\n")

# To test the game, uncomment the line below:
# guessing_game()

#3. Coding Exercise

def loop_using_while():
    dog_house = ['Bobby', 'Teddy', 'Max', 'Clifford']
    
    counter = 0
    
    while counter < len(dog_house):
        print(dog_house[counter])
        counter += 1
    
    return [dog_house, counter]

# --- Merging and Flattening Lists with For Loops ---
# Combining elements from two different lists into one flat list.

legacy_customers = ['Alice', 'Bob']
new_customers = ['Tiffany', 'Kristine']

# WRONG WAY: This creates a nested list (a list of lists)
# raw_db = [legacy_customers, new_customers] 

# CORRECT WAY: Iterating and appending
# We take each individual customer from the legacy list...
for legacy_customer in legacy_customers:
    # ...and add them one by one to the new list
    new_customers.append(legacy_customer)

print("\n--- Combined Customer List ---")
print(new_customers)
# Output: ['Tiffany', 'Kristine', 'Alice', 'Bob']

# --- Practical Loop Exercise ---
# Correct alignment (Indentation)
numbers = [1, 2, 3, 4, 5]
result = []

for number in numbers:
    incremented_number = number + 1
    # Adding to the list MUST be inside the loop to catch every number
    result.append(incremented_number) 

print(f"Final result list: {result}")


# --- List Comprehensions ---
# Advanced one-line loops to generate lists.

num_list = range(1, 11)

# Example 1: Cubing numbers
# Structure: [expression for item in list]
cubed_nums = [num ** 3 for num in num_list]
print(f"\nCubed numbers (List Comp): {cubed_nums}")

# Example 2: Filtering even numbers (With a conditional)
# Structure: [expression for item in list if condition]
even_numbers = [num for num in num_list if num % 2 == 0]
print(f"Even numbers (List Comp): {even_numbers}")

# Note: List comprehensions are great for simple operations, 
# but for complex logic, a traditional for loop is often more readable.


# --- Removing First and Last Elements ---

def remove_first_and_last(list_to_clean):
    # Destructuring:
    # The underscores (_) are for elements we want to ignore
    # The asterisk (*) globs all elements in the middle into 'content'
    _, *content, _ = list_to_clean
    return content

# Test Cases
html = ['<h1>', 'Some content', '</h1>']
html_2 = ['<h1>', 'Some content', 'More content', '</h1>']

print(f"Cleaned 1: {remove_first_and_last(html)}")
# Output: ['Some content']

print(f"Cleaned 2: {remove_first_and_last(html_2)}")
# Output: ['Some content', 'More content']

# --- Pythonic way to slice a list ---
def remove_first_and_last(list_to_clean):
    # Using '_' is a convention for variables we plan to throw away
    _, *content, _ = list_to_clean
    return content

html = ['<h1>', 'My content', '</h1>']
print(remove_first_and_last(html))

other_content_to_clean = ['', 'My content', 'Something else', '/']
print(remove_first_and_last(other_content_to_clean))