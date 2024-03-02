# Define the path of the input file
FILE = r'D:\Programmes\GitHub\clippings.txt'

# Function to parse the input file and return the data
def parse_input(file):
    with open(file) as f:
        datas = []
        for line in f:
            datas.append(line.strip())  # Remove leading and trailing spaces from each line
    return datas

# Parse the input file and store the data in the 'pairs' list
pairs = parse_input(FILE)

# Initialize a dictionary to store highlighted passages for each book
books = dict()

title = ""  # Initialize the variable to store the book title
divider = True  # Initialize the variable to detect separators between books

# Iterate through pairs (titles and highlighted passages)
for pair in pairs:
    if divider:
        title = pair
        divider = False
        continue

    if pair == "==========":
        divider = True
        continue

    if pair.startswith("- Your Highlight"):
        continue

    if pair == "":
        continue

    # Add the highlighted passage to the respective list for the book
    books[title] = books.get(title, []) + [pair]

# Function to format highlighted passages into a single string
def format_highlights(highlights):
    result = ""
    for highlight in highlights:
        result += highlight
        result += "\n\n---\n\n"

    return result

# Display the available books to the user
print("Available books:")

for i in range(0, len(books)):
    print(f"{i}: {list(books.keys())[i]}")

print("all: All books")

# Ask the user to input a book index
index = input("Enter a book index: ")

# If the user chooses "all", create Markdown files for all books
if index == "all":
    for book in books:
        with open(f"books/{book}.md", "w") as f:
            f.write(format_highlights(books.get(book)))
    exit()

# Retrieve the book selected by the user
selected_book = list(books.keys())[int(index)]
book_highlights = books.get(selected_book)

# Write to a file and create it if it doesn't exist
with open(f"books/{selected_book}.md", "w") as f:
    f.write(format_highlights(book_highlights))
