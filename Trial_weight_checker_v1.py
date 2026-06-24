# Function goes here
def weight_check(question):
    """Checks weight and converts to kg"""

    while True:
        error = "Please enter the weight of the item that more than 0, including units."
        response = input(question).lower()

        try:
            # kilograms
            if response[-2:] == "kg":
                weight = float(response[:-2])

            # grams
            elif response[-1:] == "g":
                weight = float(response[:-1]) / 1000

            else:
                print(error)
                continue

            if weight > 0:
                return weight

            else:
                print(error)

        except ValueError:
            print(error)

# Main routine
# Get item's weight
item_weight = weight_check("Item weight: ")
print(f"You entered {item_weight} kg")
