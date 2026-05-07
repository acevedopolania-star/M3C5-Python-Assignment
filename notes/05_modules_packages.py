# --- Working with Modules and Packages ---
# File: 05_modules_packages.py

# 1. Standard Library Import
import math

# 2. Using an Alias (Very common in Data Science/ADE)
import datetime as dt

# 3. Specific Import (Only what you need)
from os import path

# Using the Alias
current_date = dt.datetime.now()

# Using the Specific Import (no need to type os.path.exists)
file_exists = path.exists('05_modules_packages.py')

print(f"Today is: {current_date}")
print(f"Is this file here? {file_exists}")

# GOOD PRACTICE: Always place imports at the top of the file.
# BAD PRACTICE: 'from math import *' (This imports everything and can cause naming conflicts).

# --- Advanced Module Importing ---

import sys

# 1. Adding a custom directory to the Python path
# This tells Python: "Look inside the 'libs' folder too"
# (0) means it's the first place Python will look.
sys.path.insert(0, './libs')

# 2. Now we can import our custom module even if it's inside a folder
# Note: You need to create a folder 'libs' and a file 'helper.py' to test this.
try:
    import helper
    print("Helper module imported successfully from ./libs")
except ModuleNotFoundError:
    print("Note: Create a './libs/helper.py' file to see this in action.")

def render_page():
    """Example of using an imported function from a subfolder."""
    # This assumes helper.py has a greeting function
    # print(helper.greeting('Manuela', 'Acevedo'))
    pass

# BEST PRACTICE: Use relative paths like './libs' to keep the code portable.
# GOOD PRACTICE: Only insert paths at the very beginning of your main script.


# --- Specific Function Imports ---

import sys
sys.path.insert(0, './libs')

# 1. Importing only what we need
# Instead of 'import helper', we target the function
from helper import greeting

# 2. Cleaner usage
# We no longer need 'helper.greeting()'
def display_user():
    """Renders a greeting using a specific import."""
    print(greeting('Manuela', 'Acevedo'))

# 3. Using the standard library the same way
from math import sqrt, ceil

print(f"Direct square root: {sqrt(25)}")
print(f"Direct ceiling value: {ceil(4.2)}")

# BEST PRACTICE: Only import the functions you actually use.
# GOOD PRACTICE: This avoids 'namespace pollution' (filling your file with unused names).