# Function go here
def make_statement(statement, decoration):
    """Emphasizes headings by adding decoration at the start and end"""
    return f"{decoration * 3} {statement} {decoration * 3}"

main_heading_string = make_statement("Price Comparison Tool", "$")

to_write = [main_heading_string]

# Print area
print()
for item in to_write:
    print(item)

file_name = "make_statement_trial_3"
write_to = "{}.txt".format(file_name)

text_file = open(write_to, "w")

# Write the item to file
for item in to_write:
    text_file.write(item)
    text_file.write("\n")
text_file.close()