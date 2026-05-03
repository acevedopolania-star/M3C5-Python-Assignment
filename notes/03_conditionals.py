# --- Introduction to Conditionals ---
# Basic structure of decision making in Python.

user_status = 'active'
is_authorized = True

print("--- Authentication System ---")

# The most basic conditional
if is_authorized:
    # This block only runs if is_authorized is True
    print("Welcome to the site!")
else:
    # This block runs if is_authorized is False
    print("Access Denied. Please log in.")

# A more dynamic example using multiple conditions
if user_status == 'active':
    print("Your account is in good standing.")
elif user_status == 'suspended':
    print("Your account is suspended. Contact support.")
else:
    print("User status unknown.")


# --- Python Conditionals: If / Elif / Else ---
# Implementing age verification logic.

age = 50

print(f"--- Car Rental Verification for age: {age} ---")

if age < 25:
    # Condition 1: Too young
    print(f"I'm sorry, {age} is under 25 years old. You cannot rent.")
elif age > 100:
    # Condition 2: Too old
    print(f"I'm sorry, {age} is over 100 years old. Safety first!")
else:
    # Default: Fits the range (25-100)
    print(f"You're good to go! {age} fits in the allowed range.")

# Remember: Python checks these in order. 
# As soon as it finds a TRUE condition, it stops checking the rest.


# --- Ternary Operator ---
# One-line conditionals for simple assignments.

role = 'admin'

# Traditional way (4 lines)
if role == 'admin':
    auth = 'can access'
else:
    auth = 'cannot access'

# Ternary way (1 line)
# Reading: "Assign 'can access' IF role is admin, ELSE assign 'cannot access'"
auth_ternary = 'can access' if role == 'admin' else 'cannot access'

print(f"--- Authorization Result ---")
print(f"Standard method: {auth}")
print(f"Ternary method: {auth_ternary}")

# Tip: Use this only for simple logic to keep your code clean!


# --- Full List of Comparison Operators ---

# List of comparison operators
# == Equality
# != Inequality
# <> Inequality (deprecated)
# >  Greater than
# >= Greater than or equal to
# < Less than
# <= Less than or equal to

# 1. Equality and Inequality (Strings & Numbers)
username = 'jonsnow'
if username != 'admin':
    print("Warning: Standard user detected.")

# 2. Range Comparisons (Numbers)
age = 25
if age >= 18:
    print("Eligible for a driver's license.")
else:
    print("Too young to drive.")

# 3. List Comparison (Comparing Collections)
# Python compares every element in the list
list_one = [1, 2, 3]
list_two = [1, 2, 3]

if list_one == list_two:
    print("The lists are identical.")

# 4. Deprecated Operator (DON'T USE: <>)
# Just for your knowledge if you see it in old code:
# if age <> 25:  <-- This means age != 25


# --- Membership Operator: 'in' ---

# 1. Searching in Strings (Case Sensitive!)
sentence = 'The quick brown fox jumped over the lazy Dog'
word = 'dog'

# Tip: Use .lower() to make the search case-insensitive
if word.lower() in sentence.lower():
    print(f"Success: '{word}' was found in the sentence.")
else:
    print(f"Error: '{word}' not found.")

# 2. Searching in Lists
authorized_users = ['alice', 'bob', 'manuela']
user_to_check = 'manuela'

if user_to_check in authorized_users:
    print(f"Access Granted for {user_to_check}!")
else:
    print("Access Denied.")


# --- Compound Conditionals (and, or, not) ---

username = 'jonsnow'
email = 'jon@snow.com'
password = 'thenorth'

# 1. Using 'and' (Strict)
if username == 'jonsnow' and password == 'thenorth':
    print("Login successful!")

# 2. Using 'or' with parenthesis (Flexible login)
# This allows either username OR email, but ALWAYS requires the password
if (username == 'jonsnow' or email == 'jon@snow.com') and password == 'thenorth':
    print("Access permitted via username or email.")

# 3. Using 'not' (The inverter)
is_admin = False
is_logged_in = True

# Logical check: Is the user logged in AND NOT an admin?
if is_logged_in and not is_admin:
    print("Welcome, standard user. You cannot see the admin panel.")