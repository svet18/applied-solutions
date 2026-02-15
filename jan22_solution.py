"""
SOLUTION 1:

This solution intentionally includes different ways of combining labels and information:
    - all one string: "label info"
    - label + info: "label" + "info"
    - label, info: "label", "info"
Numeric information is added without quotations
Arithmetic operations are included directly
All this is for learning, not best practice!
"""

# Using hard-coded values and concatenation:

print("\n\nSOLUTION 1")
print("Loan Applicant Summary")
print("----------------------")
print("Applicant ID: LP001003")  # all one string
print("Gender: " + "M")  # label + info
print("Married: " + "Yes")
print("Education: " + "Graduate")
print("Self-Employed: " + "No")
print()
print("\nFinancial Information")
print("---------------------")
print("Applicant Income: $", 4583)  # label, info (numeric)
print("Coapplicant Income: $", 1508)
# label, info (numeric with arithmetic operation)
print("Total Household Income: $", 4583 + 1508)
print("Loan Amount (in thousands):", 128)
print("Loan Term (months):", 360)
print("Credit History:", "Good")  # label, info

# Using variables and concatenation:

"""
SOLUTION 2:

Here we store application info in variables.
Then use these variables inside the print function.
Pay attention to naming convention of variables and how descriptive they are.
"""

# Applicant information stored in variables:
applicant_ID = "LP001003"
gender = "M"
married = "Yes"
education = "Graduate"
self_employed = "No"
applicant_income = 4583
coapplicant_income = 1508
total_income = applicant_income + coapplicant_income
loan_amount = 128  # in thousands
loan_term = 360  # months
credit_history = "Good"

print("\n\nSOLUTION 2")
print("Loan Applicant Summary")
print("----------------------")
print("Applicant ID:", applicant_ID)
print("Gender: ", gender)
print("Married: ", married)
print("Education: ", education)
print("Self-Employed: ", self_employed)
print()
print("\nFinancial Information")
print("---------------------")
print("Applicant Income: $", applicant_income)
print("Coapplicant Income: $", coapplicant_income)
print("Total Household Income: $", total_income)
print("Loan Amount (in thousands):", loan_amount)
print("Loan Term (months):", loan_term)
print("Credit History:", credit_history)


# SOLUTION 3:
# Using variables and formatted strings
print("\n\nSOLUTION 3")
print("Loan Applicant Summary")
print("----------------------")
print(f"Applicant ID: {applicant_ID}")
print(f"Gender: {gender}")
print(f"Married: {married}")
print(f"Education: {education}")
print(f"Self-Employed: {self_employed}")
print()
print("\nFinancial Information")
print("---------------------")
print(f"Applicant Income: {applicant_income}")
print(f"Coapplicant Income: {coapplicant_income}")
print(f"Total Household Income: {total_income}")
print(f"Loan Amount (in thousands): {loan_amount}")
print(f"Loan Term (months): {loan_term}")
print(f"Credit History: {credit_history}")
