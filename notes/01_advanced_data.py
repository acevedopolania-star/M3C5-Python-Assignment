# --- Tuples as Dictionary Keys ---

# A dictionary where keys are Tuples (Level, Plan Name)
# This works because tuples are immutable.
priority_index = {
    (1, 'premier'): [1, 34, 12],
    (1, 'mvp'): [84, 22, 24],
    (2, 'standard'): [93, 81, 3],
}

# Accessing the keys (returns a list of tuples)
#We wrap it in a list() to convert the 'dict_keys' view into a usable list.
keys_list = list(priority_index.keys())

print("List of Keys (Tuples):")
print(keys_list)

# Direct Access Example:
# To retrieve the MVP package data, we use the exact tuple:
print(f"\nProducts in the MVP package: {priority_index[(1, 'mvp')]}")

# --- Python Zip Function ---
#Merging multiple lists into a collection of tuples using zip()

positions = ['2b', '3b', 'ss', 'dh']
players = ['Altuve', 'Bregman', 'Correa', 'Gattis']

# The zip function pairs elements from both lists based on their index.
# Example: positions[0] is paired with players[0]
scoreboard = zip(positions, players)

# We must cast the zip object into a list to view or manipulate the content.
# This results in a list of tuples: [('2b', 'Altuve'), ...]
scoreboard_list = list(scoreboard)

print("\n--- Scoreboard (Zipped Lists) ---")
print(scoreboard_list)

# Practical Use Case: 
# Zip is essential in data science for creating matrices or 
# preparing data for machine learning algorithms.

# --- Python Sets ---
# Working with Sets for uniqueness and membership testing

# Defining a set using curly braces (similar to dictionaries but without key-value pairs)
tags = {
    'python',
    'coding',
    'tutorials',
    'coding' # This duplicate will be automatically removed
}

print("\n--- Python Sets ---")
print(f"Set elements (notice no duplicates): {tags}")

# --- IMPORTANT: Indexing ---
# Sets do NOT support indexing. The following line would raise a TypeError:
# print(tags[0]) # -> 'set' object is not subscriptable

# --- Membership Testing (Queries) ---
# This is the most common use case for sets: checking if an element exists.

query_one = 'python' in tags
query_two = 'ruby' in tags

print(f"Is 'python' in tags? {query_one}") # Returns: True
print(f"Is 'ruby' in tags? {query_two}")   # Returns: False

# --- Python Set Operations (Merging & Comparisons) ---
# Advanced operations to merge and compare sets using Venn diagram logic.

tags_one = {
    'python',
    'coding',
    'tutorials',
    'coding'
}

tags_two = {
    'ruby',
    'coding',
    'tutorials',
    'development'
}

# 1. Merged Tags (Union)
# Uses the pipe character '|' to combine all unique elements from both sets.
merged_tags = tags_one | tags_two
print("\n--- Set Union (Merged) ---")
print(merged_tags)

# 2. Difference: Tags in tags_one but NOT in tags_two
# It "subtracts" the common elements from the first set.
exclusive_to_tag_one = tags_one - tags_two
print("\n--- Set Difference (Exclusive to Tag One) ---")
print(exclusive_to_tag_one) # Expected: {'python'}

# 3. Difference: Tags in tags_two but NOT in tags_one
exclusive_to_tag_two = tags_two - tags_one
print("\n--- Set Difference (Exclusive to Tag Two) ---")
print(exclusive_to_tag_two) # Expected: {'ruby', 'development'}

# 4. Intersection: Tags found in BOTH sets
# Uses the ampersand '&' to find shared elements.
universal_tags = tags_one & tags_two
print("\n--- Set Intersection (Shared Tags) ---")
print(universal_tags) # Expected: {'coding', 'tutorials'}