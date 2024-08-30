# Get user's name
name = input("Enter your name: ")

# Get user's favorite numbers
num1 = int(input("Enter your first favorite number: "))
num2 = int(input("Enter your second favorite number: "))
num3 = int(input("Enter your third favorite number: "))

# Message for user 
print(f"\nHello, {name}! Let's explore your favorite numbers:")

# Check if each number is even or odd, and display squares
if num1 % 2 == 0:
    print(f"The number {num1} is even.")
else:
    print(f"The number {num1} is odd.")
print(f"The number {num1} and its square: ({num1}, {num1 ** 2})")

if num2 % 2 == 0:
    print(f"The number {num2} is even.")
else:
    print(f"The number {num2} is odd.")
print(f"The number {num2} and its square: ({num2}, {num2 ** 2})")

if num3 % 2 == 0:
    print(f"The number {num3} is even.")
else:
    print(f"The number {num3} is odd.")
print(f"The number {num3} and its square: ({num3}, {num3 ** 2})")

# Calculate the sum of the numbers
total_sum = num1 + num2 + num3
print(f"\nAmazing! The sum of your favorite numbers is: {total_sum}")

# Check if the sum is a prime number
if total_sum < 2:
    is_prime = False
else:
    is_prime = True
    for i in range(2, int(total_sum **2) ):
        if total_sum % i == 0:
            is_prime = False
            break

if is_prime:
    print(f"Wow, {total_sum} is a prime number!")
else:
    print(f"{total_sum} is not a prime number.")