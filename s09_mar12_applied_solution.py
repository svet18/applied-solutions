"""
The dataset contains:
    - Extra spaces at the beginning and end of rows
    - Extra spaces around values inside rows
    - Duplicate records
    - Missing values:
        blank cells
        question marks used instead of missing values
        сome text used instead of missing values
    - Inconsistent category labels:
        capitalization (upper/lower case mixed)
        same value written in different ways
        labels containing hyphens
        Yes/No values written in multiple formats
    - Numbers stored as text
    - Unclear meaning of labels
"""

data = """ LP001002 , Male , No ,0,Graduate ,No,5849 ,0, ,360 ,1,Urban ,Y
LP001003,Male,Yes,1 , graduate,No ,4583,1508,128 ,360,1 ,RURAL ,N
LP001005 ,Male ,Yes ,0,Graduate,Yes,3000,0,66,360,1,Urban,Y 
LP001006,Male,Yes,0,Not Graduate,No,2583,2358,120,360,1,urban ,Y
LP001008,Male,No,0,Graduate,No,6000,0,141,360,1,Urban ,Yes
LP001011,Male,Yes,2,Graduate,YES,5417,4196,267,360,1,Urban,Y 
LP001013,Male,Yes,0,Not graduate,No,2333,1516,95,360,1,Urban,Y
LP001014,Male,Yes,3 +,Graduate,No,3036,2504,158,360,0,Semi-Urban,N
LP001018,Male,Yes,2,Graduate,No,4006,1526,168,360,1,Urban,Y
LP001020,Male,Yes,1,Graduate,No,12841,10968,349,360,1,Semiurban,N
LP001020,Male,Yes,1,Graduate,No,12841,10968,349,360,1,Semiurban,N
LP001021,Female ,No,0,Graduate,No,NaN,0,120,360,1,Urban,Y
LP001022,,Yes,2,Graduate,No,3500,1800,110,360,1,Rural,Y
LP001023,Male,Yes,Two,Graduate,No,4500,0,?,360,1,Urban,Y
LP001024,Male,No,0,Graduate,No,5200,0,140,360,1,Urban,Y """


""" Data Cleaning Plan:

    1. Split data into rows w/o trailing spaces.
    2. Split each row into columns w/o trailing spaces.
    3. Replace missing data with None.
    4. Standardize labels:
        Yes/No labels
        Graduate/Not Graduate labels
        Area labels
    5. Make labels more descriptive:
        Change credit history to Good/Bad.
        Change loan status to Approved/Denied.
    6. Convert income variables to numeric.
    7. Remove duplicate rows & print one per line.
    8. Print # original rows, # cleaned rows.

"""


# 1. Split data into rows and trim trailing spaces
raw_rows = data.strip().split("\n")

# Create a list to store cleaned rows
cleaned_rows = []

# Loop through each raw row
for row in raw_rows:

    # 2. Split each row into columns using commas
    columns = row.split(",")

    # 3. Clean columns: remove extra spaces and replace missing values with None
    cleaned_columns = []
    missing_values = ["", "?", "nan", "na", "none", "null"]

    for column in columns:
        cleaned = column.strip()

        if cleaned.lower() in missing_values:
            cleaned = None

        cleaned_columns.append(cleaned)

    # 4. Standardize Yes/No labels

    loan_id, gender, married, dependents, education, \
        self_emp, app_income, co_income, loan_amt, term, \
        credit_hist, area, status = cleaned_columns

    if married is not None:
        if married.lower() in ["yes", "y"]:
            married = "Yes"
        else:
            married = "No"

    if self_emp is not None:
        if self_emp.lower() in ["yes", "y"]:
            self_emp = "Yes"
        else:
            self_emp = "No"

    # 5a. Standardize education labels
    if education is not None:
        if education.lower().replace("-", " ") == "graduate":
            education = "Graduate"
        else:
            education = "Not Graduate"

    # 5b. Standardize area labels
    if area is not None:
        area_clean = area.lower().replace("-", "").replace(" ", "")

        if area_clean == "urban":
            area = "Urban"
        elif area_clean == "rural":
            area = "Rural"
        else:
            area = "Semiurban"

    # 5c. Make labels more descriptive
    if credit_hist is not None:
        if credit_hist == "1":
            credit_hist = "Good"
        else:
            credit_hist = "Bad"

    if status is not None:
        if status.lower() in ["y", "yes"]:
            status = "Approved"
        else:
            status = "Denied"

    # 6. Convert income to numeric
    if app_income is not None:
        if app_income.isdigit():
            app_income = int(app_income)
        else:
            app_income = None

    if co_income is not None:
        if co_income.isdigit():
            co_income = int(co_income)
        else:
            co_income = None

    if loan_amt is not None:
        if loan_amt.isdigit():
            loan_amt = int(loan_amt)
        else:
            loan_amt = None

    if term is not None:
        if term.isdigit():
            term = int(term)
        else:
            term = None

    # Put the updated values back into a row
    cleaned_columns = [
        loan_id, gender, married, dependents, education,
        self_emp, app_income, co_income, loan_amt, term,
        credit_hist, area, status
    ]

    cleaned_rows.append(cleaned_columns)

# 7. Remove duplicate rows & print one per line.
unique_data = []

for row in cleaned_rows:
    if row not in unique_data:
        unique_data.append(row)
    print(row)

print(len(raw_rows))
print(len(unique_data))
