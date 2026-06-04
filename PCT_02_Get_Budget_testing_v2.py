def num_check(question, low = 0):
    """Check users enter a number > 0 or the exit code"""
    error = "Please enter a number."

    while True:

        response = input(question).lower()
        # Check that number is more than 0
        try:
            value = float(response)

            if value > low:
                return value
            else:
                print(error)

        except ValueError:
            print(error)

# Main routine goes here

# Get budget detail
while True:
    budget = num_check("What is your budget?: $")

    if budget < 10:
        print("Your budget should be at least 10 dollars to buy something.")
    else:
        break

print(f"Budget accepted: ${budget}")
