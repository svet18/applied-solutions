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
LP001024,Male,No,0,Graduate,No,5200,0,140,three sixty,1,Urban,Y """


# 1. Clean one value: remove spaces and replace missing values with None.
def clean_missing(value):
    value = value.strip()
    missing_values = ["", "?", "nan", "na", "none", "null"]

    if value.lower() in missing_values:
        return None
    else:
        return value


# 2. Standardize Yes/No values.
def clean_yes_no(value):
    if value is not None:
        if value.lower() in ["yes", "y"]:
            return "Yes"
        else:
            return "No"
    else:
        return None


# 3. Standardize education values.
def clean_education(value):
    if value is not None:
        value = value.lower().replace("-", " ")

        if value == "graduate":
            return "Graduate"
        else:
            return "Not Graduate"
    else:
        return None


# 4. Standardize area values.
def clean_area(value):
    if value is not None:
        value = value.lower().replace("-", "").replace(" ", "")

        if value == "urban":
            return "Urban"
        elif value == "rural":
            return "Rural"
        else:
            return "Semiurban"
    else:
        return None


# 5. Make credit history more descriptive.
def clean_credit_history(value):
    if value is not None:
        if value == "1":
            return "Good"
        else:
            return "Bad"
    else:
        return None


# 6. Make loan status more descriptive.
def clean_status(value):
    if value is not None:
        if value.lower() in ["y", "yes"]:
            return "Approved"
        else:
            return "Denied"
    else:
        return None


# 7. Clean one full row.
def clean_row(row):
    columns = row.split(",")

    cleaned_columns = []

    for column in columns:
        cleaned = clean_missing(column)
        cleaned_columns.append(cleaned)

    loan_id, gender, married, dependents, education, \
    self_emp, app_income, co_income, loan_amt, term, \
    credit_hist, area, status = cleaned_columns

    married = clean_yes_no(married)
    self_emp = clean_yes_no(self_emp)
    education = clean_education(education)
    area = clean_area(area)
    credit_hist = clean_credit_history(credit_hist)
    status = clean_status(status)

    cleaned_columns = [
        loan_id, gender, married, dependents, education,
        self_emp, app_income, co_income, loan_amt, term,
        credit_hist, area, status
    ]

    return cleaned_columns


# 8. Split data into rows.
raw_rows = data.strip().split("\n")


# 9. Clean all rows.
cleaned_rows = []

for row in raw_rows:
    cleaned_row = clean_row(row)
    cleaned_rows.append(cleaned_row)


# 10. Remove duplicate rows.
unique_rows = []

for row in cleaned_rows:
    if row not in unique_rows:
        unique_rows.append(row)


# 11. Print final cleaned rows.
for row in unique_rows:
    print(row)