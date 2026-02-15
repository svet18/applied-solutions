# SOLUTION:

# Loan Application Simulation

print("====================================")
print("   Welcome to the Loan Application  ")
print("====================================")

# Start application
start = input("Click Enter to start your loan application...")

# Collect applicant information
name = input("Full Name: ")

birth_year = int(input("Year you were born: "))

married = input("Married? (Y/N): ").upper()
graduate = input("Graduate? (Y/N): ").upper()
self_employed = input("Self-employed? (Y/N): ").upper()

monthly_income = float(input("Monthly income ($): "))
loan_amount = float(input("Requested loan amount ($): "))
loan_term = int(input("Loan term (months): "))

# Calculate age
current_year = 2026
age = current_year - birth_year

# Print summary
print("\n====================================")
print("        Loan Application Summary     ")
print("====================================")
print(f"Applicant Name: {name}")
print(f"Age: {age}")
print(f"Married: {married}")
print(f"Graduate: {graduate}")
print(f"Self-Employed: {self_employed}")
print(f"Monthly Income: ${monthly_income:,.2f}")
print(f"Loan Amount: ${loan_amount:,.2f}")
print(f"Loan Term: {loan_term} months")
print("====================================")

# Confirmation
confirm = input("Is the above information correct? (Y/N): ").upper()

if confirm == "Y":
    print("\nThank you! Your loan application has been submitted.")
else:
    print("\nApplication canceled. Please restart to correct your information.")
