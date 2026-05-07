# --- FizzBuzz Challenge Implementation ---

def fizz_buzz(max_value):
    # Using range(1, max_value + 1) to include the max_value
    for num in range(1, max_value + 1):
        # 1. Check for both first (Multiples of 3 AND 5)
        if num % 3 == 0 and num % 5 == 0:
            print('FizzBuzz')
        # 2. Check for multiples of 3
        elif num % 3 == 0:
            print('Fizz')
        # 3. Check for multiples of 5
        elif num % 5 == 0:
            print('Buzz')
        # 4. If not a multiple of 3 or 5, print the number
        else:
            print(num)

# Call the function with 100 as requested
fizz_buzz(100)