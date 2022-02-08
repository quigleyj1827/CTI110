#Pizza Quantity Calculator
#2/8/2022
#CTI-110 P1HW2 – Pizza Order
#Joseph Quigley
#Program calculates the amount of pizzas to order for inputted amt of students if students get 3 slices each and each pizza has 6 slices
#amount of students * 3 = slices / students / 2 = pizzas
print('How many students do you want to order pizza for?', end=' ')
students = int(input())
print('----Pizza Order--------')
print('Number of Students :', students)
print('Number of Pizza slices :', students * 3)
print('Pizzas Needed :', students / 2)
