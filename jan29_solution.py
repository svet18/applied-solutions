# ------------------
# Applied Project 3: # Loan Application Simulation (Cont.)
# ------------------

# NOTE: 
# This project buils upon the previous one.
# SOLUTION: Applicant ID LN001003

print()
print("====================================")
print("       Loan Eligibility Summary     ")
print("====================================")
print()

# Applicant info:
applicant_income = 4583
coapplicant_income = 1508
loan_amount = 128
loan_term = 360
graduate = True
self_employed = False
dependents = "1"
credit_history = 1

# Check to make sure Dependents is a string.
print(type(dependents))

# Compute:
# Loan-to-income ratio is computed as a ratio of the loan amount & total annual income.
# Since loan amount is recoded in throusands (e.g., 128 instead of 128,000),
# it needs to be multiplied by 1000 to be in the same units as income.
# Total annual income can be easily computed from total monthly income.

total_monthly_income = applicant_income + coapplicant_income
total_annual_income = total_monthly_income * 12
loan_to_income = (loan_amount * 1000) / total_annual_income  

# Step 0: Print
# Total Monthly Income: $X,XXX.xx
# Total Annual Income: $X,XXX.xx
# Loan Amount: $XXX,XXX.xx
# Loan to Income Ratio: X.xx

print(f"Total Monthly Income: ${total_monthly_income:,.2f}")
print(f"Total Annual Income: ${total_annual_income:,.2f}")
print(f"Loan Amount: ${loan_amount * 1000:,.2f}")
print(f"Loan to Income Ratio: {loan_to_income:.2f}")

# Step 1: Basic Eligibility Check (bank pre-screen)
# REJECT if:
#   •	credit_history == 0 (most banks won’t pre-approve with bad credit history)
# Else APPROVE/REJECT based on affordability:
#   •	If loan_to_income <= 3 → approve
#   •	If 3 < loan_to_income <= 5 → “conditional” (needs review)
#   •	If loan_to_income > 5 → reject

if credit_history == 0:
	print(f"Pre-Screening: REJECTED — Bad credit history")
elif loan_to_income <= 3:
    print(f"Pre-Screening: APPROVED — Loan-to-income ratio: { loan_to_income:.2f}")
elif loan_to_income <= 5:
    print(f"Pre-Screening: CONDITIONAL — Borderline ratio: { loan_to_income:.2f} (needs review)")
else:
    print(f"Pre-Screening: REJECTED — Ratio too high: { loan_to_income:.2f}")

# Step 2: Decision
# APPROVE if:
# - good credit history, and 
# - total monthly income at least $5K, and 
# - loan to income ratio is not higher than 3.0

if (
    credit_history == 1 
    and total_monthly_income >= 5000 
    and loan_to_income <= 3
):
    print(f"Pre-Screening: APPROVED - Step 2.1")
else:
    print(f"Pre-Screening: REJECTED - Step 2.2")

# Step 3: Additional Eligibility Checks (Optional Practice)
#   •	If self_employed == "Yes" and loan_to_income > 4 → reject (stricter affordability)
#   •	If education == "Not Graduate" and loan_to_income > 4 → conditional
#   •	If dependents == "3+" and loan_to_income > 3 → conditional

if not self_employed and loan_to_income > 4:
    print(f"Pre-Screening: REJECTED - Step 3.1")
elif not graduate and loan_to_income > 4:
    print(f"Pre-Screening: CONDITIONAL - Step 3.2")
elif dependents == "3+" and loan_to_income > 3:
    print(f"Pre-Screening: CONDITIONAL - Step 3.3")
else:
    print(f"Pre-Screening: APPROVED - Step 3.4")

print()
