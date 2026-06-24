# Function go here
def num_check(question, low=0, exit_code="done"):
    """Check users enter a number > 0 or the exit code"""

    error = "Please enter a number more than 0."

    while True:
        response = input(question).lower()

        # Check for exit code first
        if response == exit_code.lower():
            return exit_code

        try:
            value = float(response)

            if value > low:
                return value
            else:
                print(error)

        except ValueError:
            print(error)


# Main routine
cost = num_check("How much does this book cost?: $", exit_code="done")

if cost == "done":
    print("Order cancelled.")
else:
    print(f"It costs ${cost}.")