# this is program number 1

# asks data about the end user
copay = int(input("Co-pay: Php "))
charge = int(input("Dental Charge: Php "))
# computation formula
remaining = charge - copay
insurance = copay + (remaining * 0.15)
# program display
print(f"Total amount: Php {remaining}")
print(f"Insurance: Php {insurance}")
print("-------------------------------")

# this is program number 2
# asks data about the end user
length = int(input("Length of carpet (ft): "))
width = int(input("Width of carpet (ft): "))
price = float(input("Price of the carpet per square foot: Php "))
# computation formula
area = length * width
total = area * price
# program display
print("Total cost: {:,.2f}".format(total))

print("-------------------------------")
# this is program number 3

# asks data about the end user
distance = int(input("Distance the ball took (FT): "))
mph = float(input("Speed of the ball (MPH): "))
per_sec = mph * 1.4667
total_time = distance / per_sec
print(f"Great! It took {total_time} seconds for the baseball to travel in {distance} feet in {mph} miles per hour.")
