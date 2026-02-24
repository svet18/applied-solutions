
data = """LP001002,Male,No,0,Graduate,No,5849,0,,360,1,Urban,Y
LP001003,Male,Yes,1,Graduate,No,4583,1508,128,360,1,Rural,N
LP001005,Male,Yes,0,Graduate,Yes,3000,0,66,360,1,Urban,Y
LP001006,Male,Yes,0,Not Graduate,No,2583,2358,120,360,1,Urban,Y
LP001008,Male,No,0,Graduate,No,6000,0,141,360,1,Urban,Y
LP001011,Male,Yes,2,Graduate,Yes,5417,4196,267,360,1,Urban,Y
LP001013,Male,Yes,0,Not Graduate,No,2333,1516,95,360,1,Urban,Y
LP001014,Male,Yes,3+,Graduate,No,3036,2504,158,360,0,Semiurban,N
LP001018,Male,Yes,2,Graduate,No,4006,1526,168,360,1,Urban,Y
LP001020,Male,Yes,1,Graduate,No,12841,10968,349,360,1,Semiurban,N"""

rows = data.split("\n")
loan_approved = 0
loan_denied = 0

# Part 2 While-Loop Solution
row_number = 0

while row_number < len(rows):
    columns = rows[row_number].split(",")
    status = columns[-1]

    if status == "Y":
        loan_approved += 1
    else:
        loan_denied += 1

    row_number += 1 

print(f"TOTAL APPLICATIONS: {loan_approved + loan_denied}")
print("APPROVED: ", loan_approved)
print("DENIED: ", loan_denied)
print(f"APPROVAL RATE: , {loan_approved / loan_denied:.2f}%")


# Part 2 For-Loop Solution
for row in rows:
    columns = row.split(",")
    status = columns[-1]

    if status == "Y":
        loan_approved += 1
    else:
        loan_denied += 1

print(f"TOTAL APPLICATIONS: {loan_approved + loan_denied}")
print("APPROVED: ", loan_approved)
print("DENIED: ", loan_denied)
print(f"APPROVAL RATE: , {loan_approved / loan_denied:.2f}%")

