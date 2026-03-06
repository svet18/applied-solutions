# ------------------
# Applied Project 4: # Loan Eligibility Screening
# ------------------

# SOLUTION: Nested conditions

print()
print("====================================")
print("       Loan Eligibility Summary     ")
print("====================================")
print()

# Applicant info (from previous project)
applicant_income = 4583
coapplicant_income = 1508
loan_amount = 128
loan_term = 360
graduate = True
self_employed = False
dependents = "1"
credit_history = 1

# Computed variables (from previous project)
total_monthly_income = applicant_income + coapplicant_income
total_annual_income = total_monthly_income * 12
loan_to_income = loan_amount * 1000 / total_annual_income

# ---------------------------------
# Print Applicant Information (from previous project)

# Total Monthly Income: $X,XXX.xx
# Total Annual Income: $X,XXX.xx
# Loan Amount: $XXX,XXX.xx
# Loan to Income Ratio: X.xx

print(f"Total Monthly Income: ${total_monthly_income:,.2f}")
print(f"Total Annual Income: ${total_annual_income:,.2f}")
print(f"Loan Amount: ${loan_amount:,.2f}")
print(f"Loan to Income Ratio: {loan_to_income:.2f}")
print()
# ---------------------------------
# Define 2 variables to hold decisions and reasons for decisions

decision = ""
reason = ""

# ---------------------------------
# Step 1. Basic Eligibility Check (bank pre-screen)

# Check credit history...
#   If bad:
#       decision = REJECTED
#       reason = Credit history indicates prior credit issues.

#   Otherwise, if good credit, check the loan to income ratio (LTI)...
#   Note: low LTI <=3, high LTI > 5
#       If low LTI:
#           decision = APPROVED
#           reason = Affordability is strong based on loan-to-income ratio.
#       If medium LTI:
#           decision = CONDITIONALLY APPROVED
#           reason = Affordability needs further review based on loan-to-income ratio.
#       If high LTI:
#           decision = REJECTED
#           reason = Loan-to-income ratio is too high.
#   Print the decision and the reason.

if credit_history == 0:
    decision = "REJECTED at Step 1"
    reason = "Credit history indicates prior credit issues. Bank will not pre-approve."
else:
    if loan_to_income <= 3:
        decision = "APPROVED at Step 1"
        reason = "Affordability is strong based on loan-to-income ratio."
    elif loan_to_income <= 5:
        decision = "CONDITIONALLY APPROVED at Step 1"
        reason = "Affordability needs further review based on loan-to-income ratio."
    else:
        decision = "REJECTED at Step 1"
        reason = "Loan-to-income ratio is too high for affordability standards."

print(f"Decision: {decision}")
print(f"Explanation: {reason}")
print()
# ---------------------------------

# Step 3: Continue screening only if NOT rejected at Step 2.

#  If previously NOT rejected, check LTI AND total monthly income...
#
#      If low LTI or med LTI, AND monthly income at least $5K:
#           decision = APPROVED
#           reason = Good credit, income meets minimum threshold, and affordability ratio is not high
#      If low LTI and monthly income at least $3K but less than $5K:
#           decision = CONSITIONALLY APPROVED
#           reason = Good credit, low LTI, income below minimum threshold
#      Otherwise:
#           decision = REJECTED
#           reason = Good credit, high LTI, income below min threshold.
#   Print the decision and the reason.

if decision != "REJECTED at Step 1":
    if loan_to_income <= 5.0 and total_monthly_income >= 5000:
        decision = "APPROVED at Step 2"
        reason = "Good credit, income meets minimum threshold, and affordability ratio is not high."
    elif loan_to_income <= 3.0 and 5000 > total_monthly_income >= 3000:
        decision = "CONDITIONALLY APPROVED at Step 2"
        reason = "Good credit, low LTI, income below minimum threshold."
    else:
        decision = "REJECTED at Step 2"
        reason = "Good credit, high LTI, income below min threshold."

print(f"Decision: {decision}")
print(f"Explanation: {reason}")
print()
