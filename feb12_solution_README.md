### Step 1 — Store raw data

The dataset is saved as one large multi-line string.

        data = """ row1
        row2
        row3 """

At this point Python sees the data as one big piece of text.

### Step 2 — Split text into rows at every line break
    rows = data.split("\n")

Result:

    rows = ["row1", "row2", "row3", ...]

Now Python recognizes individual records.

### Step 3 — Prepare the dataset container (an empty list)

        split_rows = []

Create an empty list to store processed rows. Think of this as creating an empty table.

### Step 4 — Loop through each row in the list of rows

        for row in rows:

Python processes the dataset one row at a time.

### Step 5 — Split each row into columns

Each row is split at commas. 

        for row in rows:
            columns = row.split(",")

Example transformation (verify with print()):

        "LP001002,Male,No" ==>
        ["LP001002","Male","No"]

Now each row is split into individual fields/columns. Each row is a list.

### Step 6 — Append each split row to the dataset (add to the end after each loop)
    
    for row in rows:
            columns = row.split(",")
            split_rows.append(columns)

Each time the loop runs, the current row (already split into its column values) is added to the end of the list called split_rows.

This repeats for every row until the list contains all rows of the dataset, where each row is stored as its own list of column values.

The finished dataset looks like this (verify with print()):

    split_rows = [
    ['LP001002','Male','No',...],
    ['LP001003','Male','Yes',...],
    ['LP001005','Male','Yes',...]
    ]

This structure is called a list of lists (2D list) and behaves like a table/dataset, with rows and columns.

### Step 7 — Extract the Loan Status column into its own list

Now that the data are structured as a list of lists, we can pull out one column of interest and make it its own list, containing only the Loan Status values (the last value in each row).

First, we create an empty list to store the loan status values:

        loan_status = []

Next, we loop through each split row in the dataset, access the last item in that row and add it to the end of the loan_status list:

        for row in split_rows:
                loan_status.append(row[-1])

row[-1] means the last value in the split row, which is the Loan Status (Y or N).

Each time the loop runs, the Loan Status value is added to the end of the loan_status list.

This repeats until all split rows have been processed.

The finished list looks like this (verify with print()):

        loan_status = ['Y','N','Y','Y','Y','Y','Y','N','Y','N']


