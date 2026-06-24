# Function go here
def num_check(question, low = 0):
    """Check users enter a number > 0"""
    error = "Please enter a number more than 0."

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

# Main routine
budget = num_check("What is your budget?: $")
print(f"Your budget is ${budget}.")