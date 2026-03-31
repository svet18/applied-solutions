# Take 1 row of data and convert it to usable types

raw_data = "LP001003,Male,Yes,1,Graduate,No,4583,1508,128,360,1,Rural,N"

# Split the row into a list of columns
columns = raw_data.split(",")

# Assign each column to a variable
loan_id, gender, married, dependents, education, \
self_emp, app_income, co_income, loan_amt, term, \
credit_hist, area, status = columns

# Convert each column to usable data types
# Note: Strings do not need to be converted
app_income = int(app_income)
co_income = int(co_income)
loan_amt = int(loan_amt)
term = int(term)
credit_hist = int(credit_hist)

# Verify conversion - print each var type and value
print(type(dependents), dependents)
print(type(app_income), app_income)

# Convert numeric dichotomos variables to Boolean
credit_hist = bool(credit_hist)
print(type(credit_hist), credit_hist)

# Convert Yes/No to Boolean & verify
married = married == "Yes"
self_emp = self_emp == "Yes"

print(type(married), married)
print(type(self_emp), self_emp)

# Convert status to readable text
status = "Approved" if status == "Y" else "Denied"
print(status)

# Convert the cleaned record into a LIST object
# using a list() function
clean_list = list([
    loan_id, gender, married, dependents, education,
    self_emp, app_income, co_income, loan_amt,
    term, credit_hist, area, status
])

# Verify that it is a list
# Print its values
print(clean_list)
print(type(clean_list))