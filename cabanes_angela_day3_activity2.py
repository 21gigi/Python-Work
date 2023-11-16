office = input("What is your office (IT, Acct, HR)? ").lower()
service_year = int(input("How many years are you in your field?"))

if office == "it":
    if service_year >= 10:
        print("Your salary is Php 10,000")
    elif service_year < 10:
        print("Your salary is Php 5,000")
elif office == "acct":
    if service_year >= 10:
        print("Your salary is Php 12,000")
    elif service_year < 10:
        print("Your salary is Php 6,000")
elif office == "hr":
    if service_year >= 10:
        print("Your salary is Php 15,000")
    elif service_year < 10:
        print("Your salary is Php 7,500")