import pandas
from tabulate import tabulate
from datetime import date

# Function go here
def make_statement(statement, decoration):
    """Emphasizes headings by adding decoration at the start and end"""
    return f"{decoration * 3} {statement} {decoration * 3}"

def yes_no_check(question):
    """Check user enter yes / y or no / n"""
    while True:
        response = input(question).lower()
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes (y) or no (n). \n")

def instruction():
    print(make_statement("Instruction", "ℹ️"))
    print()

    print('''For this program, the user will enter their budget and 
a list of items to compare.

For each item, enter:
- The item name
- The price
- The weight (kg)

Once all items have been entered and the user enters 
the exit code "done", the program will then calculate 
the cost per kg ($ / kg) for each item and determine 
which item is the best.

The program will also check if the item fits within 
the user's budget or not.

The program will display all items information, 
including $ / kg, recommend the cheapest item, and 
show the savings.

The results will also be written to a text file.
''')


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


# Main routine goes here
print(make_statement("Price Comparison Tool", "💰"))
print()

# Instructions
want_instruction = yes_no_check("Do you want to read the instruction? ")
if want_instruction == "yes":
    instruction()
print()

# Main routine

# Get budget
while True:
    budget = num_check("What is your budget?: $")

    if budget < 10:
        print("Your budget should be at least 10 dollars to buy something.")
    else:
        break

# Get item details
items_table, cheapest_item, cheapest_cost, cheapest_dollar_per_kg, item_dict = get_items_details(budget)

# Recommendation
# Calculate savings
remain_money = budget - cheapest_cost
# Create output string
recommendation_string = (
    f"Best choice: {cheapest_item} - "
    f"${cheapest_cost:.2f} (${cheapest_dollar_per_kg:.2f} / kg)\n"
    f"Budget remain: ${remain_money:.2f}")


# String output here
# Get current date for heading and file name
today = date.today()

# Get day, month and year as individual strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%Y")


# Headings / strings
main_heading_string = make_statement(f"Price Comparison Tool "
                                     f"({day}/ {month}/ {year})", "=")

item_heading_string = "--- Item Details ---"
recommendation_heading_string = "--- Recommendation ---"

# List of strings to be outputted / written to file
to_write = [
    main_heading_string,
    "",
    item_heading_string,
    items_table,
    "",
    recommendation_heading_string,
    recommendation_string
]


# Print area
print()
for item in to_write:
    print(item)

# Ask user to enter file name
enter_file_name = input("Enter file name: ")

if (enter_file_name.lower() == ""
        or enter_file_name.lower() == "none"
        or enter_file_name.lower() == "no"
        or enter_file_name.lower() == "done"):
    file_name = f"PCT_{day}_{month}_{year}"

else:
    file_name = f"{enter_file_name}_{day}_{month}_{year}"

# Create file to hold data
write_to = "{}.txt".format(file_name)
text_file = open(write_to, "w")

# Write items to file
for item in to_write:
    text_file.write(item)
    text_file.write("\n")