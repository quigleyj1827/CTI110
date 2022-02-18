#This is a program that calculates subtotal, total tax, and total from purchased items. 
#02/18/2022
#CTI-110 P2HW1 - Total Purchases
#Joseph Quigley
#sub_total is the sum of all items i1 +i2 +i3+ i4 + i5
#taxed_total is sub_total x 7%
#Total is sub_toal + taxes = total

item_one = float(input('Enter the price of item #1: '))
item_two = float(input('Enter the price of item #2: '))
item_three = float(input('Enter the price of item #3 '))
item_four = float(input('Enter the price of item #4 '))
item_five = float(input('Enter the price of item #5 '))
sub_total = float(item_one + item_two + item_three + item_four + item_five)
taxed_total = sub_total * 0.07
total_amt = (sub_total + taxed_total)

print('-------Results------')
print('Subtotal:', (sub_total))
print('Sales Tax:',  (f'{taxed_total:.2f}'))
print('Total:', (total_amt))               
