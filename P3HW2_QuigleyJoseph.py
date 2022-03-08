#Pizza Quantity Calculator
#2/8/2022
#CTI-110 P3HW2 – Pizza Order
#Joseph Quigley
#Program calculates the amount of pizzas to order for inputted amt of students if students get 3 slices each and each pizza has 6 slices
# pizzas_needed will be students / (1.5, 2, or 3)
#Price of pizzas is $5 with 6% tax

    
print('How many students do you want to order pizza for?', end=' ')
students = int(input())
print('Enter number of people per pizza ( 1.5, 2 or 3) :', end=' ')
people_per_pizza = float(input())


if people_per_pizza == 1.5:
    pizzas_needed = students / people_per_pizza
    
elif people_per_pizza == 2:
    pizzas_needed = students / people_per_pizza
    
elif people_per_pizza == 3:
    pizzas_needed = students / people_per_pizza
else:
     print('Invalid Entry !')
     print('Should have entered 1.5, 2 or 3')
     print('Run Program again')

#pizzas = int(slices_needed) * int(students)

cost_per_pizza = 5.00
sub_total = float(cost_per_pizza * pizzas_needed)
taxed_total = float(sub_total * 0.06)
total = sub_total + taxed_total


print('----Pizza Order--------')
print('Number of Students :', students)
print(f'Pizzas Needed :', round(pizzas_needed))
print(f'Price $, {total:.2f}')
