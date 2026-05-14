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

# Main routine goes here

# Get budget detail
budget = num_check("What is your budget?: $")