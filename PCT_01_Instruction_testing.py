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
the user's budget and saving goals, then calculate 
how much money can be saved.

The program will display all items information, 
including $ / kg, recommend the cheapest item, and 
show the savings.

The results will also be written to a text file.
''')

# Main routine goes here
print(make_statement("Price Comparison Tool", "💰"))
print()

# Instructions
want_instruction = yes_no_check("Do you want to read the instruction? ")
print()

if want_instruction == "yes":
    instruction()