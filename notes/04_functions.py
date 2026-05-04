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

# --- Introduction to Functions ---
# File: 05_functions.py

# 1. DEFINING the function (The Machine)
def predict_price(square_footage, neighborhood):
    """
    This is where the 'magic' happens. 
    Imagine 50 lines of complex math here.
    """
    # Simple placeholder logic
    price = square_footage * 200 
    if neighborhood == 'downtown':
        price += 50000
        
    return price

# 2. CALLING the function (Using the Machine)
house_one = predict_price(1500, 'downtown')
house_two = predict_price(2000, 'suburbs')

print(f"House 1 Price: ${house_one}")
print(f"House 2 Price: ${house_two}")


# --- Basic Function Syntax ---

# 1. Function with arguments (The Full Name Machine)
def full_name(first, last):
    print(f"{first} {last}")

# Calling it
full_name('Manuela', 'Acevedo')


# 2. Function with internal logic (The Auth Machine)
def auth(email, password):
    if email == 'manuela@test.com' and password == 'secret123':
        print("Authorized access")
    else:
        print("Access denied")

auth('manuela@test.com', 'secret123')


# 3. Function with loops (The Counter Machine)
def counter(max_value):
    for num in range(1, max_value + 1):
        print(num)

# This will count from 1 to 10
counter(10)


# --- Return vs Print ---

def funcion_con_print(a, b):
    print(a + b)  # Solo lo muestra en la terminal

def funcion_con_return(a, b):
    return a + b  # Entrega el resultado para ser usado

# CASO 1: Intentar guardar un print
resultado_print = funcion_con_print(5, 5)
print(f"Lo que guardó el print: {resultado_print}") 
# Imprimirá: None (porque el print no "entrega" nada, solo "avisa")

# CASO 2: Guardar un return
resultado_return = funcion_con_return(5, 5)
print(f"Lo que guardó el return: {resultado_return}") 
# Imprimirá: 10 (porque el return entregó el valor y lo pudimos guardar)


# --- Nested Functions ---

def greeting(first, last):
    # Esta función vive SOLO aquí dentro
    def full_name():
        return f"{first} {last}"

    # Llamamos a la función interna dentro del print
    print(f"Hi {full_name()}!")

# Ejecución
greeting('Manuela', 'Acevedo')

# Si intentara llamar a full_name() aquí afuera, Python te daría un Error.