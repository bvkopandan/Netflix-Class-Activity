#TASK 1
#td1
username = input("Please insert your username: \n")
#td2
billing = input("What is your billing month?: \n")
#td3
acc_type = input("Please insert your account type: \n")
#td4
subs = input("What is your monthly subscription fee?: \n")
#td5
province = input("What province do you live in? (two characters): \n")
province = province.upper()

#TASK 2
print("\nYOUR INFORMATION:")
print("Netflix username: ", username)
print("Billing Month: ", billing)
print("Account type: ", acc_type)
print("Subscription fee: ", subs)
print("Province: ", province)

#TASK 3
print("\nDATA TYPE:")
print("Data type username: ", type(username))
print("Data type billing month: ", type(billing))
print("Data type account type: ", type(acc_type))
print("Data type subscription fee: ", type(subs))
print("Data type province: ", type(province), "\n")

#TASK 4
subs = float(subs)

if province == "AB" or "BC" or "MB" or "NT" or "NU" or "SK" or "QC" or "YT":
    final_bill = subs + (subs * 0.05)
elif province == "ON":
    final_bill = subs + (subs * 0.13)
elif province == "NB" or "NL" or "NS" or "PE":
    final_bill = subs + (subs * 0.15)

print("Your final bill is: ", final_bill)