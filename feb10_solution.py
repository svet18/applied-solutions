# Loan Portfolio Summary Report

# Step 1. Copy the first 10 rows of the loan prediction dataset
#         and manually create a list of loan status

loan_status = ["Y","N","Y","Y","Y","Y","Y","N","Y","N"]

# Step 2.  Create the counter variables to count
#      - number of loans approved
#      - number of loans denied
#          Set them both to 0

loan_approved = 0
loan_denied = 0

# Step 3.  Loop through the list and count loans approved and denied
for loan in loan_status:
    if loan == "Y":
        loan_approved += 1
    else:
        loan_denied += 1

# Step 4. Print a clean summary (see sample output in README)
print(f"TOTAL APPLICATIONS: {loan_approved + loan_denied}")
print("APPROVED: ", loan_approved)
print("DENIED: ", loan_denied)
print(f"APPROVAL RATE: , {loan_approved / loan_denied:.2f}%")
