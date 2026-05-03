# --- HTML Heading Generator ---
# Function that generates dynamic HTML headings using f-strings.

def heading_generator(title, heading_type):
  return f'<h{heading_type}>{title}</h{heading_type}>'
  
# --- Testing the Function ---

# Generate an H1 tag
print("--- H1 Generation ---")
print(heading_generator('Greetings!', '1'))

# Generate an H3 tag
print("\n--- H3 Generation ---")
print(heading_generator('I am in a title', '3'))

# Practical use case: Generating web content dynamically