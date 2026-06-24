# Function go here
def num_check(question, low = 0, exit_code = "done"):
    """Check users enter a number > 0 or the exit code"""
    error = "Please enter a number more than 0."

    while True:

        response = input(question).lower()

        # check for the exit code and return it if entered
        if response.lower() == exit_code:
            return response

        # Check that number is more than 0
        try:
            response = float(response)

            if response > low:
                return response
            else:
                print(error)

        except ValueError:
            print(error)

def values(x):
    """Formats numbers as value $"""
    return "${:.2f}".format(x)

# Main routine
amount_dollars = num_check("How much is this cake costs? ")
print(f"This cake costs {values(amount_dollars)}")
