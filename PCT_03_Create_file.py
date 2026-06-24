from datetime import date

# Function go here
def make_statement(statement, decoration):
    """Emphasizes headings by adding decoration at the start and end"""
    return f"{decoration * 3} {statement} {decoration * 3}"

def not_blank(question):
    """Check that a user response is not blank"""
    while True:
        response = input(question)

        if response != "":
            return response
        else:
            print("This cannot be blank. Please try again.")


# Main routine
# Get current date for heading and file name
today = date.today()

# Get day, month and year as individual strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%Y")


# Headings / strings
main_heading_string = make_statement(f"Create file testing"
                                     f"({day}/ {month}/ {year})", "=")
print()
print(main_heading_string)
print()

# Ask the question
Question = not_blank("What is your name? ")
Answer = f"Hi {Question}!"
print(Answer)
print()

# List of strings to be outputted / written to file
to_write = [
    main_heading_string,
    Answer
]

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