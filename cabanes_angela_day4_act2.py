first = int(input("Enter first number: "))
second = int(input("Enter second number: "))

decision = input("Would you like to try again (Y/N)? ").upper()

while decision == "Y":
    first = int(input("Enter first number: "))
    second = int(input("Enter second number: "))

    print(f"The sum of {first} and {second} is", first + second)

    decision = input("Would you like to try again (Y/N)? ").upper()
    if decision == "N":
        break

    else:
        print("Invalid input.")
print("The program will now end.")

