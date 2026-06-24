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

def values(x, unit):
    """Formats values with units"""

    if unit == "$":
        return "${:.2f}".format(x)

    elif unit == "kg":
        return "{:.2f} kg".format(x)

    elif unit == "$ / kg":
        return "${:.2f} / kg".format(x)


# Main routine
amount_dollars = num_check("Enter a number use $: ")
amount_kg = num_check("Enter a number use kg: ")
amount_dollars_per_kg = num_check("Enter a number use $ / kg: ")

print(values(amount_dollars, unit="$"))
print(values(amount_kg, unit="kg"))
print(values(amount_dollars_per_kg, unit="$ / kg"))