# Store raw data in a text block
data = """LP001002,Male,No,0,Graduate,No,5849,0,,360,1,Urban,Y
LP001003,Male,Yes,1,Graduate,No,4583,1508,128,360,1,Rural,N
LP001005,Male,Yes,0,Graduate,Yes,3000,0,66,360,1,Urban,Y
LP001006,Male,Yes,0,Not Graduate,No,2583,2358,120,360,1,Urban,Y
LP001008,Male,No,0,Graduate,No,6000,0,141,360,1,Urban,Y
LP001011,Male,Yes,2,Graduate,Yes,5417,4196,267,360,1,Urban,Y
LP001013,Male,Yes,0,Not Graduate,No,2333,1516,95,360,1,Urban,Y
LP001014,Male,Yes,3+,Graduate,No,3036,2504,158,360,0,Semiurban,N
LP001018,Male,Yes,2,Graduate,No,4006,1526,168,360,1,Urban,Y
LP001020,Male,Yes,1,Graduate,No,12841,10968,349,360,1,Semiurban,N"""

# Verify that Python sees it as a big chunk of text (string)
print("\n ------- Verify that data is string: ", type(data))

# Break the string into a list, where each item is a row.
# Verify that it is a list.
rows = data.split("\n")
print("\n ------- Verify that data are split into rows and rows is a list: ", type(rows))

# ------------------------------
# Misc practice
# ------------------------------
# Print row 10 of data
row10 = rows[9]
print("\n ------- Print row 10 from the list: \n")
print(row10)

# Verify that each row in the list of rows is a string
print("\n ------- Verify that a row is a string: ", type(row10))

# Loop through the items on the list & extract them
print("\n ------- Loop through list items (rows) and print them with a blank line: \n")
for row in rows:
    print(row, "\n")

# Access items on the list using index numbers
print("------- Access list items using indenx number: \n")
print("Row 1: ", rows[0], "\n")

# ------------------------------
# Solution begins here
# ------------------------------

# Start processing rows...
# At this point each row is an item (a string) in the list "rows"
# We need to convert it into its own list 
# by splitting it into columns w/comma as a delimiter
# Then we want to add all split rows together into a new list (split_rows)

# First, create an empty list that will hold split rows
split_rows = []

# Then, loop through each row in the list of rows
for row in rows:
    # split it into columns/fields
    columns = row.split(",")
    # add the split row to the end of the list of split rows
    split_rows.append(columns)

# Verify that you have a new list of split rows
print("\n Verify creating a list of split rows: \n")
print(split_rows, "\n")

# Extract loan status values and put them in a separate list

# First, create an empty list to hold loan status values
loan_status = []

# Then, loop through each row inthe list of split rows &
for row in split_rows:
    # access the loan status column by its index number [-1]
    # and add it to the end of the loan_status list
    loan_status.append(row[-1])

# Verify that you have a loan status list
print("\n Verify the loan status list: \n")
print(loan_status)