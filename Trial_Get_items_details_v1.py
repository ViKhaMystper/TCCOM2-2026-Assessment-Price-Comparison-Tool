# Function go here
def not_blank(question):
    """Check that a user response is not blank"""
    while True:
        response = input(question)

        if response != "":
            return response
        else:
            print("This cannot be blank. Please try again.")

def num_check(question, low = 0):
    """Check users enter a number > 0"""
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

def weight_check(question):
    """Checks weight and converts to kg"""

    while True:
        error = "Please enter the weight of the item that at least 100 mg, including units."
        response = input(question).lower().strip()

        try:
            # kilograms
            if response[-2:] == "kg":
                weight = float(response[:-2].strip())

            # milligrams
            elif response[-2:] == "mg":
                weight = float(response[:-2].strip()) / 1000000

            # millilitres
            elif response[-2:] == "ml":
                weight = float(response[:-2].strip()) / 1000

            # grams
            elif response[-1:] == "g":
                weight = float(response[:-1].strip()) / 1000

            # litres
            elif response[-1:] == "l":
                weight = float(response[:-1].strip())

            else:
                print(error)
                continue

            if weight >= 0.0001:
                return weight
            else:
                print("Weight is too small.")
                continue

        except ValueError:
            print(error)

def get_items_details():
    """Gets items details and outputs pandas (as a string)."""

    # Expenses dictionary
    while True:
        # Get items names
        item_name = not_blank("Item name: ")
        if item_name.lower() == "done":
            break
        print(f"You entered {item_name}")

        # Get item cost
        item_cost = num_check("Item cost: $")
        print(f"You entered ${item_cost}")

        # Get item's weight
        item_weight = weight_check("Item weight: ")
        print(f"You entered {item_weight} kg")

# Main routine start here
get_items_details()