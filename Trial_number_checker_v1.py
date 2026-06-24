# Function go here
def num_check(question, low=0, exit_code="done"):
    """Check users enter an integer > 0 or the exit code"""

    error = "Please enter an integer more than 0."

    while True:
        response = input(question).lower()

        # Check for exit code first
        if response == exit_code.lower():
            return exit_code

        try:
            value = int(response)

            if value > low:
                return value
            else:
                print(error)

        except ValueError:
            print(error)


# Main routine
banana = num_check("How many bananas do you want to buy?", exit_code="done")

if banana == "done":
    print("Order cancelled.")
else:
    print(f"You bought {banana} bananas.")