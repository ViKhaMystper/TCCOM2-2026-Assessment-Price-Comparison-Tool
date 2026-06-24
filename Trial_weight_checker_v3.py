# Function goes here
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

# Main routine
# Get item's weight
item_weight = weight_check("Item weight: ")
print(f"You entered {item_weight} kg")