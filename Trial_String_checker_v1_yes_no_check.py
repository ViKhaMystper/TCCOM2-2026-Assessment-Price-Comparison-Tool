# Function go here
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

# Main routine goes here
Instruction = '''For this program, the user will enter their budget and 
a list of items to compare.

For each item, enter:
- The item name
- The price
- The weight (kg)

Once all items have been entered and the user enters 
the exit code "done", the program will then calculate 
the cost per kg ($ / kg) for each item and determine 
which item is the cheapest.

The program will also check if the item fits within 
the user's budget or not.

The program will display all items information, 
including $ / kg, recommend the cheapest item, and 
show the savings.

The results will also be written to a text file.
'''

# Instructions
want_instruction = yes_no_check("Do you want to read the instruction? ")
print()

if want_instruction == "yes":
    print(Instruction)