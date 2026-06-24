import pandas
from tabulate import tabulate
from datetime import date

# Function go here
def not_blank(question):
    """Check that a user response is not blank"""
    while True:
        response = input(question)

        if response != "":
            return response
        else:
            print("This cannot be blank. Please try again.")

def make_statement(statement, decoration):
    """Emphasizes headings by adding decoration at the start and end"""
    return f"{decoration * 3} {statement} {decoration * 3}"

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

def values(x, unit):
    """Formats values with units"""

    if unit == "$":
        return "${:.2f}".format(x)

    elif unit == "kg":
        return "{:.2f} kg".format(x)

    elif unit == "$ / kg":
        return "${:.2f} / kg".format(x)


def get_items_details(budget):
    """Gets items details and outputs pandas (as a string)."""

    # List for panda
    all_item = []
    all_cost = []
    all_weight = []
    all_dollars_per_kg = []

    # Create dictionary
    item_dict = {
        "Item": all_item,
        "Cost ($)": all_cost,
        "Weight (kg)": all_weight,
        "$ / kg": all_dollars_per_kg
    }

    # Loop to get items details
    while True:
        # Get items names
        item_name = not_blank("Item name: ")
        if item_name.lower() == "done":
            if not all_item:
                print("You must enter at least one item.")
                continue
            break

        print(f"You entered {item_name}")
        skip_item = False

        # Get item cost
        while True:
            item_cost = num_check("Item cost: $")

            if item_cost > budget:
                print(f"This item costs ${item_cost:.2f}, which is over your budget (${budget})!")

                choice = input("Please choose (1) re-enter price or (2) skip this item: ")

                if choice == "1":
                    continue

                elif choice == "2":
                    print("This item is eliminated\n")
                    skip_item = True
                    break

                else:
                    print("Please choose 1 or 2.\n")
                    continue

            else:
                print(f"You entered ${item_cost}")
                break

        # skip item → bỏ qua toàn bộ item này
        if skip_item:
            continue

        # Get item's weight
        item_weight = weight_check("Item weight: ")
        print(f"You entered {item_weight} kg")

        # Calculate cost per kg (STORE AS NUMBER)
        dollars_per_kg = item_cost / item_weight

        # lưu dữ liệu
        all_item.append(item_name)
        all_cost.append(item_cost)
        all_weight.append(item_weight)
        all_dollars_per_kg.append(dollars_per_kg)

    # Make pandas
    item_frame = pandas.DataFrame(item_dict)

    # Lưu bản số để tính toán (QUAN TRỌNG FIX)
    unit_price_list = all_dollars_per_kg

    # Format cho hiển thị
    item_frame["$ / kg"] = item_frame["$ / kg"].apply(values, unit="$ / kg")

    item_frame["Cost ($)"] = item_frame["Cost ($)"].apply(values, unit="$")

    item_frame["Weight (kg)"] = item_frame["Weight (kg)"].apply(values, unit="kg")

    # Format table
    item_string = tabulate(item_frame, headers='keys', tablefmt='psql', showindex=False)

    # Find cheapest item (DÙNG LIST SỐ)
    min_unit_price = min(unit_price_list)
    cheapest_idx = unit_price_list.index(min_unit_price)

    cheapest_dollar_per_kg = all_dollars_per_kg[cheapest_idx]
    cheapest_item = all_item[cheapest_idx]
    cheapest_cost = all_cost[cheapest_idx]

    return item_string, cheapest_item, cheapest_cost, cheapest_dollar_per_kg, item_dict

# Main routine
# Get budget
while True:
    budget = num_check("What is your budget?: $")

    if budget < 10:
        print("Your budget should be at least 10 dollars to buy something.")
    else:
        break

# Get item details
items_table = get_items_details(budget)