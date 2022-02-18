current_price = int(input())
last_months_price = int(input())

print("This house is $" + str(current_price), end = ". "),
print("The change is $" + str(current_price - last_months_price) + " since last month.")
print("The estimated monthly mortgage is ${:.2f}".format((current_price * 0.051) / 12), end = ".\n")
   