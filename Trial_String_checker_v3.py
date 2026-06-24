# Function go here
def string_checker(question, valid_ans_list, num_letters):
    """Checks user enters first n letters or whole word"""

    while True:

        response = input(question).lower()

        for item in valid_ans_list:

            if response == item or response == item[:num_letters]:
                return item

        print(f"Please choose an option from {valid_ans_list}")


# Main routine
drink_list = ["coke", "pepsi", "water", "tea", "coffe"]

drink = string_checker("What would you like to drink?: ", drink_list, 3)

print(f"You chose {drink}")