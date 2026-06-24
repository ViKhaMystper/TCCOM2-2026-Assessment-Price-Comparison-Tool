# Function go here
def string_check(question, valid_ans_list):
    """Checks user enters first letter or whole word"""

    while True:

        response = input(question).lower()

        for item in valid_ans_list:

            if response == item or response == item[0]:
                return item

        print(f"Please choose an option from {valid_ans_list}")


# Main routine
colour_list = ["red", "blue", "green"]

colour = string_check("Choose a colour: ", colour_list)

print(f"You chose {colour}")