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


# Dataset specific column index constants
LOAN_ID = 0
GENDER = 1
MARRIED = 2
DEPENDENTS = 3
EDUCATION = 4
SELF_EMPLOYED = 5
APP_INCOME = 6
CO_INCOME = 7
LOAN_AMOUNT = 8
TERM = 9
CREDIT_HISTORY = 10
AREA = 11
LOAN_STATUS = 12


# Reusable constants
MISSING_VALUES = {"", "?", "nan", "na", "none", "null"}
YES_VALUES = {"yes", "y"}
NO_VALUES = {"no", "n"}


# Reusable UDFs
def get_rows(text_data):
    """Return a list of non-empty rows from a multiline string."""
    return text_data.strip().split("\n")


def split_and_strip_row(row):
    """Split a row on commas and strip extra spaces from each value."""
    
    values = row.split(",")

    clean_values = []
    for value in values:
        clean_values.append(value.strip())

    return clean_values
    
    #  More advanced way... using list comprehension:
    #   - what to produce
    #   - for each item
    #   - in the list
    # Logic: Give me cleaned values for each value in the list.
    # return [value.strip() for value in row.split(",")]

def clean_missing(value, missing_values=MISSING_VALUES):
    """Convert common missing-value markers to None."""
    if value is None:
        return None

    value = value.strip()
    if value.lower() in missing_values:
        return None
    return value


def standardize_yes_no(value):
    """Convert yes/no style values to 'Yes' or 'No'."""
    if value is None:
        return None

    value_clean = value.strip().lower()
    if value_clean in YES_VALUES:
        return "Yes"
    if value_clean in NO_VALUES:
        return "No"
    return value


def standardize_gender(value):
    """Standardize gender capitalization."""
    if value is None:
        return None
    return value.strip().title()


def standardize_dependents(value):
    """Standardize dependents values such as 'Two' and '3 +'."""
    if value is None:
        return None

    value_clean = value.strip().lower().replace(" ", "")

    if value_clean == "two":
        return "2"
    if value_clean in {"3+", "3plus"}:
        return "3+"
    return value.strip()


def standardize_education(value):
    """Standardize education labels."""
    if value is None:
        return None

    value_clean = value.strip().lower().replace("-", " ")
    if value_clean == "graduate":
        return "Graduate"
    if value_clean == "not graduate":
        return "Not Graduate"
    return value


def standardize_area(value):
    """Standardize property area labels."""
    if value is None:
        return None

    value_clean = value.strip().lower().replace("-", "").replace(" ", "")

    if value_clean == "urban":
        return "Urban"
    if value_clean == "rural":
        return "Rural"
    if value_clean == "semiurban":
        return "Semiurban"
    return value


def standardize_credit_history(value):
    """Convert credit history codes to descriptive labels."""
    if value is None:
        return None

    if value == "1":
        return "Good"
    if value == "0":
        return "Bad"
    return value


def standardize_loan_status(value):
    """Convert loan status codes to descriptive labels."""
    if value is None:
        return None

    value_clean = value.strip().lower()
    if value_clean in YES_VALUES:
        return "Approved"
    if value_clean in NO_VALUES:
        return "Denied"
    return value


def to_int_or_none(value):
    """Convert a value to int; return None if conversion fails."""
    if value is None:
        return None

    try:
        return int(value)
    except ValueError:
        return None


def remove_duplicates(rows):
    """Remove duplicate rows while keeping the first occurrence."""
    unique_rows = []
    seen = set()

    for row in rows:
        row_tuple = tuple(row)
        if row_tuple not in seen:
            seen.add(row_tuple)
            unique_rows.append(row)

    return unique_rows


def clean_row(columns):
    """Clean one row of loan data."""
    # Step 1: convert missing values
    row = [clean_missing(value) for value in columns]

    # Step 2: standardize selected columns
    row[GENDER] = standardize_gender(row[GENDER])
    row[MARRIED] = standardize_yes_no(row[MARRIED])
    row[DEPENDENTS] = standardize_dependents(row[DEPENDENTS])
    row[EDUCATION] = standardize_education(row[EDUCATION])
    row[SELF_EMPLOYED] = standardize_yes_no(row[SELF_EMPLOYED])
    row[AREA] = standardize_area(row[AREA])
    row[CREDIT_HISTORY] = standardize_credit_history(row[CREDIT_HISTORY])
    row[LOAN_STATUS] = standardize_loan_status(row[LOAN_STATUS])

    # Step 3: convert numeric columns
    for index in [APP_INCOME, CO_INCOME, LOAN_AMOUNT, TERM]:
        row[index] = to_int_or_none(row[index])

    return row


def clean_dataset(text_data):
    """Clean the full dataset."""
    rows = get_rows(text_data)
    cleaned_rows = []

    for row in rows:
        columns = split_and_strip_row(row)
        cleaned_row = clean_row(columns)
        cleaned_rows.append(cleaned_row)

    cleaned_rows = remove_duplicates(cleaned_rows)

    return rows, cleaned_rows


# Run the cleaning process
original_rows, cleaned_data = clean_dataset(data)

for row in cleaned_data:
    print(row)

print()
print("Original rows:", len(original_rows))
print("Cleaned rows:", len(cleaned_data))