# Function go here
def make_statement( statement, decoration, lines):
    """Creates headings (3 lines), subheadings (2 times) and emphasis text / mini
    headings (1 line). Only use emoji for single line statements."""

    middle = f"{decoration * 3} {statement} {decoration * 3}"
    top_bottom = decoration * len(middle)
    if lines == 1:
        print(middle)
    elif lines == 2:
        print(middle)
        print(top_bottom)
    else:
        print(top_bottom)
        print(middle)
        print(top_bottom)


# main routine goes here
make_statement( "Price Comparison Tool","💰", 1)
print()
make_statement("Price Comparison Tool", "🪙", 2)
print()
make_statement("Price Comparison Tool", "🤑", 3)
print()