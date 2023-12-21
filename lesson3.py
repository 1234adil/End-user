# Write a program that repeatedly prompts a user for integer
# numbers until the user enters 'done'.
# Once 'done' is entered, print out the largest and smallest of the numbers.
# If the user enters anything other than a valid number catch it with a try/except and
# put out an appropriate message and ignore the number.
# Enter 7, 2, bob, 10, and 4 and match the output below.

largest = None
smallest = None

while True:
    user_input = input("Enter an integer number or 'done' to finish: ")

    if user_input.lower() == 'done':
        break  # Exit the loop if user enters 'done'

    try:
        number = int(user_input)  # Convert input to an integer
        # Check for the largest number
        if largest is None or number > largest:
            largest = number
        # Check for the smallest number
        if smallest is None or number < smallest:
            smallest = number
    except ValueError:
        print("Invalid input")
        continue  # Skip to the next iteration if input is not an integer

if largest is not None and smallest is not None:
    print(f"Maximum is {largest}")
    print(f"Minimum is {smallest}")
else:
    print("No valid numbers were entered.")
